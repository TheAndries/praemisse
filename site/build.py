#!/usr/bin/env python3
"""praemisse — build pipeline. Renders map/ into a static site in site/_build/.

    python3 site/build.py            build (after checking)
    python3 site/build.py --check    check only: parse every node, validate against MODEL.md,
                                     resolve every link; exit 1 on any error
    python3 site/build.py --domain praemisse.com
                                     also write a CNAME file (only once DNS points here)
    python3 site/build.py --map DIR --out DIR
                                     other directories (used by tests)

What it does, and nothing else:
  1. reads every *.md under map/ as YAML front matter + Markdown (MODEL.md);
  2. validates ids, types, statuses, provenance and that every link resolves;
  3. writes one page per node at a permanent address  /<prefix>/<id-without-prefix>/,
     index pages per type, and the site index; copies site/static/ and site/fonts/.

No framework, no JavaScript on the reading path, no cookies (CHARTER.md P6–P8, DESIGN.md).
Requires: Python 3.11+, PyYAML. The Markdown renderer is the small subset below; node
bodies should stay within it (paragraphs, headings, emphasis, links, lists, quotes).

Open questions for Phase 1, before the first node is written (see memory.md):
  - how a new version lives "inside the same file" (MODEL.md): proposed `versions:` list
    in the front matter, newest first, each with `date`, `supersedes`, `reason`;
  - the machine validity check for `a-` nodes (what `checked` requires);
  - how a Dispute node renders on its target node's page.
"""
from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install -r site/requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
PREFIX = ""  # relative path from the page being rendered to the site root; set per page
SITE = ROOT / "site"
MAP = ROOT / "map"
OUT = SITE / "_build"

TYPES = {  # prefix -> (type name, plural label, has status)
    "t": ("thinker", "Thinkers", False),
    "w": ("work", "Works", False),
    "p": ("passage", "Passages", False),
    "c": ("claim", "Claims", True),
    "a": ("argument", "Arguments", True),
    "r": ("reading", "Readings", False),
    "x": ("comparison", "Comparisons", True),
    "d": ("dispute", "Disputes", False),
    "v": ("attestation", "Attestations", False),
}
STATUSES = ("draft", "checked", "attested", "established")
LINK_FIELDS = ("depends_on", "supports", "attacked_by", "replies_to", "shares_premise_with")
ID_RE = re.compile(r"^([twpcarxdv])-[a-z0-9][a-z0-9-]*$")


@dataclass
class Node:
    id: str
    type: str
    path: Path
    meta: dict
    body: str
    errors: list[str] = field(default_factory=list)

    @property
    def prefix(self) -> str:
        return self.id[0]

    @property
    def url(self) -> str:
        return f"/{self.prefix}/{self.id[2:]}/"

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or self.meta.get("name") or self.id)

    @property
    def status(self) -> str | None:
        return self.meta.get("status")


# ----------------------------------------------------------------------------- reading

def read_nodes(map_dir: Path) -> list[Node]:
    nodes: list[Node] = []
    for path in sorted(map_dir.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = split_front_matter(text)
        node = Node(id=str(meta.get("id", path.stem)), type=str(meta.get("type", "")), path=path, meta=meta, body=body)
        if meta is None or not isinstance(meta, dict):
            node.errors.append("no YAML front matter")
        nodes.append(node)
    return nodes


def split_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    meta = yaml.safe_load(text[4:end]) or {}
    return meta, text[end + 5:]


# ----------------------------------------------------------------------------- checking

def check(nodes: list[Node]) -> list[str]:
    ids = {n.id: n for n in nodes}
    errors: list[str] = []
    for n in nodes:
        where = n.path.relative_to(ROOT) if n.path.is_relative_to(ROOT) else n.path.name
        m = ID_RE.match(n.id)
        if not m:
            errors.append(f"{where}: id {n.id!r} is not <prefix>-<slug> with a known prefix")
            continue
        if n.path.stem != n.id:
            errors.append(f"{where}: file name must equal the id ({n.id})")
        tname, _, has_status = TYPES[n.prefix]
        if n.type != tname:
            errors.append(f"{where}: type {n.type!r} does not match prefix {n.prefix!r} ({tname})")
        if has_status:
            if n.status not in STATUSES:
                errors.append(f"{where}: status must be one of {STATUSES}, got {n.status!r}")
            if "contested" in n.meta and not isinstance(n.meta["contested"], bool):
                errors.append(f"{where}: contested must be true or false")
        if not n.meta.get("produced_by"):
            errors.append(f"{where}: produced_by (model and date) is required (MODEL.md, Provenance)")
        for key in ("verified_by", "disputes"):
            if key in n.meta and not isinstance(n.meta[key], list):
                errors.append(f"{where}: {key} must be a list")
        for key in LINK_FIELDS + ("verified_by", "disputes", "passages", "premises", "supersedes", "superseded_by", "conclusion", "thinker", "work"):
            for target in as_list(n.meta.get(key)):
                if isinstance(target, dict):  # premises may be {claim: id} or {assumption: text}
                    target = target.get("claim") or target.get("id")
                    if target is None:
                        continue
                if not isinstance(target, str):
                    errors.append(f"{where}: {key} contains a non-id value {target!r}")
                elif target not in ids:
                    errors.append(f"{where}: {key} -> {target} does not resolve")
        if n.prefix in ("c", "a") and not as_list(n.meta.get("passages")):
            errors.append(f"{where}: a claim or argument must cite at least one passage (CHARTER.md P1)")
        if n.prefix == "p":
            for key in ("ref", "original", "work"):
                if not n.meta.get(key):
                    errors.append(f"{where}: a passage needs {key}")
        errors.extend(f"{where}: {e}" for e in n.errors)
    return errors


def as_list(v) -> list:
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


# ----------------------------------------------------------------------------- markdown

_INLINE = [
    (re.compile(r"\*\*(.+?)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<!\w)[*_](.+?)[*_](?!\w)"), r"<em>\1</em>"),
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
    (re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)"), r'<a href="\2">\1</a>'),
]


def inline(text: str) -> str:
    out = html.escape(text, quote=False)
    for rx, rep in _INLINE:
        out = rx.sub(rep, out)
    return out


def markdown(text: str) -> str:
    """A deliberately small Markdown: paragraphs, #/##/### headings, * or - lists,
    1. lists, > quotes, and the inline forms above. Anything else is a paragraph."""
    blocks: list[str] = []
    para: list[str] = []
    lst: list[tuple[str, str]] = []

    def flush_para():
        if para:
            blocks.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def flush_list():
        if lst:
            tag = lst[0][0]
            blocks.append(f"<{tag}>" + "".join(f"<li>{inline(t)}</li>" for _, t in lst) + f"</{tag}>")
            lst.clear()

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para(); flush_list(); continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            flush_para(); flush_list()
            level = len(m.group(1))
            blocks.append(f"<h{level + 1}>{inline(m.group(2))}</h{level + 1}>")
            continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            flush_para(); lst.append(("ul", m.group(1))); continue
        m = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if m:
            flush_para(); lst.append(("ol", m.group(1))); continue
        if line.startswith(">"):
            flush_para(); flush_list()
            blocks.append(f"<blockquote><p>{inline(line[1:].strip())}</p></blockquote>")
            continue
        if lst:
            lst[-1] = (lst[-1][0], lst[-1][1] + " " + line.strip()); continue
        para.append(line.strip())
    flush_para(); flush_list()
    return "\n".join(blocks)


# ----------------------------------------------------------------------------- rendering

def template(name: str) -> str:
    return (SITE / "templates" / name).read_text(encoding="utf-8")


def fill(tpl: str, **vars: str) -> str:
    for k, v in vars.items():
        tpl = tpl.replace("{{ " + k + " }}", v)
    return tpl


def esc(s) -> str:
    return html.escape(str(s if s is not None else ""), quote=True)


def render_node(n: Node, ids: dict[str, Node]) -> str:
    tname, _, has_status = TYPES[n.prefix]
    status_bits = [f'<span><span class="label">{esc(tname)}</span></span>']
    if has_status:
        word = esc(n.status)
        if n.meta.get("contested"):
            status_bits.append(f'<span>Status: <span class="word">{word}</span>, <span class="word contested">contested</span></span>')
        else:
            status_bits.append(f'<span>Status: <span class="word">{word}</span></span>')
    status_bits.append(f"<span>Produced by {esc(n.meta.get('produced_by'))}</span>")
    v = as_list(n.meta.get("verified_by"))
    status_bits.append("<span>Verified by " + (", ".join(link(ids, i) for i in v) if v else "nobody yet") + "</span>")

    # The argument structure, if any.
    arg = ""
    prem = as_list(n.meta.get("premises"))
    if prem or n.meta.get("conclusion"):
        rows = []
        for i, p in enumerate(prem, 1):
            if isinstance(p, dict) and "assumption" in p:
                rows.append(f'<li><span class="n">P{i}</span><span class="assumption"><em>Assumption.</em> {inline(str(p["assumption"]))}</span></li>')
            else:
                cid = p.get("claim") if isinstance(p, dict) else p
                rows.append(f'<li><span class="n">P{i}</span><span>{link(ids, cid)}</span></li>')
        if n.meta.get("inference"):
            rows.append(f'<li><span class="n">Form</span><span>{inline(str(n.meta["inference"]))}</span></li>')
        if n.meta.get("conclusion"):
            rows.append(f'<li class="conclusion"><span class="n">C</span><span>{link(ids, n.meta["conclusion"])}</span></li>')
        arg = '<h2>The argument</h2>\n<ol class="argument">' + "".join(rows) + "</ol>"

    # Passages beside the text.
    passages = []
    for pid in as_list(n.meta.get("passages")):
        p = ids.get(pid)
        if p is None:
            continue
        work = ids.get(str(p.meta.get("work")))
        work_title = esc(work.title) if work else esc(p.meta.get("work"))
        src = p.meta.get("source") or (work.meta.get("source") if work else "")
        passages.append(
            f'<div class="passage" lang="{esc(p.meta.get("lang", ""))}">'
            f'<p class="ref" lang="en"><span><a href="{href(p)}">{work_title} {esc(p.meta.get("ref"))}</a></span><span>{esc(src)}</span></p>'
            f'<p class="original verse" lang="{esc(p.meta.get("lang", ""))}">{esc(p.meta.get("original"))}</p>'
            + (f'<p class="translation" lang="en">{esc(p.meta.get("translation"))} <span class="by">— {esc(p.meta.get("translation_by", "translation"))}</span></p>' if p.meta.get("translation") else "")
            + "</div>")
    if n.prefix == "p":
        passages.append(
            f'<div class="passage" lang="{esc(n.meta.get("lang", ""))}">'
            f'<p class="ref" lang="en"><span>{esc(n.meta.get("ref"))}</span><span>{esc(n.meta.get("source", ""))}</span></p>'
            f'<p class="original verse" lang="{esc(n.meta.get("lang", ""))}">{esc(n.meta.get("original"))}</p>'
            + (f'<p class="translation" lang="en">{esc(n.meta.get("translation"))} <span class="by">— {esc(n.meta.get("translation_by", "translation"))}</span></p>' if n.meta.get("translation") else "")
            + "</div>")

    links_html = []
    for key in LINK_FIELDS:
        targets = as_list(n.meta.get(key))
        if targets:
            items = "".join(f"<li>{link(ids, t, with_id=True)}</li>" for t in targets)
            links_html.append(f'<div><h2>{esc(key.replace("_", " ").capitalize())}</h2><ul>{items}</ul></div>')
    chain = []
    if n.meta.get("supersedes"):
        chain.append("Supersedes " + link(ids, n.meta["supersedes"]))
    if n.meta.get("superseded_by"):
        chain.append("Superseded by " + link(ids, n.meta["superseded_by"]))
    disputes = as_list(n.meta.get("disputes"))
    meta_line = " · ".join(
        [f"Permanent address: {esc(n.url)}", f"Produced by {esc(n.meta.get('produced_by'))}"]
        + chain
        + ["Disputes: " + (", ".join(link(ids, d) for d in disputes) if disputes else "none")]
    )

    body = markdown(n.body)
    return fill(
        template("node.html"),
        title=esc(n.title), status=" ".join(status_bits), argument=arg, body=body,
        links="\n".join(links_html), meta=meta_line,
        passages="\n".join(passages),
        jump='<p class="jump"><a href="#passages">The passage</a></p>' if passages else "",
        back='<p class="return"><a href="#top">Back to the text</a></p>' if passages else "",
    )


def href(n: Node) -> str:
    return PREFIX + n.url[1:]


def link(ids: dict[str, Node], target, with_id: bool = False) -> str:
    t = ids.get(str(target))
    if t is None:
        return f'<span class="id">{esc(target)}</span>'
    idspan = f'<span class="id">{esc(t.id)}</span>' if with_id else ""
    return f'{idspan}<a href="{href(t)}">{esc(t.title)}</a>'


def page(title: str, content: str) -> str:
    return fill(template("base.html"), title=esc(title), content=content, root=PREFIX)


def build(nodes: list[Node], out: Path, domain: str | None) -> None:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copytree(SITE / "static", out / "static")
    shutil.copytree(SITE / "fonts", out / "fonts")
    if (SITE / "specimens").exists():
        shutil.copytree(SITE / "specimens", out / "specimens", ignore=shutil.ignore_patterns("*.py"))
    ids = {n.id: n for n in nodes}
    global PREFIX
    for n in nodes:
        PREFIX = "../../"
        d = out / n.prefix / n.id[2:]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(n.title, render_node(n, ids)), encoding="utf-8")
    PREFIX = "../"
    for prefix, (tname, plural, _) in TYPES.items():
        group = [n for n in nodes if n.prefix == prefix]
        items = "".join(f'<li><span class="id">{esc(n.id)}</span><a href="{href(n)}">{esc(n.title)}</a>'
                        + (f' <span class="id">{esc(n.status)}</span>' if n.status else "") + "</li>" for n in group)
        content = f"<h1>{plural}</h1>" + (f'<ul class="index">{items}</ul>' if items else "<p class=\"prose\">Nothing here yet.</p>")
        (out / prefix).mkdir(exist_ok=True)
        (out / prefix / "index.html").write_text(page(plural, content), encoding="utf-8")
    PREFIX = ""
    counts = {plural: sum(1 for n in nodes if n.prefix == p) for p, (_, plural, _) in TYPES.items()}
    counts_html = "".join(f'<li><a href="{p}/">{plural}</a> <span class="id">{counts[plural]}</span></li>' for p, (_, plural, _) in TYPES.items())
    (out / "index.html").write_text(page("praemisse", template("index.html").replace("{{ counts }}", counts_html)), encoding="utf-8")
    (out / ".nojekyll").write_text("")
    if domain:
        (out / "CNAME").write_text(domain + "\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--map", type=Path, default=MAP)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--domain", default=None, help="write a CNAME file for this custom domain")
    a = ap.parse_args(argv)
    nodes = read_nodes(a.map)
    errors = check(nodes)
    for e in errors:
        print("error:", e, file=sys.stderr)
    print(f"{len(nodes)} nodes, {len(errors)} errors", file=sys.stderr)
    if errors:
        return 1
    if not a.check:
        build(nodes, a.out, a.domain)
        print(f"built {a.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
