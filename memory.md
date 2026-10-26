# memory.md

Carried state for the operator. Capped at 8,000 words. Rewritten each run.

## State as of 2026-10-26 (run 20, end)

**Identity and governance.** Name `praemisse`; domain praemisse.com at TransIP; site live at
https://praemisse.com/ (GitHub Pages, HTTPS enforced, certificate to 2027-01-03, GitHub
renews). Repository https://github.com/TheAndries/praemisse, public, `main`. Routine
`trig_01CybW54QF5Q5hCdyVQzM8qX`, `34 5 * * *` UTC, model `claude-fable-5-1`; runs 1–20 were
served on that model, no handover note needed. Runs 12 to 20 fired on consecutive days. **No run is recorded for 2026-10-16 or
2026-10-17** (no commit, no changelog entry between run 11 on 10-15 and run 12 on 10-18);
the operator cannot see the routine's run history and asked the owner to look (Ask 10).
The GitHub and Claude Code Remote tools in the tool list are platform-attached to every
cloud session and are not a config change (`ROUTINE.md`, Ask 6): do not raise it again, and
do not use them; everything goes through git and the repository. Open disputes: none.
Attestations: none. Open motions: none (the design motion of 2026-10-19 closed as moot; owner decision instead). INBOX: three owner notes of 2026-10-19, all handled in the owner sessions; nothing new at runs 1–20; no form filing yet; nothing arrived
between run 19 and run 20 (`origin/main` at run 19's commit when run 20 began). Open asks: 4 (mailbox; deferred by owner; now the second filing
route, for anyone without a GitHub account), 9 (the owner's qualified review of https://praemisse.com/x/the-will/,
opened 2026-10-15; blocks nothing), **10 (opened 2026-10-18: test the filing route once from
a node page, and look at the routine's run history for 10-16 and 10-17; blocks the
confidence of Phase 2, not the plan)**. Asks 1, 2, 3, 5, 6, 7, 8, 11, 12 done.

**The design, merged into `main` on 2026-10-19 (Asks 11, 12 done).** Direction A, *the edition*, owner's brief and approval ("Yes to all"); *Colour, space and pages* binds in `DESIGN.md`. Files: `site/static/tokens.css`, `site.css`, templates `base`, `comparison`, `node`, `measure`, `index`, `about`; `site/site.yaml`; `build.py` renders them (`--specimen ID PATH`); specimens under `site/specimens/`. Type fluid (`--size-3` 19–22px, `--measure` 60ch); fonts subset by `tools/subset_fonts.py` (full faces in `site/fonts/libertinus/full/`); **rerun the script when a passage brings a new character, since `build.py` fails on a character the subsets lack**. A node page is 161 KB on first visit (the 120 KB budget unmet, fonts); the dispute and attestation templates have no page until the first filing. Colour or spacing: `tokens.css` only.

**Checkpoint 1 (Ask 7) answered 2026-10-10:** nothing read as fabrication, eight decisions applied (`BOARD.md`); no rethink ordered; proceed.

**`PLAN.md` rewritten 2026-10-18 (run 12): Phase 2 opened.** The filing route is built (below); the deadlines of `DISPUTES.md` bind (publish next run, reply within three runs); the owner invites people in his own name, the operator does no outreach; the mailbox of Ask 4 is the second route; a fourth thinker by lineage (Phase 3) comes after Phase 2's first filing or the owner's word; §5 names the risk that the route is unexercised and a run that fails to fire lets a deadline pass.

**The filing route (run 12, 2026-10-18; `MODEL.md`, *Filing*; a method decision).** Two issue forms in `.github/ISSUE_TEMPLATE/`, `dispute.yml` and `attestation.yml` (the fields `DISPUTES.md` and `MODEL.md` list, `terms` consent to CC BY-SA 4.0 by name; titles »Dispute: <node id>« / »Attestation: <node id>«). `site/build.py`: `REPO`; `render_filing(n)` appends »Dispute this node« (c/a/p/r/x) and »Attest this node« (c/a/x) to the `.meta` paragraph, links to `REPO/issues/new?template=...&node=<id>`, one sentence on real name, passage, publication; `check_filing_issue` allows `issue:` (positive integer) on `d-`/`v-` only. `.github/workflows/inbox.yml` (no concurrency group, or a filing would be dropped; `workflow_dispatch` with `issue` re-runs intake): job `intake` on `issues: opened` runs `tools/inbox_from_issue.py intake --issue N`, which recognizes a filing by the form headings alone, appends a `##` entry to `INBOX.md` (date, kind, node, issue, login, URL, body verbatim), commits as `github-actions[bot]`, pushes `HEAD:main` with retries, posts one receipt (fingerprint `<!-- praemisse-inbox:received:N -->`); job `record` on a push touching `map/d-*.md`, `map/v-*.md` or `CHANGELOG.md` posts on the node's `issue:` its address `https://praemisse.com/<p>/<slug>/` and state once per state, and posts every `Returned (issue #N, YYYY-MM-DD): reason.` line (that exact form, one line) the operator writes in the changelog; it checks the issue is a form filing before posting. The token's push does not start `site.yml`; the build never reads `INBOX.md`. **The daily run must `git fetch origin main` and rebase before pushing.** Handling a filing: publish the `d-`/`v-` node (`target`, `disputant`/`attester`, `date`, `kind`, `contested_claim`, `alternative`, `passages`, `issue`, `outcome: published`; the target's `disputes`/`verified_by` must equal the set targeting it), move the INBOX entry to the changelog, reply within three runs by `reply: {date, text}` and outcome `argued`/`conceded` (a concession adds a `versions:` entry with `credit: d-...`); an attestation moves a `c-`/`a-`/`x-` to `attested`, two independent to `established`.

**Phase 0 complete (2026-10-05).** `site/build.py` (reads `map/*.md`, validates against `MODEL.md`, renders to `site/_build/`; `--check`, `--map`, `--out`, `--domain`; PyYAML only; node pages at `/<prefix>/<slug>/`), `.github/workflows/site.yml`, `notify-asks.yml` + `tools/open_asks_issue.py`.

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
»wenigstens«; morality would yield had freedom been proved unthinkable, under »supposing«; **run 17, the footnote's four sentences, each a claim with its quote, all four in row 4 of the first page (what can be said): to cognize an object requires »daß ich seine Möglichkeit ... beweisen könne«; »denken kann ich, was ich will, wenn ich mir nur nicht selbst widerspreche« ("provided only that"; »was ich will« the idiom, not »Wille«); objective validity, »reale Möglichkeit«, needs »etwas mehr«; »Dieses Mehrere ... kann auch in praktischen« sources lie; no link on any; on the will page set on no row, one sentence under *On freedom***; **run 13, 15 claims from A 538–541, all subjunctive »würde« kept as "would" except the asserted clauses:** »intelligibel« defined; the causality of a being from two sides; the double side contradicts no concept of experience; a transcendental object must underlie appearances; every efficient cause has a character; the empirical and the intelligible character, »den Charakter des Dinges an sich selbst«; under no conditions of time, »denn die Zeit ist nur die Bedingung der Erscheinungen, nicht aber der Dinge an sich selbst« (asserted; the shared premise on time, with § 24 and § 23); intellectual causality not in the series; the intelligible character »niemals unmittelbar gekannt«; the active being free of natural necessity; freedom and nature at the same actions, `depends_on` the two it sums by »So würde denn«. »Wille« does not occur in the section: every cell set from it says it is set for »Ursache«, »Handlungen«, »frei«, »unmittelbar«, and reading its »handelndes Subject« as the will of B xxvii–xxviii is the map's step**);
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

**Schopenhauer nodes on `main` (80: 1 t, 1 w, 25 p, 49 c, 4 a):** `t-schopenhauer`; `w-schopenhauer-wwv1`
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
first paragraph, §§ 26–29, the fourth Book beyond § 55's three spans, the Anhang beyond the four spans held (nothing of 517–533 or 537–650, the Fichte paragraph, the theorems on time, the categories). **Run 20, § 55 (Viertes Buch), the first fourth-Book passages, from zeno.org with ZA pages, collated against Grisebach (Gutenberg chapter 57): `p-wwv1-s55-will-as-such-free-everything-as-appearance-necessary` (ZA I 360, the opening, eight sentences by Grisebach's full stops), `p-wwv1-s55-person-never-free` (ZA I 362, two), `p-wwv1-s55-kant-intelligible-and-empirical-character` (ZA I 363, two; the mark of footnote 80 after »nachgewiesen« omitted, the note's text, KrV A 532–558 / B 560–586 and KpV, given in the body; Gutenberg prints the footnote's words inside the sentence, a transcription artefact to watch on every Gutenberg span). Variants named: zeno's »Beides«, »Ihre« (slip), »d.h.«, a comma after »geredet worden« for Grisebach's full stop, »absehn«, »Zusammenbestehn«, »Räume« (slip); Grisebach letterspaces »frei« twice and »an sich«, not reproduced. Seven claims, all in the will page's row on freedom after the three older: the will as such free »folgt schon daraus« that it is the thing in itself (»nach unserer Ansicht« = "on the view of Schopenhauer's work" in the statement); the will, thing in itself, not subject to »dem Satz vom Grunde, der Form alles Objekts«, »also keine Nothwendigkeit kennt, d.h. frei ist« (free of what); »Der Begriff der Freiheit ist also eigentlich ein negativer«, `depends_on` the former by »also«, the one link; »Jedes Ding ist als Erscheinung ... nothwendig: dasselbe ist an sich Wille, und dieser ist völlig frei, für alle Ewigkeit«; the person »ist nie frei, obwohl sie die Erscheinung eines freien Willens ist« (the will in its actions, B xxvii's sense, answered no); Kant »zuerst« showed the coexistence of necessity and the will's freedom in itself by the distinction of intelligible and empirical character, »welchen ich ganz und gar beibehalte«, with Schopenhauer's own definitions (the one § 55 sentence naming Kant; the Priestley half dropped and named); the intelligible character »als ein außerzeitlicher ... Willensakt zu betrachten«. No shared premise with Kant (B xxvii conditional and »gedacht«, the antinomy's »würde«; Kant's will belongs to a thing in itself, Schopenhauer's thing is in itself will), no attack from JGB 21 (denies an unfree will; § 55 denies the person's freedom) or GD 8 (»noch er selbst« against an act of will outside time is the map's identification, not made), all argued on the nodes and in the *On freedom* paragraph. Terms: »Gestaltungen« "shapes", »Wechselbegriffe« "convertible concepts", »kennen« "know", »nachweisen« "show", »dargethan« "set forth", »außerzeitlich« "outside time", »Willensakt« "act of will", »Korporisation« "corporization", »Handlungsweise« "manner of acting", »Thier« "animal". Not held: § 55's sentences between and after the spans (the self-denial of the will, every deed felt a priori as free, the simile of the tree, the whole remainder on empirical freedom, repentance, the Stoics), the essay on the fourfold root.**

**Nietzsche nodes on `main` (96: 1 t, 2 w, 27 p, 61 c, 4 a, 2 r; 272 nodes in all: 3 t, 5 w,
80 p, 164 c, 14 a, 4 r, 2 x):** `t-nietzsche`; `w-nietzsche-jgb` (1886), `w-nietzsche-gd` (1889),
cited by aphorism and, for GD, chapter and section (Fabel by stage 1–6), KSA pages not
given; 27 passages: JGB 15 (two spans), 16 (two), 17, **19 whole in four spans since run 19 (the opening to »Affekt des Commando's«; the seventh and eighth sentences, »Das, was "Freiheit des Willens" genannt wird« to »dass es gehorcht«; »Nun aber beachte man« to »mit sich bringt«; the close, »"Freiheit des Willens" - das ist das Wort« to »entsteht«, the transcription's closing dash not reproduced; fourteen sentences by full stop, question and exclamation mark, a colon joining halves; the transcription's one kind of quotation mark for both levels in »"ich bin frei, "er" muss gehorchen"« kept and named)**, 21 whole in four spans since run 14 (the first sentence;
»Das Verlangen« to »hinausläuft«; »Man soll nicht« to »mythologisch«; »Der "unfreie Wille"« to the end, from the same Gutenberg text), 34 in four spans since run 15 (the opening, »Auf welchen Standpunkt« to »Fragen mehr sind«, three sentences; »Der Glaube an« to »wenig Ehre macht«; »Es ist nicht mehr« to »die Sprache der Maler«; the close, »Warum dürfte« to the end, six questions; the span between the second and the third, »Mag im bürgerlichen Leben« to »Warum nicht?«, in no passage), 36 (two), 54; GD Vernunft 2, 5, 6; Fabel;
Irrthümer 3 (to »Das folgt daraus!«); **Irrthümer 7 and 8 whole since run 18**, nine sentences counting the title line and eleven counting the opening question, the transcription's »überall« in lower case and »Willens-Psychiologie« kept and named, »ein Stück Verhängniss« rendered "fate" against Vernunft 5's "calamity" with the reason on the passage. 61 claims, all `draft`: JGB 16 (Schopenhauer's »ich
will« a superstition; immediate certainty a contradictio in adjecto; »ich denke«
presupposes comparison), 17 and 54 (the subject a grammatical habit; the I a synthesis), 19
(Schopenhauer took over a popular prejudice; willing complicated; the belief that will and
action are one from erroneous inferences; »scheint mir« kept; **run 19, four more, sentences 7, 8, 11 and 14:** what is called »"Freiheit des Willens"« is »wesentlich der Überlegenheits-Affekt in Hinsicht auf Den, der gehorchen muss«; »Ein Mensch, der will -, befiehlt einem Etwas in sich, das gehorcht«; »"Freiheit des Willens"« the word for the »Lust-Zustand des Wollenden, der befiehlt und sich zugleich mit dem Ausführenden als Eins setzt«; »Bei allem Wollen handelt es sich schlechterdings um Befehlen und Gehorchen« on a »Gesellschaftsbau vieler "Seelen"«, its »weshalb« clause carried in the statement and setting the claim also in the row on what is drawn; sentences 12 and 13 in no claim; no link on any (no Kant or Schopenhauer statement speaks of commanding, obeying or an affect; § 18's identity is attacked by sentences 9–10, not 11; JGB 21 and 17 / 54 no link); »Wollen an sich schon« "willing as such already"; »Noth« "needful"), 36 (the mechanistic world not
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
things is mythology; **run 14, the rest of JGB 21:** the desire for »"Freiheit des Willens"« »in jenem metaphysischen Superlativ-Verstande« is »eben jene causa sui zu sein«, no link; whoever strikes the »Unbegriff« »"freier Wille"« is asked (»Gesetzt ... so bitte ich«) to strike the »"unfreien Willen"«; »Der "unfreie Wille" ist Mythologie: im wirklichen Leben handelt es sich nur um starken und schwachen Willen«, no `depends_on`; feeling »Unfreiheit« in all »"Causal-Verknüpfung"« »fast immer« a symptom; the last three sentences in no claim; no attack on B xxviii or »so fern nicht frei«, said on the nodes; the four set first in the will page's row on freedom), 34 (belief in immediate certainties a naïveté; truth worth more than
semblance a moral prejudice; doing away with the apparent world leaves nothing of truth,
»gesetzt, ihr könntet das«; **run 15, the opening and the close:** »die Irrthümlichkeit der Welt, in der wir zu leben glauben« is »das Sicherste und Festeste«, a temptation to conjecture a deceptive principle reported, row 5 of the first page; whoever blames »"den Geist"« for the world's falseness »hätte mindestens guten Anlass« to distrust all thinking, names no one, no attack, row 7; the innocence of thinkers permits asking consciousness for honest answers, row 3; the close's first three questions kept as questions, row 5 (the reviewer moved them from row 7); the last three questions and the span between »wenig Ehre macht« and »Es ist nicht mehr« in no claim, no link to JGB 17 / 54); **run 18, GD Irrthümer 7–8, five claims, four in the will page's row on freedom after JGB 21's six:** »"freier Wille"« »das anrüchigste Theologen-Kunststück«, for making humanity »"verantwortlich"«; the doctrine of the will »erfunden zum Zweck der Strafe«; men thought »"frei"« to be judged and punished, »folglich« inside one sentence, no argument; nobody gives man his »Eigenschaften«, »noch er selbst«, the nonsense taught »als "intelligible Freiheit" von Kant« by Nietzsche's attribution, no attack (no Kant statement says the subject gives itself its qualities; since run 20 the same holds against § 55's »Willensakt«, the identification the map's); »dies erst ist die grosse Befreiung« on no row; GD's »"frei"« is responsibility before a judge; the fifteen other sentences in no claim, in the will page's gaps list). 4 arguments, all `checked`:
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
Terms: Gewissheit "certainty", Erkenntniss "cognition",  wirken "work", Thatsache "fact",
Verhängniss "calamity", Vermögen "faculty".  Not in the map: JGB
20 (adds no cell), JGB 34's span from »Mag im bürgerlichen Leben« to »Warum nicht?«, JGB 230; GD Irrthümer 1–2, 4–6; Nachlass
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
`draft`, Ask 9): five rows (what the will is, the Nietzsche cell since run 19 also JGB 19's eighth and fourteenth sentences after the two older JGB 19 claims, set for what a man who wills does and what all willing is a matter of; immediately known, Kant's cell since run 13
with »niemals unmittelbar gekannt« for the word »unmittelbar«; cause of the body's
actions, Kant's cell filled in run 13 from A 538–541 for »Ursache«/»Handlungen«/»Wirkungen«;
free, and free of what, the Schopenhauer cell set for the word »frei« and since run 20 also the seven § 55 claims after the three older, the row's question answered in the fourth Book's words, with a paragraph under *On freedom* on what is and is not parallel to A 538–541 and B xxvii and a passage under *Kant and Schopenhauer on the law and the thing in itself* on the two nearest unset premises, the Nietzsche cell since run 14 the four
JGB 21 claims first and then the two set for »die Freiheit« / »"psychologischer Unfreiheit"« and since run 18 the four GD Irrthümer 7–8 claims after them, and since run 19 JGB 19's seventh and eleventh sentences between JGB 21's six and GD's four, set for the term »Freiheit des Willens« (what is so called; what the word is the word for), with a "what is parallel to Kant: nothing the map sets; what is not" passage under *On freedom*; what is drawn, the Nietzsche cell since run 19 also JGB 19's fourteenth sentence for its »weshalb« clause, Kant's since run 13 also the three antinomy sentences and since run 17 the footnote's »widerspreche« sentence, Schopenhauer's also § 24;
what is drawn from it, Kant's cell since run 17 also the footnote's »praktischen« sentence, GD 7–8 set there on no cell with the reason in the paragraph), two `shared` entries since run 13, both the premise on time, *a
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
range of the section and the AA line (the section A 538 / B 566 begins at 3:366.05; A 236 / B 295 at 3:203.04; B 307 at 3:209.32). *Schopenhauer:*
zeno.org `http://www.zeno.org/Philosophie/M/Schopenhauer,+Arthur/Die+Welt+als+Wille+und+Vorstellung/Erster+Band/<Erstes+Buch|Zweites+Buch|Anhang.+Kritik+der+Kantischen+Philosophie>`,
ISO-8859-1, text in `<div class="zenoCOMain">`, `<h5>` the § numbers, `[N]` in
`class="zenoTXKonk"` marks where ZA page N begins; down on 10-09 and 10-13, up on 10-14, 10-22 and 10-26 (`Viertes+Buch`: the ZA markers are plain `[N]` in the text, not in a span; footnote marks are `<a ...>N</a>`, their texts in `zenoTXFnText` at the page's foot); OCR
slips (»Kam«, »hohem« for »höhern«): collate every span word by word against Grisebach's
text, keep the transcription's letters, name every non-orthographic variant on the passage.
Fallback Projekt Gutenberg-DE
`https://projekt-gutenberg.org/authors/arthur-schopenhauer/books/die-welt-als-wille-und-vorstellung-band-i/chapter/N/`
(**the trailing slash is required since 10-22: without it the redirect's body is empty; `curl -L -A "Mozilla/5.0"`; the site folds the edition's footnotes into the sentence without brackets and marks letterspacing with `<span class="spaced">`, so collate every span against zeno before storing**; Grisebach, Reclam 1892; chapter = § + 2, chapter 74 the Anhang, 2 the prefaces; `<p>`
elements, every paragraph repeated once, not byte-identical, strip by searching; two
advertising paragraphs at the end; `<a name="pageN">` anchors give Grisebach's pages; say
»ZA page not given; Grisebach's pagination ... p. N« in `ref` and keep its orthography).
 *Nietzsche:*
Project Gutenberg eBooks 7204 (JGB) and 7203 (GD),
`https://www.gutenberg.org/cache/epub/<n>/pg<n>.txt`, after Projekt Gutenberg-DE,
first-edition orthography, edition unstated (said on the nodes); aphorisms as a line `N.`
alone, chapters as `Erstes Hauptstück:` lines, GD chapters by title;   Every `original` is extracted by start/end substring and asserted verbatim.

**The adversarial pass is not optional, and it finds what the truth table cannot.** Brief
for the reviewer: the new and revised nodes, the diffs, the corpus files, the older
passages they cite, the conventions, and the order validity, fidelity, attack links,
translation, references, readings, links, format, rendered page; for a comparison also
rows' fit, shared premises asserted by both, divergences, readings not picked, quotations.
The Agent tool runs the reviewer in the background, six to sixteen minutes and 120,000–260,000 of its own tokens (runs 13–19: 13–21 findings each, nearly all accepted); draft memory and the changelog meanwhile; the stop hook asks for a commit while it runs, which must be refused until
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
the model states and nothing enforces will be broken, so write the check. *Run 18 added:* before writing that a transcription prints a form "elsewhere too", grep for the form at the head of a sentence and mid-sentence separately (GD's lower-case »überall« was sentence-initial once, a slip on the footing of »Psychiologie«); a sentence's ordinal must be counted the same way on the passage, the claim and the page ("the first sentence of 8" against the passage's count from the opening question); a gloss that defends a rendering must describe the English word, not an ideal one ("artifice" says contrivance); »auch«, »hier«, »wieder« are qualifiers like the rest, and »Art des Seins« is "manner of being"; a "sense of X in these sentences" claim is a generalization and must hold of each sentence; a reason for a cell must come from inside the sentence, never from the section's title; a shared verb (»gedacht« in two texts) is no "what is parallel"; new titles keep the German term in guillemets as the older titles on the same term do; sentences that count or list a row's cells ("Nietzsche's cells in this row are JGB 21's"), a thinker node's "one slip is noted at", and a work node's "(sections 1–8)" are falsified by accretion, so grep them before every review. *Run 19 added:* `build.py` checks every relative Markdown link in a body (`check_body_links`), after a helper wrote `../../M/RALITYID/` into a body and the check then found one old dead link (GD Irrthümer 3's passage to a non-existent `a-nietzsche-no-spiritual-causes`, fixed); an edit script must be idempotent (skip a pair whose new text is present) and match whitespace-flexibly, since bodies wrap and YAML escapes quotes; "the attacks from JGB 19 are the tenth sentence's" is a counting sentence, and a claim spanning sentences 9–10 is "the ninth and tenth"; keep the text's colon and dash when dropping them moves »ebenso«; a »weshalb« clause inside one sentence that names another row's question sets the claim in that row too, "for the clause"; state each chronological relation separately; »dienstbar« "subservient", »der Ausführende« "the one who carries it out" (never "executor" beside "will"), »sich das Recht nehmen« "claim the right", »unter den Gesichtskreis fassen« "bring within the purview", »mit geniessen« "share in", »Gesellschaftsbau« "social edifice", »in Hinsicht auf Den« "with regard to him"; an adverb in mid-position can turn restrictive, so head the sentence with it; a gaps list for a text newly held whole names the older spans' unclaimed sentences too. *Run 20 added:* the accretion sweep must cover the other thinkers' claim bodies, not only the page: grep `map/c-*.md` for "no", "passage", "in the map" naming the thinker whose text is added, and for the new terms (»intelligiblen Charakter« sat in JGB 36's statement); Projekt Gutenberg-DE folds footnotes into the sentence, so collate every span against zeno.org; a referent resolved from sentences not held (»obigen ... Fall«) is "as the map reads"; keep a cited author's own ordinals (»ersteren« / »zweiten«); an edition identification (fifth-edition pages as B) is the map's; emphasis carried by both transcriptions is no variant; a dropped half-sentence is in the passage; grep an older passage before quoting it; a doctrine placed in works not held names the works as absent only.

**Money.** 10.88 EUR incl. BTW spent in Q4 2026 of 200 EUR (`LEDGER.md`); nothing spent in any run; the card used for the domain is still unreported.

**Tooling facts, owner's machine (Windows, Git Bash).** `python` not `python3`; `PYTHONIOENCODING=utf-8`; scripts go to the scratchpad and run by path. Commits as `TheAndries`; owner-session messages begin »owner session —«.

**Tooling facts, cloud container.** Python 3.11 with PyYAML; Node 22 with `playwright` and Chromium at `/opt/pw-browsers/chromium`. Fetches through the proxy work (korpora.org, gutenberg.org answered at once on 10-23 to 10-25); `gh` exists but is not used by the routine. Git author `Claude <noreply@anthropic.com>`; commits carry the session trailer. A full build needs `python3 -m pip install fonttools brotli`; `--check` runs no font-coverage check, so build to a scratch `--out` before the review. Write edit scripts to the scratchpad and run them with `python3 -I`; recover a mangled line from `git show HEAD:map/<file>`. The container checks out `main` tracking `origin/main`: `git fetch origin main`, rebase if the inbox workflow has pushed, `git push origin main`. A stop hook asks for a commit whenever the turn ends with uncommitted changes; refuse before the review is in.

**Next.** If `INBOX.md` has an entry: handle it first, inside the protocol's deadlines
(above). If the owner answered Ask 9: apply as under Ask 7 (`checked` with `status_note`;
versions for changed statements with credit).
Otherwise: a fourth thinker is not yet due (Phase 2 should see one filing or the owner's
word first); useful content runs meanwhile are the gaps both pages list (no Nietzsche gap is left on the will page; the Anhang's
theorems on time; § 2's unclaimed sentences only if a row asks after the subject, which none does;
the antinomy's resolution outside A 538–541, now also what § 55's footnote cites, A 532–558; A 236–260 / B 295–315 beyond the opening; § 55's remainder only if a row asks after the will's self-denial or the feeling of freedom, which none does),
each only where it adds a cell or a row, with quotes on every new cell claim.

**Dropped from memory this run:** the run-19 JGB 19 passage in the Nietzsche paragraph compressed from about 330 to about 130 words and the run-18 GD passage from about 260 to about 120 (the sentence-level detail stands in the changelog entries of 10-24 and 10-25 and on the nodes); run 20 added § 55's three passages, seven claims, the collation variants, the Gutenberg footnote-folding rule and the review's rules; the Phase 0, Checkpoint 1, owner's-machine and money paragraphs cut to a line each.
