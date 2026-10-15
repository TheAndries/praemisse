# memory.md

Carried state for the operator. Capped at 8,000 words. Rewritten each run.

## State as of 2026-10-15 (run 11, end)

**Identity and governance.** Name `praemisse`; domain praemisse.com at TransIP; site live at
https://praemisse.com/ (GitHub Pages, HTTPS enforced, certificate to 2027-01-03, GitHub
renews). Repository https://github.com/TheAndries/praemisse, public, `main`. Routine
`trig_01CybW54QF5Q5hCdyVQzM8qX`, `34 5 * * *` UTC, model `claude-fable-5-1`; runs 1–11 were
served on that model, no handover note needed. The GitHub and Claude Code Remote tools in
the tool list are platform-attached to every cloud session and are not a config change
(`ROUTINE.md`, Ask 6): do not raise it again. Open disputes: none. Attestations: none. Open
motions: none. INBOX empty at runs 1–11; the owner made no commit between runs 8 and 11, so Ask 8 is unanswered and nothing on the design side changed. Open asks: 4 (mailbox; deferred by owner; blocks
Phase 2), **8 (the design brief the mockups refer to; blocks nothing)** and **9 (the owner's qualified review of the second comparison, https://praemisse.com/x/the-will/, opened 2026-10-15; blocks nothing)**. Asks 1, 2, 3, 5,
6, 7 done. **The mockups:** on 2026-10-11 the owner uploaded through the GitHub web UI
(commit `1823719`, »Add files via upload«, no INBOX note) `praemisse-mockup-a.html`
(»direction A, the edition«, a home page) and `praemisse-mockup-b.html` (»direction B, the
apparatus«, a comparison page) at the repository root, each calling itself a reference
mockup »for the praemisse design brief, 2026-10-11«, set in stand-in Google fonts, and saying
the brief wins where they differ and `DESIGN.md` over both. No brief exists in the
repository. Run 8 treated the upload as an owner note (`BOARD.md`: a note is not an
instruction), left the files where they are (the build reads only `map/` and `site/`, so
they are not published), changed nothing on the site, and opened Ask 8 asking what the
brief is and whether it wants pages inside `DESIGN.md` (operator's, on a note) or a change
to `DESIGN.md` (a motion). Four things in them not to carry over as they stand: »behind«
in the copy (picks the two-object reading, struck from the comparison on 2026-10-10);
`checked` on a claim (claims are `draft` until attested); a legend omitting the comparison
sense of `checked`; Google Fonts (`DESIGN.md` 8). Their counts (48 passages, 88 claims, 10
arguments, 4 readings) were the map's at run 7. When the owner answers, read the brief
before building anything, and treat any page layout the brief asks for as the operator's
to build on a note unless it touches a `DESIGN.md` principle. **Ask 7 (Checkpoint 1) was answered 2026-10-10 in an
owner session:** the owner read the comparison against the project's translations, found
nothing that reads as fabrication, gave eight decisions (owner decision in `BOARD.md`;
his note verbatim in the changelog entry of that session) and they were applied the same
day. He did not say in the ask's words whether the page is better than what he could find
elsewhere; no rethink was ordered; proceed. `PLAN.md` rewritten 2026-10-10 (owner session):
Checkpoint 1 answered; next the gaps the comparison page lists, then the second comparison
on the will, built to the same convention and offered for the same qualified review;
quotations set on every claim a comparison cell cites as pages are touched; a fourth
thinker after those; Phase 2 still needs a route into INBOX.md settled in MODEL.md before
the forms are built.

**Phase 0 complete (2026-10-05).** `site/build.py` (reads `map/*.md`, validates against
`MODEL.md`, renders to `site/_build/`, gitignored; `--check` for CI; `--map DIR` for a
scratch copy; `--domain praemisse.com` in the workflow; PyYAML the only dependency; own
small Markdown subset with `[text](../../c/slug/)` links between node pages, which live at
`/<prefix>/<slug>/`), `site/static/style.css` and `type.css` (Libertine, owner decision),
`.github/workflows/site.yml` (check, build, deploy on push to `main`), `notify-asks.yml` +
`tools/open_asks_issue.py` (one GitHub issue *praemisse - open asks*; keep the `| # | Date
| Ask | Blocks | Status |` table; `done ...` closes, *deferred*/*queued* lists as no action).

**Phase 1 in progress.** Model settled in `MODEL.md`, *How the model is applied*:
`versions:` in the same file (date, reason, superseded statement, credit); `statement:` one
sentence on every claim, argument and comparison; `form:` in propositional logic checked by
`tools/validity.py` (truth table, ≤16 atoms, `not/and/or/->/<->`), `checked` only on an
argument whose form passes, claims `draft` until attested; premises may be `{claim: id}` or
`{assumption: text}`, and an assumption is where the map's own bridge goes, named as such;
`depends_on` on a claim names its argument, or a claim it is drawn from by an "also"/
"denn"/"mithin"/"folglich" step not yet formalized (the body quotes the connective); `r-`
nodes carry `reading_of`, `statement`, `passages`, `literature` (author, title, year,
chapter), no status, and a body with *the texts it rests on*, *what it holds*, *what
depends on it*, *what tells against it*; the map never picks a reading (P9); `d-`/`v-`
nodes name a `target` and render in full on it; `verified_by`/`disputes` must equal the
set targeting the node; `attested` one `v-`, `established` two; `contested` iff a `d-` has
outcome contested. **Attacks (settled 2026-10-09, MODEL.md last paragraph):** `attacked_by`
on the target and `replies_to` on the attacker are converses and the build checks they
agree (negative test passed on a scratch copy), and since run 5 it also checks that
`supports` and `depends_on` are converses on every node (three old nodes were fixed); an attack is set only when the attacker's
statement denies what the target *states*, not its topic; the attacker's body quotes the
sentence naming the target or says none does; a link-only change on an old node does not
add a `versions:` entry, the changelog records it. All enforced by `--check`.

**Kant nodes on `main` (53 after run 3; 55 after the owner session of 2026-10-10; 67 after run 7):** `t-kant`; `w-kant-krv`, `w-kant-prolegomena`;
17 passages: `p-krv-b-xxvi` (3:16.30–17.07), `p-krv-b-xxviii-xxix` (3:18.21–30),
`p-krv-b-xxix-xxx` (3:18.33–19.09), `p-krv-a24-b38`, `p-krv-a26-b42`, `p-krv-a42-b59`,
`p-krv-a43-b60`, `p-krv-a235-b294` (3:202.12–22), `p-krv-a236-b295` (3:203.04–09),
`p-krv-b307`, `p-krv-b308-309`, `p-prol-289`, `p-prol-314`, `p-prol-350` (4:350.21–33),
`p-prol-350-351` (4:350.34–351.12), `p-prol-352` (4:352.21–33), `p-prol-353` (4:353.16–22);
27 claims (space, appearance, the limits of knowledge, the noumenon; B xxix–xxx: the
pretension, its principles, the practical assumption, knowledge annulled for faith,
dogmatism defined; the island and the understanding's principles; Prolegomena §57: the two
absurdities, principles taken for conditions of things, restricting principles becoming
transcendent, the map's absurdity premise, the critique clause, bounds against limits, the
space for things in themselves, metaphysics leads to limits; the same action in another
relation); 4 arguments, all `checked`: `a-kant-space-not-of-things-in-themselves` (s→¬a ⊢
¬s), `a-kant-appearance-requires-thing-in-itself` (¬t→¬w, w ⊢ t),
`a-kant-practical-assumption-requires-removing-speculative-pretension` (k→e, e→x, a→¬x ⊢
a→¬k; a→¬x is the map's bridge), `a-kant-denying-things-in-themselves-absurd` (n→g, g→u,
¬u ⊢ ¬n; ¬u is the map's claim, said so on the node); 2 readings, `r-kant-two-aspect`
(Prauss 1974; Allison 2004, ch. 2) and `r-kant-two-object` (Strawson 1966, Part Four;
Guyer 1987, Part V; Van Cleve 1999, ch. 10), both `reading_of:
c-kant-things-in-themselves-thinkable-not-knowable`. Translations are the project's own,
marked. *Grenzen* = "limits", *Schranken* = "bounds" (Kant's definition, 4:352.21–25);
"aufheben" = "annul"; "ihr Ziel setzen" = "put a stop to". **Run 7 (2026-10-11) added B xxvii–xxix, 3:17.07–18.21, in four passages**
(`p-krv-b-xxvii-distinction-not-made` 17.07–18, `p-krv-b-xxvii-xxviii-same-will-free`
17.18–28, `p-krv-b-xxviii-freedom-thinkable` 17.28–18.11, `p-krv-b-xxviii-morality-would-yield`
18.11–21; the Korpus's »nothwendiggemachte« kept and noted), seven claims (without the
distinction causality would hold of all things; without it a free will under natural
necessity is a contradiction, drawn by »also«; if the deduction is right causality applies
only to things as objects of experience, the »mithin«; the same will not free as appearance
and free »als einem Dinge an sich selbst angehörig«, conditional as the sentence is;
freedom cannot be cognized by speculative reason; freedom thinkable if the critical
distinction holds, »wenigstens« kept; had freedom been proved unthinkable morality would
yield, both limbs under »supposing«) and one argument, `checked`,
`a-kant-freedom-thinkable-under-the-critical-distinction` ((k∧r)→f, f→t ⊢ (k∧r)→t; f→t is
the map's bridge from the will of B xxvii–xxviii to the freedom of B xxviii, and the two
»Widerspruch« differ, between two predicates of one will vs inside the representation of
freedom; the conclusion claim's antecedent, »kritische Unterscheidung beider
Vorstellungsarten und die davon herrührende Einschränkung«, is read as k∧r, the two
meanings of the object identified with the two kinds of representation, said on the node;
the deduction sentence, e→r by »mithin«, is not a premise, since the conclusion's antecedent
has r and not e; the review caught a first form d→t with d including the deduction, which
proved a weaker conditional than the claim). The two readings each cite the
B xxvii–xxviii passage (»in zweierlei Bedeutung«; »als einem Dinge an sich selbst
angehörig« claimable by both). Kant says the will *belongs to* a thing in itself, never
that it is one: the hinge of the comparison with Schopenhauer's § 21. Still not in the
map: A 236–260 / B 295–315 beyond the opening, Prolegomena §§58–59, Kant's footnote at B
xxvi–xxvii (3:17.05 mark), the Grundlegung and the second Critique (so no sentence may say
Kant asserts that morality presupposes freedom; B xxviii only supposes it).

**Schopenhauer nodes on `main` (38 after run 4; 50 after run 9; 65 after run 10):** `t-schopenhauer`; `w-schopenhauer-wwv1`
(Zürcher Ausgabe 1977 text after Hübscher's 1859 text, vol. 1 = Books 1–2, vol. 2 = Books
3–4 and the Anhang, continuous pagination); 13 passages `p-wwv1-*`: § 1 (the first
paragraph, ZA I 28 inferred; the »Objekt an sich« sentence, 30), § 18 (the body given in
two ways, 142; the identity shown not proved, 144–145), § 19 (causality never leads beyond
representation, 146–147; the analogy of the body, 147–148), § 21 (the will alone is the
thing in itself, 153–154), § 22 (denominatio a potiori, 154; the will not inferred, 155),
§ 23 (free of the forms, 156; groundless and one, 157), Anhang (Kant's derivation of the
thing in itself, ZA II 534–535; only the derivation is faulty, 535); 21 claims
`c-schopenhauer-*`, all `draft`; 2 arguments, both `checked`:
`a-schopenhauer-corporeal-world-in-itself-is-will` (m→a, a→(v∨w), m→¬v ⊢ m→w; premises 1
and 3 are the map's, the conclusion is epistemic) and
`a-schopenhauer-kant-derivation-cannot-reach-thing-in-itself` (k, b, (k∧b)→¬e ⊢ ¬e; b is
the § 19 principle; the bridge is the definition of a thing in itself at ZA II 535). No
attack link on any Kant node: Schopenhauer accepts »die Anerkennung eines Dinges an sich
zur gegebenen Erscheinung« (ZA II 535). Two Schopenhauer claims now carry `attacked_by`
from Nietzsche (below). Terms: Vorstellung "representation", Erscheinung "appearance",
Objektität "objectity", Satz vom Grunde "principle of sufficient reason", nachweisen
"show" against beweisen "prove", Voraussetzung "presupposition", Annahme "assumption",
Besonnenheit "discernment". The identity of will and body is a claim, not an argument,
because § 18 says it can never be proved. **Run 9 (2026-10-13) added §§ 24–25 from Projekt Gutenberg-DE (below), four passages
with Grisebach's page (pp. 174–178, 184) and no ZA page:** `p-wwv1-s24-forms-learned-from-kant-and-the-question` (§ 24 first
paragraph, »Wir haben von dem großen Kant gelernt« to »bei Seite setze«),
`p-wwv1-s24-kant-rightly-concluded` (second paragraph to »kund giebt«),
`p-wwv1-s24-etiology-never-fathoms-the-thing-in-itself` (»Wenn daher auch alle Mathematik«
to »nicht im Mindesten erklärt«; the transcription's »in Hinsicht aus« kept and noted),
`p-wwv1-s25-will-outside-time-and-space-knows-no-plurality` (§ 25 to »untheilbar«); seven
claims, each with its quote: the forms in consciousness independent of the objects,
»von dem großen Kant gelernt«, »mit gleichem Recht« two namings, `shares_premise_with`
`c-kant-space-a-priori` (»nicht als eine von ihnen abhängende Bestimmung«), a third `shared`
entry *space is not dependent on the objects that appear in it*; the conditional »Sollten nun aber ... nicht leere Phantome seyn ... so müßten
sie ... ein Ding an sich« with the »wenigstens fragen« kept, neither limb asserted, set
beside Kant's B xxvi conditional on the page, no link; »Was auch immer das Ding an sich sei,
so hat Kant richtig geschlossen« that time, space and causality are »nicht Bestimmungen
desselben«, Kant's own word at A 26 / B 42, so `shares_premise_with`
`c-kant-space-not-of-things-in-themselves` and a second `shared` entry with the same
premise sentence (the build allows two entries with one premise; a `shared` entry cannot
hold two claims of one thinker); »Umgekehrt« what is unconditioned by the forms is where
the thing in itself »sich unmittelbar ... kund giebt«, kept as a where, not a cognition, no
link to § 22; mathematics and etiology »nimmermehr in das innere Wesen der Dinge«, about
explanation, kept apart from § 19's law of causality; § 25's plurality conditioned by time
and space, the principium individuationis, »nicht Eigenschaft des Dinges an sich«, no
third link, said so; and the conditional conclusion »Ist nun dieses Ding an sich ... der
Wille; so liegt er ... außer der Zeit und dem Raum, und kennt demnach keine Vielheit«. One
argument, `checked`, `a-schopenhauer-will-knows-no-plurality` (p∧f1∧f2, (f1∧f2∧w)→o, (p∧o)→¬m
⊢ w→(o∧¬m); f2 is »frei von aller Form der Erkenntniß«, the text's middle term; w is not a premise, the text draws the step conditionally and the claim keeps
it; both bridges the map's, named in the statement; »folglich einer« not formalized, § 23
has it). Comparison cells added: row 1 (the conditional), row 2 (etiology), row 3
(»unmittelbar« where), row 4 (the argument), row 7 (the forms in consciousness). Still not
in the map: § 2, § 20, § 24 beyond its first two paragraphs (the attack on materialism,
the method of philosophy against etiology, Spinoza's stone), § 25 beyond its first
paragraph (grades of objectivation), §§ 26–29, the Anhang on the Transcendental
Aesthetic (»Kants größtes Verdienst ist die Unterscheidung der Erscheinung vom Dinge an
sich« is at ch74.txt paragraph 15 of the PG-DE extract; the Aesthetic praised as
»unumstößliche Wahrheiten« further on) and on the categories. **Run 10 (2026-10-14) added three Anhang passages from zeno.org (back up), with ZA pages:**
`p-wwv1-anhang-kants-greatest-merit` (ZA II 513–514, the opening paragraph's first six
sentences to »von uns a priori erkannt werden«; zeno's »hohem« for Grisebach's »höhern«
kept and noted; »des Kantischen« vs Grisebach »der Kantischen« noted),
`p-wwv1-anhang-laws-of-experience-not-applicable-to-existence-itself` (ZA II 516, the same
paragraph's four sentences »Er zeigte, daß die Gesetze« to »Eichhörnchen im Rade«; zeno's
»Kam zeigte« slip for »Kant zeigte« kept and noted; the sentences between the two spans, on
Plato, the Vedas, Maja and the dogmatists, not held),
`p-wwv1-anhang-transcendental-aesthetic-a-priori-cognitions-forms-of-the-intellect` (ZA II
536–537, the whole paragraph »Die transscendentale Aesthetik ist ein so überaus
verdienstvolles Werk« to »gewissermaaßen Synonyma«; zeno »Formen seines Erkennens« vs
Grisebach »seiner Erkenntniß« noted). Eleven claims, each with its quote: Kant's greatest
merit is the distinction, on the ground that the intellect stands between things and us
(C1, row 4 cell; no link to A 42/B 59, argued: praise of a doctrine for its ground); the
Kantian distinction makes Locke's primary qualities appearance »weil Bedingungen desselben,
Raum, Zeit und Kausalität, von uns a priori erkannt werden« (C2, `shares_premise_with`
`c-kant-space-a-priori`, a second `shared` entry *Space is given a priori*); Kant showed the
laws ruling in experience not applicable to derive existence itself, validity only relative
(C3, `shares_premise_with` `c-kant-understanding-principles-only-for-experience`, A 236/B
295, new `shared` entry *The laws that govern experience have no use beyond it*, the
identification of Kant's Grundsätze with Schopenhauer's Gesetze conceded on the page as what
Schopenhauer's last sentence says of Kant); Kant showed those laws and the world conditioned
by the subject's Erkenntnißweise, »woraus folgte« no step toward the essence of the world in
itself (C4, rows 2 and 7, no link); the Aesthetic's theorems among the »unumstößlichen
Wahrheiten«, first person kept (C5, no link: names no proposition); a part of our cognitions
a priori, a fact Kant proved (C6a); that fact admits no other explanation than that these
are the forms of our intellect (C6, the thesis, not in the argument); a priori means not
gained from experience, not from outside (C7); what is in the intellect without coming from
outside is its own essence (C8); if what is thus in it is the universal manner all its
objects must present themselves, it is the forms of its cognizing (C9, conditional kept);
»Erkenntnisse a priori« and »selbsteigene Formen des Intellekts« two expressions for one
thing, »im Grunde nur«, »gewissermaaßen« kept (C10, row 7). One argument, `checked`,
`a-schopenhauer-cognitions-a-priori-are-the-intellects-own-forms` (a, a→¬e, ¬e→b, m,
(b∧m)→f, f→s ⊢ s; m is the map's bridge discharging C9's antecedent, which the text's
»Demnach« does tacitly and the Aesthetic's theorems state of space and time; f→s the bridge
for »Demnach«; the form proves the synonymy, not C6's uniqueness). Still not in the map:
the Anhang beyond those four spans (nothing of 517–533 or 537–650 but the Fichte paragraph
is skipped, the Aesthetic's theorems on time, the categories, the Analytic), § 2, the rest
of §§ 24–25, §§ 26–29.

**Nietzsche nodes on `main` (53 after run 5; 72 after run 8; 145 nodes in all after run 6, 147 after the owner session, 159 after run 7, 178 after run 8, 190 after run 9, 205 after run 10: 3 t, 5 w, 61 p, 118 c, 13 a, 4 r, 1 x):**
`t-nietzsche`; `w-nietzsche-jgb` (1886), `w-nietzsche-gd` (1889); cited by aphorism number
and, for GD, chapter and section (the Fabel chapter by stage 1–6); KSA pages not given
(unverified). 19 passages: `p-jgb-16-immediate-certainties`,
`p-jgb-16-ich-denke-presupposes-comparison`, `p-jgb-17-es-denkt`,
`p-jgb-19-willing-complicated`, `p-jgb-19-will-and-action-one`,
`p-jgb-36-not-representation`, `p-jgb-36-will-to-power`, `p-jgb-54-grammatical-subject`,
`p-gd-vernunft-2-apparent-world`, `p-gd-vernunft-5-will-as-cause`,
`p-gd-vernunft-6-four-theses`, `p-gd-wahre-welt-fabel`, `p-gd-irrthuemer-3-will-as-cause`,
and from run 8 `p-jgb-15-sense-organs-not-appearances`, `p-jgb-15-external-world-not-work-of-organs`,
`p-jgb-21-causa-sui`, `p-jgb-21-cause-and-effect-fictions`, `p-jgb-34-immediate-certainties`,
`p-jgb-34-truth-and-semblance` (JGB 34 is Zweites Hauptstück).
45 claims `c-nietzsche-*`, all `draft`: JGB 16 (Schopenhauer's »ich will« a superstition;
immediate certainty a contradictio in adjecto; »ich denke« presupposes comparison; has no
immediate certainty), JGB 17 (subject as condition a falsification; »es denkt« already an
interpretation; subject inferred by grammatical habit), JGB 54 (the soul believed like the
grammatical subject; the I a synthesis made by thinking), JGB 19 (Schopenhauer took over a
popular prejudice; willing is complicated; feelings, thought and affect; the belief that
will and action are one, from habit), JGB 36 (mechanistic world not representation in
Schopenhauer's sense; will-causality posited as the only; the world would be will to
power, conditional), GD Vernunft (apparent world the only one; grounds for "apparent"
establish reality; dividing the world true/apparent, Kant's included, is décadence; the
will as cause the great error), GD Fabel (true world unattained; unknown cannot obligate;
not obligating; not consoling, redeeming or obligating, the full sentence, no argument;
idea refuted; abolishing the true abolishes the apparent; the stage-4 nodes all framed
"At the positivist stage of the history of the error", the map's reading, Clark 1990
ch. 3 cited for the stages as Nietzsche's own development), GD Irrthümer 3
(belief in causation from inner facts; will moves nothing; motive a surface phenomenon;
the I a fable; the evidence for spiritual causes gone; no spiritual causes, by »Das folgt
daraus«, unformalized); **run 8:** JGB 15 (sense organs not appearances in the idealist
sense, the sense unidentified; the two »dann« steps as two conditional claims; the external
world not the work of our organs, the statement keeping »gesetzt, dass der Begriff causa sui
etwas gründlich Absurdes ist« inside it and the text's closing »-?« noted on node and
passage), JGB 21 (causa sui the best self-contradiction; cause and effect only as conventional
fictions, a »soll«; in the »"An-sich"« nothing of causal connections, every quotation mark
Nietzsche's and kept; we alone invented causes ... and reading the sign-world »als "an sich"«
into things is mythology; the free/unfree will sentences left for the will comparison), JGB 34
(belief in immediate certainties a moral naïveté and a stupidity, naming no one; truth worth
more than semblance a moral prejudice; doing away with the apparent world leaves nothing of
truth, the converse of Fabel stage 6, »gesetzt, ihr könntet das« kept, »eurer« made
impersonal; the degrees-of-apparentness claim reported as the two questions it is, »It is
asked ...«). 4 arguments, all `checked`: `a-nietzsche-external-world-not-work-of-organs`
(w→b, b→o, s→¬o ⊢ s→¬w; s→¬o is the map's bridge reading organs that are their own work as a
causa sui, which the supposition excludes; the conclusion is the conditional the text's
»gesetzt« makes it, atom for atom the claim's; JGB 21's assertion is not taken as a premise so
the supposition stays);
`a-nietzsche-ich-denke-has-no-immediate-certainty` (c, c→b, b→¬g ⊢ ¬g; both conditionals
are the map's, the identification via »dieser« and the »wegen«; »er« is the state, not
»ich denke«), `a-nietzsche-true-world-does-not-obligate` (¬r, ¬r→¬k, ¬k→¬o ⊢
¬o; stage 4 of the Fabel; ¬r→¬k is the map's bridge for »als unerreicht auch unbekannt«;
the form reaches only »verpflichtend«), `a-nietzsche-evidence-for-spiritual-causes-gone` (¬w, ¬m, ¬i,
e→(w∨m∨i) ⊢ ¬e; epistemic, as the text's step is; the disjunction is the map's bridge
from »diesen drei inneren Thatsachen« and »die ganze angebliche Empirie dafür«; ¬m rests
on »Nebenher der That«, not the comparative). 2 readings on
`c-nietzsche-world-would-be-will-to-power`: `r-nietzsche-will-to-power-asserted`
(Richardson 1996, ch. 1 "Being") and `r-nietzsche-will-to-power-not-asserted` (Clark 1990,
ch. 7 "The will to power"; both chapter titles confirmed by search). No attack or shared-premise link was set in run 8; the absences are argued on the nodes and
the page (JGB 15's »Andere« unnamed and the idealist sense unidentified; JGB 34 judges the
belief, JGB 16 denies it; JGB 21's »"An-sich"« in scare quotes against Kant's B xxvii clause
under »wenn die Deduction ... richtig ist« and § 23's Satz vom Grunde, the nearest three-way
shared premise the map has, left open on the page for dispute). Attack links set, the
first in the map: `c-schopenhauer-will-not-inferred-but-immediately-known` ←
`c-nietzsche-schopenhauer-ich-will-a-superstition` (JGB 16) and
`c-nietzsche-schopenhauer-took-over-popular-prejudice` (JGB 19);
`c-schopenhauer-act-of-will-and-action-of-body-identical` ←
`c-nietzsche-belief-will-and-action-one-an-erroneous-inference` (JGB 19, the statement
opening with the »irrthümlichen Schlüssen« of the sentence before, Schopenhauer named at
the aphorism's opening, not in the sentence); `c-kant-things-in-themselves-thinkable-not-knowable`
← `c-nietzsche-immediate-certainty-contradictio-in-adjecto` (JGB 16, on the words »Ding
an sich« alone, no sentence naming Kant). Claim→claim `depends_on` with the connective quoted: true-world-not-obligating →
idea-refuted (»nicht einmal mehr verpflichtend ... folglich«); evidence-gone →
no-spiritual-causes (»Das folgt daraus«). Not set: idea-refuted → abolishing (narrative
sequence, »schaffen wir sie ab!« / »haben wir abgeschafft«, is not a step). Terms: Gewissheit "certainty", Erkenntniss "cognition", Vorstellung "representation", Schein and Anschein "semblance", scheinbar "apparent", Täuschung "deception", wirken "work", nachweisen "show", Thatsache "fact", Empirie "empirical evidence", Verhängniss "calamity", der Wollende "the one who wills". Gutenberg's »wie es in ein Satz ist« (JGB 36) is a transcription slip for »mein
Satz«; rendered "as is my proposition" and said so on the passage. Still not in the map:
JGB 20 (struck from the comparison's gaps list: the common philosophy of grammar adds no
cell on this question; JGB 17 and 54 carry grammar), JGB 21's free/unfree will sentences,
JGB 34's »Warum dürfte die Welt ... nicht eine Fiktion sein?« and its close on grammar, JGB
230; GD Irrthümer 7–8; Nachlass nothing, by design.

**Source of Nietzsche's text.** zeno.org reset every connection on 2026-10-09 (curl,
HTTP and HTTPS, and WebFetch 503); it may be back later for a cross-check of the KSA/
Schlechta text, but do not depend on it. Used instead: Project Gutenberg eBooks 7204 (JGB)
and 7203 (GD), `https://www.gutenberg.org/cache/epub/<n>/pg<n>.txt`, UTF-8, derived from
Projekt Gutenberg-DE, first-edition orthography, edition unstated (said so on `t-` and `w-`
nodes). Layout: aphorisms as a line `N.` alone, chapters as `Erstes Hauptstück:` lines;
GD chapters by title line, sections as `N.` lines. The corpus and `texts.json` (the
relevant aphorisms with line breaks joined by a space) are in the scratchpad; each
passage's `original` is extracted by start/end substring and asserted to be a verbatim
substring. deutschestextarchiv.de has no Nietzsche; de.wikisource has neither work;
nietzschesource.org is JavaScript-rendered and unusable through the proxy.

**Source of Schopenhauer's text.** zeno.org, `http://www.zeno.org/Philosophie/M/Schopenhauer,+Arthur/Die+Welt+als+Wille+und+Vorstellung/Erster+Band/<Erstes+Buch|Zweites+Buch|Anhang.+Kritik+der+Kantischen+Philosophie>`,
one Book per HTML file, served as ISO-8859-1; the text is in `<div class="zenoCOMain">`,
`<h5>` carries the § numbers, `[N]` in `class="zenoTXKonk"` anchors marks where ZA page N
begins, footnote numbers are glued to the preceding word. zeno.org was down on 2026-10-13 (HTTP timed out, HTTPS reset) and up again on 2026-10-14
(HTTP 200 in seconds; the Anhang page 374k bytes, extracted by `extract_zeno.py` to
`anhang.txt` with ⟦N⟧ page marks). Its transcription has OCR slips (»Kam« for »Kant«,
»hohem«/»tiefem«/»grobem« for »höhern«/»tiefern«/»gröbern«): cross-check every span word by
word against Grisebach's `ch74.txt` (`slipcheck.py`; the PG-DE page's duplicate half is not
byte-identical, so strip by searching, not by halving), keep the transcription's letters,
name the slip on the passage, translate the sense. **Fallback used in run 9: Projekt Gutenberg-DE**,
`https://projekt-gutenberg.org/authors/arthur-schopenhauer/books/die-welt-als-wille-und-vorstellung-band-i/chapter/N`
(the old `/schopenh/wwv/` paths 404), Grisebach's edition (Reclam, Leipzig 1892, »zweiter,
mehrfach berichtigter Abdruck«), chapters 3–73 are §§ 1–71 (chapter = § + 2), chapter 74
the Anhang (650k chars, all in one page), chapter 2 the prefaces; the text is in `<p>`
elements and the page repeats every paragraph once (strip the duplicate half) and ends
in two advertising paragraphs (»Zeitgenössische Bücher«, »Projekt Gutenberg lebt«); the
extracted files are in the scratchpad as `chN.txt`. No ZA pages, but Grisebach's: the HTML has `<a name="pageN">` anchors (§ 24 pp. 174–184, § 25
from 184); cite by § and paragraph, say »ZA page not given; Grisebach's pagination ... p. N« in `ref`, name the edition in `source`, and keep its orthography
(»seyn«, »Gränze«). Passages of one § from two editions may differ in a letter; each
passage names its transcription. The Internet Archive has the 1859 scans
(`bub_gb_xhfF5h_0EggC`, vol. 2) if a page number is ever needed.

**Source of Kant's text.** https://korpora.org/kant/aa{03,04}/{page:03d}.html, one AA page
per file, lines in `<tr>` rows: first non-empty `<td>` is the line number, the rest the
text; join hyphenated words across lines by hand. The `korpora.zim.uni-duisburg-essen.de`
host fails through the proxy; use `korpora.org`. The Korpus joins "nothwendiggemachte" at
3:17.07 and has an OCR slip at 3:65.25. A/B pages are from the standard concordance; the
AA line is the authoritative locator.

**The adversarial pass is not optional, and it finds what the truth table cannot.** Runs
2–4: every serious finding was on an argument: a bridge premise that was "premises imply
conclusion" while the textual principle sat unlisted; a disjunction silently resolved; an
epistemic conclusion made ontological; an attack link on a claim the attacker accepts.
Rules distilled: when a form's conclusion is not word for word the conclusion claim, the
missing step is a tacit premise; make it an `assumption` and say it is the map's. When the
text gives a verdict and then the consequences, the premise that the consequence is
unacceptable is the map's. Before linking an attack, check that the attacked node states
what the attacker denies. Quote the connective for every claim→claim `depends_on` or set
none. Keep every qualifier (»nur«, »jedenfalls«, »scheint mir«, »gesetzt«) in the
statement; keep reported views in reported form. Brief for the reviewer: the node list,
the corpus files, the older passages the new nodes cite, and the order validity,
fidelity, attack links, translation, references, readings, links, format. Run 5: 46 findings, 3
serious: a stage of a narrated »Geschichte eines Irrthums« attributed to the narrator
as his own argument (frame narrated positions as the stage's, cite the reading, invite
dispute); a single bridge »premise implies conclusion« swallowing the text's middle term
(»wegen dieser Rückbeziehung«: give the middle term its own atom); bodies picking a
reading the r- nodes say is open (write "on the reading ... ; the other reading ..."
every time a claim body relates to a contested claim). New rules: the pronoun's
antecedent decides the atom's subject; a comparative (»eher ... als«) denies nothing;
an attack rests on the attacker's statement, so the denying words must be inside it;
the refusal reason for an attack must be of the kind the convention names; a body may
quote only text inside a passage node (P1), so widen the span or refer without quoting;
"orthography of the first edition" is a claim about an edition, say "consistent with". Run 6 (the comparison, 34 findings, 31 accepted): the map
picked a reading in one word (»behind«) in the question, statement and shared premise;
a note misdescribed the map's own framing of a Nietzsche stage; eight quoted passages
were not listed. Rules: word a shared premise in the texts' own terms and say what it
comes to under each reading; a note that summarizes a statement must not outrun it; a
rule the model states and nothing enforces will be broken, so write the check (the
quotation check now exists for comparisons; consider extending it to all bodies, after
measuring how many old nodes fail). Reviewer brief for a comparison: rows' fit, shared
premises asserted by both, divergences supported, readings section not picking,
quotations, references, statement, convention vs build, rendered page, format. Run 7 (20
findings, 2 serious, all but one accepted): a form's antecedent must be the conclusion
claim's antecedent atom for atom, not a condition that implies it (a form proving a weaker
conditional is not a check of the claim); when a premise claim turns out idle in the form,
take it out of `premises:` and say in the body what it supplies; an argument's `statement`
must contain the map's bridge, since that is the sentence a dispute quotes; two
occurrences of one word (»Widerspruch«) in two sentences are not one atom until the body
says why; keep the indicative where Kant keeps it inside a counterfactual (»genommen
habe«); a claim statement must be readable alone, so restate the supposition it stands
under; "Kant does not say X" is a universal about the corpus, write "no passage in the map
says X"; a quote block should be the load-bearing sentence, not the whole passage, or the
page shows the passage twice; two passages may not share a title. The Agent tool launches the reviewer in the background even
when the foreground is asked for; its transcript file is written only at the end, so a
quiet-file watcher fires at once and is useless: wait a fixed 10–12 minutes in a
background sleep instead, then `SendMessage` for the report if it has not arrived (run 6:
it arrived by itself after 11 minutes); the stop hook asks for a commit
while it runs, which must be refused until the report is in. Run 9 (21 findings, 2 serious, 20 accepted): a
coverage sentence (»beyond its first two paragraphs«) false by omission when two spans of
one paragraph are stored with a gap between, so say exactly which spans are held; a
relative pronoun's gender decides its antecedent (»die aber« = »Erkenntniß«, not »Satz«)
and a truth table cannot see it; when a premise claim states a middle term (»frei von aller
Form der Erkenntniß«) the atom must carry it or the bridge swallows it; before arguing an
absent link, reread every Kant statement on the page for the same proposition (A 24 / B 38
»nicht als eine von ihnen abhängende Bestimmung« was missed); a cell placed in a row for one
word (»unmittelbar«) must say so in the note; a sentence that denies a Kant statement in one
sentence needs the attack absence argued; check a source for page anchors before writing
»no page marks«. Use the wait for building
and screenshotting the site to the scratchpad (`--out`), drafting memory and the
changelog.

**Two conventions added in the owner session of 2026-10-10 (`MODEL.md`, enforced by
`--check`, six negative tests passed).** *Checked comparisons:* a comparison may be
`checked` when a named human has reviewed its claims and readings against the project's
translations short of attesting; it must carry `status_note` (shown in the status line
after the word); the build refuses `checked` on a comparison without it and the note on
anything else; lists print »checked, with a qualification on the page« (`status_word`);
the index and about legends say both senses; claims and arguments get no such status. *Quotations:* a claim may carry
`quotes:` (list of `passage`, `original`, `translation`); each must be a verbatim
substring, whitespace aside, of that passage's `original`/`translation`, the translation
required where the passage has one, an empty original refused; a voice note on a
narrated text is a reading: name it and keep sentences about the thinker to passages; rendered under
the statement, two columns from 48rem (`render_quotes`, CSS block "Added 2026-10-10
(owner session)"). Set on 16 claims (B xxvi ×4, Prol § 32, Anhang ZA II 534 ×2, 535,
§ 21, § 22, JGB 16 ×2, Vernunft 6 Satz 4, Fabel 5 and 6, A 24/B 38, A 26/B 42 (a) and
(b)). When writing a new claim for a comparison cell, set its quote.

**The comparison node (run 6, 2026-10-10; revised in the owner session the same day).**
`x-thing-in-itself`, the Checkpoint 1 page, at /x/thing-in-itself/, now `checked` with
the owner's status note. Owner-session changes: row-1 note says the three places that
make GD's »wahre Welt« Kant's (Satz 4 names Kant; Fabel stage 3 »königsbergisch«; JGB 16
»Ding an sich«); `c-kant-noumenon-negative-only` moved from row 2 to row 4; row-5 note
and the nodes `c-nietzsche-true-world-idea-refuted`,
`c-nietzsche-abolishing-true-world-abolishes-apparent` and the stage-4 argument read
Fabel stages 5 and 6 as Nietzsche's own voice (parenthesis »Teufelslärm aller freien
Geister«; »INCIPIT ZARATHUSTRA«), stage 4 still the positivist stage's; the shared
premise on space split in two, *given a priori* (A 24/B 38 ↔ Anhang ZA II 534) and *a
subjective form, on the side of the subject* (new `p-krv-a26-b42-b`, AA 3:55.09–18,
conclusion (b), and new `c-kant-space-subjective-condition-of-sensibility` ↔ the same
Anhang sentence; premise worded »Space is a subjective form«, Kant's »Bedingung« not
put in Schopenhauer's mouth), four shared premises in all; the page's last paragraph
names the owner and lists what he ordered but has not read; a `shared` entry cannot hold two claims of
one thinker, since every pair must name each other. Convention settled in `MODEL.md`, *Comparisons* (last paragraph):
`question`, `thinkers` (column order), `statement`, `rows` (each `question`, `positions`
keyed by thinker id listing that thinker's `c-`/`a-` ids, a short `note` that must relate
to the readings where a cell's claim has any), `shared` (each `premise`, `claims` of
different thinkers, `passages` cited by those claims), `passages` = every span the body or
a note quotes; status `draft` until attested; an empty cell renders "No position in the
map" and the note says whether the text is absent or silent. `shares_premise_with`: both
statements assert the proposition, or one asserts and the other expressly keeps that
thinker's assertion (Schopenhauer's »nicht die Anerkennung«). The build
(`check_comparison`) checks thinkers resolve to `t-` with no duplicate and each placed
somewhere, every position belongs to its column's thinker, `shared` claims are `c-` of
different thinkers naming each other, shared passages are cited by the claims, every
`shares_premise_with` pair in the map is named by some comparison, every »...« quotation
in body or notes is inside a listed passage (pieces split at »...« must all lie in one
passage; a chapter title matches a passage's `ref`), and the body links every `r-` whose
`reading_of` is a cell claim (six negative tests passed on a scratch copy).
Rendering: `site/templates/comparison.html`, the table full-width above the two-column
text/passages grid, `render_comparison` in build.py, CSS block "Added 2026-10-10" (phone:
cells stack with `data-thinker` labels via `::before`, no JavaScript); the index page lists
the comparisons by title. Body headings are `#` (the
renderer adds a level); cell refs anchor to `#p-id` in the aside; readings listed in the
cell. Five rows: whether there is a thing in itself *to* a given appearance (never
»behind«, which picks the two-object reading); whether it can be reached by inference;
whether anything is cognized immediately (Kant cell: A 42/B 59, silent on immediacy);
what can be said of it; what the division is and what follows from refusing it. Shared
premises, the first `shares_premise_with` links, all Kant–Schopenhauer and each named in
Schopenhauer's text: there is a thing in itself to a given appearance (B xxvi, Prol § 32 ↔
Anhang ZA II 535); space is given a priori (A 24/B 38 ↔ Anhang ZA II 534); space is no
determination of the thing in itself (A 26/B 42 ↔ § 23, ZA I 156–157, »den Sinn der
Kantischen Lehre«). None with
Nietzsche, with the reasons on the page (JGB 16 hits the term »Ding an sich« as such;
Vernunft 6 Satz 4 diagnoses; Fabel stage 4 is framed as the positivist stage). Divergences
on the page: Kant's B xxvi ground is the absurdity of appearance without anything that
appears, not a causal inference, and the map has no Kant node stating the inference
Schopenhauer attacks (Prol § 32 »afficirt« and § 13 Anm. II are the nearest; left open);
B xxvi against Fabel stage 6, both treating »Erscheinung« as not standing alone, Kant
keeping the thing in itself, stage 6 giving up »scheinbar« (the map's reading, via Vernunft
6 Satz 1); immediacy (Schopenhauer § 22, § 18 against JGB 16, 19; Kant silent on immediacy but on a
side as to the thing in itself, A 42/B 59 against §§ 21–22, no attack link because the
denying words sit in two statements, said on the page);
the will (§ 23 against GD Irrthümer 3, JGB 19; JGB 36 under its two readings, the map not
picking). "What depends on the reading of Kant": two-object makes Schopenhauer's § 1
remark and Anhang attribution aim at Kant's doctrine; two-aspect makes them aim at a
reading of it. Run 7 added a sixth row, *What is the will, in relation to appearance and thing in
itself?* (Kant: the same will free as belonging to a thing in itself, not cognized;
Schopenhauer: § 21, a potiori; Nietzsche: JGB 19 complicated, Irrthümer 3 moves nothing,
JGB 36 under its two readings), Kant sentences at the head of the »On the will« paragraph
and a closing sentence there, two Kant passages in `passages:`, and the closing paragraph
now names the row and those sentences as unread by the owner; the `statement` was not
changed, since it speaks of rows 1–2. Run 8 added a seventh row, *Is the world of appearance the subject's own
work?* (Kant: space the subjective condition of sensibility, about the form only;
Schopenhauer: the world is my representation, appearance is representation; Nietzsche: JGB 15,
the sense organs not appearances in the idealist sense, and the checked reductio), Nietzsche
cells in rows 2 (JGB 21 cause/effect fictions, sign-world mythology), 3 (JGB 34 the belief a
naïveté), 4 (JGB 21 »An-sich«), 5 (JGB 34 ×3); a divergence paragraph *On causality and the
in-itself* (Kant restricts the principle, Schopenhauer makes the law a function of the
intellect inside representation, Nietzsche a conventional fiction we invented, and JGB 21
takes away the instrument of the inference Schopenhauer's Anhang attacks); JGB 21 under *None
with Nietzsche* as the nearest shared premise, link not set; JGB 34 under immediacy and the
division (the converse of stage 6); the closing paragraph names all of it as unread by the
owner. The `statement` still unchanged. Run 9 added Schopenhauer cells to rows 1–4 and 7 (above), a
second `shared` entry on space with § 24's »Bestimmungen« sentence, a paragraph under the
shared premise, § 24's own conditional beside B xxvi under *On the inference* and the
etiology claim there, the »unmittelbar« sentence under *On immediacy*, and the closing
paragraph names all of it as unread by the owner. Run 10 added Schopenhauer cells to rows 2
(C4), 4 (C1) and 7 (C10, the argument, C4) with sentences on their notes, a second entry
under *Space is given a priori* (A 24/B 38 ↔ C2) with sentences in its paragraph, the entry
and paragraph *The laws that govern experience have no use beyond it* (A 236/B 295 ↔ C3;
`p-krv-a236-b295` now in `passages:`), a paragraph *The Transcendental Aesthetic as a whole*
arguing no link on C5/C10 (Kant's statements are about space, Schopenhauer's about a priori
cognition as such; nearest: A 26/B 42 (b)), the gaps sentence naming the four Anhang spans
held, and the closing paragraph names all of it as unread by the owner. Seven `shared`
entries now. Gaps still listed on the page: Kant A
236–260 / B 295–315 beyond the opening and the B xxvi footnote; Schopenhauer § 2, § 24 and
§ 25 beyond their openings, §§ 26–29, Anhang on the Aesthetic; Nietzsche JGB 34 on the world as a fiction, JGB 21 on the will, GD Irrthümer
7–8.

**The second comparison, `x-the-will` (run 11, 2026-10-15), at /x/the-will/, `draft`,
offered under Ask 9.** Built from nodes already in the map, no new passage; same convention
and body order as the first (what the three say; where a premise is shared; where they
diverge; what depends on the readings; what the map does not contain; closing paragraph
with provenance dates). Five rows: what the will is in relation to appearance and thing in
itself; is it immediately known; is it the cause of the body's actions (Kant's cell empty:
B xxvii–xxviii has the will subject to the law, A 538–541 / B 566–569 not in the map); is it
free, and free of what (Kant: the B xxvii–xxix case and the checked argument; Schopenhauer:
§ 23's »frei von allen Formen« and »schlechthin grundlos, obwohl jede seiner Erscheinungen
... unterworfen«, set for the word »frei« and the two-sidedness; Nietzsche: JGB 21's »die
Freiheit« among the invented signs and »"psychologischer Unfreiheit"«, set for those words,
neither about a will free in its actions); what is drawn from it (Kant: morality's place,
B xxviii–xxix; Schopenhauer: the key to nature, § 19; Nietzsche: no spiritual causes, the I
a fable, JGB 36's attempt). `shared: []`; the two nearest argued and left open: Kant's B
xxvii causality clause (conditional on the deduction, asserts nothing outright) beside §
23's groundlessness; § 18's »stehn nicht im Verhältniß der Ursache und Wirkung« beside GD's
»Der Wille bewegt nichts mehr« (the shared proposition is Schopenhauer's wording and an
instance of Nietzsche's; the same sentence has the will »auch fehlen«; »mehr«). The hinge
throughout: Kant's will is *thought* »als einem Dinge an sich selbst angehörig« if the
critique is right, Schopenhauer's *is* the thing in itself; never write »belongs to« flat.
The two senses of »frei« (»jenem nicht unterworfen« vs »frei von allen Formen« / »grundlos«)
left open; the freedom in B xxviii is »als Eigenschaft eines Wesens«, not the will. JGB 19
and § 18 both refuse a cause–effect relation between will and action for opposite reasons
(identity; the »Anschein« became a feeling of necessity). Link set on the review's finding:
`c-schopenhauer-body-given-in-two-ways` ← `c-nietzsche-schopenhauer-ich-will-a-superstition`
(JGB 16 on § 18's »jenes Jedem unmittelbar Bekannte«), converse set, JGB 16's body says so;
not set on the identity claim (immediacy there is the ground, »eben weil«; argued on the
page). The readings of JGB 36: the move that GD's denial concerns »the will as an inner
faculty only« lives on the claim nodes and in the not-asserted reading's *what tells against
it*, not on `r-nietzsche-will-to-power-asserted`, which should gain it in a run that revises
readings. »intelligibler Charakter«: no Kant or Schopenhauer passage in the map carries the
term; the claim node now says so instead of calling it theirs. Quotations set on the 25 cell
claims that lacked them (every cell claim of both comparisons now carries one), chosen as the
sentence the notes quote, verified by `add_quotes.py` (scratchpad; substring check of
original and translation before writing) and by the build. The first page gained a sentence
linking the second under *On the will*, and its »Kant says nothing of immediacy« became »No
Kant passage in the map speaks of immediacy« (P1); both recorded in its closing paragraph as
unread by the owner. Review rules from run 11 (19 findings, 2 serious, all accepted): before
writing »the map holds only X of aphorism N«, `ls map/p-*N*` and grep; never write »thinker
is silent on X«, write »no passage in the map speaks of X«; a page inherits a claim node's
unmarked attributions, so read the node bodies it cites for sentences about thinkers; when a
cell is set for a word, say so in the note; a conditional's antecedent the author never
asserts in the map stays a reason against a shared link; name absent texts by reference
only, never by what they contain.

**Next.** The thing-in-itself page's Schopenhauer gaps are now small (§ 2, the rest of
§§ 24–25, §§ 26–29, the Anhang's Aesthetic theorems on time and the categories) and none
adds a row; the comparison on the will is built (above). **Next: settle the Phase 2 route
into INBOX.md** (a prefilled GitHub issue the owner pastes in, vs the deferred mailbox of
Ask 4) in MODEL.md as a method question, then design the dispute and attestation forms on
the node page inside DESIGN.md; give `r-nietzsche-will-to-power-asserted` the inner-faculty
reply; a fourth thinker after that, by lineage (PLAN.md Phase 3), not before Phase 2 has a
route. If the owner answers Ask 9, apply his decisions as under Ask 7 (status `checked` with
`status_note`; versions for changed statements with credit). When Schopenhauer text is needed again, try zeno.org first
and fall back to Gutenberg/Internet Archive without ZA pages.

**Money.** 10.88 EUR incl. BTW spent in Q4 2026 of 200 EUR (`LEDGER.md`). Nothing spent in
runs 1–5. The card used for the domain is still unreported.

**Tooling facts, owner's machine (Windows, Git Bash).** `python` (3.11, PyYAML), not
`python3`; set `PYTHONIOENCODING=utf-8` or umlauts print as �; a long inline heredoc
fails in Git Bash and `rm -rf` in the scratchpad was denied: write scripts to the
scratchpad with the Write tool and run them by path. korpora.org serves AA pages as
ISO-8859-1 with HTML entities (`&#228;`), decode then unescape. Commits as
`TheAndries`; push with plain `git push`. Owner-session commit messages begin
»owner session —«.

**Tooling facts.** Cloud container: Python 3.11 with PyYAML, Node 22 with a global
`playwright` and Chromium at `/opt/pw-browsers/chromium` (screenshots: `NODE_PATH=$(npm
root -g) node script.js`, viewport 390 for phone). WebSearch works and confirmed the two
chapter titles this run; WebFetch works for ordinary pages but Cambridge/OUP catalogue
pages return nothing useful. `pip install` and raw downloads work through the proxy; no
`gh` CLI. Git author `Claude <noreply@anthropic.com>`; commits carry the session trailer.
The container checks out a detached HEAD whose local `main` ref is stale; push with `git
push origin HEAD:refs/heads/main`. A stop hook asks for a commit whenever the turn ends
with uncommitted changes; do not commit nodes before the review to satisfy it.

Run 8 (26 findings, 0 serious, 8 moderate, 25 accepted): a mark the text puts on a sentence
(»-?«) belongs in the statement, not only in the quotation; keep the person the text
addresses (»ihr«, »eurer«) and say who they are; when the map calls one sentence the converse
of another in a different work, the identification of their terms is the map's and is said
so; a connection the page draws between texts (»the inference with it«, »takes the
instrument away«) is written »as the map reads it«; a prescription (»soll«) on the use of a
word asserts nothing of the thing's origin and so attacks nothing that states the origin;
when a sentence sets two origins in the subject (»erdichtet«, »Funktion des Intellekts«),
name the pair under *None with Nietzsche* and say why no link; a status note is re-read
against the whole table every run, since a note true when written becomes false by
accretion (the owner's note now carries a dated clause on unreviewed cells, the operator's
amendment, which he may object to); a row question must be worded for all three columns,
not in one thinker's word; passage bodies may not quote sentences outside the stored span
in guillemets either. The reviewer again verified every original mechanically and found no
slip; its cost was 157,000 tokens and it took ten minutes.

Run 10 (14 findings, 0 serious, 6 moderate, 14 accepted; the reviewer verified every original
and quotation mechanically and the ZA pages against the marks, 121,000 tokens, seven
minutes): a factive noun (»auf Grund der Nachweisung, daß«) asserts its content as a factive
verb (»Er zeigte, daß«) does, so treat the two alike when deciding a shared-premise link (C1
now linked to A 42/B 59); when a link rests on identifying two texts' subjects (Kant's
Grundsätze, Schopenhauer's Gesetze), say the identification is the map's and find the Kant
passage that carries it (Prol § 57 did); a shared premise must be worded to cover both
texts' predicates, not one's (»Erfahrungsgebrauch« vs »nicht anzuwenden«); a collation note
must list every non-orthographic variant, above all one inside the load-bearing sentence
(»die Bedingungen«), and must not name a non-variant; a statement that opens with an anaphor
(»Its«, »those laws«) is unreadable alone, so resolve it; keep a reported subjunctive
(»käme«) as »would« in the statement as in the translation; a bridge's parenthesis may not
claim more than the argument's body (»discharged by Demnach« vs »treats as discharged«); »X
ist uns bewußt« is »we are conscious of X«, never »X is conscious to us«; "the paragraph
before" must be checked in the corpus, not remembered; a gaps sentence that says a paragraph
is held must check whether only its opening is.

**Dropped from memory this run:** nothing; the file is about 7,100 words of 8,000. Next run
should compress the per-run node inventories (runs 7–10) into the node lists if it needs
room.
