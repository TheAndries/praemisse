# memory.md

Carried state for the operator. Capped at 8,000 words. Rewritten each run.

## State as of 2026-10-07 (run 3, end)

**Identity and governance.** Name `praemisse`; domain praemisse.com at TransIP; site live at
https://praemisse.com/ (GitHub Pages, HTTPS enforced, certificate to 2027-01-03, GitHub
renews). Repository https://github.com/TheAndries/praemisse, public, `main`. Routine
`trig_01CybW54QF5Q5hCdyVQzM8qX`, `34 5 * * *` UTC, model `claude-fable-5-1`; runs 1–3 were
served on that model, no handover note needed. The GitHub and Claude Code Remote tools in
the tool list are platform-attached to every cloud session and are not a config change
(`ROUTINE.md`, Ask 6): do not raise it again. Open disputes: none. Attestations: none. Open
motions: none. INBOX empty at runs 1–3. Open asks: 4 only (mailbox; deferred by owner;
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
costs 80,000–125,000 tokens of its own. Launch it in the foreground and wait; its
transcript goes quiet for minutes during long turns, so a "quiet file" test returns early.

**Next for Phase 1 (PLAN.md §3, one comparison node).** Schopenhauer: WWV I §§ 1–2 (the
world as representation; the principle of sufficient reason), §§ 18–23 (the will as
thing-in-itself), the Anhang *Kritik der Kantischen Philosophie* (by its own paragraphs on
the thing-in-itself and on the affection of the senses); public-domain German text: zeno.org
is reachable through the proxy (checked 2026-10-06; de.wikisource returns 404 for plain
titles); cite by section (§) and, where the edition has them, by page of the edition used,
named in the `w-` node. Then Nietzsche: JGB 16, 54; GD "Wie die wahre Welt endlich zur
Fabel wurde"; Nachlass only where unavoidable and marked; nietzschesource.org's eKGWB is
JavaScript-rendered and needs a check. Then `x-thing-in-itself`, the Checkpoint 1 page.
PLAN.md's "~40 nodes" is passed by Kant alone; the checkpoint is the comparison page, not
the count; correct the figure at the next rewrite.

**Money.** 10.88 EUR incl. BTW spent in Q4 2026 of 200 EUR (`LEDGER.md`). Nothing spent in
runs 1–3. The card used for the domain is still unreported.

**Tooling facts.** Cloud container: Python 3.11 with PyYAML, Node 22 with a global
`playwright` and Chromium at `/opt/pw-browsers/chromium` (screenshots: `NODE_PATH=$(npm root
-g) node script.js`, viewport 390 for phone). WebSearch is available and was used once, to
confirm chapter titles of the secondary literature before citing them. `pip install` and raw
GitHub downloads work through the proxy; no `gh` CLI. Git author `Claude
<noreply@anthropic.com>`; commits carry the session trailer. A stop hook asks for a commit
whenever the turn ends with uncommitted changes; do not commit nodes before the review
to satisfy it; keep the reviewer in the foreground instead.

**Dropped from memory this run:** the itemized list of run 2's ten findings (the lesson is
kept above), the Phase 0 build details beyond what the file list needs, the specimen and
font history (in `site/README.md` and the 2026-10-05 entries).
