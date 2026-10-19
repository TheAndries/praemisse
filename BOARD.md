# BOARD.md

The project is governed by a board of two seats. Both hold a share; neither runs the other.

| Seat | Holder | Role |
|------|--------|------|
| Owner | Andries | Steers. Holds the veto (`CHARTER.md` P12). Pays. Appears in his own name. |
| Operator | the AI system on the routine | Runs. Builds, formalizes, replies to disputes, rules on them, keeps the files. |

## How decisions are made

**Day to day, the operator decides** — what to formalize next, how to formalize it, what to
reply to a dispute, how to rule on it, what the site renders. It records what it did in
`CHANGELOG.md` and does not wait for approval.

**The owner steers through notes.** He writes to `INBOX.md` like anyone else: observations,
preferences, objections, ideas. A note is not an instruction. The operator decides what to do
with it in a scheduled run and argues acceptance or rejection in the changelog. If the owner
wants something done regardless, he says so and it is recorded as an **owner decision**,
stamped as such.

**Either seat may file a motion** here, under *Open motions*, for anything that changes the
charter, the design rules, the dispute protocol, the money ceiling, the scope of the map, or
the project's public posture. The other seat responds — the operator in its next run, the
owner in his next session. Agreement becomes a decision below. Disagreement is resolved by
the tie-break and recorded with both positions.

**Tie-break.** When the seats disagree:
- the **owner** decides matters of purpose, scope, values, public posture, and money;
- the **operator** decides matters of method, formalization, scheduling, and the ruling on
  any single dispute (`DISPUTES.md` step 5).

A ruling the owner thinks wrong is overturned only by the veto, in writing, with the reason.

**Quarterly reflection.** On the last scheduled run of each quarter the operator opens an ask
titled *"Quarterly reflection: <quarter>"*: progress against `PLAN.md` checkpoints, state of
every dispute, what it would change in the plan, the capacity or the charter, and every risk
it is tracking. The board meets, and the decisions land here.

## Open motions

### Colour, space and pages

Moved by the operator on 2026-10-19, in the owner session, at the owner's instruction
(`INBOX.md`, 2026-10-19), and drafted from the amendment section of the design brief
(`DESIGN-BRIEF-2026-10-11.md`, *What this amendment adds, and what it leaves alone* and
*The design system*). Tabled at the specimen checkpoint. **Exhibit:** the comparison
specimen `site/specimens/comparison-a.html` on branch `design`, with its screenshots (Ask
11). The owner votes when he answers that ask. Until the motion passes, `DESIGN.md` does
not change.

**What it adds.** A section *Colour, space and pages* in `DESIGN.md`, under the ten
principles as they stand: a palette (paper, ink, two greys, a hairline, one accent) with
its dark-mode values and the measured contrast ratios; four type sizes and a spacing scale
of six steps, every value a token in `site/static/tokens.css`; a page grammar (eleven
components, seven templates and the index pages, one breakpoint); and a menu of five words.
The text is `site/DESIGN-amendment.md` as it stands when the owner votes, moved in whole
with the date and the decision line.

**It says three things plainly.**

1. **One accent colour,** used for links and for the word *contested*, and no second
   colour. Nothing else on the site is coloured; the word carries the status, as P4 requires.
2. **The counts stay visible to readers but move from the front page to the colophon** on
   every page, each count a link to its index, in old-style figures.
3. **The header stays the one header of P7, set as a running head:** the wordmark, the
   one-line description, the menu and a hairline, centred, not sticky; no second header,
   no sidebar.

**What it leaves alone.** The ten principles and the *Not permitted* list; the type
(2026-10-05) and the fonts under `site/fonts/`; the status vocabulary and the words draft,
checked, attested, established, contested; every URL; the map and the model; the rendered
prose.

**Relation to the decision of 2026-10-11.** That decision made the amendment binding on the
owner's approval of the specimen. The owner has since said (2026-10-19) that the approval
answers the ask and the vote on this motion amends `DESIGN.md`; this motion is the route.
If the owner's answer to Ask 11 changes a colour or a spacing, the token value changes in
the exhibit and in the amendment, and the motion is voted on as amended.

**Votes.** Operator: for. Owner: open.

## Decisions

| Date | Decision | Moved by | Notes |
|------|----------|----------|-------|
| 2026-10-04 | Project founded; `CHARTER.md`, `DISPUTES.md`, `DESIGN.md`, `MODEL.md` adopted as drafted | both | Founding session. Working name `premise`; renamed `praemisse` the same day under Ask 1. |
| 2026-10-05 | The site's type is direction B, Libertine (Libertinus Serif and Sans) | owner | Owner decision under Ask 3, given in an owner session after reading the three specimens at praemisse.com. Transcribed into `DESIGN.md`, *Open design asks*. |
| 2026-10-10 | Checkpoint 1 review of `x-thing-in-itself`: the comparison is `checked` with a qualification in its status line, a status later comparisons may use (`MODEL.md`, *Checked comparisons*); Fabel stages 5 and 6 are read as Nietzsche's own voice, stage 4 as the positivist stage; A 26 / B 42 joins the shared premise on space; the noumenon claim sits in the row on what can be said; the German is shown beside the English inside the load-bearing claims; the Kant / stage 6 parallel and the handling of Schopenhauer's attack stand as written | owner | Owner review under Ask 7, given in an owner session; applied the same session with the operator's conventions for the status note and for quotations (`CHANGELOG.md`). |
| 2026-10-11 | The site's colour, spacing, page grammar and menu follow direction A, *the edition*, of the two mockups the owner gave with his design brief; the type (2026-10-05) and the ten principles stand; built on branch `design` and binding in `DESIGN.md` under *Colour, space and pages* once the owner has approved the comparison specimen set in Libertinus | owner | Owner decision given in the design brief filed in `INBOX.md` on 2026-10-11 (owner session). The brief asks for an amendment to `DESIGN.md`, made only after the specimen is approved; until then nothing in `DESIGN.md` changes. Direction B is not built; its grid is kept as four tokens in `site/static/tokens.css` so that it can be swapped in on request. |
