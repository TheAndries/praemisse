# praemisse

*praemisse.com — registered 2026-10-04 (Ask 1). Repository: https://github.com/TheAndries/praemisse*

A map of every significant argument in the history of philosophy, broken into explicit
premises, inferences and conclusions, each tied to the passage it comes from, each linked
to every argument that depends on it or attacks it — and open to dispute by anyone who can
cite a text.

Founded 2026-10-04 by Andries, Breda, Netherlands. Governed by a two-seat board (`BOARD.md`):
the owner and the AI operator. Operated day to day by the operator on a scheduled routine
(`ROUTINE.md`), under `CHARTER.md`.

**Goal:** an artifact that is more valuable in 2036 than in 2026 because of what has
accumulated in it, not because of what was generated for it. Structure, passages,
attestations and disputes are the asset. Prose is rendered from them by whatever the best
available model is, and is never the thing that is checked.

**Phase:** 1 built, Checkpoint 1 answered 2026-10-10: the site is live at https://praemisse.com/, the map holds Kant, Schopenhauer and Nietzsche on the thing in itself (147 nodes, all `draft` or `checked`), and the comparison page https://praemisse.com/x/thing-in-itself/ has been read by the owner and is `checked` with the qualification its status line shows (Ask 7 done). See `PLAN.md`.

## The files

| File | What it is |
|------|-----------|
| [CHARTER.md](CHARTER.md) | Purpose and binding principles. Amendable only by board decision. |
| [BOARD.md](BOARD.md) | How the two seats decide, and the decision log. |
| [DISPUTES.md](DISPUTES.md) | The protocol by which anyone may argue with the map. |
| [DESIGN.md](DESIGN.md) | Binding rules for how the site looks and reads. |
| [MODEL.md](MODEL.md) | The data model: what a node is and how it is stored. |
| [PLAN.md](PLAN.md) | Current strategy. Rewritten, with the date, whenever it changes. |
| [ASKS.md](ASKS.md) | The operator's channel to the owner. Numbered, dated, blocking. |
| [INBOX.md](INBOX.md) | Mail, owner notes and filed disputes, until connectors exist. |
| [CHANGELOG.md](CHANGELOG.md) | Newest first. What was done, decided, and got wrong. |
| [memory.md](memory.md) | Carried state, capped at 8,000 words. |
| [LEDGER.md](LEDGER.md) | Every euro in and out. |
| [ROUTINE.md](ROUTINE.md) | The scheduled run's exact configuration, and how the owner is told about asks. |
| [tools/](tools/) | Repository automation: `open_asks_issue.py` keeps the *open asks* issue that mails the owner. |

## Licences

Code is under the MIT licence ([LICENSE](LICENSE)). Everything under `map/` — nodes, passages,
attestations, disputes, comparisons — is under CC BY-SA 4.0 ([LICENSE-DATA](LICENSE-DATA)),
as `CHARTER.md` P8 requires.
