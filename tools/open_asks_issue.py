#!/usr/bin/env python3
"""Keep one GitHub issue in sync with the open asks in ASKS.md.

Copied from keel's tools/open_asks_issue.py (v3) in the owner session of 2026-10-05 and
adapted to praemisse's ASKS.md, which is a table (one row per ask) rather than one
section per ask. The owner asked to be told when there are asks waiting, rather than
having to remember to look.

Mechanism: the Action's built-in GITHUB_TOKEN edits one issue, "praemisse - open asks",
assigned to the repository owner. Assignment notifies by mail regardless of watch
settings, and every comment on the issue is mailed too. No secrets, no app password,
no credentials held by the operator or by the routine (CHARTER.md Money: free tier).

A comment is posted only when the *set* of open asks changes, and it says what changed
and carries the FULL TEXT of every new ask, because the comment is what GitHub mails the
owner and he acts from his phone: everything he needs must be in the mail body, not
behind a link. GitHub caps a comment at 65,536 characters; a new ask longer than the room
left is cut with a pointer to the file.

ASKS.md format this reads:   | # | Date | Ask | Blocks | Status |
An ask is open unless its Status cell starts with "done". An open ask whose Status says
"deferred" or "queued" is listed as queued (no action needed yet).

    python tools/open_asks_issue.py --dry-run    # prints the body and comment, calls nothing
"""
import json, os, re, subprocess, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")  # the asks carry arrows and accents; a cp1252 console must not crash a dry-run

ASKS = "ASKS.md"
TITLE = "praemisse - open asks"
VERSION = "v3"
COMMENT_LIMIT = 60000  # GitHub refuses comments over 65,536 characters; leave room
MARK = "<!-- open-asks-fingerprint:" + VERSION + ":%s -->"


def gh(*args, check=True):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        print("gh %s failed: %s" % (" ".join(args), r.stderr.strip()), file=sys.stderr)
        sys.exit(1)
    return r.stdout.strip()


def plain(text):
    text = " ".join(text.split())
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)   # links -> label
    return re.sub(r"[*`]", "", text)                        # bold/code marks


def summarise(ask, limit=180):
    """One plain-text line saying what this ask actually wants: its first sentence
    after the bold title."""
    body = re.sub(r"^\s*\*\*[^*]+\*\*\s*", "", ask.strip())
    text = plain(body)
    parts = re.split(r"(?<=[.!?]) ", text)
    out = parts[0] if parts else text
    if len(out) > limit:
        out = out[:limit].rsplit(" ", 1)[0] + "..."
    return out


def title_of(ask):
    """'**Choose the type.** When the operator...' -> 'Choose the type'"""
    m = re.match(r"\s*\*\*([^*]+?)\*\*", ask)
    t = m.group(1).strip() if m else plain(ask)[:80]
    return t.rstrip(".").strip()


def rows(text):
    """Every table row of ASKS.md as (number, date, ask, blocks, status)."""
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = line.strip("|").split("|")
        if len(cells) < 5 or not cells[0].strip().isdigit():
            continue
        num, date = cells[0].strip(), cells[1].strip()
        blocks, status = cells[-2].strip(), cells[-1].strip()
        ask = "|".join(cells[2:-2]).strip()
        out.append((num, date, ask, blocks, status))
    return out


def open_asks(text):
    """(number, title, ask text, status) for every ask whose Status is not done."""
    out = []
    for num, date, ask, blocks, status in rows(text):
        if status.lower().startswith("done"):
            continue
        out.append({"num": num, "date": date, "title": title_of(ask), "ask": ask,
                    "blocks": blocks or "nothing", "status": status})
    return out


def block_of(a):
    """The full markdown of one ask, as it goes into the issue and the mail."""
    return "\n".join([
        "**Ask %s** (%s)" % (a["num"], a["date"]), "", a["ask"], "",
        "*Blocks:* %s  " % a["blocks"], "*Status:* %s" % a["status"],
    ])


def is_queued(a):
    s = a["status"].lower()
    return "deferred" in s or "queued" in s


def key(n):
    return int(n) if n.isdigit() else 0


def main():
    dry = "--dry-run" in sys.argv
    repo = os.environ.get("GITHUB_REPOSITORY", "owner/repo" if dry else None)
    if repo is None:
        print("GITHUB_REPOSITORY is not set", file=sys.stderr)
        return 2
    owner = repo.split("/")[0]

    with open(ASKS, encoding="utf-8") as fh:
        asks = open_asks(fh.read())

    now_set = sorted((a["num"] for a in asks), key=key)
    fingerprint = ",".join(now_set) or "none"

    if dry:
        # Pretend the issue exists with every ask but the newest already in it, so the comment
        # that would be posted for a new ask is what gets printed.
        prev = [n for n in now_set if n != now_set[-1]] if now_set else []
        issue = {"number": 0, "title": TITLE, "body": MARK % (",".join(prev) or "none")}
    else:
        existing = json.loads(
            gh("issue", "list", "--state", "open", "--search", TITLE,
               "--json", "number,title,body", "--limit", "20") or "[]"
        )
        issue = next((i for i in existing if i["title"] == TITLE), None)

    if not asks:
        if issue:
            gh("issue", "close", str(issue["number"]),
               "--comment", "Nothing waits on you any more. praemisse reopens this when it does.")
            print("All asks closed; issue closed.")
        else:
            print("No open asks, no issue. Nothing to do.")
        return 0

    live = [a for a in asks if not is_queued(a)]
    queued = [a for a in asks if is_queued(a)]

    # ---------- issue body: summary first, full text folded away ----------
    body = [MARK % fingerprint, ""]
    if live:
        body += ["## Waiting on you", ""]
        for a in live:
            body += ["**Ask %s - %s**" % (a["num"], a["title"]), "", "> %s" % summarise(a["ask"]), ""]
    else:
        body += ["## Waiting on you", "", "_Nothing. Everything below is deferred or queued._", ""]
    if queued:
        body += ["## Deferred or queued - no action needed yet", ""]
        for a in queued:
            body.append("- **Ask %s** - %s _(%s)_" % (a["num"], a["title"], a["status"]))
        body.append("")
    body += ["---", "",
             "Mark one done by setting its **Status** cell to `done <date>` and writing whatever the",
             "operator needs to know in the same row or in `INBOX.md`. The operator reads the file",
             "at the start of every run.",
             "", "<details><summary>Full text of every open ask</summary>", ""]
    for a in asks:
        body += [block_of(a), "", "---", ""]
    body += ["</details>", "", "_Posted by praemisse. Automated, not a person._"]
    text = "\n".join(body)

    if issue is None:
        num = gh("issue", "create", "--title", TITLE, "--body", text, "--assignee", owner)
        print("Created issue for %d open asks: %s" % (len(asks), num))
        return 0

    prev_body = issue.get("body") or ""
    if (MARK % fingerprint) in prev_body:
        print("Open asks unchanged (%s). Silent." % fingerprint)
        return 0

    prev_m = re.search(r"open-asks-fingerprint:(?:v\d+:)?([^\s>]*)", prev_body)
    prev_set = [x for x in (prev_m.group(1).split(",") if prev_m else []) if x and x != "none"]
    added = [n for n in now_set if n not in prev_set]
    closed = [n for n in prev_set if n not in now_set]

    by_num = {a["num"]: a for a in asks}
    lines = []
    for n in added:
        a = by_num[n]
        tag = " _(deferred or queued - nothing to do yet)_" if is_queued(a) else ""
        lines += ["**Ask %s is new - %s**%s" % (n, a["title"], tag), "",
                  "> %s" % summarise(a["ask"]), ""]
    # The full text of each new ask, so the mail this comment becomes is complete in itself.
    for n in added:
        room = COMMENT_LIMIT - len("\n".join(lines)) - 400
        full = block_of(by_num[n])
        if len(full) > room:
            full = full[:max(room, 0)].rsplit("\n", 1)[0] + "\n\n_[cut here: the rest of Ask %s is in ASKS.md]_" % n
        lines += ["---", "", "### Full text of Ask %s" % n, "", full, ""]
    if added:
        lines += ["---", ""]
    if closed:
        lines += ["Closed since last time: %s."
                  % ", ".join("Ask %s" % n for n in closed), ""]
    if not added and not closed:
        lines += ["No asks were added or closed - this summary was rebuilt so it says "
                  "what changed without you opening the file.", ""]

    lines.append("**Waiting on you now:** %s"
                 % (", ".join("Ask %s" % a["num"] for a in live) if live else "nothing"))
    if queued:
        lines.append("**Deferred or queued, no action needed:** %s"
                     % ", ".join("Ask %s" % a["num"] for a in queued))

    comment = "\n".join(lines)
    if dry:
        print("=== issue body (%d chars) ===\n%s\n=== comment (%d chars) ===\n%s" % (len(text), text, len(comment), comment))
        return 0
    gh("issue", "edit", str(issue["number"]), "--body", text)
    gh("issue", "comment", str(issue["number"]), "--body", comment)
    print("Updated issue #%s (%s -> %s)." % (issue["number"], ",".join(prev_set), fingerprint))
    return 0


if __name__ == "__main__":
    sys.exit(main())
