#!/usr/bin/env python3
"""Carry a dispute or attestation filed as a GitHub issue into INBOX.md, and tell the
filer where their record is once the operator has published it.

The route settled in MODEL.md ("Filing") on 2026-10-18: the node page links to the two
issue forms in .github/ISSUE_TEMPLATE/ with the node's id prefilled; this script, run by
.github/workflows/inbox.yml with the built-in GITHUB_TOKEN, does two things.

  intake --issue N   If issue N was opened from one of the forms, append it verbatim to
                     INBOX.md (source, date, filer's login, address, the whole body),
                     commit to main, and post one receipt comment on the issue. Any other
                     issue is left alone. The operator handles every INBOX entry in its
                     next scheduled run (ROUTINE.md); nothing here publishes anything.

  record             For every map/d-*.md or map/v-*.md whose front matter carries
                     `issue: N`, post on issue N the node's permanent address and its
                     outcome, once per state (a fingerprint in the comment stops repeats),
                     so that a filer who watches the issue learns of the publication,
                     the reply and the ruling without the operator writing to them
                     anywhere else (CHARTER.md P10: this answers someone who wrote in).
                     Also, for every line in CHANGELOG.md of the form
                     `Returned (issue #N, YYYY-MM-DD): <reason>.`, post that reason on
                     issue N once: a filing without a passage reference or a real name is
                     returned, not published (DISPUTES.md), and the return reaches the
                     filer by the same route. Before posting anything, the script checks
                     that issue N is a filing from the forms, so that a mistyped number
                     never lands a comment on someone else's issue.

The dry run of `intake` still reads the real issue through `gh` (it needs `gh` auth and a
real issue number) and prints what it would write and post without writing or posting;
the dry run of `record` calls nothing.

Everything posted is signed as the project and says it was posted by the workflow
(CHARTER.md P11). No secrets, no cost.

    python tools/inbox_from_issue.py intake --issue 12 --dry-run
    python tools/inbox_from_issue.py record --dry-run
"""
import argparse, datetime, json, os, re, subprocess, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "INBOX.md"
MAP = ROOT / "map"
SITE = "https://praemisse.com"
FORMS = {"Dispute": "dispute", "Attestation": "attestation"}
EMPTY = "*(empty)*"
MARK = "<!-- praemisse-inbox:%s -->"


def gh(*args, check=True, dry=False):
    if dry:
        print("+ gh " + " ".join(args))
        return ""
    r = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8")
    if check and r.returncode != 0:
        print("gh %s failed: %s" % (" ".join(args), r.stderr.strip()), file=sys.stderr)
        sys.exit(1)
    return r.stdout.strip()


def git(*args, dry=False):
    if dry:
        print("+ git " + " ".join(args))
        return ""
    r = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
    if r.returncode != 0:
        print("git %s failed: %s" % (" ".join(args), r.stderr.strip()), file=sys.stderr)
        sys.exit(1)
    return r.stdout.strip()


def kind_of(issue):
    """'dispute', 'attestation' or None, from the body's headings alone, which are the
    forms' labels: a filer may edit the prefilled title, and a hand-written issue titled
    like a filing must not be mistaken for one."""
    body = issue.get("body") or ""
    if "### Node" not in body or "### Your name" not in body:
        return None
    if "### The claim contested" in body:
        return "dispute"
    if "### What you attest" in body:
        return "attestation"
    return None


def field(body, label):
    """The text under the form heading `### <label>` up to the next heading."""
    m = re.search(r"^### " + re.escape(label) + r"\s*\n(.*?)(?=^### |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""


def intake(number, dry):
    raw = gh("issue", "view", str(number), "--json", "number,title,body,author,createdAt,url,comments")
    issue = json.loads(raw)
    kind = kind_of(issue)
    if kind is None:
        print("issue #%s is not a filing from the forms; nothing to do" % number)
        return
    login = (issue.get("author") or {}).get("login", "")
    created = (issue.get("createdAt") or "")[:10]
    url = issue.get("url", "")
    node = field(issue.get("body") or "", "Node") or "(no node given)"
    header = (f"## {created} — {kind} filed through the form on the node page: {node} "
              f"(GitHub issue #{issue['number']}, opened by @{login}, {url})")
    entry = (f"{header}\n\nCarried here verbatim by `.github/workflows/inbox.yml` on "
             f"{datetime.date.today().isoformat()}; the body below is the filer's text, unedited.\n\n"
             f"{(issue.get('body') or '').strip()}\n")
    text = INBOX.read_text(encoding="utf-8")
    if url and url in text:
        print("issue #%s is already in INBOX.md; nothing to do" % number)
    else:
        if EMPTY in text:
            text = text.replace(EMPTY, entry.rstrip() + "\n")
        else:
            text = text.rstrip() + "\n\n" + entry
        if dry:
            print(text)
        else:
            INBOX.write_text(text, encoding="utf-8")
            git("config", "user.name", "github-actions[bot]")
            git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
            git("add", "INBOX.md")
            git("commit", "-m", f"{datetime.date.today().isoformat()} — INBOX: {kind} filed through the form, issue #{issue['number']}")
            for attempt in range(4):  # the daily run may push at the same time
                r = subprocess.run(["git", "push", "origin", "HEAD:main"], capture_output=True, text=True, cwd=ROOT)
                if r.returncode == 0:
                    break
                print("push failed (%s); rebasing and retrying" % r.stderr.strip()[:200])
                git("pull", "--rebase", "origin", "main")
            else:
                print("push failed four times", file=sys.stderr)
                sys.exit(1)
    mark = MARK % ("received:%s" % issue["number"])
    if any(mark in (c.get("body") or "") for c in issue.get("comments") or []):
        print("receipt already posted")
        return
    comment = (
        f"Received, {created}. This {kind} has been carried verbatim into `INBOX.md` and will be "
        f"handled by the project's operator in its next scheduled run (one run a day; `ROUTINE.md`). "
        f"What it does is recorded in `CHANGELOG.md`; a published {kind} appears on the node's page "
        f"at a permanent address, and a comment here will give that address. "
        + (f"A dispute without a passage reference or a real name is returned with a one-line reason "
           f"(`DISPUTES.md`), posted here. " if kind == "dispute" else
           f"An attestation without a real name is returned with a one-line reason (`DISPUTES.md`), posted here. ")
        + f"Replies are written by the operator, an AI system, and signed as the project.\n\n"
        f"— praemisse, the project. Posted by the repository's inbox workflow.\n\n{mark}")
    if dry:
        print(comment)
    else:
        gh("issue", "comment", str(number), "--body", comment)


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    import yaml  # the workflow installs site/requirements.txt
    return yaml.safe_load(text[3:end]) or {}


def is_filing(number, dry):
    """True if issue `number` was opened from one of the forms; nothing is ever posted on
    an issue that was not."""
    if dry:
        return True
    raw = gh("issue", "view", str(number), "--json", "body,comments", check=False)
    if not raw:
        print("issue #%s cannot be read; nothing posted" % number)
        return False
    issue = json.loads(raw)
    if kind_of(issue) is None:
        print("issue #%s is not a filing from the forms; nothing posted" % number)
        return False
    return issue


def post_once(number, mark, text, dry):
    issue = is_filing(number, dry)
    if not issue:
        return
    comments = issue.get("comments", []) if isinstance(issue, dict) else []
    if any(mark in (c.get("body") or "") for c in comments):
        return
    body = (f"{text}\n\n— praemisse, the project. Replies are written by the operator, an AI system, "
            f"and signed as the project; this comment was posted by the repository's inbox workflow.\n\n{mark}")
    if dry:
        print(f"#{number}: {body}")
    else:
        gh("issue", "comment", str(number), "--body", body)


def record(dry):
    # returns: `Returned (issue #N, YYYY-MM-DD): reason.` anywhere in CHANGELOG.md
    log = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    for m in re.finditer(r"Returned \(issue #(\d+), (\d{4}-\d{2}-\d{2})\): ([^\n]+)", log):
        number, date, reason = m.group(1), m.group(2), m.group(3).strip().rstrip("*_")
        post_once(number, MARK % f"returned:{number}:{date}",
                  f"Returned, not published, {date}: {reason} A filing may be made again with what was missing "
                  f"(`DISPUTES.md`, Who may dispute).", dry)
    for path in sorted(list(MAP.glob("d-*.md")) + list(MAP.glob("v-*.md"))):
        meta = front_matter(path)
        number = meta.get("issue")
        if not number:
            continue
        nid = str(meta.get("id") or path.stem)
        address = f"{SITE}/{nid[0]}/{nid[2:]}/"
        if nid.startswith("d-"):
            state = "outcome %s" % meta.get("outcome", "")
            for key, label in (("reply", "the project's reply"), ("counter", "your counter"), ("ruling", "the ruling")):
                v = meta.get(key)
                if isinstance(v, dict) and v.get("date"):
                    state += f"; {label} of {v['date']}"
            what = "dispute"
        else:
            state = "recorded"
            what = "attestation"
        mark = MARK % f"record:{nid}:{re.sub(r'[^a-z0-9]+', '-', state.lower())}"
        post_once(number, mark, f"Your {what} is published at {address} ({state}). The exchange stays there, "
                                f"in full, permanently (`CHARTER.md` P4).", dry)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["intake", "record"])
    ap.add_argument("--issue", type=int)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.command == "intake":
        if not a.issue:
            ap.error("intake needs --issue N")
        intake(a.issue, a.dry_run)
    else:
        record(a.dry_run)


if __name__ == "__main__":
    main()
