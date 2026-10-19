# memory.md

Carried state for the operator. Capped at 8,000 words. Rewritten each run.

## State as of 2026-10-19 (run 13, end; owner session on branch `design` the same day)

**Identity and governance.** Name `praemisse`; domain praemisse.com at TransIP; site live at
https://praemisse.com/ (GitHub Pages, HTTPS enforced, certificate to 2027-01-03, GitHub
renews). Repository https://github.com/TheAndries/praemisse, public, `main`. Routine
`trig_01CybW54QF5Q5hCdyVQzM8qX`, `34 5 * * *` UTC, model `claude-fable-5-1`; runs 1–13 were
served on that model, no handover note needed. Run 13 fired the day after run 12. **No run is recorded for 2026-10-16 or
2026-10-17** (no commit, no changelog entry between run 11 on 10-15 and run 12 on 10-18);
the operator cannot see the routine's run history and asked the owner to look (Ask 10).
The GitHub and Claude Code Remote tools in the tool list are platform-attached to every
cloud session and are not a config change (`ROUTINE.md`, Ask 6): do not raise it again, and
do not use them; everything goes through git and the repository. Open disputes: none.
Attestations: none. Open motions: one, *Colour, space and pages* (2026-10-19). INBOX empty at runs 1–13; no form filing yet; the owner made no commit
between runs 8 and 13. Open asks: 4 (mailbox; deferred by owner; now the second filing
route, for anyone without a GitHub account), 9 (the owner's qualified review of https://praemisse.com/x/the-will/,
opened 2026-10-15; blocks nothing), **10 (opened 2026-10-18: test the filing route once from
a node page, and look at the routine's run history for 10-16 and 10-17; blocks the
confidence of Phase 2, not the plan)**. 11 (the comparison specimen on branch `design`, with the motion
*Colour, space and pages* beside it; blocks nothing in the plan). Asks 1, 2, 3, 5, 6, 7, 8 done.

**The design branch (Ask 11; the motion *Colour, space and pages*).** The owner's design
brief of 2026-10-11 (`DESIGN-BRIEF-2026-10-11.md` at the root since 2026-10-19; verbatim in
`INBOX.md`) chose direction A, *the edition* (`BOARD.md`, owner decision 2026-10-11). Built
on branch `design`, not merged, `main` and `DESIGN.md` untouched: `site/static/tokens.css`
(imports `type.css`; four sizes, spacing scale, palette light and dark, the grid's four
levers with B's values in a comment), `site/static/site.css` (eleven components, the
comparison template), `base.html` (running head, menu with `aria-current`, skip link,
colophon with the counts), `site/site.yaml` (`palette: a`, `start_here: []`), the
comparison rendering in `build.py` (`render_comparison`, `render_texts`, `render_shared`,
`deps_html`, `status_html`, `page(kind, section, measure, after)`, `--specimen ID PATH`),
`site/specimens/components.html` and `comparison-a.html` with screenshots. `main` was
merged into the branch on 2026-10-19 (`524d00e`), so the branch carries runs 7–13 and the
filing links; the specimen is rendered from the merged map (seven rows; grid 10,800px tall
at 1280). Draft amendment with every decision and its reasoning: `site/DESIGN-amendment.md`.
The owner answered run 8's question on 2026-10-19 (`INBOX.md`): note *and* motion. The
templates are built inside `DESIGN.md` on the note; the palette, spacing scale, page grammar
and menu are the motion *Colour, space and pages*, tabled in `BOARD.md` (operator for; owner
votes when he answers Ask 11), exhibit the specimen; `DESIGN.md` changes only when it passes.
The four reservations of run 8 are accepted and stand in the amendment in the owner's words.
**Ask 11 (the specimen; replaces the branch's Ask 8, whose number collided with run 8's)
blocks nothing in the plan, but on the branch step 4 of the brief (record the approval,
move the amendment into `DESIGN.md`, log it), step 5 (node, front page, thinker and work,
passage, index pages, dispute, about), step 6 (verification) and the merge ask wait for it.**
A colour or spacing change: `tokens.css` only. B's grid: the four `--grid-*` tokens. A
different direction: stop, note in `INBOX.md`, no build without a `BOARD.md` line. Known: the
brief's 120 KB weight budget cannot be met with the fonts (820 KB, off limits; `PLAN.md` §5).
The old templates still use `style.css` and look unstyled on the branch until step 5. The
scheduled runs work on `main` and must not touch the branch; when the branch merges, the
routine inherits the templates. Screenshots: Playwright's Chromium on the owner's machine;
PIL for the 64-colour reduction.

**Checkpoint 1 (Ask 7) was answered 2026-10-10 in an owner session:** the owner read the
first comparison against the project's translations, found nothing that reads as
fabrication, gave eight decisions (owner decision in `BOARD.md`; his note verbatim in that
changelog entry), applied the same day. He did not say in the ask's words whether the page
is better than what he could find elsewhere; no rethink was ordered; proceed.

**`PLAN.md` rewritten 2026-10-18 (run 12): Phase 2 opened.** The filing route is settled
in `MODEL.md`, *Filing*, and built (below). What follows: the owner's test (Ask 10); the
operator handles any filing inside the deadlines of `DISPUTES.md`, which now bind (publish
in the next run, reply within three runs); the owner invites two or three people in his own
name, the operator does no outreach; the mailbox of Ask 4 as the second route when he sets
it up; meanwhile the map grows where a filing or his review points, otherwise by the plan: a
fourth thinker by lineage (Phase 3) comes after Phase 2 has had its first filing or the
owner says to go on. A new risk in §5: the route is unexercised and a run that fails to fire
would let a deadline pass.

**The filing route (run 12, 2026-10-18; `MODEL.md`, *Filing*; a method decision).**
`.github/ISSUE_TEMPLATE/dispute.yml` (fields, by id: `node`, `kind` dropdown fidelity /
validity, `contested`, `alternative`, `passages`, `literature` optional, `name`,
`affiliation` optional, `terms` checkbox consenting to publication by name under CC BY-SA
4.0; title »Dispute: <node id>«) and `attestation.yml` (`node`, `statement`, `passage` optional, `sides_with`
optional, `name`, `affiliation`, `terms`; title »Attestation: <node id>«).
`site/build.py`: `REPO` constant; `render_filing(n)` appends to the `.meta` paragraph of
every c/a/p/r/x page »Dispute this node« and, on c/a/x, »Attest this node«, plain links to
`REPO/issues/new?template=<form>.yml&title=...&node=<id>` (prefill by field id), followed by
one sentence saying under your real name, citing a passage, the form is a GitHub issue and
what is filed is published on the page under `DISPUTES.md` (linked to the repository); t/w/d/v pages get nothing; `check_filing_issue`
allows `issue:` (a positive integer, the issue number) on `d-` and `v-` nodes and refuses
anything else (negative test passed). `.github/workflows/inbox.yml` (permissions `contents:
write` on the intake job only, `issues: write`, built-in token, **no concurrency group**,
since GitHub keeps one pending run per group and would drop a filing; `workflow_dispatch`
with an optional `issue` input re-runs the intake): job `intake` on `issues: opened` runs
`tools/inbox_from_issue.py intake --issue N`, which takes the issue through `gh issue view
--json`, recognizes a filing by the form headings alone (`### Node`, `### Your name`, and
`### The claim contested` for a dispute or `### What you attest` for an attestation; the
title is ignored, since a filer may edit it; anything else is left alone, so the owner's
issues and the open-asks issue pass through), appends to `INBOX.md` a `##` entry
(date, kind, node, issue number, login, URL, then the body verbatim), replacing the
`*(empty)*` line if present, commits as `github-actions[bot]` with the message »<date> —
INBOX: <kind> filed through the form, issue #N«, pushes `HEAD:main` with up to four `pull
--rebase` retries, and posts one receipt comment (fingerprint `<!--
praemisse-inbox:received:N -->`; says carried into INBOX.md, handled in the next scheduled
run, one run a day, recorded in CHANGELOG.md, a published filing gets a permanent address
posted here, a filing without passage or real name is returned with a one-line reason,
replies are written by the operator, an AI system, signed as the project, posted by the
workflow); job `record` on a push to `main` touching `map/d-*.md`, `map/v-*.md` or
`CHANGELOG.md` (installs PyYAML) posts on each node's `issue:` the permanent address
`https://praemisse.com/<p>/<slug>/` and the state (outcome; dates of reply / counter /
ruling), once per state by fingerprint, and posts once every return the operator writes in
`CHANGELOG.md` as **`Returned (issue #N, YYYY-MM-DD): reason.`** (that exact form, on one
line); before posting anything it reads the issue and checks it is a filing from the forms.
A push by the token does not start `site.yml`, and the build never reads `INBOX.md`, so
nothing is published automatically. Dry-runs of both paths passed on a fake issue. **The
daily run must now `git pull --rebase origin main` before pushing**, since the workflow may
have committed `INBOX.md` meanwhile. A returned filing: no node; the operator writes the `Returned (...)` line in the changelog
entry that handles it, and the workflow posts it. The about page says how to file and that filing needs
a GitHub account, reading none. Handling a filing in a run: publish the `d-`/`v-` node
(`MODEL.md`, *Disputes and attestations*: `target`, `disputant`/`attester`, `date`, `kind`,
`contested_claim`, `alternative`, `passages`, `issue`, `outcome: published`; the target's
`disputes`/`verified_by` list must equal the set targeting it), move the INBOX entry to the
changelog with what was done, reply within three runs by `reply: {date, text}` and outcome
`argued`/`conceded` (a concession adds a `versions:` entry with `credit: d-...`); an
attestation moves a `c-`/`a-`/`x-` to `attested`, two independent to `established`.

**Phase 0 complete (2026-10-05).** `site/build.py` (reads `map/*.md`, validates against
`MODEL.md`, renders to `site/_build/`, gitignored; `--check` for CI; `--map DIR` for a
scratch copy; `--out DIR`; `--domain praemisse.com` in the workflow; PyYAML the only
dependency; own small Markdown subset with `[text](../../c/slug/)` links between node pages,
which live at `/<prefix>/<slug>/`), `site/static/style.css` and `type.css` (Libertine, owner
decision), `.github/workflows/site.yml` (check, build, deploy on push to `main`),
`notify-asks.yml` + `tools/open_asks_issue.py` (one GitHub issue *praemisse - open asks*;
keep the `| # | Date | Ask | Blocks | Status |` table; `done ...` closes,
*deferred*/*queued* lists as no action).

**The model as applied (`MODEL.md`, *How the model is applied*; all enforced by `--check`).**
`versions:` in the same file (date, reason, superseded statement, credit) when a statement
changes; a body-only or link-only change adds no version, the changelog records it, and
`produced_by` keeps the original date; `statement:` one sentence on every claim, argument
and comparison; `form:` in propositional logic checked by `tools/validity.py` (truth table,
≤16 atoms, `not/and/or/->/<->`), `checked` only on an argument whose form passes, claims
`draft` until attested; premises `{claim: id}` or `{assumption: text}`, an assumption is the
map's own bridge, named as such and contained in the argument's `statement`; `depends_on` on
a claim names its argument, or a claim it is drawn from by an »also«/»denn«/»mithin«/
»folglich« step not formalized (the body quotes the connective); `supports` the converse,
checked; `attacked_by`/`replies_to` converses, checked; an attack only when the attacker's
statement denies what the target *states*, the attacker's body quotes the naming sentence or
says none does; `r-` nodes carry `reading_of`, `statement`, `passages`, `literature`
(author, title, year, chapter), no status, body in bold-headed paragraphs *The texts it
rests on*, *What it holds*, *What depends on it*, *What tells against it*; the map never
picks a reading (P9), so every body that relates to a contested claim writes »on the reading
...; the other reading ...«; `d-`/`v-` nodes name a `target` and render in full on it;
`contested` iff a `d-` has outcome contested. *Checked comparisons:* a comparison may be
`checked` on a named human's review short of attestation, with `status_note` shown after the
word; refused without it, refused on anything else; lists print »checked, with a
qualification on the page«. *Quotations:* a claim may carry `quotes:` (`passage`,
`original`, `translation`), each a verbatim substring, whitespace aside, of its passage;
rendered two columns under the statement; every cell claim of both comparisons carries one;
set the quote on every new claim a comparison cell cites. *Comparisons:* `question`,
`thinkers` (column order), `statement`, `rows` (each `question`, `positions` keyed by
thinker id, a short `note` that must relate to the readings where a cell's claim has any and
say when a cell is set for one word), `shared` (each `premise` in both texts' terms, `claims`
of different thinkers naming each other by `shares_premise_with`, `passages` cited by those
claims; one entry cannot hold two claims of one thinker; two entries may share a premise),
`passages` = every span the body or a note quotes; an empty cell renders »No position in the
map« and the note says whether the text is absent from the map or no passage in the map
speaks of it (never »the thinker is silent«); the build checks all of it, including that
every »...« quotation in body or notes lies inside one listed passage (pieces split at »...«)
and that the body links every `r-` whose `reading_of` is a cell claim. Templates:
`site/templates/{base,index,about,node,comparison}.html`; comparison table full-width above
the text/passages grid, phone cells stack with `data-thinker` labels, no JavaScript.

**Kant nodes on `main` (87: 1 t, 2 w, 27 p, 50 c, 6 a, 2 r):** `t-kant`; `w-kant-krv`, `w-kant-prolegomena`;
22 passages `p-krv-*`, `p-prol-*` by AA page and line (B xxvi 3:16.30–17.07; B xxvii–xxix
in four spans 3:17.07–18.21, run 7; B xxviii–xxix, B xxix–xxx; A 24/B 38; A 26/B 42 and
`p-krv-a26-b42-b` conclusion (b) 3:55.09–18; A 42/B 59; A 43/B 60; A 235/B 294; A 236/B 295;
B 307; B 308–309; Prol 289, 314, 350, 350–351, 352, 353; **run 13: A 538–541 / B 566–569,
the section »Möglichkeit der Causalität durch Freiheit ...« of the third antinomy's
resolution, AA 3:366.08–368.13 in five spans `p-krv-b566-569-{intelligible,double-side,
two-characters,no-time-conditions,freedom-and-nature}`, A/B pages given as the section's
since korpora marks no B page break, AA line the locator**); 50 claims (space a priori, a
subjective condition of sensibility, not of things in themselves; appearance requires a
thing in itself; things in themselves thinkable not knowable; the noumenon negative only;
B xxix–xxx the pretension, annulling knowledge for faith, dogmatism; the island and the
understanding's principles only for experience; Prol § 57 the two absurdities, bounds
against limits, metaphysics leads to limits; B xxvii–xxix the same will not free as
appearance and free »als einem Dinge an sich selbst angehörig«, conditional; freedom not
cognized by speculative reason; freedom thinkable if the critical distinction holds,
»wenigstens«; morality would yield had freedom been proved unthinkable, under »supposing«; **run 13, 15
claims from A 538–541, all subjunctive »würde« kept as »would« except the asserted clauses:
»intelligibel« defined; the causality of a being from two sides, conditional; the double side
contradicts no concept of experience; a transcendental object must underlie appearances; nothing
hinders attributing it a non-appearing causality; every efficient cause has a character; the
empirical and the intelligible character, »den Charakter des Dinges an sich selbst«; under no
conditions of time, »denn die Zeit ist nur die Bedingung der Erscheinungen, nicht aber der
Dinge an sich selbst« (asserted; the shared premise on time, with § 24 and § 23); intellectual causality not in the
series; the intelligible character »niemals unmittelbar gekannt«; actions explicable by laws of
nature; the active being free of natural necessity; begins its effects of itself; freedom and
nature at the same actions, `depends_on` the two it sums by »So würde denn«. The word »Wille«
does not occur in the section: every cell set from it says it is set for »Ursache«,
»Handlungen«, »Wirkungen«, »frei«, »unmittelbar«, and that reading its »handelndes Subject« as
the will of B xxvii–xxviii is the map's step**);
6 arguments, all `checked`: `a-kant-space-not-of-things-in-themselves` (s→¬a ⊢ ¬s),
`a-kant-appearance-requires-thing-in-itself` (¬t→¬w, w ⊢ t),
`a-kant-practical-assumption-requires-removing-speculative-pretension` (k→e, e→x, a→¬x ⊢
a→¬k; a→¬x the map's bridge), `a-kant-denying-things-in-themselves-absurd` (n→g, g→u, ¬u ⊢
¬n; ¬u the map's claim), `a-kant-freedom-thinkable-under-the-critical-distinction` ((k∧r)→f,
f→t ⊢ (k∧r)→t; f→t the map's bridge; the two »Widerspruch« differ; the deduction sentence
e→r is not a premise), `a-kant-double-side-contradicts-no-concept-of-experience` (n∧(n→g),
g→h, h→d ⊢ d; h→d the map's bridge, the transcendental object = what the object of the senses
is in itself also the map's); 2 readings, `r-kant-two-aspect` (Prauss 1974; Allison 2004, ch. 2)
and `r-kant-two-object` (Strawson 1966, Part Four; Guyer 1987, Part V; Van Cleve 1999, ch.
10), both `reading_of: c-kant-things-in-themselves-thinkable-not-knowable`, each citing B
xxvii–xxviii (»in zweierlei Bedeutung«). Translations the project's own. *Grenzen* =
"limits", *Schranken* = "bounds" (4:352.21–25); "aufheben" = "annul"; "ihr Ziel setzen" =
"put a stop to"; the Korpus's »nothwendiggemachte« at 3:17.07 kept and noted. Kant says the
will *belongs to* a thing in itself, thought so if the critique is right, never that it is
one: the hinge of both comparisons; never write »belongs to« flat. Not in the map: A 236–260
/ B 295–315 beyond the opening, Prol §§ 58–59, the B xxvi–xxvii footnote, the antinomy's
resolution outside A 538–541 (A 532–537, A 542 ff.), the Grundlegung and the second Critique (so no sentence may say Kant asserts that
morality presupposes freedom; B xxviii only supposes it, »da ich zur Moral nichts weiter
brauche, als daß Freiheit sich nur nicht selbst widerspreche«).

**Schopenhauer nodes on `main` (65: 1 t, 1 w, 20 p, 39 c, 4 a):** `t-schopenhauer`; `w-schopenhauer-wwv1`
(Zürcher Ausgabe 1977 after Hübscher 1859; vol. 1 = Books 1–2, vol. 2 = Books 3–4 and the
Anhang, continuous pagination); 20 passages `p-wwv1-*`: § 1 (ZA I 28, 30), § 18 (142;
144–145), § 19 (146–147; 147–148), § 21 (153–154), § 22 (154; 155), § 23 (156; 157), § 24
from Projekt Gutenberg-DE with Grisebach's pages and no ZA page (the first paragraph »Wir
haben von dem großen Kant gelernt«; the second »Kant richtig geschlossen«; »Wenn daher auch
alle Mathematik« to »nicht im Mindesten erklärt«, »in Hinsicht aus« kept), § 25 (to
»untheilbar«), Anhang (ZA II 513–514 Kant's greatest merit, six sentences; 516 »Er zeigte,
daß die Gesetze« to »Eichhörnchen im Rade«, zeno's »Kam zeigte« kept and noted; 534–535
Kant's derivation of the thing in itself; 535 only the derivation is faulty; 536–537 the
Transcendental Aesthetic paragraph whole, »Formen seines Erkennens« noted); 39 claims, all
`draft`, with quotes on every cell claim; 4 arguments, all `checked`:
`a-schopenhauer-corporeal-world-in-itself-is-will` (m→a, a→(v∨w), m→¬v ⊢ m→w; premises 1 and
3 the map's, the conclusion epistemic), `a-schopenhauer-kant-derivation-cannot-reach-thing-in-itself`
(k, b, (k∧b)→¬e ⊢ ¬e; b the § 19 principle; the bridge the definition at ZA II 535),
`a-schopenhauer-will-knows-no-plurality` (p∧f1∧f2, (f1∧f2∧w)→o, (p∧o)→¬m ⊢ w→(o∧¬m); f2
»frei von aller Form der Erkenntniß«; w not a premise, the text draws the step
conditionally), `a-schopenhauer-cognitions-a-priori-are-the-intellects-own-forms` (a, a→¬e,
¬e→b, m, (b∧m)→f, f→s ⊢ s; m discharges C9's antecedent as the text's »Demnach« tacitly
does; f→s the bridge; the form proves the synonymy, not the uniqueness). No attack link on
any Kant node: Schopenhauer accepts »die Anerkennung eines Dinges an sich zur gegebenen
Erscheinung« (ZA II 535). Shared-premise links with Kant, all Schopenhauer's own words: B
xxvi, Prol § 32 ↔ Anhang 535 (a thing in itself to a given appearance); A 24/B 38 ↔ Anhang
534 and ↔ Anhang 513–514 »weil Bedingungen desselben ... a priori erkannt werden« (space
given a priori); A 26/B 42 (b) ↔ Anhang 534 (a subjective form); A 26/B 42 ↔ § 23 and ↔
§ 24 »nicht Bestimmungen desselben« (no determination of the thing in itself); A 24/B 38 ↔
§ 24 »nicht als eine von ihnen abhängende Bestimmung« (not dependent on the objects); A
236/B 295 with Prol § 57 ↔ Anhang 516 (the laws of experience have no use beyond it, the
identification of Grundsätze and Gesetze the map's, carried by § 57); A 42/B 59 ↔ Anhang
513 »auf Grund der Nachweisung, daß« (things not cognized as in themselves; a factive noun
asserts as a factive verb does). Terms: Vorstellung "representation", Erscheinung
"appearance", Objektität "objectity", Satz vom Grunde "principle of sufficient reason",
nachweisen "show" vs beweisen "prove", Voraussetzung "presupposition", Annahme
"assumption", Besonnenheit "discernment", »X ist uns bewußt« = "we are conscious of X". The
identity of will and body is a claim, not an argument, because § 18 says it can never be
proved. Not in the map: § 2, § 20, § 24 beyond its first two paragraphs, § 25 beyond its
first paragraph, §§ 26–29, the fourth Book, the Anhang beyond the four spans held (nothing
of 517–533 or 537–650, the Fichte paragraph, the theorems on time, the categories).

**Nietzsche nodes on `main` (71: 1 t, 2 w, 19 p, 44 c, 4 a, 2 r; 227 nodes in all: 3 t, 5 w,
66 p, 133 c, 14 a, 4 r, 2 x):** `t-nietzsche`; `w-nietzsche-jgb` (1886), `w-nietzsche-gd` (1889),
cited by aphorism and, for GD, chapter and section (Fabel by stage 1–6), KSA pages not
given; 19 passages: JGB 15 (two spans), 16 (two), 17, 19 (two), 21 (two: the first sentence;
»Man soll nicht« to »mythologisch«), 34 (two), 36 (two), 54; GD Vernunft 2, 5, 6; Fabel;
Irrthümer 3 (to »Das folgt daraus!«). 44 claims, all `draft`: JGB 16 (Schopenhauer's »ich
will« a superstition; immediate certainty a contradictio in adjecto; »ich denke«
presupposes comparison), 17 and 54 (the subject a grammatical habit; the I a synthesis), 19
(Schopenhauer took over a popular prejudice; willing complicated; the belief that will and
action are one from erroneous inferences; »scheint mir« kept), 36 (the mechanistic world not
representation in Schopenhauer's sense; will-causality posited as the only, conditional;
the world would be will to power, conditional), GD Vernunft (the apparent world the only
one; dividing the world is décadence; the will as cause the great error), Fabel (stage 4
framed »At the positivist stage of the history of the error«, Clark 1990 ch. 3; stages 5–6
in Nietzsche's own voice, owner decision; idea refuted; abolishing the true world abolishes
the apparent), Irrthümer 3 (belief in causation from the inner facts; the will moves nothing,
»mehr« kept; the motive a surface phenomenon; the I a fable; evidence for spiritual causes
gone; no spiritual causes by »Das folgt daraus«), 15 (sense organs not appearances in the
idealist sense; the external world not the work of our organs, »gesetzt, dass der Begriff
causa sui etwas gründlich Absurdes ist« inside it, »-?« noted), 21 (causa sui the best
self-contradiction; cause and effect conventional fictions, a »soll«; in the »"An-sich"«
nothing of causal connections, »"psychologischer Unfreiheit"« among them; we alone
invented causes, »die Freiheit« among them, and reading the sign-world »als "an sich"« into
things is mythology), 34 (belief in immediate certainties a naïveté; truth worth more than
semblance a moral prejudice; doing away with the apparent world leaves nothing of truth,
»gesetzt, ihr könntet das«). 4 arguments, all `checked`:
`a-nietzsche-external-world-not-work-of-organs` (w→b, b→o, s→¬o ⊢ s→¬w; s→¬o the map's
bridge), `a-nietzsche-ich-denke-has-no-immediate-certainty` (c, c→b, b→¬g ⊢ ¬g),
`a-nietzsche-true-world-does-not-obligate` (¬r, ¬r→¬k, ¬k→¬o ⊢ ¬o; stage 4),
`a-nietzsche-evidence-for-spiritual-causes-gone` (¬w, ¬m, ¬i, e→(w∨m∨i) ⊢ ¬e; epistemic). 2
readings on `c-nietzsche-world-would-be-will-to-power`: `r-nietzsche-will-to-power-asserted`
(Richardson 1996, ch. 1 "Being") and `r-nietzsche-will-to-power-not-asserted` (Clark 1990,
ch. 7 "The will to power"). **Run 12 gave the asserted reading the paragraph *What it
answers to GD*** (GD Irrthümer 3 denies the will as the first of the »"inneren
Thatsachen"«, Vernunft 5 the will as »ein Vermögen«; JGB 36's »Willens-Causalität« is
»Wille auf Wille wirkt« and neither GD passage in the map speaks of that; against the
answer: Vernunft 5's »an Willen als Ursache überhaupt« and JGB 36's »im Grunde ist der
Glaube daran eben unser Glaube an Causalität selbst«; the two GD passages added to its
`passages:`; the map picks neither), and the sentence on it in `x-the-will` and that page's
closing paragraph were updated. Attack links, the only ones in the map: JGB 16 →
`c-schopenhauer-will-not-inferred-but-immediately-known` and →
`c-schopenhauer-body-given-in-two-ways` (§ 18's »jenes Jedem unmittelbar Bekannte«); JGB
19 → the same § 22 claim and → `c-schopenhauer-act-of-will-and-action-of-body-identical`;
JGB 16 → `c-kant-things-in-themselves-thinkable-not-knowable` (the words »Ding an sich«
alone, no sentence naming Kant). No shared premise with Nietzsche, with the reasons on the
pages (JGB 16 hits the term as such; Vernunft 6 Satz 4 diagnoses; stage 4 is framed as the
positivist stage; JGB 21's »"An-sich"« in scare quotes is the nearest three-way premise,
left open). Claim→claim `depends_on` with the connective quoted: true-world-not-obligating
→ idea-refuted (»folglich«); evidence-gone → no-spiritual-causes (»Das folgt daraus«).
Terms: Gewissheit "certainty", Erkenntniss "cognition", Schein/Anschein "semblance",
scheinbar "apparent", wirken "work", Thatsache "fact", Empirie "empirical evidence",
Verhängniss "calamity", Vermögen "faculty". Gutenberg's »wie es in ein Satz ist« (JGB 36)
is read as »mein Satz«, "as is my proposition", said on the passage. Not in the map: JGB
20 (adds no cell), JGB 21 and 34 beyond the spans held, JGB 230; GD Irrthümer 7–8; Nachlass
nothing, by design.

**The two comparisons.** `x-thing-in-itself` (/x/thing-in-itself/, `checked` with the
owner's status note of 2026-10-10, which carries the operator's dated clause on cells
added since; re-read it against the whole table every run): seven rows (a thing in itself
*to* a given appearance, never »behind«; reached by inference; cognized immediately; what
can be said of it; the division and refusing it; the will; the world of appearance the
subject's own work), seven `shared` entries (above), divergences (B xxvi's ground is the
absurdity of appearance without anything that appears, not a causal inference; B xxvi
against Fabel stage 6; immediacy; the will; causality and the in-itself), what depends on
the reading of Kant, gaps, and a closing paragraph naming what the owner ordered and what
he has not read (everything since 2026-10-10, listed). `x-the-will` (/x/the-will/,
`draft`, Ask 9): five rows (what the will is; immediately known, Kant's cell since run 13
with »niemals unmittelbar gekannt« for the word »unmittelbar«; cause of the body's
actions, Kant's cell filled in run 13 from A 538–541 for »Ursache«/»Handlungen«/»Wirkungen«;
free, and free of what, the Schopenhauer and Nietzsche cells set for the word »frei« / »die
Freiheit«, Kant's since run 13 also the three antinomy sentences, Schopenhauer's also § 24;
what is drawn from it), two `shared` entries since run 13, both the premise on time, *a
condition or form of appearances only, and no determination of the thing in itself* (Kant's
»denn« clause ↔ § 24's »Kant richtig geschlossen, daß Zeit, Raum und Kausalität ... nicht
Bestimmungen desselben seyn« and ↔ § 23's »frei von allen Formen«, the same two claims that
share the space premise with A 26 / B 42; »Bedingung« = »Form« the map's step; not § 25,
whose statement predicates »Erkenntnißform« of the cognition a priori and whose body says the
link is not set there), with the two nearest on the will itself argued and left open (Kant's B xxvii causality clause, conditional, beside § 23's
groundlessness; § 18's »stehn nicht im Verhältniß der Ursache und Wirkung« beside GD's »Der
Wille bewegt nichts mehr«), the three attack links described, divergences (the hinge above;
immediacy; the will as cause, where JGB 19 and § 18 refuse cause and effect for opposite
reasons; the two senses of »frei«; what each draws), the readings of JGB 36 and of Kant
without picking, gaps, closing paragraph with provenance dates. »intelligibler Charakter«:
since run 13 Kant's A 539 / B 567 carries it (»intelligibelen Charakter«); no Schopenhauer
passage does, and no passage says whether JGB 36's quotation marks point at Kant's; the JGB
36 node and both pages say so.

**Sources.** *Kant:* https://korpora.org/kant/aa{03,04}/{page:03d}.html, one AA page per
file, lines in `<tr>` rows, ISO-8859-1 with HTML entities; join hyphenated words by hand; the
transcription marks no A/B page breaks, so inside a section longer than a page give the A/B
range of the section and the AA line (the section A 538 / B 566 begins at 3:366.05; A 236 / B 295 at 3:203.04; B 307 at 3:209.32);
the `korpora.zim.uni-duisburg-essen.de` host fails through the proxy. *Schopenhauer:*
zeno.org `http://www.zeno.org/Philosophie/M/Schopenhauer,+Arthur/Die+Welt+als+Wille+und+Vorstellung/Erster+Band/<Erstes+Buch|Zweites+Buch|Anhang.+Kritik+der+Kantischen+Philosophie>`,
ISO-8859-1, text in `<div class="zenoCOMain">`, `<h5>` the § numbers, `[N]` in
`class="zenoTXKonk"` marks where ZA page N begins; down on 10-09 and 10-13, up on 10-14; OCR
slips (»Kam«, »hohem« for »höhern«): collate every span word by word against Grisebach's
text, keep the transcription's letters, name every non-orthographic variant on the passage.
Fallback Projekt Gutenberg-DE
`https://projekt-gutenberg.org/authors/arthur-schopenhauer/books/die-welt-als-wille-und-vorstellung-band-i/chapter/N`
(Grisebach, Reclam 1892; chapter = § + 2, chapter 74 the Anhang, 2 the prefaces; `<p>`
elements, every paragraph repeated once, not byte-identical, strip by searching; two
advertising paragraphs at the end; `<a name="pageN">` anchors give Grisebach's pages; say
»ZA page not given; Grisebach's pagination ... p. N« in `ref` and keep its orthography).
The Internet Archive has the 1859 scans (`bub_gb_xhfF5h_0EggC`, vol. 2). *Nietzsche:*
Project Gutenberg eBooks 7204 (JGB) and 7203 (GD),
`https://www.gutenberg.org/cache/epub/<n>/pg<n>.txt`, after Projekt Gutenberg-DE,
first-edition orthography, edition unstated (said on the nodes); aphorisms as a line `N.`
alone, chapters as `Erstes Hauptstück:` lines, GD chapters by title; zeno.org resets
connections for Nietzsche; deutschestextarchiv, de.wikisource and nietzschesource are
unusable. Every `original` is extracted by start/end substring and asserted verbatim.

**The adversarial pass is not optional, and it finds what the truth table cannot.** Brief
for the reviewer: the new and revised nodes, the diffs, the corpus files, the older
passages they cite, the conventions, and the order validity, fidelity, attack links,
translation, references, readings, links, format, rendered page; for a comparison also
rows' fit, shared premises asserted by both, divergences, readings not picked, quotations.
The Agent tool runs the reviewer in the background; it takes seven to twelve minutes and
120,000–260,000 of its own tokens; draft memory and the changelog meanwhile; the stop hook
asks for a commit while it runs, which must be refused until the report is in. Rules
distilled (runs 2–11): when a form's conclusion is not word for word the conclusion claim,
the missing step is a tacit premise, make it an `assumption` and say it is the map's; a
form's antecedent must be the conclusion claim's antecedent atom for atom; a premise claim
that states a middle term gets its own atom; an idle premise comes out of `premises:`; when
the text gives a verdict then consequences, the premise that the consequence is
unacceptable is the map's; before linking an attack, check that the target states what the
attacker denies, and the denying words must be inside the attacker's statement; a
comparative, a prescription (»soll«) and a conditional whose antecedent the author never
asserts deny and share nothing; quote the connective for every claim→claim `depends_on` or
set none; keep every qualifier (»nur«, »jedenfalls«, »scheint mir«, »gesetzt«, »mehr«,
»wenigstens«) and the mode (conditional, subjunctive »käme« = "would", reported views in
reported form, »gedacht« not asserted); the pronoun's antecedent and a relative pronoun's
gender decide the atom's subject; a statement must be readable alone (no opening anaphor;
restate the supposition it stands under); keep the person the text addresses; a mark the
text puts on a sentence (»-?«) belongs in the statement; a body may quote in »...« only text
inside a passage node, so widen the span or refer without quoting; a narrated stage is the
stage's, not the narrator's, until a reading says so; a voice note on a narrated text is a
reading; write »on the reading ...; the other reading ...« every time a body relates to a
contested claim; a connection the page draws between texts is »as the map reads it«; an
identification of two texts' terms is the map's and is said so; a factive noun asserts as
its verb does; word a shared premise in both texts' terms and to cover both predicates;
a note that summarizes a statement must not outrun it; never write »thinker X is silent
on Y« or »X does not say Y«, write »no passage in the map speaks of Y«; name absent texts
by reference only, never by what they contain; before writing »the map holds only X of
aphorism N«, `ls map/p-*N*`; a page inherits a claim node's unmarked attributions, so read
the node bodies it cites; a coverage sentence must say exactly which spans are held; check
the neighbouring paragraph in the corpus, not from memory; check a source for page anchors
before writing »no page marks«; a collation note lists every non-orthographic variant and
no non-variant; a bridge's parenthesis may not claim more than the body; a quote block is
the load-bearing sentence, not the whole passage; two passages may not share a title;
"orthography of the first edition" becomes "consistent with"; a rule the model states and
nothing enforces will be broken, so write the check; a status note true when written
becomes false by accretion, so re-read it every run. Run 13 added: a generalization about a
text's mode (»the one clause asserted outright«, »every main clause under ›würde‹«) must be
checked against every passage body of the span, which are the project's own refutation; a
link set in front matter must agree with the node's prose, which the build never checks; a
quotation can be verbatim, inside a listed passage, and still transplanted to another
subject (said of two concepts, used of two causings); when citing the other comparison for a
parallel link, re-read which claims carry it; a comparative »so wie ... wie« is not a
condition; »the same X« across two texts is a connection the map drew, so »as the map reads
it«; a sentence true when written (»the one empty cell«, »with no new node«) is falsified by
the same run's additions, so grep the page for them before the review; the A page of a KrV
span is checked against de.wikisource.org's page-by-page transcription of the 1781 scan
(`Seite:Kant_Critik_der_reinen_Vernunft_NNN.png`, `action=raw`, different orthography), the
B page inside a long section is unverified and is given as the section's range. The review
of run 13 took 212,000 tokens and sixteen minutes on 21 new nodes.

**Money.** 10.88 EUR incl. BTW spent in Q4 2026 of 200 EUR (`LEDGER.md`). Nothing spent in
runs 1–12. The card used for the domain is still unreported.

**Tooling facts, owner's machine (Windows, Git Bash).** `python` (3.11, PyYAML), not
`python3`; set `PYTHONIOENCODING=utf-8`; a long inline heredoc fails in Git Bash and `rm
-rf` in the scratchpad was denied: write scripts to the scratchpad and run them by path.
Commits as `TheAndries`; push with plain `git push`. Owner-session commit messages begin
»owner session —«.

**Tooling facts, cloud container.** Python 3.11 with PyYAML, Node 22 with a global
`playwright` and Chromium at `/opt/pw-browsers/chromium` (screenshots: `NODE_PATH=$(npm root
-g) node script.js`, viewport 390 for phone). WebSearch and WebFetch work (Cambridge/OUP
catalogue pages return nothing useful); `pip install` and raw downloads work through the
proxy; `gh` exists on the path but is not to be used by the routine (no connector; the
scripts that call it run only in Actions). Git author `Claude <noreply@anthropic.com>`;
commits carry the session trailer. The container checks out a detached HEAD whose local
`main` is stale: `git fetch origin main && git pull --rebase origin main` is not possible on
a detached HEAD, so `git fetch origin main`, `git rebase origin/main` if the inbox workflow
has pushed, then `git push origin HEAD:refs/heads/main`. A stop hook asks for a commit
whenever the turn ends with uncommitted changes; do not commit nodes before the review.
Writing a Python heredoc through the shell can hang; write scripts to the scratchpad and
run them by path.

**Next.** If `INBOX.md` has an entry: handle it first, inside the protocol's deadlines
(above). If the owner answered Ask 9: apply as under Ask 7 (`checked` with `status_note`;
versions for changed statements with credit). If Ask 8: read the brief before building.
Otherwise: a fourth thinker is not yet due (Phase 2 should see one filing or the owner's
word first); useful content runs meanwhile are the gaps both pages list (the first
comparison's Kant cell on cognizing immediately could take
`c-kant-intelligible-character-never-known-immediately`, which needs its status note's dated
clause and closing paragraph extended; Schopenhauer § 2 and the Anhang's theorems on time;
Nietzsche JGB 21 and 34 beyond the spans held; the antinomy's resolution outside A 538–541),
each only where it adds a cell or a row, with quotes on every new cell claim; and the
quotation check could be extended from comparisons to all bodies after measuring how many old
nodes fail.

**Dropped from memory this run:** nothing; run 12's compression left room, and run 13 added
the A 538–541 nodes, the shared premise on time and the korpora page-break fact; about 5,450
words of 8,000.
