# memory.md

Carried state for the operator. Capped at 8,000 words. Rewritten each run.

## State as of 2026-10-08 (run 4, end)

**Identity and governance.** Name `praemisse`; domain praemisse.com at TransIP; site live at
https://praemisse.com/ (GitHub Pages, HTTPS enforced, certificate to 2027-01-03, GitHub
renews). Repository https://github.com/TheAndries/praemisse, public, `main`. Routine
`trig_01CybW54QF5Q5hCdyVQzM8qX`, `34 5 * * *` UTC, model `claude-fable-5-1`; runs 1–4 were
served on that model, no handover note needed. The GitHub and Claude Code Remote tools in
the tool list are platform-attached to every cloud session and are not a config change
(`ROUTINE.md`, Ask 6): do not raise it again. Open disputes: none. Attestations: none. Open
motions: none. INBOX empty at runs 1–4. Open asks: 4 only (mailbox; deferred by owner;
blocks Phase 2). Asks 1, 2, 3, 5, 6 done.

**Phase 0 complete (2026-10-05).** `site/build.py` (reads `map/*.md`, validates against
`MODEL.md`, renders to `site/_build/`, gitignored; `--check` for CI; `--domain
praemisse.com` in the workflow; PyYAML the only dependency; own small Markdown subset with
`[text](../../c/slug/)` links between node pages, which live at `/<prefix>/<slug>/`),
`site/static/style.css` and `type.css` (Libertine, owner decision), `.github/workflows/
site.yml` (check, build, deploy on push to `main`), `notify-asks.yml` + `tools/
open_asks_issue.py` (one GitHub issue *praemisse - open asks*; keep the `| # | Date | Ask |
Blocks | Status |` table; `done ...` closes, *deferred*/*queued* lists as no action).

**Phase 1 in progress.** Model settled in `MODEL.md`, *How the model is applied*:
`versions:` in the same file (date, reason, superseded statement, credit); `statement:` one
sentence on every claim, argument and comparison; `form:` in propositional logic checked by
`tools/validity.py` (truth table, ≤16 atoms, `not/and/or/->/<->`), `checked` only on an
argument whose form passes, claims `draft` until attested; premises may be `{claim: id}` or
`{assumption: text}`, and an assumption is where the map's own bridge goes, named as such;
`depends_on` on a claim names its argument, or a claim it is drawn from by an "also"/
"denn"/"mithin" step not yet formalized (recorded in MODEL.md on 2026-10-07); `r-` nodes
carry `reading_of`, `statement`, `passages`, `literature` (author, title, year, chapter), no
status, and a body with *the texts it rests on*, *what it holds*, *what depends on it*,
*what tells against it*; the map never picks a reading (P9); `d-`/`v-` nodes name a `target`
and render in full on it; `verified_by`/`disputes` must equal the set targeting the node;
`attested` one `v-`, `established` two; `contested` iff a `d-` has outcome contested. All
enforced by `--check`.

**Kant nodes on `main` (53 after run 3):** `t-kant`; `w-kant-krv`, `w-kant-prolegomena`;
17 passages: `p-krv-b-xxvi` (3:16.30–17.07), `p-krv-b-xxviii-xxix` (3:18.21–30),
`p-krv-b-xxix-xxx` (3:18.33–19.09), `p-krv-a24-b38`, `p-krv-a26-b42`, `p-krv-a42-b59`,
`p-krv-a43-b60`, `p-krv-a235-b294` (3:202.12–22), `p-krv-a236-b295` (3:203.04–09),
`p-krv-b307`, `p-krv-b308-309`, `p-prol-289`, `p-prol-314`, `p-prol-350` (4:350.21–33),
`p-prol-350-351` (4:350.34–351.12), `p-prol-352` (4:352.21–33), `p-prol-353` (4:353.16–22);
27 claims (run 2's ten on space, appearance, the limits of knowledge and the noumenon;
run 3's seventeen on B xxix–xxx: the pretension, its principles, the practical assumption,
knowledge annulled for faith, dogmatism defined; the island and the understanding's
principles; Prolegomena §57: the two absurdities, principles taken for conditions of
things, restricting principles becoming transcendent, the map's absurdity premise, the
critique clause, bounds against limits, the space for things in themselves, metaphysics
leads to limits; and the same action in another relation); 4 arguments, all `checked`:
`a-kant-space-not-of-things-in-themselves` (s→¬a ⊢ ¬s),
`a-kant-appearance-requires-thing-in-itself` (¬t→¬w, w ⊢ t),
`a-kant-practical-assumption-requires-removing-speculative-pretension` (k→e, e→x, a→¬x ⊢
a→¬k; a→¬x is an assumption premise, the map's bridge),
`a-kant-denying-things-in-themselves-absurd` (n→g, g→u, ¬u ⊢ ¬n; ¬u is the map's claim
`c-kant-restricting-principles-becoming-transcendent-is-absurd`, said so on the node);
2 readings, `r-kant-two-aspect` (Prauss 1974; Allison 2004, ch. 2) and `r-kant-two-object`
(Strawson 1966, Part Four; Guyer 1987, Part V; Van Cleve 1999, ch. 10 "Noumena and Things
in Themselves"), both `reading_of: c-kant-things-in-themselves-thinkable-not-knowable`.
Translations are the project's own, marked. *Grenzen* = "limits", *Schranken* = "bounds"
everywhere (Kant's definition, 4:352.21–25); "aufheben" = "annul", noted on the passage;
"ihr Ziel setzen" = "put a stop to". Still not in the map: B xxvii–xxviii on the will
(3:17.08–18.21), A 236–260 / B 295–315 beyond the opening, Prolegomena §§58–59 (symbolic
anthropomorphism, the limit as a point of contact), Kant's footnote at B xxvii.

**Schopenhauer nodes on `main` (36 after run 4; 89 nodes in all plus README):** `t-schopenhauer`;
`w-schopenhauer-wwv1` (Zürcher Ausgabe 1977 text after Hübscher's 1859 text, vol. 1 = Books
1–2, vol. 2 = Books 3–4 and the Anhang, continuous pagination); 13 passages `p-wwv1-*`:
§ 1 (the first paragraph, ZA I 28 inferred; the »Objekt an sich« sentence, 30), § 18 (the
body given in two ways, 142; the identity shown not proved, 144–145), § 19 (causality never
leads beyond representation, 146–147; the analogy of the body, 147–148), § 21 (the will
alone is the thing in itself, 153–154), § 22 (denominatio a potiori, 154; the will not
inferred, 155), § 23 (free of the forms, 156; groundless and one, 157), Anhang (Kant's
derivation of the thing in itself, ZA II 534–535; only the derivation is faulty, 535);
21 claims `c-schopenhauer-*`, all `draft`; 2 arguments, both `checked`:
`a-schopenhauer-corporeal-world-in-itself-is-will` (m→a, a→(v∨w), m→¬v ⊢ m→w; premises 1
and 3 are the map's, the conclusion is epistemic, »so müssen wir sagen«) and
`a-schopenhauer-kant-derivation-cannot-reach-thing-in-itself` (k, b, (k∧b)→¬e ⊢ ¬e; b is
the § 19 principle, which the appendix does not cite and the map reads behind its
»Mithin«; the bridge is the definition of a thing in itself at ZA II 535). No attack link
on any Kant node: Schopenhauer accepts »die Anerkennung eines Dinges an sich zur gegebenen
Erscheinung« (ZA II 535) and the map has no Kant node stating the causal inference he
attributes to Kant without a passage. `attacked_by`/`replies_to` are still unused in the
map; settle their convention (converses? a `versions:` entry for a link-only change?) in
MODEL.md the first time one is set. Terms: Vorstellung "representation", Erscheinung
"appearance", Objektität "objectity", Satz vom Grunde "principle of sufficient reason",
nachweisen "show" against beweisen "prove", darthun "show"/"set forth", Voraussetzung
"presupposition", Annahme "assumption", Besonnenheit "discernment", »Grund und Boden«
"ground and soil". The identity of will and body is a claim, not an argument, because
§ 18 says it can never be proved. Still not in the map: § 2, § 20, §§ 24–29, the §§ 18–19
sentences on pain and pleasure, the Anhang on the Transcendental Aesthetic and on the
categories.

**Source of Schopenhauer's text.** zeno.org, `http://www.zeno.org/Philosophie/M/Schopenhauer,+Arthur/Die+Welt+als+Wille+und+Vorstellung/Erster+Band/<Erstes+Buch|Zweites+Buch|Anhang.+Kritik+der+Kantischen+Philosophie>`,
one Book per HTML file, served as ISO-8859-1 (decode as such, not UTF-8); the text is in
`<div class="zenoCOMain">`, `<h5>` carries the § numbers, `[N]` in `class="zenoTXKonk"`
anchors marks where ZA page N begins (confirmed by page lengths), footnote numbers are
glued to the preceding word (»u.s.w.31«). The extractor (strip tags, unescape, keep § and
page markers) and the passage generator that extracts each `original` by start/end
substring and strips markers are rewritten in twenty lines each; keep them in the
scratchpad. Nietzsche: zeno.org serves JGB and GD too (Schlechta, Werke in drei Bänden,
München 1954, by aphorism groups such as `.../Erstes+Hauptstück.../11-20`); cite by
aphorism number, which is canonical, and give the KSA volume and page only if verified.
nietzschesource.org is JavaScript-rendered and returns nothing usable through the proxy.

**Source of Kant's text.** https://korpora.org/kant/aa{03,04}/{page:03d}.html, one AA page
per file, lines in `<tr>` rows: first non-empty `<td>` is the line number, the rest the
text; join hyphenated words across lines by hand. The extractor and the diff script
(`original` must be a substring of the joined page text; prints the start and end line) are
rewritten each run in ten lines; keep them in the scratchpad, not the repository. The
`korpora.zim.uni-duisburg-essen.de` host fails through the proxy; use `korpora.org`. The
Korpus joins "nothwendiggemachte" at 3:17.07 and has an OCR slip at 3:65.25. A/B pages are
not in the Korpus; they are given from the standard concordance and the AA line is the
authoritative locator (B xxx = "Ich mußte also das Wissen aufheben"; A 235/B 294 = chapter
opening of Phenomena and Noumena; A 236/B 295 = "Wir haben nämlich gesehen").

**The adversarial pass is not optional, and it finds what the truth table cannot.** Run 2:
one form that asserted premises-imply-conclusion. Run 3: both forms valid, both wrong as
reconstructions, one by a premise the passage's own Hume example contradicts, one by a
silent identification of the conclusion claim with the form's conclusion. Pattern: when a
form's conclusion is not word for word the conclusion claim, the missing step is a tacit
premise; make it an `assumption` premise and say it is the map's. When Kant gives a verdict
("Ungereimtheit") and then the consequences, the premise that the consequence is
unacceptable is the map's; make it a claim whose body says so in its first sentence. Brief
for the reviewer: the node list, the corpus files, the older passages the new nodes cite,
and the order validity, fidelity, translation, line references, readings, links; it
costs 80,000–125,000 tokens of its own. Run 4: 47 findings, the serious ones again
on the arguments: a bridge premise that was "premises imply conclusion" while the textual
principle (§ 19) sat unlisted; a disjunction (»Wille und Vorstellung«) silently resolved;
an epistemic conclusion (»müssen wir sagen«) made ontological; an attack link set on a
Kant claim that Schopenhauer explicitly accepts. Lesson added: before linking an attack,
check that the attacked node states what the attacker denies, not merely the nearest
topic; and quote the connective for every claim→claim `depends_on` or set none. The Agent
tool launches the reviewer in the background even when asked for the foreground; its
transcript stays quiet for 15–20 minutes during one long turn, a quiet-file wait returns
early, and the stop hook then asks for a commit, which must be refused until the report
is in. A `SendMessage` to the agent asking for the report now makes it hand back (it did
in run 4, and the same report arrived twice). It cost 178,000 tokens of its own.

**Next for Phase 1 (PLAN.md §3, one comparison node).** Nietzsche: JGB 16 (the »unmittelbare
Gewißheit« of the I), JGB 54 (the subject as grammatical habit), JGB 15–17 and 36 (the will
as the only reality, the "will to power" hypothesis as an answer to Schopenhauer), GD "Wie
die »wahre Welt« endlich zur Fabel wurde" (the abolition of the true world together with
the apparent), GD "Die vier großen Irrthümer" §3 (the will as a cause; against
Schopenhauer's »unmittelbar Erkanntes«), and JGB 19 (willing is not simple, against
§ 18's identity); Nachlass only where unavoidable and marked. Source: zeno.org (above).
Then `x-thing-in-itself`, the Checkpoint 1 page: Kant's thinkable-not-knowable thing in
itself and the two readings; Schopenhauer keeping the thing in itself and replacing the
derivation with the will (ZA II 535) while rejecting an object in itself (ZA I 30);
Nietzsche denying the distinction. PLAN.md's "~40 nodes" is passed (89); the checkpoint is
the comparison page, not the count; correct the figure at the next rewrite.

**Money.** 10.88 EUR incl. BTW spent in Q4 2026 of 200 EUR (`LEDGER.md`). Nothing spent in
runs 1–3. The card used for the domain is still unreported.

**Tooling facts.** Cloud container: Python 3.11 with PyYAML, Node 22 with a global
`playwright` and Chromium at `/opt/pw-browsers/chromium` (screenshots: `NODE_PATH=$(npm root
-g) node script.js`, viewport 390 for phone). WebSearch is available and was used once, to
confirm chapter titles of the secondary literature before citing them. `pip install` and raw
GitHub downloads work through the proxy; no `gh` CLI. Git author `Claude
<noreply@anthropic.com>`; commits carry the session trailer. The container checks out a detached HEAD whose local
`main` ref is stale, so `git push origin main` is rejected as non-fast-forward even when
the remote tip is HEAD's parent; push with `git push origin HEAD:refs/heads/main`, or run
`git branch -f main HEAD` first. A stop hook asks for a commit
whenever the turn ends with uncommitted changes; do not commit nodes before the review
to satisfy it; keep the reviewer in the foreground instead.

**Dropped from memory this run:** the itemized Kant-run findings beyond the lessons kept
above, the Kant extractor's line-by-line description (the URL pattern and the two Korpus
quirks are kept), and run 3's note on the reviewer's "quiet file" test, now folded into the
adversarial-pass paragraph.
