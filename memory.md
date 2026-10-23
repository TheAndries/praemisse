# memory.md

Carried state for the operator. Capped at 8,000 words. Rewritten each run.

## State as of 2026-10-23 (run 17, end)

**Identity and governance.** Name `praemisse`; domain praemisse.com at TransIP; site live at
https://praemisse.com/ (GitHub Pages, HTTPS enforced, certificate to 2027-01-03, GitHub
renews). Repository https://github.com/TheAndries/praemisse, public, `main`. Routine
`trig_01CybW54QF5Q5hCdyVQzM8qX`, `34 5 * * *` UTC, model `claude-fable-5-1`; runs 1–17 were
served on that model, no handover note needed. Runs 12 to 17 fired on consecutive days. **No run is recorded for 2026-10-16 or
2026-10-17** (no commit, no changelog entry between run 11 on 10-15 and run 12 on 10-18);
the operator cannot see the routine's run history and asked the owner to look (Ask 10).
The GitHub and Claude Code Remote tools in the tool list are platform-attached to every
cloud session and are not a config change (`ROUTINE.md`, Ask 6): do not raise it again, and
do not use them; everything goes through git and the repository. Open disputes: none.
Attestations: none. Open motions: none (the design motion of 2026-10-19 closed as moot; owner decision instead). INBOX: three owner notes of 2026-10-19, all handled in the owner sessions; nothing new at runs 1–17; no form filing yet; nothing arrived
between run 16 and run 17 (`origin/main` at run 16's commit when run 17 began). Open asks: 4 (mailbox; deferred by owner; now the second filing
route, for anyone without a GitHub account), 9 (the owner's qualified review of https://praemisse.com/x/the-will/,
opened 2026-10-15; blocks nothing), **10 (opened 2026-10-18: test the filing route once from
a node page, and look at the routine's run history for 10-16 and 10-17; blocks the
confidence of Phase 2, not the plan)**. Asks 1, 2, 3, 5, 6, 7, 8, 11, 12 done.

**The design, merged into `main` on 2026-10-19 (Asks 11, 12 done).** The owner's brief of 2026-10-11
(`DESIGN-BRIEF-2026-10-11.md`) chose direction A, *the edition*; the owner approved the specimen
("Yes to all"), said the look is his to decide and not the board's, and *Colour, space and pages*
is binding in `DESIGN.md`. Files: `site/static/tokens.css`, `site.css`, templates `base`,
`comparison`, `node` (claim, argument, reading), `measure` (thinker, work, passage, dispute,
attestation), `index`, `about`; `site/site.yaml` (palette, `start_here`); `build.py` renders
(`render_node`, `render_index`, `render_front`, `render_pair`, `--specimen ID PATH`); specimens
and screenshots under `site/specimens/`; verification in `DESIGN.md`. Branch `design-type`
(merged) made the type fluid (`--size-3` 19px to 22px at 1920, `--measure` 60ch, hyphens off at
720px and above except in passages, the front page's lead in roman from "Broken into explicit
premises") and subset the fonts by `tools/subset_fonts.py` (the full faces in
`site/fonts/libertinus/full/`, unpublished); **rerun the script when a passage brings a new
character, since `build.py` fails on a character the subsets lack**. A node page is 161 KB on
first visit; the 120 KB budget is not met (fonts; `PLAN.md` §5); the dispute and attestation
templates have no page to render until the first filing. A colour or spacing change: `tokens.css`
only; B's grid: the four `--grid-*` tokens.

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

**Kant nodes on `main` (92: 1 t, 2 w, 28 p, 54 c, 6 a, 2 r):** `t-kant`; `w-kant-krv`, `w-kant-prolegomena`;
23 passages `p-krv-*`, `p-prol-*` by AA page and line (B xxvi 3:16.30–17.07; **run 17: `p-krv-b-xxvi-footnote`, Kant's own footnote at B xxvi whole, four sentences, the mark at 3:17.05 after »denken können«, the note printed at the foot of AA III 17 in ten lines korpora does not number, cited by the page of its mark, the B page of the note itself unverified; korpora's double spaces at the nine line breaks reduced to one**; B xxvii–xxix
in four spans 3:17.07–18.21, run 7; B xxviii–xxix, B xxix–xxx; A 24/B 38; A 26/B 42 and
`p-krv-a26-b42-b` conclusion (b) 3:55.09–18; A 42/B 59; A 43/B 60; A 235/B 294; A 236/B 295;
B 307; B 308–309; Prol 289, 314, 350, 350–351, 352, 353; **run 13: A 538–541 / B 566–569,
the section »Möglichkeit der Causalität durch Freiheit ...« of the third antinomy's
resolution, AA 3:366.08–368.13 in five spans `p-krv-b566-569-{intelligible,double-side,
two-characters,no-time-conditions,freedom-and-nature}`, A/B pages given as the section's
since korpora marks no B page break, AA line the locator**); 54 claims (space a priori, a
subjective condition of sensibility, not of things in themselves; appearance requires a
thing in itself; things in themselves thinkable not knowable; the noumenon negative only;
B xxix–xxx the pretension, annulling knowledge for faith, dogmatism; the island and the
understanding's principles only for experience; Prol § 57 the two absurdities, bounds
against limits, metaphysics leads to limits; B xxvii–xxix the same will not free as
appearance and free »als einem Dinge an sich selbst angehörig«, conditional; freedom not
cognized by speculative reason; freedom thinkable if the critical distinction holds,
»wenigstens«; morality would yield had freedom been proved unthinkable, under »supposing«; **run 17, the footnote's four sentences, each a claim with its quote, all four in row 4 of the first page (what can be said), set for »erkennen« and »denken« on the strength of the mark's place: to cognize an object requires »daß ich seine Möglichkeit ... beweisen könne«; »denken kann ich, was ich will, wenn ich mir nur nicht selbst widerspreche, d. i. wenn mein Begriff nur ein möglicher Gedanke ist«, no vouching that an object corresponds, »was ich will« the idiom and not »Wille«; objective validity, »reale Möglichkeit, denn die erstere war bloß die logische«, needs »etwas mehr«, »einem solchen Begriffe« resolved as the possible thought; »Dieses Mehrere ... kann auch in praktischen« sources of cognition lie, »kann auch« kept, »eben« as "for that matter"; no link on any of the four (»Aber« a contrast, »Dieses Mehrere« resumptive, the parenthesis's »denn« grounds a gloss), the rule / application relation to B xxviii's »d. i. die Vorstellung davon enthält wenigstens keinen Widerspruch« and the pointer of »praktischen« to B xxviii–xxx both the map's reading, said on the nodes; sentence 2 also in the will page's row on freedom for »widerspreche«, sentence 4 in its row on what is drawn for »praktischen«**; **run 13, 15
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
/ B 295–315 beyond the opening, Prol §§ 58–59, the antinomy's
resolution outside A 538–541 (A 532–537, A 542 ff.), the Grundlegung and the second Critique (so no sentence may say Kant asserts that
morality presupposes freedom; B xxviii only supposes it, »da ich zur Moral nichts weiter
brauche, als daß Freiheit sich nur nicht selbst widerspreche«).

**Schopenhauer nodes on `main` (70: 1 t, 1 w, 22 p, 42 c, 4 a):** `t-schopenhauer`; `w-schopenhauer-wwv1`
(Zürcher Ausgabe 1977 after Hübscher 1859; vol. 1 = Books 1–2, vol. 2 = Books 3–4 and the
Anhang, continuous pagination); 22 passages `p-wwv1-*`: § 1 (ZA I 28, 30), **§ 2 since run 16, from zeno.org collated against Grisebach: the first paragraph whole, eight sentences (ZA I 30; zeno's »daist« kept, its consistent one-word form and not a slip, named with Grisebach's »da ist«, the footnote mark after »unmittelbares Objekt ist« omitted), and the second paragraph's first seven sentences to »ein sehr großes« (ZA I 31; zeno's »d.h.« for »d. h.« named); the paragraph's remainder on the Satz vom Grunde in no passage**, § 18 (142;
144–145), § 19 (146–147; 147–148), § 21 (153–154), § 22 (154; 155), § 23 (156; 157), § 24
from Projekt Gutenberg-DE with Grisebach's pages and no ZA page (the first paragraph »Wir
haben von dem großen Kant gelernt«; the second »Kant richtig geschlossen«; »Wenn daher auch
alle Mathematik« to »nicht im Mindesten erklärt«, »in Hinsicht aus« kept), § 25 (to
»untheilbar«), Anhang (ZA II 513–514 Kant's greatest merit, six sentences; 516 »Er zeigte,
daß die Gesetze« to »Eichhörnchen im Rade«, zeno's »Kam zeigte« kept and noted; 534–535
Kant's derivation of the thing in itself; 535 only the derivation is faulty; 536–537 the
Transcendental Aesthetic paragraph whole, »Formen seines Erkennens« noted); 42 claims, all
`draft`, with quotes on every cell claim (**run 16, § 2, all three in row 7 of the first page:** the subject, »was Alles erkennt und von Keinem erkannt wird«, is »der Träger der Welt, die durchgängige, stets vorausgesetzte Bedingung alles Erscheinenden, alles Objekts«, the first two sentences joined by an added "and", the »denn« clause kept inside; the forms of all object »auch ohne die Erkenntniß des Objekts selbst, vom Subjekt ausgehend gefunden und vollständig erkannt werden können, d.h. in Kants Sprache, a priori in unserm Bewußtseyn liegen«, »dieser Gränze« restated as the boundary at which subject and object bound each other; »Dieses entdeckt zu haben, ist ein Hauptverdienst Kants und ein sehr großes«, »Dieses« restated; the twelve sentences of the two spans in no claim are listed on the passages and in the gaps list; no argument, no attack link); 4 arguments, all `checked`:
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
asserts as a factive verb does); **A 24/B 38 ↔ § 2 »a priori in unserm Bewußtseyn liegen« (space given a priori, the third entry under that premise, run 16; what § 2 adds, »vom Subjekt ausgehend«, the premise does not cover)**. Terms: Vorstellung "representation", Erscheinung
"appearance", Objektität "objectity", Satz vom Grunde "principle of sufficient reason",
nachweisen "show" vs beweisen "prove", Voraussetzung "presupposition", Annahme
"assumption", Besonnenheit "discernment", »X ist uns bewußt« = "we are conscious of X". The
identity of will and body is a claim, not an argument, because § 18 says it can never be
proved. Not in the map: § 2 beyond its two spans, § 20, § 24 beyond its first two paragraphs, § 25 beyond its
first paragraph, §§ 26–29, the fourth Book, the Anhang beyond the four spans held (nothing
of 517–533 or 537–650, the Fichte paragraph, the theorems on time, the categories).

**Nietzsche nodes on `main` (83: 1 t, 2 w, 23 p, 52 c, 4 a, 2 r; 249 nodes in all: 3 t, 5 w,
73 p, 148 c, 14 a, 4 r, 2 x):** `t-nietzsche`; `w-nietzsche-jgb` (1886), `w-nietzsche-gd` (1889),
cited by aphorism and, for GD, chapter and section (Fabel by stage 1–6), KSA pages not
given; 23 passages: JGB 15 (two spans), 16 (two), 17, 19 (two), 21 whole in four spans since run 14 (the first sentence;
»Das Verlangen« to »hinausläuft«; »Man soll nicht« to »mythologisch«; »Der "unfreie Wille"« to the end, from the same Gutenberg text), 34 in four spans since run 15 (the opening, »Auf welchen Standpunkt« to »Fragen mehr sind«, three sentences; »Der Glaube an« to »wenig Ehre macht«; »Es ist nicht mehr« to »die Sprache der Maler«; the close, »Warum dürfte« to the end, six questions; the span between the second and the third, »Mag im bürgerlichen Leben« to »Warum nicht?«, in no passage), 36 (two), 54; GD Vernunft 2, 5, 6; Fabel;
Irrthümer 3 (to »Das folgt daraus!«). 52 claims, all `draft`: JGB 16 (Schopenhauer's »ich
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
things is mythology; **run 14, the rest of JGB 21:** the desire for »"Freiheit des Willens"« »in jenem
metaphysischen Superlativ-Verstande« is »nichts Geringeres, als eben jene causa sui zu sein«, the
»nämlich« explaining the causa sui sentence, no link; whoever strikes the »Unbegriff« »"freier Wille"« is
asked, »Gesetzt« and »bitte ich« kept, to strike the »"unfreien Willen"«, »der auf einen Missbrauch von
Ursache und Wirkung hinausläuft«; »Der "unfreie Wille" ist Mythologie: im wirklichen Leben handelt es
sich nur um starken und schwachen Willen«, no connective to »mythologisch«, no `depends_on`; feeling
»Unfreiheit« in all »"Causal-Verknüpfung"« is »fast immer« a symptom of a lack in the thinker; the
sentences on the two sides from which »die "Unfreiheit des Willens"« is taken as a problem are in the
passage and in no claim; no attack on Kant's B xxviii (the denial would need the causa sui sentence
joined to the desire sentence, two statements; Kant's conditional) nor on »so fern nicht frei« (a
predicate thought in the appearance; whether it is Nietzsche's »unfreie Wille« no passage says), said on
the nodes; the four set first in the Nietzsche cell of `x-the-will`'s row on freedom, the mythology
sentence leading), 34 (belief in immediate certainties a naïveté; truth worth more than
semblance a moral prejudice; doing away with the apparent world leaves nothing of truth,
»gesetzt, ihr könntet das«; **run 15, the opening and the close:** »die Irrthümlichkeit der Welt, in der wir zu leben glauben« is »das Sicherste und Festeste«, the grounds »verlocken möchten« to conjectures about a deceptive principle in the »"Wesen der Dinge"«, a temptation reported, set in row 5 of the first page; whoever makes »"den Geist"« responsible for the world's falseness and takes it »sammt Raum, Zeit, Gestalt, Bewegung, als falsch erschlossen« »hätte mindestens guten Anlass« to distrust all thinking, the two questions after that colon in no statement, names no one, no attack link on Kant's subjective condition or Schopenhauer's forms (a consequence drawn, no denial), row 7; the innocence of thinkers permits them to ask consciousness for honest answers, »ob es "real" sei«, no connective to »Der Glaube an«, row 3 for the request to consciousness; the close's first three questions, why the world that concerns us might not be a fiction and whether the »"Gehört"« of »zur Fiktion gehört ein Urheber« belongs to the fiction, kept as questions, row 5 after the »"wahr"« / »"falsch"« questions they follow in the text (the reviewer moved them from row 7, where they had been set for the word »Urheber«; »die uns etwas angeht« is "that is of any concern to us", »mit zur Fiktion« "also belong"), the last three questions (irony towards subject, predicate and object; faith in grammar; the governesses) in the passage and in no claim, no link to JGB 17 / 54). 4 arguments, all `checked`:
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
20 (adds no cell), JGB 34's span from »Mag im bürgerlichen Leben« to »Warum nicht?«, JGB 19 beyond its two spans, JGB 230; GD Irrthümer 7–8; Nachlass
nothing, by design.

**The two comparisons.** `x-thing-in-itself` (/x/thing-in-itself/, `checked` with the
owner's status note of 2026-10-10, which carries the operator's dated clause on cells
added since; re-read it against the whole table every run): seven rows (a thing in itself
*to* a given appearance, never »behind«; reached by inference; cognized immediately, Kant's cell since run 14 also
`c-kant-intelligible-character-never-known-immediately`, set for »unmittelbar«, the *On immediacy* paragraph's
sentence »No Kant passage in the map speaks of immediacy« replaced, since it was false from run 13 on; what
can be said of it, Kant's cell since run 17 also the four footnote claims, with sentences in the note and under *What the three say*; the division and refusing it; the will; the world of appearance the
subject's own work; Nietzsche's cells in rows 3, 5 and 7 since run 15 also JGB 34's opening and close, with a sentence each under *On immediacy* and *On what the division is*; Schopenhauer's cell in row 7 since run 16 also the three § 2 claims, with sentences in the note and under *Space is given a priori*), ten `shared` entries (above; the memory of runs 13–15 said seven, which was stale), divergences (B xxvi's ground is the
absurdity of appearance without anything that appears, not a causal inference; B xxvi
against Fabel stage 6; immediacy; the will; causality and the in-itself), what depends on
the reading of Kant, gaps, and a closing paragraph naming what the owner ordered and what
he has not read (everything since 2026-10-10, listed). `x-the-will` (/x/the-will/,
`draft`, Ask 9): five rows (what the will is; immediately known, Kant's cell since run 13
with »niemals unmittelbar gekannt« for the word »unmittelbar«; cause of the body's
actions, Kant's cell filled in run 13 from A 538–541 for »Ursache«/»Handlungen«/»Wirkungen«;
free, and free of what, the Schopenhauer cell set for the word »frei«, the Nietzsche cell since run 14 the four
JGB 21 claims first and then the two set for »die Freiheit« / »"psychologischer Unfreiheit"«, Kant's since run 13 also the three antinomy sentences and since run 17 the footnote's »widerspreche« sentence, Schopenhauer's also § 24;
what is drawn from it, Kant's cell since run 17 also the footnote's »praktischen« sentence), two `shared` entries since run 13, both the premise on time, *a
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
`class="zenoTXKonk"` marks where ZA page N begins; down on 10-09 and 10-13, up on 10-14 and 10-22; OCR
slips (»Kam«, »hohem« for »höhern«): collate every span word by word against Grisebach's
text, keep the transcription's letters, name every non-orthographic variant on the passage.
Fallback Projekt Gutenberg-DE
`https://projekt-gutenberg.org/authors/arthur-schopenhauer/books/die-welt-als-wille-und-vorstellung-band-i/chapter/N/`
(**the trailing slash is required since 10-22: without it the redirect's body is empty; `curl -L -A "Mozilla/5.0"`**; Grisebach, Reclam 1892; chapter = § + 2, chapter 74 the Anhang, 2 the prefaces; `<p>`
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
The Agent tool runs the reviewer in the background; it takes six to sixteen minutes and
120,000–260,000 of its own tokens (runs 13–17: 212k/16 min on 21 nodes; 145k/7 min; 144k/8.5
min; 126k/6 min; 152k/8.5 min; 13–18 findings each, nearly all accepted); draft memory and the
changelog meanwhile; the stop hook asks for a commit while it runs, which must be refused until
the report is in; wait with a background loop on the agent's transcript, not by ending the turn.
Rules distilled, runs 2–17. *Forms:* when a form's conclusion is not word for word the
conclusion claim, the missing step is a tacit premise, an `assumption` said to be the map's; a
form's antecedent is the conclusion claim's antecedent atom for atom; a premise claim stating a
middle term gets its own atom; an idle premise comes out; when the text gives a verdict then
consequences, the premise that the consequence is unacceptable is the map's; a bridge's
parenthesis may not claim more than the body. *Links:* before linking an attack, check that the
target states what the attacker denies, and the denying words must be inside the attacker's
statement; a comparative (»so wie ... wie«), a prescription (»soll«) and a conditional whose
antecedent the author never asserts deny and share nothing; quote the connective for every
claim→claim `depends_on` or set none; a link set in front matter must agree with the node's
prose, which the build never checks; when citing the other comparison for a parallel link,
re-read which claims carry it; every new claim's body says why each neighbouring link is not
set (JGB 17 on any claim about the subject; §19's »noch denkbar« and §25's »nur in ihnen
denkbar« on any claim about thinking), so grep the statements for the term before writing »no X
statement in the map ...«, and name what is found with why no link is due. *Statements and
translation:* keep every qualifier (»nur«, »jedenfalls«, »scheint mir«, »gesetzt«, »mehr«,
»wenigstens«, »etwas«, »da«, »mit«, »aller-«, »dergestalt«, »nunmehr«, an added "and") and the
mode (conditional, subjunctive »käme« = "would", reported views in reported form, »gedacht« not
asserted); a »nur« inside a »wenn« clause scopes the conditional ("provided only that"), never
the noun after it; »ob ... auch ... oder nicht« is "does ... or not", not "also"; modal »eben« is
"simply"; »selbst« attaches to the word before it, »welchen selbst« and »auch jenes« are "even";
»nicht stehen kann« is "cannot vouch", never "without vouching"; the pronoun's antecedent and a
relative pronoun's gender decide the subject, and a resolved pronoun carries its antecedent's
qualifiers (»daher«, »unmittelbar«, »einem solchen Begriffe«), the same way in statement and
note; a dropped »aber«, an apposition rendered "that is", a colon turned comma are named like
any change; a statement is readable alone (no opening anaphor; restate the supposition it
stands under); keep the person the text addresses and a mark the text puts on a sentence
(»-?«); a supposition joined to a request (»Gesetzt ... so bitte ich«) is not the author's act,
write "supposes struck and asks"; a translation must parse in English alone; gloss a shared
stem the sentence plays on (»Noth« / »Nothwendigkeit«); keep the text's dashes when commas
would move an apposition; inside »...« keep the text's words and case and start the English
sentence otherwise; a body may not claim for the English what only the German carries; a
quote block is the load-bearing sentence, not the whole passage, and its translation is
checked for length against its original (a script cut one to five words and the substring check
passed it); a factive noun asserts as its verb does. *Attribution and absence:* never write
»thinker X is silent on Y«, »X does not say Y« or "X's will is not ..." where only X's statement
is in the map, write »no passage in the map speaks of Y«; "are to be assumed" where the text
says »nicht einmal annehmen, wenn ich nicht« is unsourced; a generalization over several
sentences or about a text's mode must hold of each sentence, checked against every passage
body of the span; a connection the page draws between texts, an identification of two texts'
terms, »the same X« across two texts, a relation like "gives the ground" with no connective,
and "the same »d. i.«" are the map's and said so; a narrated stage is the stage's until a
reading says so, and a voice note on a narrated text is a reading; write »on the reading ...;
the other reading ...« every time a body relates to a contested claim; word a shared premise
in both texts' terms and to cover both predicates; a note that summarizes a statement must not
outrun it. *Coverage and references:* name absent texts by reference only; before writing »the
map holds only X of aphorism N«, `ls map/p-*N*`; a coverage sentence says exactly which spans
are held, a gaps list names every remainder in a passage and in no claim, and "the cells are the
aphorism" is false while sentences sit in no claim, so count them; count a text's sentences one
way across all its passages (full stop and question mark; a colon joins halves) and fix the older
pages; count dashes before writing "the two dashes"; one sentence carries one reference on both
pages (A 540, not the span's A 539–540); "a third time" is the map's order of entry, so say
where the sentence stands in the text; a page inherits a claim node's unmarked attributions, so
read the node bodies it cites; a cell is placed where the text's neighbouring sentences point,
not where one word matches the row, and a sentence naming neither the row's subject nor its
question goes into the page's prose as the map's reading, not onto the row; a cell justified by
"the place of its mark" belongs where the marked sentence is set, so give the real reason or do
not set it. *Sources:* check the neighbouring paragraph in the corpus, not from memory; check a
source for page anchors before writing »no page marks«; before naming a transcription's form a
slip, grep the stored passages of the same text for it (zeno's »daist« is its orthography); a
collation note lists every non-orthographic variant and no non-variant; a transcription's double
spaces read as the edition's line breaks are "as the map reads the transcription"; the A page
of a KrV span is checked against de.wikisource.org's page-by-page transcription of the 1781
scan (`Seite:Kant_Critik_der_reinen_Vernunft_NNN.png`, `action=raw`), the B page inside a long
section is unverified and given as the section's range; "orthography of the first edition"
becomes "consistent with"; two passages may not share a title. *Pages:* a body may quote in
»...« only text inside a passage node, so widen the span or refer without quoting; a quotation
can be verbatim, inside a listed passage, and still transplanted to another subject; backslash
escapes belong in YAML, never in a Markdown body; a sentence true when written (»the one empty
cell«, »no Kant passage speaks of immediacy«, the closing paragraph's "on his instructions", a
status note) is falsified by accretion, so grep the page for them before every review; a rule
the model states and nothing enforces will be broken, so write the check.

**Money.** 10.88 EUR incl. BTW spent in Q4 2026 of 200 EUR (`LEDGER.md`). Nothing spent in
runs 1–12. The card used for the domain is still unreported.

**Tooling facts, owner's machine (Windows, Git Bash).** `python` (3.11, PyYAML), not
`python3`; set `PYTHONIOENCODING=utf-8`; a long inline heredoc fails in Git Bash and `rm
-rf` in the scratchpad was denied: write scripts to the scratchpad and run them by path.
Commits as `TheAndries`; push with plain `git push`. Owner-session commit messages begin
»owner session —«.

**Tooling facts, cloud container.** Python 3.11 with PyYAML (korpora.org answered at once on 10-23), Node 22 with a global
`playwright` and Chromium at `/opt/pw-browsers/chromium` (screenshots: `NODE_PATH=$(npm root
-g) node script.js`, viewport 390 for phone). WebSearch and WebFetch work (Cambridge/OUP
catalogue pages return nothing useful); `pip install` and raw downloads work through the
proxy; `gh` exists on the path but is not to be used by the routine (no connector; the
scripts that call it run only in Actions). Git author `Claude <noreply@anthropic.com>`;
commits carry the session trailer. A full build needs fontTools and brotli, which the container lacks and which `pip install -r site/requirements.txt`
did not supply for this interpreter: `python3 -m pip install fonttools brotli` did; `--check` runs no font-coverage
check, so run a full build to a scratch `--out` before the review. In an edit script, `re.sub` with a lambda does not
expand `\1`; a mangled front-matter line is recovered from `git show HEAD:map/<file>`. The container has checked out a detached HEAD whose local
`main` is stale (runs up to 14; run 15 found `main` checked out and tracking `origin/main`): `git fetch origin main && git pull --rebase origin main` is not possible on
a detached HEAD, so `git fetch origin main`, `git rebase origin/main` if the inbox workflow
has pushed, then `git push origin HEAD:refs/heads/main`. A stop hook asks for a commit
whenever the turn ends with uncommitted changes; do not commit nodes before the review.
Writing a Python heredoc through the shell can hang; write scripts to the scratchpad and
run them by path.

**Next.** If `INBOX.md` has an entry: handle it first, inside the protocol's deadlines
(above). If the owner answered Ask 9: apply as under Ask 7 (`checked` with `status_note`;
versions for changed statements with credit). If Ask 8: read the brief before building.
Otherwise: a fourth thinker is not yet due (Phase 2 should see one filing or the owner's
word first); useful content runs meanwhile are the gaps both pages list (the Anhang's
theorems on time; § 2's unclaimed sentences only if a row asks after the subject, which none does; Nietzsche JGB 19 beyond its two spans; GD Irrthümer 7–8;
the antinomy's resolution outside A 538–541; A 236–260 / B 295–315 beyond the opening),
each only where it adds a cell or a row, with quotes on every new cell claim; and the
quotation check could be extended from comparisons to all bodies after measuring how many old
nodes fail.

**Dropped from memory this run:** the design paragraph compressed from 346 to about 200 words (the list of `build.py` helper names, the `524d00e` merge note, the screenshot tooling on the owner's machine, the two copy notes already in `PLAN.md` §5); the review-rules paragraph rewritten from 1,700 to about 1,300 words, grouped by kind instead of by run, the per-run cost sentences reduced to one line (the full record is in `CHANGELOG.md`), every rule kept; run 17 added the footnote passage and four claims, the cell, and the review's rules; about 7,500 words of 8,000.
