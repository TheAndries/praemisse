# ROUTINE.md — the scheduled run

**Status: CREATED AND ENABLED** (2026-10-04, founding session; Ask 2).

## Configuration to create

| Field | Value |
|-------|-------|
| Name | `praemisse — daily run` |
| Schedule | `34 5 * * *` (cron, UTC) — 07:34 Europe/Amsterdam, 22 minutes after keel so the two never contend |
| Environment | Default, Anthropic cloud |
| Repository | the public repository from Ask 2 |
| Model | the most capable generally available model at creation (`claude-fable-5-1` as of 2026-10-04); when a more capable one appears the operator writes an ask naming it |
| Tools | `Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`, `WebSearch`, `WebFetch` |
| Connectors | **none** — clear all defaults, then read back |
| Outcomes | **none** — read back; a `claude/*` branch means the config was altered |
| Token ceiling per run | 300,000 |

**Lessons carried over from keel, binding here:** never edit this routine through the web
UI; every change through the API in an owner-initiated session, with the whole stored config
read back afterwards. Check connectors and outcomes after any change, not just the field
that was edited.

## As created

| Field | Value |
|-------|-------|
| Routine ID | `trig_01CybW54QF5Q5hCdyVQzM8qX` |
| URL | https://claude.ai/code/routines/trig_01CybW54QF5Q5hCdyVQzM8qX |
| Created | 2026-10-04 10:17:34 UTC, through the API (`created_via: http_api`) in the founding session |
| Model set | `claude-fable-5-1` (the most capable generally available model on 2026-10-04) |
| Repository | https://github.com/TheAndries/praemisse |
| Environment | `env_01Qz9JZFH3Aho6k888eZzxdK` (Default, Anthropic cloud) |
| First scheduled run | 2026-10-05 05:34 UTC = Monday 2026-10-05 07:34 Europe/Amsterdam (CEST) |

**Read-back, 2026-10-04 10:17:57 UTC, after creation:** the stored prompt matches the fenced
block below character for character (1,682 characters); `allowed_tools` is exactly the eight
listed; `outcomes` is `[]`; the repository is the new one; `mcp_connections` is `[]`.

**What went wrong and was fixed:** the create call passed `mcp_connections: []`, yet the stored
routine came back with three default connectors attached (Google_Calendar, Claude_Docs,
Claude_Code_Remote). A second call with `clear_mcp_connections: true` removed them; a fresh
`get` confirmed the empty list. Lesson, binding alongside the keel lessons above: an empty list
on create is not honoured; always clear explicitly, then read back.

## The prompt

```
You run praemisse, a map of the arguments of philosophy governed by a two-seat board. Read CHARTER.md, BOARD.md, DISPUTES.md, DESIGN.md, MODEL.md, PLAN.md, ASKS.md, INBOX.md, memory.md and the latest three changelog entries first. Then, in order: (1) note any asks marked done and unblock what depended on them; (2) handle INBOX.md — publish any filed dispute, reply to any dispute due a reply, record any attestation, and for any owner note decide what to do with it, record the source, and argue acceptance or rejection in the changelog; (3) respond to any open motion in BOARD.md; (4) do as much of PLAN.md as fits inside this run's 300,000-token ceiling, most important first, and before committing any new or revised node run an adversarial pass that tries to break its validity and its fidelity to the passage, recording what it found; (5) if strategy changed, rewrite PLAN.md with the date; (6) update memory.md, staying under 8,000 words; (7) write today's changelog entry: what you did, what was wrong and why, what you dropped from memory, and an honest estimate of effort used — never skip it, even if earlier steps consumed the run; (8) if you need the owner, add a numbered ask to ASKS.md. If a checkpoint in PLAN.md was missed, argue what to change. If you are on a different model than the last entry records, say so and write a handover note. Commit and push to main with a dated message, then stop. Never change CHARTER.md, DISPUTES.md or DESIGN.md except when transcribing a board decision recorded in BOARD.md. Never write a sentence about a thinker that does not cite a passage. Never contact anyone who has not written to the project. Never impersonate a human.
```
