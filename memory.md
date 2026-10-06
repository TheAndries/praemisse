# memory.md

Carried state for the operator. Capped at 8,000 words. Rewritten each run.

## State as of 2026-10-06 (run 2, end)

**Identity and governance.** Name `praemisse`; domain praemisse.com at TransIP; site live at
https://praemisse.com/ (GitHub Pages, HTTPS enforced, certificate to 2027-01-03, GitHub
renews). Repository https://github.com/TheAndries/praemisse, public, `main`. Routine
`trig_01CybW54QF5Q5hCdyVQzM8qX`, `34 5 * * *` UTC, model `claude-fable-5-1`; runs 1 and 2
were served on that model, no handover note needed. The GitHub and Claude Code Remote tools
in the tool list are platform-attached to every cloud session and are not a config change
(`ROUTINE.md`, Ask 6): do not raise it again. Open disputes: none. Attestations: none. Open
motions: none. INBOX empty at runs 1 and 2. Open asks: 4 only (mailbox; deferred by owner;
blocks Phase 2). Asks 1, 2, 3, 5, 6 done.

**Phase 0 complete (2026-10-05).** `site/build.py` (reads `map/*.md`, validates against
`MODEL.md`, renders to `site/_build/`, gitignored; `--check` for CI; PyYAML the only
dependency; own small Markdown subset), `site/static/style.css` and `type.css` (direction
B, Libertine, owner decision), `site/fonts/libertinus/` only, `site/specimens/` kept but not
published, `.github/workflows/site.yml` (check, build with `--domain praemisse.com`, deploy
on push to `main`), `.github/workflows/notify-asks.yml` + `tools/open_asks_issue.py` (one
GitHub issue *praemisse - open asks*, assigned to the owner, updated on every push touching
`ASKS.md`; keep the `| # | Date | Ask | Blocks | Status |` table; `done ...` closes, *deferred*
or *queued* lists as no action).

**Phase 1 started (run 2, 2026-10-06).** The three model questions are settled and written
into `MODEL.md`, section *How the model is applied* (operator's domain, method): `versions:`
list in the same file; `statement:` one sentence on every claim, argument and comparison;
`form:` block in propositional logic checked by `tools/validity.py` (truth table, ≤16 atoms,
`not/and/or/->/<->`), `checked` only on an argument whose form passes, claims stay `draft`
until attested; `d-` and `v-` nodes name a `target` and render in full on the target's page;
`verified_by`/`disputes` must equal the set targeting the node; `attested` needs one `v-`,
`established` two; `contested` iff a `d-` has outcome contested. All enforced by `--check`.
Dispute outcomes: published, argued, conceded, contested, resolved, escalated. An `about/`
page exists (template `site/templates/about.html`). Exercised on a scratch map with a
dispute, an attestation and a version; not committed.

**Kant nodes on `main` (24):** `t-kant`; `w-kant-krv`, `w-kant-prolegomena`; passages
`p-krv-b-xxvi` (AA 3:16.30–17.07), `p-krv-a24-b38` (3:52.30–53.16), `p-krv-a26-b42`
(3:55.02–08), `p-krv-a42-b59` (3:65.17–22), `p-krv-a43-b60` (3:65.28–66.04), `p-krv-b307`
(3:209.32–210.12), `p-krv-b308-309` (3:210.24–34), `p-prol-289` (4:289.03–14), `p-prol-314`
(4:314.33–315.06); claims `c-kant-space-a-priori`, `c-kant-determinations-not-intuited-a-priori`,
`c-kant-space-not-of-things-in-themselves`, `c-kant-objects-known-only-as-appearances`,
`c-kant-knowledge-limited-to-experience`, `c-kant-things-in-themselves-unknown`,
`c-kant-appearance-presupposes-something-appearing`,
`c-kant-things-in-themselves-thinkable-not-knowable`, `c-kant-noumenon-negative-only`,
`c-kant-without-things-in-themselves-appearance-without-appearing`;
arguments `a-kant-space-not-of-things-in-themselves` (a; s→¬a ⊢ ¬s, checked) and
`a-kant-appearance-requires-thing-in-itself` (w; ¬t→¬w ⊢ t, checked, a reductio). Translations are the project's own, marked. Every `original` was diffed
word for word against the korpora.org text before commit.

**Source of Kant's text.** https://korpora.org/kant/aa{03,04}/{page:03d}.html, one Akademie
page per file with line numbers in a table; the extractor is the small script described in
the 2026-10-06 changelog (regex over `<tr>`/`<td>`, prints `vol:page.line text`). The
`korpora.zim.uni-duisburg-essen.de` host resets connections; use `korpora.org`. The Korpus
joins hyphenated line-end words ("nothwendiggemachte" at 3:17.07) and has an OCR slip at
3:65.25 ("daßmacht, da"): quote around such lines. A/B pages are not in the Korpus; they
are given from the standard concordance and the AA line is the authoritative locator.
AA III = KrV B; AA IV 1–252 = KrV A, 253–383 = Prolegomena.

**The adversarial pass is not optional.** Run 2's first form of the B xxvi argument had an
assumption that asserted premises-imply-conclusion and a body that denied Kant states the
bridge he states; the reviewing agent caught it, plus nine smaller faults (see the
2026-10-06 entry). Give the reviewer the nodes, the fetched corpus files and the brief to
break validity, fidelity, translation and line references; budget ~80,000 tokens for it.

**Next for Phase 1 (PLAN.md §3, target ~40 nodes, one comparison node).** Kant: the
critique of dogmatic metaphysics is not yet in the map (candidates: B xxx "Ich mußte also
das Wissen aufheben", A 235–260/B 294–315 on the land of truth, Prolegomena §57 on the
limits, AA 4:350–356 already fetched to scratch but lost with the container). Reading nodes
for the two-aspect / two-object question on "eben dieselben Gegenstände" (B xxvi). Then
Schopenhauer: WWV I §§ 1–2, 18–23 (will as thing-in-itself), the Anhang "Kritik der
Kantischen Philosophie" (by section); public-domain German text: zeno.org is reachable
through the proxy (checked 2026-10-06; de.wikisource returns 404 for the plain titles);
nietzschesource.org answers too, but its eKGWB is JavaScript-rendered and needs a check. Then Nietzsche: JGB 16, 54; GD "Wie die wahre Welt
endlich zur Fabel wurde"; Nachlass only where unavoidable and marked. Then `x-thing-in-itself`.
Checkpoint 1 needs the comparison page; at the present pace (two arguments a run) that is
roughly ten runs away, which is on plan.

**Money.** 10.88 EUR incl. BTW spent in Q4 2026 of 200 EUR (`LEDGER.md`). Nothing spent in
runs 1 or 2. The card used for the domain is still unreported.

**Tooling facts.** Cloud container: Python 3.11 with PyYAML, Node 22 with a global
`playwright` and Chromium at `/opt/pw-browsers/chromium` (screenshots: `NODE_PATH=$(npm root
-g) node script.js`, viewport 390 for phone). `pip install` and raw GitHub downloads work
through the proxy; the GitHub REST API returns 403 unauthenticated; no `gh` CLI. Git author
`Claude <noreply@anthropic.com>`; commits carry the session trailer.

**Dropped from memory this run:** the Phase 0 build details that are now in `site/README.md`
and the 2026-10-05 entries (font subsetting, rejected families, the specimen texts), and
the run-1 verification notes about whether the workflow ran (it does; deploys are green
since Ask 5).
