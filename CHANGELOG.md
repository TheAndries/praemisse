# CHANGELOG.md

Newest first. What was done, decided, and got wrong.

## 2026-10-04 — founding session: setup

Owner-initiated session, same day as founding, following `SETUP.md`. Operator on
`claude-fable-5-1`.

**Named.** Three names were proposed with domain checks (RDAP for .com/.org/.nl, EURid whois
for .eu) and TransIP prices. `premise` was registered on all four TLDs; every plain English
or Latin one-word candidate was taken on .com. The owner wanted .com for a worldwide
readership and chose **`praemisse`**, the Latin and German spelling of the word. He
registered praemisse.com at TransIP: 8.99 EUR ex BTW + 1.89 BTW = 10.88 EUR, twelve months,
logged in `LEDGER.md` against Ask 1 (card still to be reported). The working name was
replaced in README, ROUTINE (name and prompt), ASKS, BOARD and memory.

**Created.** The owner created the public repository https://github.com/TheAndries/praemisse.
The operator added `LICENSE` (MIT), `LICENSE-DATA` (CC BY-SA 4.0) with a licences section in
README, a Python/Node `.gitignore`, `.gitattributes` (LF), and `map/README.md` and
`site/README.md`, then made the first commit `2026-10-04 founding` and pushed `main`.
Verified through the public GitHub API: public, default branch `main`, 19 files.

**Configured.** The owner granted the Claude GitHub App access. The routine was created
through the API, never the web UI: `trig_01CybW54QF5Q5hCdyVQzM8qX`, `praemisse — daily run`,
`34 5 * * *` UTC, model `claude-fable-5-1`, tools Bash, Read, Write, Edit, Glob, Grep,
WebSearch, WebFetch, Default environment, repository the new one. First run Monday
2026-10-05 07:34 Europe/Amsterdam.

**Verifications.** Full stored config read back twice. Prompt compared character by character
against the fenced block in `ROUTINE.md`: identical, 1,682 characters. `outcomes`: `[]`.
Repository: correct. `mcp_connections`: **not** empty after creation — see below — empty
after the fix.

**What went wrong.** The create call passed an empty connector list, but the stored routine
came back with three default connectors attached (Google Calendar, Claude Docs, Claude Code
Remote). This is the keel failure repeating. A second API call with `clear_mcp_connections:
true` removed them and a fresh read confirmed `[]`. Recorded in `ROUTINE.md` as a binding
lesson: an empty list on create is not honoured; clear explicitly and read back. Also: this
machine has no GitHub CLI, so the owner created the repository himself and the operator pushed
with git; the operator did not inspect stored credentials.

**Not done.** Mailbox (Ask 4): the owner deferred it to a later date, to be set up as keel's
was. Card for the domain spend: not yet reported. Ask 3 (type) waits for tomorrow's specimens.

**Tomorrow's run should produce:** a new entry at the top of this file dated 2026-10-05 on
`main`; the build pipeline skeleton started in `site/`; three typographic specimen pages for
Ask 3; nothing written about any philosopher. If the entry is missing, lands on a `claude/*`
branch, or contains nodes, the routine config is the first place to look.

**Effort.** One owner session including the domain purchase and the GitHub steps; operator
work was domain lookups, file edits, three API calls and two full read-backs.

## 2026-10-04 — founding

Owner-initiated session. The project was founded and its governing files drafted:
`CHARTER.md`, `BOARD.md`, `DISPUTES.md`, `DESIGN.md`, `MODEL.md`, `PLAN.md`. Decisions taken
at founding:

- **Governance:** two seats, operator runs, owner steers; tie-break by domain (`BOARD.md`).
- **Disputes:** nobody overrides; one reply each; contested status; a second independent
  human resolves; escalation to the board (`DISPUTES.md`). No credential check — the citation
  is the filter.
- **Appreciation:** structure and human record are the asset; prose is rendered and
  regenerable (`CHARTER.md` P3).
- **Wedge:** Kant → Schopenhauer → Nietzsche on the thing-in-itself (`PLAN.md` §2).
- **Money:** 200 EUR per quarter.
- **Open:** name and domain, repository, type choice, mailbox (Asks 1–4).

Nothing built. No run has yet occurred.
