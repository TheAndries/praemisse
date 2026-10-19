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

Settled 2026-10-06 (MODEL.md, "How the model is applied"; CHANGELOG.md):
  - a revised node keeps its id and file; `versions:` in the front matter lists every
    earlier version, newest first, with `date`, `reason`, the superseded `statement` and,
    when a dispute or attestation caused it, `credit`;
  - `status: checked` is allowed only on an argument whose `form:` block passes
    tools/validity.py (truth-table entailment); a `form:` that fails is a build error;
  - a dispute (`d-`) or attestation (`v-`) names its `target`; the target's page renders
    every one of them in full, and the target's `disputes`/`verified_by` lists, status
    and `contested` flag must agree with them.

Settled 2026-10-10 (owner session, Ask 7; MODEL.md, "Checked comparisons" and "Quotations"):
  - a comparison may be `checked` when a named human has reviewed it against the project's
    translations without attesting it; it must then carry `status_note`, which the status
    line shows after the word, saying who reviewed what and what was not verified;
  - a claim may carry `quotes:`, each with `passage`, `original` and `translation`; the
    build checks that each is a verbatim substring (whitespace normalized) of that passage's
    `original` and `translation`, and the page shows the two beside the statement.
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
sys.path.insert(0, str(ROOT / "tools"))
import validity  # noqa: E402  (tools/validity.py, the machine validity check)
PREFIX = ""  # relative path from the page being rendered to the site root; set per page
REPO = "https://github.com/TheAndries/praemisse"  # where the dispute and attestation forms live (MODEL.md, Filing)
SITE = ROOT / "site"
MAP = ROOT / "map"
OUT = SITE / "_build"
# Design-layer settings (site/site.yaml, added 2026-10-11 with the design brief): the palette
# set on <html>, and the "Start here" list of the front page. Not the map, not the model.
CONFIG = yaml.safe_load((SITE / "site.yaml").read_text(encoding="utf-8")) or {}
COUNTS: dict[str, int] = {}  # per type prefix, set by build() and rendered in every colophon

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
DISPUTE_KINDS = ("validity", "fidelity")
# DISPUTES.md steps: 1 published, 2 argued/conceded, 4 contested, 5 resolved, 6 escalated.
DISPUTE_OUTCOMES = ("published", "argued", "conceded", "contested", "resolved", "escalated")
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
        for key in LINK_FIELDS + ("verified_by", "disputes", "passages", "premises", "supersedes", "superseded_by", "conclusion", "thinker", "work", "reading_of"):
            for target in as_list(n.meta.get(key)):
                if isinstance(target, dict):  # premises may be {claim: id} or {assumption: text}
                    target = target.get("claim") or target.get("id")
                    if target is None:
                        continue
                if not isinstance(target, str):
                    errors.append(f"{where}: {key} contains a non-id value {target!r}")
                elif target not in ids:
                    errors.append(f"{where}: {key} -> {target} does not resolve")
        if n.prefix in ("c", "a", "x") and not as_list(n.meta.get("passages")):
            errors.append(f"{where}: a claim, argument or comparison must cite at least one passage (CHARTER.md P1)")
        # MODEL.md: supports is the converse of depends_on (checked since 2026-10-09).
        for target in as_list(n.meta.get("depends_on")):
            if isinstance(target, str) and target in ids and n.id not in as_list(ids[target].meta.get("supports")):
                errors.append(f"{where}: depends_on {target}, but that node's supports does not name {n.id}")
        for target in as_list(n.meta.get("supports")):
            if isinstance(target, str) and target in ids and n.id not in as_list(ids[target].meta.get("depends_on")):
                errors.append(f"{where}: supports {target}, but that node's depends_on does not name {n.id}")
        # MODEL.md, Attacks: attacked_by and replies_to are converses.
        for target in as_list(n.meta.get("attacked_by")):
            if isinstance(target, str) and target in ids and n.id not in as_list(ids[target].meta.get("replies_to")):
                errors.append(f"{where}: attacked_by {target}, but that node's replies_to does not name {n.id}")
        for target in as_list(n.meta.get("replies_to")):
            if isinstance(target, str) and target in ids and n.id not in as_list(ids[target].meta.get("attacked_by")):
                errors.append(f"{where}: replies_to {target}, but that node's attacked_by does not name {n.id}")
        # MODEL.md, Comparisons: shares_premise_with is symmetric (checked since 2026-10-10).
        for target in as_list(n.meta.get("shares_premise_with")):
            if isinstance(target, str) and target in ids and n.id not in as_list(ids[target].meta.get("shares_premise_with")):
                errors.append(f"{where}: shares_premise_with {target}, but that node does not name {n.id}")
        if n.prefix == "x":
            errors.extend(f"{where}: {e}" for e in check_comparison(n, ids))
        if n.prefix == "p":
            for key in ("ref", "original", "work"):
                if not n.meta.get(key):
                    errors.append(f"{where}: a passage needs {key}")
        if n.prefix in ("c", "a", "x") and not n.meta.get("statement"):
            errors.append(f"{where}: a {tname} needs a one-sentence statement")
        if n.prefix == "a":
            errors.extend(f"{where}: {e}" for e in check_argument(n))
        elif n.status == "checked" and n.prefix == "x":
            # MODEL.md, Checked comparisons (settled 2026-10-10): a human review short of attestation.
            note = n.meta.get("status_note")
            if not isinstance(note, str) or not note.strip():
                errors.append(f"{where}: a checked comparison needs status_note saying who reviewed it against what, and what was not verified")
        elif n.status == "checked":
            errors.append(f"{where}: only an argument with a passing form can be checked; a {tname} is draft until a human attests it")
        if n.meta.get("status_note") and not (n.prefix == "x" and n.status == "checked"):
            errors.append(f"{where}: status_note is allowed only on a checked comparison")
        if n.meta.get("quotes") is not None:
            errors.extend(f"{where}: {e}" for e in check_quotes(n, ids))
        for i, v in enumerate(as_list(n.meta.get("versions"))):
            if not isinstance(v, dict) or not v.get("date") or not v.get("reason") or not v.get("statement"):
                errors.append(f"{where}: versions[{i}] needs date, reason and the superseded statement")
            elif v.get("credit") and str(v["credit"]) not in ids:
                errors.append(f"{where}: versions[{i}].credit -> {v['credit']} does not resolve")
        if n.prefix == "d":
            errors.extend(f"{where}: {e}" for e in check_dispute(n, ids))
        if n.prefix == "v":
            errors.extend(f"{where}: {e}" for e in check_attestation(n, ids))
        if has_status:
            errors.extend(f"{where}: {e}" for e in check_human_record(n, nodes))
        errors.extend(f"{where}: {e}" for e in n.errors)
    # MODEL.md, Comparisons: every shares_premise_with pair is named in some comparison's shared entry.
    named = set()
    for x in nodes:
        if x.prefix == "x":
            for sh in as_list(x.meta.get("shared")):
                cl = [str(c) for c in as_list((sh or {}).get("claims"))] if isinstance(sh, dict) else []
                named.update((a, b) for a in cl for b in cl if a != b)
    for n in nodes:
        for target in as_list(n.meta.get("shares_premise_with")):
            if isinstance(target, str) and (n.id, target) not in named:
                errors.append(f"{n.path.name}: shares_premise_with {target}, but no comparison names the shared premise")
    return errors


def norm(text) -> str:
    return " ".join(str(text if text is not None else "").split())


def check_quotes(n: Node, ids: dict) -> list[str]:
    """MODEL.md, Quotations (settled 2026-10-10): a claim's `quotes:` list the load-bearing
    sentences in the original and the project's translation; each must be a verbatim
    substring of a passage the claim cites (CHARTER.md P1), so that what the page shows
    beside the statement is exactly what the passage shows below it. A substring check
    cannot tell that the translation is of the same sentence as the original; the
    reviewer's eye does that."""
    errs: list[str] = []
    if n.prefix != "c":
        return ["quotes are allowed on a claim only"]
    quotes = n.meta.get("quotes")
    if not isinstance(quotes, list) or not quotes:
        return ["quotes must be a non-empty list"]
    cited = [str(x) for x in as_list(n.meta.get("passages"))]
    for i, q in enumerate(quotes):
        if not isinstance(q, dict) or not q.get("passage") or not q.get("original"):
            errs.append(f"quotes[{i}] needs passage and original")
            continue
        pid = str(q["passage"])
        if pid not in cited:
            errs.append(f"quotes[{i}].passage -> {pid} is not among this claim's passages")
            continue
        p = ids.get(pid)
        if p is None or p.prefix != "p":
            errs.append(f"quotes[{i}].passage -> {pid} is not a passage")
            continue
        if not norm(q["original"]):
            errs.append(f"quotes[{i}].original is empty")
        elif norm(q["original"]) not in norm(p.meta.get("original")):
            errs.append(f"quotes[{i}].original is not inside the original of {pid} (CHARTER.md P1)")
        if p.meta.get("translation") and not norm(q.get("translation")):
            errs.append(f"quotes[{i}] needs the translation, since {pid} has one")
        elif q.get("translation") and norm(q["translation"]) not in norm(p.meta.get("translation")):
            errs.append(f"quotes[{i}].translation is not inside the translation of {pid} (CHARTER.md P1)")
        for key in q:
            if key not in ("passage", "original", "translation"):
                errs.append(f"quotes[{i}] has an unknown key {key!r}")
    return errs


def check_argument(n: Node) -> list[str]:
    """An argument has premises and a conclusion; `checked` needs a `form:` that passes."""
    errs: list[str] = []
    prem = as_list(n.meta.get("premises"))
    if not prem or not n.meta.get("conclusion"):
        errs.append("an argument needs premises and a conclusion")
    form = n.meta.get("form")
    if form is None:
        if n.status == "checked":
            errs.append("status checked requires a form: block that passes tools/validity.py")
        return errs
    verdict, ferrs = validity.check_form(form)
    errs.extend(f"form: {e}" for e in ferrs)
    if verdict is not None:
        if not verdict.valid:
            errs.append(f"form is {verdict}")
        if len(form["premises"]) != len(prem):
            errs.append(f"form has {len(form['premises'])} premises but the argument lists {len(prem)}; they must correspond one to one")
    return errs


def check_comparison(n: Node, ids: dict) -> list[str]:
    """A comparison (MODEL.md, Comparisons): at least two thinkers, a one-sentence question, rows
    of positions per thinker (claims or arguments of that thinker), and shared premises whose
    claims belong to different thinkers and name each other in shares_premise_with."""
    errs: list[str] = []
    thinkers = [str(t) for t in as_list(n.meta.get("thinkers"))]
    if len(thinkers) < 2:
        errs.append("a comparison needs at least two thinkers")
    if len(set(thinkers)) != len(thinkers):
        errs.append("thinkers lists a thinker twice")
    for t in thinkers:
        if t not in ids or ids[t].prefix != "t":
            errs.append(f"thinkers -> {t} is not a thinker in the map")
    if not n.meta.get("question"):
        errs.append("a comparison needs a one-sentence question")
    rows = as_list(n.meta.get("rows"))
    if not rows:
        errs.append("a comparison needs rows: each a question and the positions per thinker")
    placed: set[str] = set()
    cell_claims: list[str] = []
    for i, row in enumerate(rows):
        if not isinstance(row, dict) or not row.get("question"):
            errs.append(f"rows[{i}] needs a question")
            continue
        pos = row.get("positions") or {}
        placed.update(str(t) for t in pos if as_list(pos[t]))
        cell_claims.extend(str(c) for v in pos.values() for c in as_list(v))
        if not isinstance(pos, dict) or not pos:
            errs.append(f"rows[{i}] needs positions keyed by thinker id")
            continue
        for t, cids in pos.items():
            if t not in thinkers:
                errs.append(f"rows[{i}].positions: {t} is not among this comparison's thinkers")
            for cid in as_list(cids):
                c = ids.get(str(cid))
                if c is None:
                    errs.append(f"rows[{i}].positions.{t} -> {cid} does not resolve")
                elif c.prefix not in ("c", "a"):
                    errs.append(f"rows[{i}].positions.{t} -> {cid} is not a claim or argument")
                elif str(c.meta.get("thinker")) != t:
                    errs.append(f"rows[{i}].positions.{t} -> {cid} belongs to {c.meta.get('thinker')}")
    for t in thinkers:
        if t not in placed:
            errs.append(f"thinker {t} has no position in any row")
    # the body says what depends on each reading of a cell's claim (MODEL.md, Comparisons)
    for r in ids.values():
        if r.prefix == "r" and str(r.meta.get("reading_of")) in cell_claims and f"/r/{r.id[2:]}/" not in n.body:
            errs.append(f"the body does not link {r.id}, a reading of a claim in the table")
    # every »...« quotation in the body or a note is found in a listed passage (CHARTER.md P1)
    listed = [ids[str(pid)] for pid in as_list(n.meta.get("passages")) if str(pid) in ids]
    texts: list[str] = []
    for p in listed:
        texts.append(" ".join(str(p.meta.get("original", "")).split()))
        texts.append(" ".join(str(p.meta.get("ref", "")).split()))
    sources = n.body + " " + " ".join(str(r.get("note", "")) for r in rows if isinstance(r, dict))
    for q in re.findall(r"»([^»«]+)«", " ".join(sources.split())):
        pieces = [x.strip(" ,;:") for x in q.split("...")]
        pieces = [x for x in pieces if x]
        if not any(all(piece in t for piece in pieces) for t in texts):
            errs.append(f"the quotation »{q}« is not inside any listed passage (CHARTER.md P1)")
    for i, sh in enumerate(as_list(n.meta.get("shared"))):
        if not isinstance(sh, dict) or not sh.get("premise"):
            errs.append(f"shared[{i}] needs the premise in one sentence")
            continue
        cl = [str(c) for c in as_list(sh.get("claims"))]
        if len(cl) < 2:
            errs.append(f"shared[{i}] needs at least two claims")
        for c in cl:
            if c not in ids:
                errs.append(f"shared[{i}].claims -> {c} does not resolve")
            elif ids[c].prefix != "c":
                errs.append(f"shared[{i}].claims -> {c} is not a claim")
        cited = {str(pid) for c in cl if c in ids for pid in as_list(ids[c].meta.get("passages"))}
        owners = {str(ids[c].meta.get("thinker")) for c in cl if c in ids}
        if len(cl) >= 2 and len(owners) < 2:
            errs.append(f"shared[{i}]: the claims must belong to different thinkers")
        for a in cl:
            for b in cl:
                if a != b and a in ids and b not in as_list(ids[a].meta.get("shares_premise_with")):
                    errs.append(f"shared[{i}]: {a} does not name {b} in shares_premise_with")
        for pid in as_list(sh.get("passages")):
            if str(pid) not in ids:
                errs.append(f"shared[{i}].passages -> {pid} does not resolve")
            elif str(pid) not in cited:
                errs.append(f"shared[{i}].passages -> {pid} is cited by none of the shared claims")
    return errs


def check_filing_issue(n: Node) -> list[str]:
    """`issue:` on a d- or v- node is the number of the GitHub issue it was filed as, by
    which the inbox workflow tells the filer where their record is (MODEL.md, Filing)."""
    v = n.meta.get("issue")
    if v is not None and (not isinstance(v, int) or isinstance(v, bool) or v < 1):
        return ["issue must be the number of the GitHub issue the filing was made as"]
    return []


def check_dispute(n: Node, ids: dict) -> list[str]:
    errs: list[str] = check_filing_issue(n)
    for key in ("target", "disputant", "date", "kind", "contested_claim", "alternative", "outcome"):
        if not n.meta.get(key):
            errs.append(f"a dispute needs {key}")
    if n.meta.get("target") and str(n.meta["target"]) not in ids:
        errs.append(f"target -> {n.meta['target']} does not resolve")
    if n.meta.get("kind") and n.meta["kind"] not in DISPUTE_KINDS:
        errs.append(f"kind must be one of {DISPUTE_KINDS}")
    if n.meta.get("outcome") and n.meta["outcome"] not in DISPUTE_OUTCOMES:
        errs.append(f"outcome must be one of {DISPUTE_OUTCOMES}")
    if not as_list(n.meta.get("passages")):
        errs.append("a dispute without a passage reference is returned, not published (DISPUTES.md)")
    for key in ("reply", "counter", "ruling"):
        v = n.meta.get(key)
        if v is not None and (not isinstance(v, dict) or not v.get("date") or not v.get("text")):
            errs.append(f"{key} needs date and text")
    if n.meta.get("outcome") in ("argued", "conceded", "contested", "resolved", "escalated") and not n.meta.get("reply"):
        errs.append(f"outcome {n.meta['outcome']} requires the project's reply")
    return errs


def check_attestation(n: Node, ids: dict) -> list[str]:
    errs: list[str] = check_filing_issue(n)
    for key in ("target", "attester", "date", "statement"):
        if not n.meta.get(key):
            errs.append(f"an attestation needs {key}")
    if n.meta.get("target") and str(n.meta["target"]) not in ids:
        errs.append(f"target -> {n.meta['target']} does not resolve")
    if n.meta.get("sides_with") and str(n.meta["sides_with"]) not in ids:
        errs.append(f"sides_with -> {n.meta['sides_with']} does not resolve")
    return errs


def about_node(nodes: list[Node], target: str, prefix: str) -> list[Node]:
    return [m for m in nodes if m.prefix == prefix and str(m.meta.get("target")) == target]


def check_human_record(n: Node, nodes: list[Node]) -> list[str]:
    """Status and the contested flag must agree with the attestations and disputes on file."""
    errs: list[str] = []
    vs = sorted(m.id for m in about_node(nodes, n.id, "v"))
    ds = sorted(m.id for m in about_node(nodes, n.id, "d"))
    if sorted(map(str, as_list(n.meta.get("verified_by")))) != vs:
        errs.append(f"verified_by must list exactly the attestations that target this node: {vs or 'none'}")
    if sorted(map(str, as_list(n.meta.get("disputes")))) != ds:
        errs.append(f"disputes must list exactly the disputes that target this node: {ds or 'none'}")
    if n.status == "attested" and len(vs) < 1:
        errs.append("status attested needs one attestation on file")
    if n.status == "established" and len(vs) < 2:
        errs.append("status established needs two attestations on file")
    open_contest = any(m.meta.get("outcome") == "contested" for m in about_node(nodes, n.id, "d"))
    if open_contest != bool(n.meta.get("contested")):
        errs.append("contested must be true exactly while a dispute on this node has outcome contested")
    return errs


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


def kicker_status(n: Node) -> str:
    """The status for a kicker line: the word, contested if so, the qualification in full on
    a checked comparison; on a node without a status, nothing."""
    return status_line(n) if n.status else ""


def render_argument(n: Node, ids: dict[str, Node]) -> str:
    """The argument's premises, inference and conclusion as a numbered list, then its form."""
    prem = as_list(n.meta.get("premises"))
    if not prem and not n.meta.get("conclusion"):
        return ""
    rows = []
    for i, p in enumerate(prem, 1):
        if isinstance(p, dict) and "assumption" in p:
            rows.append(f'<li><span class="n">P{i}</span><span class="assumption"><em>Assumption.</em> {inline(str(p["assumption"]))}</span></li>')
        else:
            cid = p.get("claim") if isinstance(p, dict) else p
            rows.append(f'<li><span class="n">P{i}</span><span>{link(ids, cid)}</span></li>')
    if n.meta.get("inference"):
        rows.append(f'<li><span class="n">Infer.</span><span>{inline(str(n.meta["inference"]))}</span></li>')
    if n.meta.get("conclusion"):
        rows.append(f'<li class="conclusion"><span class="n">C</span><span>{link(ids, n.meta["conclusion"])}</span></li>')
    return '<h2 class="label">The argument</h2>\n<ol class="argument">' + "".join(rows) + "</ol>" + render_form(n)


def render_record(n: Node, ids: dict[str, Node]) -> str:
    """The human record on a node: the disputes and attestations that target it, in full,
    and its earlier versions (CHARTER.md P4)."""
    record = ""
    vs = [m for m in ids.values() if m.prefix == "v" and str(m.meta.get("target")) == n.id]
    ds = [m for m in ids.values() if m.prefix == "d" and str(m.meta.get("target")) == n.id]
    if vs or ds:
        record = '<section class="record">' + "".join(render_dispute(d, ids) for d in sorted(ds, key=lambda m: str(m.meta.get("date")))) \
            + "".join(render_attestation(v, ids) for v in sorted(vs, key=lambda m: str(m.meta.get("date")))) + "</section>"
    versions = as_list(n.meta.get("versions"))
    if versions:
        items = "".join(
            f"<li><strong>{esc(v.get('date'))}.</strong> {inline(str(v.get('reason')))}"
            + (f" Credit: {link(ids, v['credit'])}." if v.get("credit") else "")
            + f" Superseded statement: <q>{inline(str(v.get('statement')))}</q></li>" for v in versions)
        record += f'<section class="versions"><h2>Earlier versions</h2><p>This is version {len(versions) + 1}. Earlier versions, newest first, stay here at the same address (CHARTER.md P4).</p><ol>{items}</ol></section>'
    return record


def meta_line(n: Node, ids: dict[str, Node]) -> str:
    """The apparatus note at the foot of every node page: address, provenance, the chain of
    versions, who verified it, the disputes, and the filing links (MODEL.md, Filing)."""
    _, _, has_status = TYPES[n.prefix]
    chain = []
    if n.meta.get("supersedes"):
        chain.append("Supersedes " + link(ids, n.meta["supersedes"]))
    if n.meta.get("superseded_by"):
        chain.append("Superseded by " + link(ids, n.meta["superseded_by"]))
    disputes = as_list(n.meta.get("disputes"))
    verified = as_list(n.meta.get("verified_by"))
    line = " · ".join(
        [f"Permanent address: {esc(n.url)}", f"Produced by {esc(n.meta.get('produced_by'))}"]
        + chain
        + (["Verified by " + (", ".join(link(ids, i) for i in verified) if verified else "nobody yet")] if has_status else [])
        + (["Disputes: " + (", ".join(link(ids, d) for d in disputes) if disputes else "none")] if has_status or n.prefix in ("p", "r") else [])
    )
    filing = render_filing(n)
    if filing:
        line += '</p><p class="apparatus-note">' + filing  # the filing links keep the apparatus setting
    return line


def href_to_url(h: str) -> str:
    """The site path of a relative href, printed after the link on paper (DESIGN.md, Colour,
    space and pages, Print)."""
    if h.startswith("http") or h.startswith("#"):
        return ""
    return "/" + h.lstrip("./")


def contents(items: list[tuple[str, str, str]]) -> str:
    """The contents list component: (href, name, note) per entry; the note at the right."""
    out = []
    for h, name, note in items:
        u = href_to_url(h)
        data = f' data-url="{esc(u)}"' if u else ""
        out.append(f'<li><span class="name"><a href="{h}"{data}>{name}</a></span><span class="note">{note}</span></li>')
    return '<ul class="contents">' + "".join(out) + "</ul>"


def node_entry(m: Node, note: str | None = None) -> tuple[str, str, str]:
    """A node as a contents-list entry: its title, and at the right its status word, or the
    note given, or its type."""
    return (href(m), esc(m.title), note if note is not None else (status_html(m) or esc(TYPES[m.prefix][0])))


def node_lists(label_items: list[tuple[str, list[tuple[str, str, str]]]]) -> str:
    """Section labels and contents lists; an empty list is omitted (DESIGN.md P6)."""
    return "\n".join(f'<h2 class="label">{esc(label)}</h2>{contents(items)}' for label, items in label_items if items)


def by_thinker(ids: dict[str, Node], tid: str, prefix: str) -> list[Node]:
    return [m for m in ids.values() if m.prefix == prefix and str(m.meta.get("thinker")) == tid]


def citing(ids: dict[str, Node], pid: str) -> list[Node]:
    """Every node that cites a passage, in the build's order."""
    return [m for m in ids.values() if m.prefix in ("c", "a", "x", "r", "d") and pid in [str(x) for x in as_list(m.meta.get("passages"))]]


def cites_any(m: Node, pids: set[str]) -> bool:
    return any(str(pid) in pids for pid in as_list(m.meta.get("passages")))


def render_node(n: Node, ids: dict[str, Node]) -> str:
    """One node's page (DESIGN.md, Colour, space and pages, Templates): the comparison on the
    page width; a claim, argument or reading on the page width in two columns, the apparatus
    beside the claim; a thinker, work, passage, dispute or attestation at the reading width."""
    tname, _, has_status = TYPES[n.prefix]
    body = "" if n.prefix in ("d", "v") else markdown(n.body)
    record = render_record(n, ids)
    if n.prefix == "x":
        table, shown = render_comparison(n, ids)
        return fill(
            template("comparison.html"),
            title=esc(n.title), status=status_line(n), question=inline(str(n.meta.get("question", ""))),
            statement=f'<p class="statement">{inline(str(n.meta["statement"]))}</p>' if n.meta.get("statement") else "",
            table=table, texts=render_texts(n, ids, shown), shared=render_shared(n, ids),
            body=body + record, links=deps_html(n, ids), meta=meta_line(n, ids),
        )
    if n.prefix in ("c", "a", "r"):
        # Node template: the claim and its statement in the text column, the status, the source
        # and the passage pairs in the apparatus column; the prose and the lists beneath.
        statement = f'<p class="statement">{inline(str(n.meta["statement"]))}</p>' if n.meta.get("statement") else ""
        statement += render_quotes(n, ids)
        if n.prefix == "r":
            rows = []
            if n.meta.get("reading_of"):
                rows.append(f'<dt>A reading of</dt><dd>{link(ids, n.meta["reading_of"])}</dd>')
            if n.meta.get("literature"):
                rows.append("<dt>Literature</dt>" + "".join(f"<dd>{inline(str(x))}</dd>" for x in as_list(n.meta["literature"])))
            if rows:
                statement += f'<dl class="facts">{"".join(rows)}</dl>'
        apparatus = []
        if has_status:
            apparatus.append(f'<p><span class="term">Status</span> {status_html(n)}</p>')
        if n.meta.get("thinker") and str(n.meta["thinker"]) in ids:
            apparatus.append(f'<p><span class="term">Thinker</span> <span class="quiet">{link(ids, n.meta["thinker"])}</span></p>')
        pairs = [render_pair(ids[str(pid)], ids) for pid in as_list(n.meta.get("passages")) if str(pid) in ids]
        if pairs:
            apparatus.append(f'<h2 class="label">{"The passage" if len(pairs) == 1 else "The passages"}</h2>' + "".join(pairs))
        readings = [r for r in ids.values() if r.prefix == "r" and str(r.meta.get("reading_of")) == n.id]
        if readings:
            apparatus.append('<h2 class="label">Readings</h2>' + contents([node_entry(r, "reading") for r in readings]))
        return fill(
            template("node.html"),
            type=esc(tname), status=kicker_status(n) or esc(tname), title=esc(n.title),
            statement=statement, argument=render_argument(n, ids) if n.prefix == "a" else "",
            apparatus="\n".join(apparatus), body=body + record, links=deps_html(n, ids), meta=meta_line(n, ids),
        )
    # Reading-width templates: thinker, work, passage, dispute, attestation.
    kicker, lead, top, lists = f'<span class="type">{esc(tname)}</span>', "", "", ""
    if n.prefix == "t":
        if n.meta.get("dates"):
            kicker += f' · <span class="dates">{esc(n.meta["dates"])}</span>'
        top = render_facts(n, ids, skip=("dates",))
        works = sorted(by_thinker(ids, n.id, "w"), key=lambda m: str(m.meta.get("year", "")))
        xs = [m for m in ids.values() if m.prefix == "x" and n.id in [str(t) for t in as_list(m.meta.get("thinkers"))]]
        lists = node_lists([
            ("Works", [node_entry(w, esc(w.meta.get("year", ""))) for w in works]),
            ("Comparisons", [node_entry(x) for x in xs]),
            ("Arguments", [node_entry(a) for a in by_thinker(ids, n.id, "a")]),
            ("Claims", [node_entry(c) for c in by_thinker(ids, n.id, "c")]),
            ("Readings", [node_entry(r, "reading") for r in by_thinker(ids, n.id, "r")]),
        ])
    elif n.prefix == "w":
        th = ids.get(str(n.meta.get("thinker")))
        if th:
            kicker += f' · <span class="quiet">{link(ids, th.id)}</span>'
        if n.meta.get("year"):
            kicker += f' · <span class="dates">{esc(n.meta["year"])}</span>'
        top = render_facts(n, ids, skip=("thinker", "year"))
        ps = [m for m in ids.values() if m.prefix == "p" and str(m.meta.get("work")) == n.id]
        pids = {p.id for p in ps}
        lists = node_lists([
            ("Passages", [node_entry(p, esc(p.meta.get("ref", ""))) for p in ps]),
            ("Claims", [node_entry(c) for c in ids.values() if c.prefix == "c" and cites_any(c, pids)]),
            ("Arguments", [node_entry(a) for a in ids.values() if a.prefix == "a" and cites_any(a, pids)]),
        ])
    elif n.prefix == "p":
        work = ids.get(str(n.meta.get("work")))
        kicker += (f' · <span class="quiet">{link(ids, work.id)}</span>' if work else "") + f' · <span class="ref">{esc(n.meta.get("ref"))}</span>'
        top = render_pair(n, ids, anchor=False, link_ref=False)
        lists = node_lists([("Cited by", [node_entry(m) for m in citing(ids, n.id)])])
    elif n.prefix == "d":
        kicker += f' · <span class="status-word">{esc(n.meta.get("outcome"))}</span>'
        top = render_dispute_page(n, ids)
    elif n.prefix == "v":
        target = ids.get(str(n.meta.get("target")))
        kicker += (f' · on <span class="quiet">{link(ids, target.id)}</span>' if target else "")
        top = render_attestation(n, ids, full=True)
    return fill(
        template("measure.html"),
        kicker=kicker, title=esc(n.title), lead=lead, top=top, body=body + record, lists=lists, meta=meta_line(n, ids),
    )


def render_dispute_page(d: Node, ids: dict[str, Node]) -> str:
    """The dispute template: the contested node quoted with its passage pair, then the exchange
    as dated, signed turns, the project's one reply marked the map replies (DISPUTES.md)."""
    m = d.meta
    target = ids.get(str(m.get("target")))
    out = []
    if target is not None:
        out.append(f'<h2 class="label">The node contested</h2><p class="statement"><span class="quiet">{link(ids, target.id)}</span></p>')
        if target.meta.get("statement"):
            out.append(f'<p class="statement">{inline(str(target.meta["statement"]))}</p>')
        first = next((ids[str(pid)] for pid in as_list(target.meta.get("passages")) if str(pid) in ids), None)
        if first is not None:
            out.append(render_pair(first, ids, anchor=False))
    who = esc(m.get("disputant")) + (f", {esc(m['affiliation'])}" if m.get("affiliation") else "")
    turns = [f'<div class="turn"><p class="turn-head"><span class="who">{who}</span> · {esc(m.get("date"))} · {esc(m.get("kind"))}</p>'
             f'<p><strong>The claim contested.</strong> <q>{inline(str(m.get("contested_claim")))}</q></p>'
             f'<p><strong>The alternative reading.</strong> {inline(str(m.get("alternative")))}</p>'
             '<p><strong>Passages.</strong> ' + ", ".join(link(ids, x) if str(x) in ids else esc(x) for x in as_list(m.get("passages"))) + "</p>"
             + (('<p><strong>Literature.</strong> ' + "; ".join(inline(str(x)) for x in as_list(m["literature"])) + "</p>") if m.get("literature") else "")
             + (markdown(d.body) if d.body.strip() else "") + "</div>"]
    for key, label in (("reply", "the map replies"), ("counter", f"{esc(m.get('disputant'))} counters"), ("ruling", "Ruling")):
        v = m.get(key)
        if v:
            turns.append(f'<div class="turn"><p class="turn-head"><span class="who">{label}</span> · {esc(v.get("date"))}</p><p>{inline(str(v.get("text")))}'
                         + (f" Attestation: {link(ids, v['attestation'])}." if v.get("attestation") else "") + "</p></div>")
    out.append(f'<h2 class="label">The exchange</h2><div class="exchange">{"".join(turns)}</div>'
               f'<p class="small">Outcome: <span class="status-word">{esc(m.get("outcome"))}</span>.</p>')
    return "".join(out)


def status_html(n: Node) -> str:
    """The status word component: the word in small caps, contested in the one warning colour,
    and on a checked comparison the fact of the qualification (CHARTER.md P2, DESIGN.md P4)."""
    if not n.status:
        return ""
    out = f'<span class="status-word">{esc(n.status)}</span>'
    if n.meta.get("contested"):
        out += ', <span class="status-word contested">contested</span>'
    if n.meta.get("status_note"):
        out += '<span class="status-more">, with a qualification on the page</span>'
    return out


def status_line(n: Node) -> str:
    """The status for the label line above a title: the word, contested if so, and the
    qualification in full on a checked comparison (MODEL.md, Checked comparisons)."""
    out = f'<span class="status-word">{esc(n.status)}</span>'
    if n.meta.get("contested"):
        out += ', <span class="status-word contested">contested</span>'
    if n.meta.get("status_note"):
        out += f', <span class="qualification">{inline(str(n.meta["status_note"]))}</span>'
    return out


def type_word(n: Node) -> str:
    return TYPES[n.prefix][0].capitalize()


def render_pair(p: Node, ids: dict[str, Node], anchor: bool = True, link_ref: bool = True) -> str:
    """The passage pair component: the original first, in its script and serif italic, the
    translation beneath, the reference line last (DESIGN.md P1, P9)."""
    work = ids.get(str(p.meta.get("work")))
    work_title = esc(work.title) if work else esc(p.meta.get("work"))
    src = p.meta.get("source") or (work.meta.get("source") if work else "")
    lang = esc(p.meta.get("lang", ""))
    ref = f'<a href="{href(p)}">{work_title}, {esc(p.meta.get("ref"))}</a>' if link_ref else f'{work_title}, {esc(p.meta.get("ref"))}'
    if src:
        ref += f" · {esc(src)}"
    if p.meta.get("translation"):
        ref += f' · <span class="by">{esc(p.meta.get("translation_by", "translation"))}</span>'
    return (f'<div class="pair" lang="{lang}"' + (f' id="{esc(p.id)}"' if anchor else "") + ">"
            f'<p class="pair-original verse" lang="{lang}">{esc(p.meta.get("original"))}</p>'
            + (f'<p class="pair-translation" lang="en">{esc(p.meta.get("translation"))}</p>' if p.meta.get("translation") else "")
            + f'<p class="pair-ref" lang="en">{ref}</p></div>')


def row_passages(row: dict, thinkers: list[Node], ids: dict[str, Node]) -> list[tuple[Node, list[Node]]]:
    """For one row of a comparison: each thinker in column order with the passages its
    positions cite, in citation order, each passage once."""
    out = []
    for t in thinkers:
        seen: list[Node] = []
        for cid in as_list((row.get("positions") or {}).get(t.id)):
            c = ids.get(str(cid))
            for pid in as_list(c.meta.get("passages")) if c else []:
                p = ids.get(str(pid))
                if p is not None and p not in seen:
                    seen.append(p)
        out.append((t, seen))
    return out


def render_comparison(n: Node, ids: dict[str, Node]) -> tuple[str, set[str]]:
    """The comparison grid (DESIGN.md P5): a table, one column per thinker with th cells for
    the thinkers, each row's question a th across the width, each cell the thinker's
    statements (the first at the lead size), each with the type word linking to the node,
    the passage references linking to the pair shown beneath the grid, the status word and
    the readings. Returns the table and the ids of the passages the cells cite, which the
    texts section shows."""
    thinkers = [ids[str(t)] for t in as_list(n.meta.get("thinkers")) if str(t) in ids]
    head = "".join(f'<th scope="col"><span class="grid-name">{esc(t.title)}</span>'
                   + (f'<span class="grid-dates">{esc(t.meta["dates"])}</span>' if t.meta.get("dates") else "") + "</th>" for t in thinkers)
    shown: set[str] = set()
    groups = []
    for i, row in enumerate(as_list(n.meta.get("rows")), 1):
        cells = []
        for t in thinkers:
            items = []
            for cid in as_list((row.get("positions") or {}).get(t.id)):
                c = ids.get(str(cid))
                if c is None:
                    continue
                refs = []
                for pid in as_list(c.meta.get("passages")):
                    p = ids.get(str(pid))
                    if p is not None:  # the passage is one tap away, beneath the grid (DESIGN.md P1)
                        shown.add(p.id)
                        refs.append(f'<a href="#{esc(p.id)}">{esc(p.title)}</a>')
                readings = [r for r in ids.values() if r.prefix == "r" and str(r.meta.get("reading_of")) == c.id]
                items.append(f'<li><p class="cell-statement">{inline(str(c.meta.get("statement", "")))}</p>'
                             f'<p class="cell-ref"><a href="{href(c)}">{type_word(c)}</a>'
                             + (" · " + "; ".join(refs) if refs else "")
                             + " · " + status_html(c)
                             + (" · readings: " + ", ".join(f'<a href="{href(r)}">{esc(r.title)}</a>' for r in readings) if readings else "") + "</p></li>")
            cells.append(f'<td data-thinker="{esc(t.title)}">' + (f'<ul class="cell">{"".join(items)}</ul>' if items else '<p class="cell-empty">No position in the map.</p>') + "</td>")
        groups.append(f'<tbody id="row-{i}"><tr class="grid-q"><th scope="rowgroup" colspan="{len(thinkers)}"><span class="n">{i}</span>{inline(str(row.get("question", "")))}</th></tr>'
                      f'<tr class="grid-cells">{"".join(cells)}</tr></tbody>')
    box = "grid-box wide" if len(thinkers) > 3 else "grid-box"
    table = f'<div class="{box}"><table class="grid" data-thinkers="{len(thinkers)}"><thead><tr>{head}</tr></thead>{"".join(groups)}</table></div>'
    return table, shown


def render_texts(n: Node, ids: dict[str, Node], shown: set[str]) -> str:
    """Beneath the grid, for each row: the row's note in the text column and the passage
    pairs of that row in the apparatus column, grouped by thinker, each passage shown once
    under the first row that cites it and anchored by its id; a passage shown in an earlier
    row is given as one line linking there. The passages the comparison lists that no cell
    cites follow as a last group, since the body quotes them (CHARTER.md P1)."""
    thinkers = [ids[str(t)] for t in as_list(n.meta.get("thinkers")) if str(t) in ids]
    placed: dict[str, int] = {}
    out = []
    for i, row in enumerate(as_list(n.meta.get("rows")), 1):
        groups = []
        for t, ps in row_passages(row, thinkers, ids):
            if not ps:
                continue
            parts = []
            for p in ps:
                if p.id in placed:
                    parts.append(f'<p class="pair-again"><a href="#{esc(p.id)}">{esc(p.title)}</a>, shown at row {placed[p.id]}</p>')
                else:
                    placed[p.id] = i
                    parts.append(render_pair(p, ids))
            groups.append(f'<div class="pair-group" id="{esc(t.id[2:])}-{i}"><h4 class="label">{esc(t.title)}</h4>{"".join(parts)}</div>')
        # The passages are the text of this section and take the text column; the row's note
        # is the map's commentary and sits in the apparatus column, with the way back.
        note = f'<p class="text-i">{inline(str(row["note"]))}</p>' if row.get("note") else ""
        back = f'<p><a href="#row-{i}">Back to row {i} of the grid</a></p>'
        out.append(f'<section class="row-texts" id="texts-{i}"><h3 class="row-q"><span class="n">{i}</span>{inline(str(row.get("question", "")))}</h3>'
                   f'<div class="two-col"><div class="text">{"".join(groups)}</div><div class="apparatus">{note}{back}</div></div></section>')
    rest = [ids[str(pid)] for pid in as_list(n.meta.get("passages")) if str(pid) in ids and str(pid) not in placed]
    if rest:
        by_thinker: dict[str, list[Node]] = {}
        for p in rest:
            work = ids.get(str(p.meta.get("work")))
            by_thinker.setdefault(str(work.meta.get("thinker")) if work else "", []).append(p)
        groups = []
        for t in thinkers:
            if t.id in by_thinker:
                groups.append(f'<div class="pair-group"><h4 class="label">{esc(t.title)}</h4>{"".join(render_pair(p, ids) for p in by_thinker[t.id])}</div>')
        out.append('<section class="row-texts" id="texts-more"><h3 class="row-q">Cited in the shared premises and the text</h3>'
                   f'<div class="two-col"><div class="text">{"".join(groups)}</div><div class="apparatus"></div></div></section>')
    return "\n".join(out)


def render_shared(n: Node, ids: dict[str, Node]) -> str:
    """The premises shared (MODEL.md, Comparisons): each in one sentence, with the claims that
    assert it and the passages where each does."""
    items = []
    for sh in as_list(n.meta.get("shared")):
        claims = ", ".join(link(ids, c) for c in as_list(sh.get("claims")))
        pas = ", ".join(f'<a href="#{esc(p)}">{esc(ids[str(p)].title)}</a>' if str(p) in ids else esc(p) for p in as_list(sh.get("passages")))
        items.append(f'<li><p class="shared-premise">{inline(str(sh.get("premise", "")))}</p>'
                     f'<p class="shared-held">Held in {claims}.' + (f" Passages: {pas}." if pas else "") + "</p></li>")
    return f'<h2 class="label">Premises shared</h2><ol class="shared">{"".join(items)}</ol>' if items else ""


def deps_html(n: Node, ids: dict[str, Node]) -> str:
    """The dependency lists (DESIGN.md P6): a section label and a contents list for each
    relation the node has; an empty relation is omitted."""
    out = []
    for key in LINK_FIELDS:
        targets = [ids[str(t)] for t in as_list(n.meta.get(key)) if str(t) in ids]
        if targets:
            items = "".join(f'<li><span class="name"><a href="{href(t)}">{esc(t.title)}</a></span><span class="note">{status_html(t) or esc(TYPES[t.prefix][0])}</span></li>' for t in targets)
            out.append(f'<h2 class="label">{esc(key.replace("_", " ").capitalize())}</h2><ul class="contents">{items}</ul>')
    return "\n".join(out)


def render_filing(n: Node) -> str:
    """The two links by which a reader files a dispute or an attestation on this node
    (DISPUTES.md: "Filed through the form on the node page"; MODEL.md, Filing). Plain links
    to the two issue forms with the node's id prefilled, no script, no button (DESIGN.md 2, 7).
    A dispute may be filed on any claim, argument, passage, reading or comparison; an
    attestation only on what carries a status. Thinkers, works, disputes and attestations
    themselves get neither."""
    from urllib.parse import quote_plus
    parts = []
    if n.prefix in ("c", "a", "p", "r", "x"):
        parts.append(f'<a href="{REPO}/issues/new?template=dispute.yml&amp;title={quote_plus("Dispute: " + n.id)}&amp;node={quote_plus(n.id)}">Dispute this node</a>')
    if n.prefix in ("c", "a", "x"):
        parts.append(f'<a href="{REPO}/issues/new?template=attestation.yml&amp;title={quote_plus("Attestation: " + n.id)}&amp;node={quote_plus(n.id)}">Attest this node</a>')
    if not parts:
        return ""
    return " · ".join(parts) + f' — under your real name, citing a passage; the form is a GitHub issue, and what you file is published on this page under <a href="{REPO}/blob/main/DISPUTES.md">DISPUTES.md</a>.'


def render_quotes(n: Node, ids: dict[str, Node]) -> str:
    """The load-bearing sentence in the original beside the project's translation, under the
    statement (DESIGN.md 9; settled 2026-10-10). The passage itself stays in the aside; the
    reference links to it there."""
    blocks = []
    for q in as_list(n.meta.get("quotes")):
        if not isinstance(q, dict):
            continue
        p = ids.get(str(q.get("passage")))
        if p is None:
            continue
        work = ids.get(str(p.meta.get("work")))
        work_title = esc(work.title) if work else esc(p.meta.get("work"))
        lang = esc(p.meta.get("lang", ""))
        blocks.append(
            f'<div class="quote">'
            f'<p class="quote-original" lang="{lang}">{esc(q.get("original"))}</p>'
            + (f'<p class="quote-translation" lang="en">{esc(q.get("translation"))}</p>' if q.get("translation") else "")
            + f'<p class="quote-ref"><a href="#{esc(p.id)}">{work_title} {esc(p.meta.get("ref"))}</a></p>'
            "</div>")
    return "".join(blocks)


def render_form(n: Node) -> str:
    form = n.meta.get("form")
    if not form:
        return '<p class="form note">No form has been given for this argument yet, so it cannot be <span class="sc">checked</span>.</p>'
    verdict, _ = validity.check_form(form)
    glosses = "".join(f"<li><code>{esc(k)}</code> {inline(str(v))}</li>" for k, v in form["atoms"].items())
    prem = "".join(f"<li><span class=\"n\">P{i}</span><code>{esc(validity.show(validity.parse(f)))}</code></li>" for i, f in enumerate(form["premises"], 1))
    conc = f"<li class=\"conclusion\"><span class=\"n\">C</span><code>{esc(validity.show(validity.parse(form['conclusion'])))}</code></li>"
    return (f'<div class="form"><h3>Form</h3><ul class="atoms">{glosses}</ul><ol class="argument">{prem}{conc}</ol>'
            f'<p class="note">Machine check, truth table: {esc(verdict)}. The check says nothing about whether the premises are true or faithful to the passage; only a named human can (DISPUTES.md).</p></div>')


def render_facts(n: Node, ids: dict[str, Node], skip: tuple = ()) -> str:
    """A thinker or a work: its front-matter facts as a short definition list."""
    rows = []
    for key in ("dates", "tradition", "thinker", "year", "edition", "scheme", "source", "editions"):
        v = n.meta.get(key)
        if not v or key in skip:
            continue
        if key == "thinker":
            val = link(ids, v)
        elif isinstance(v, list):
            val = "; ".join(inline(str(x)) for x in v)
        elif isinstance(v, dict):
            val = "; ".join(f"{esc(k)}: {inline(str(x))}" for k, x in v.items())
        else:
            val = inline(str(v))
        rows.append(f"<dt>{esc(key.capitalize())}</dt><dd>{val}</dd>")
    return f'<dl class="facts">{"".join(rows)}</dl>' if rows else ""


def render_dispute(d: Node, ids: dict[str, Node], full: bool = False) -> str:
    """A dispute, verbatim, with its exchange (DISPUTES.md steps 1–6)."""
    m = d.meta
    head = (f'<h2>Dispute {esc(d.id)}: {esc(m.get("kind"))}</h2>' if not full
            else f'<p class="statement">A {esc(m.get("kind"))} dispute on {link(ids, m.get("target"))}, filed {esc(m.get("date"))}.</p>')
    who = esc(m.get("disputant")) + (f", {esc(m['affiliation'])}" if m.get("affiliation") else "")
    parts = [head,
             f'<p><strong>{who}</strong>, {esc(m.get("date"))}. Outcome: <span class="sc">{esc(m.get("outcome"))}</span>.' + ("" if full else f' Permanent address: <a href="{href(d)}">{esc(d.url)}</a>.') + "</p>",
             f'<p><strong>The claim contested.</strong> <q>{inline(str(m.get("contested_claim")))}</q></p>',
             f'<p><strong>The alternative reading.</strong> {inline(str(m.get("alternative")))}</p>',
             "<p><strong>Passages.</strong> " + ", ".join(link(ids, x) if str(x) in ids else esc(x) for x in as_list(m.get("passages"))) + "</p>"]
    if m.get("literature"):
        parts.append("<p><strong>Literature.</strong> " + "; ".join(inline(str(x)) for x in as_list(m["literature"])) + "</p>")
    if d.body.strip() and full:
        parts.append(markdown(d.body))
    for key, label in (("reply", "The project replies"), ("counter", "The disputant counters"), ("ruling", "Ruling")):
        v = m.get(key)
        if v:
            parts.append(f'<p><strong>{label}, {esc(v.get("date"))}.</strong> {inline(str(v.get("text")))}' + (f" Attestation: {link(ids, v['attestation'])}." if v.get("attestation") else "") + "</p>")
    return "".join(parts)


def render_attestation(v: Node, ids: dict[str, Node], full: bool = False) -> str:
    m = v.meta
    who = esc(m.get("attester")) + (f", {esc(m['affiliation'])}" if m.get("affiliation") else "")
    head = (f'<h2>Attestation {esc(v.id)}</h2>' if not full
            else f'<p class="statement">An attestation of {link(ids, m.get("target"))}, {esc(m.get("date"))}.</p>')
    out = head + f'<p><strong>{who}</strong>, {esc(m.get("date"))}: <q>{inline(str(m.get("statement")))}</q>'
    if m.get("sides_with"):
        out += f" Sides with {link(ids, m['sides_with'])}."
    if not full:
        out += f' Permanent address: <a href="{href(v)}">{esc(v.url)}</a>.'
    return out + "</p>" + (markdown(v.body) if full and v.body.strip() else "")


def href(n: Node) -> str:
    return PREFIX + n.url[1:]


def link(ids: dict[str, Node], target, with_id: bool = False) -> str:
    t = ids.get(str(target))
    if t is None:
        return f'<span class="id">{esc(target)}</span>'
    idspan = f'<span class="id">{esc(t.id)}</span>' if with_id else ""
    return f'{idspan}<a href="{href(t)}" data-url="{esc(t.url)}">{esc(t.title)}</a>'


MENU = (("t", "Thinkers"), ("w", "Works"), ("x", "Comparisons"), ("d", "Disputes"), ("about", "About"))
SINGULAR = {"t": "thinker", "w": "work", "p": "passage", "c": "claim", "a": "argument", "r": "reading", "x": "comparison", "d": "dispute", "v": "attestation"}


def counts_html() -> str:
    """The colophon's counts line: every count a link to its index (the design brief, 2026-10-11)."""
    return " · ".join(f'<a href="{PREFIX}{p}/">{COUNTS.get(p, 0)} {SINGULAR[p] if COUNTS.get(p, 0) == 1 else TYPES[p][1].lower()}</a>' for p in TYPES)


def page(title: str, content: str, kind: str = "node", section: str = "", measure: bool = False, after: str = "") -> str:
    """One page: the running head with the menu (the current section marked), the body, the
    colophon with the counts. `kind` names the template for the body class; `measure` sets the
    reading width instead of the page width."""
    menu = " ".join(f'<a href="{PREFIX}{key}/"' + (' aria-current="page"' if key == section else "") + f">{label}</a>" for key, label in MENU)
    tab = title if title == "praemisse" else f"{title} · praemisse"  # the browser title; the front page is the name alone
    return fill(template("base.html"), title=esc(tab), content=content, root=PREFIX, palette=esc(CONFIG.get("palette", "a")),
                kind=kind, menu=menu, main_class="main-measure" if measure else "main-page", counts=counts_html(), after=after)


INDEX_LINES = {  # one line on what each list is, from MODEL.md, Node types
    "t": "A person: dates, tradition, the canonical editions used.",
    "w": "A text: edition, reference scheme, the source of the public-domain text.",
    "p": "A located span of a work: canonical reference, original text, translation.",
    "c": "A position a thinker holds, stated in one sentence, tied to one or more passages.",
    "a": "Premises, an inference form and a conclusion, tied to the passages where the argument is made.",
    "r": "One interpretation of a contested claim or argument, with the literature that holds it.",
    "x": "Two or more thinkers on one question: which claims align, which premises are shared, where they diverge.",
    "d": "Filed under DISPUTES.md: the node, the disputant, the date, the text, the replies, the outcome.",
    "v": "A named human's sign-off on a node against its passage.",
}


def index_note(m: Node, ids: dict[str, Node]) -> str:
    """The note at the right of an index entry: the status word where the node has one,
    else the fact that places it."""
    if m.status:
        return status_html(m)
    if m.prefix == "t":
        return esc(m.meta.get("dates", ""))
    if m.prefix == "w":
        th = ids.get(str(m.meta.get("thinker")))
        return (esc(th.title) + " · " if th else "") + esc(m.meta.get("year", ""))
    if m.prefix == "p":
        work = ids.get(str(m.meta.get("work")))
        return esc(work.title) if work else ""
    if m.prefix == "r":
        th = ids.get(str(m.meta.get("thinker")))
        return esc(th.title) if th else "reading"
    if m.prefix == "d":
        return f'<span class="status-word">{esc(m.meta.get("outcome"))}</span>'
    if m.prefix == "v":
        return esc(m.meta.get("date", ""))
    return esc(TYPES[m.prefix][0])


def render_index(prefix: str, nodes: list[Node], ids: dict[str, Node]) -> str:
    """An index page: the title with the count, one line on what the list is, the line naming
    all nine indexes, one contents list; an empty index says so in one sentence."""
    tname, plural, _ = TYPES[prefix]
    group = [n for n in nodes if n.prefix == prefix]
    nine = " · ".join(f'<a href="{PREFIX}{p}/"' + (' aria-current="page"' if p == prefix else "") + f">{pl}</a>" for p, (_, pl, _) in TYPES.items())
    head = (f'<h1 class="title">{esc(plural)} <span class="count">{len(group)}</span></h1>'
            f'<p class="lead">{esc(INDEX_LINES[prefix])}</p>'
            f'<p class="indexes">{nine}</p>')
    if not group:
        return head + f'<p class="prose">No {esc(tname)} is in the map yet.</p>'
    return head + contents([(href(m), esc(m.title), index_note(m, ids)) for m in group])


def render_front(nodes: list[Node], ids: dict[str, Node]) -> str:
    """The front page: the description, the status paragraph, the comparisons, Start here,
    the thinkers, how to dispute. The counts are in the colophon."""
    xs = [n for n in nodes if n.prefix == "x"]
    entries = []
    for x in xs:
        thinkers = ", ".join(esc(ids[str(t)].title) for t in as_list(x.meta.get("thinkers")) if str(t) in ids)
        entries.append(f'<li class="entry"><p class="entry-title"><a href="{href(x)}" data-url="{esc(x.url)}">{esc(x.title)}</a></p>'
                       f'<p class="entry-thinkers"><i>{thinkers}</i></p>'
                       f'<p class="entry-line">{inline(str(x.meta.get("question", "")))}</p>'
                       f'<p class="entry-status">{status_line(x)}</p></li>')
    comparisons = "".join(entries) if entries else '<li class="entry"><p class="entry-line">No comparison is in the map yet.</p></li>'
    start = [ids[str(i)] for i in as_list(CONFIG.get("start_here")) if str(i) in ids][:3]
    start_html = ""
    if start:
        items = "".join(f'<li><span class="name"><a href="{href(m)}" data-url="{esc(m.url)}">{esc(m.title)}</a></span>'
                        f'<span class="note">{esc(TYPES[m.prefix][0])} · {status_html(m)}</span></li>' for m in start)
        start_html = f'<h2 class="label">Start here</h2><ol class="contents">{items}</ol>'
    thinkers = contents([(href(t), esc(t.title), esc(t.meta.get("dates", ""))) for t in nodes if t.prefix == "t"])
    thinkers = thinkers[len('<ul class="contents">'):-len("</ul>")]
    return fill(template("index.html"), comparisons=comparisons, start_here=start_html, thinkers=thinkers)


def build(nodes: list[Node], out: Path, domain: str | None) -> None:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copytree(SITE / "static", out / "static")
    shutil.copytree(SITE / "fonts", out / "fonts")
    # site/specimens/ (the type directions of Ask 3, the mockups and the design specimens)
    # stays in the repository as the record and is not published.
    ids = {n.id: n for n in nodes}
    global PREFIX
    COUNTS.update({p: sum(1 for n in nodes if n.prefix == p) for p in TYPES})
    for n in nodes:
        PREFIX = "../../"
        d = out / n.prefix / n.id[2:]
        d.mkdir(parents=True, exist_ok=True)
        measure = n.prefix in ("t", "w", "p", "d", "v")
        (d / "index.html").write_text(page(n.title, render_node(n, ids), kind=TYPES[n.prefix][0], section=n.prefix, measure=measure), encoding="utf-8")
    PREFIX = "../"
    for prefix, (tname, plural, _) in TYPES.items():
        (out / prefix).mkdir(exist_ok=True)
        (out / prefix / "index.html").write_text(page(plural, render_index(prefix, nodes, ids), kind="index", section=prefix, measure=True), encoding="utf-8")
    PREFIX = ""
    (out / "index.html").write_text(page("praemisse", render_front(nodes, ids), kind="front", measure=True), encoding="utf-8")
    PREFIX = "../"
    (out / "about").mkdir(exist_ok=True)
    (out / "about" / "index.html").write_text(page("About", template("about.html"), kind="about", section="about", measure=True), encoding="utf-8")
    (out / ".nojekyll").write_text("")
    if domain:
        (out / "CNAME").write_text(domain + "\n")


def specimen(nodes: list[Node], node_id: str, out: Path) -> None:
    """One node's page written as a specimen under site/specimens/ (the design brief,
    2026-10-11): the real page from the real map, with the specimen's relative paths, and
    one line at the foot saying what it is. Links to other pages resolve on the site only."""
    ids = {n.id: n for n in nodes}
    n = ids[node_id]
    global PREFIX
    COUNTS.update({p: sum(1 for m in nodes if m.prefix == p) for p in TYPES})
    PREFIX = "../"
    line = f'<p class="specimen-line">Specimen: the {TYPES[n.prefix][0]} page {esc(n.url)} rendered from the map by site/build.py (DESIGN.md, Colour, space and pages). Links to other pages resolve on the site, not here.</p>'
    measure = n.prefix in ("t", "w", "p", "d", "v")
    out.write_text(page(n.title, render_node(n, ids), kind=TYPES[n.prefix][0], section=n.prefix, measure=measure, after=line), encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--map", type=Path, default=MAP)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--domain", default=None, help="write a CNAME file for this custom domain")
    ap.add_argument("--specimen", nargs=2, metavar=("ID", "PATH"), default=None, help="write one node's page as a specimen to PATH instead of building")
    a = ap.parse_args(argv)
    nodes = read_nodes(a.map)
    errors = check(nodes)
    for e in errors:
        print("error:", e, file=sys.stderr)
    print(f"{len(nodes)} nodes, {len(errors)} errors", file=sys.stderr)
    if errors:
        return 1
    if a.specimen:
        specimen(nodes, a.specimen[0], Path(a.specimen[1]))
        print(f"wrote specimen {a.specimen[1]}", file=sys.stderr)
    elif not a.check:
        build(nodes, a.out, a.domain)
        print(f"built {a.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
