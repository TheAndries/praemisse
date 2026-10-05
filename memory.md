# memory.md

Carried state for the operator. Capped at 8,000 words. Rewritten each run.

## State as of 2026-10-05 (run 1, end)

**Identity and governance.** Name `praemisse`; domain praemisse.com at TransIP (Ask 1 done;
DNS pointing is now Ask 5). Repository https://github.com/TheAndries/praemisse, public, `main`.
Routine `trig_01CybW54QF5Q5hCdyVQzM8qX`, `34 5 * * *` UTC, model `claude-fable-5-1`. Run 1 was
served on the configured model `claude-fable-5-1`; no handover note needed. Open disputes: none.
Attestations: none. Open motions: none. INBOX empty at run 1.

**Phase 0, nearly done.** Built in run 1, all on `main`:
- `site/build.py`: reads `map/*.md` (YAML front matter + Markdown), validates against
  `MODEL.md` (id prefix ↔ type, status words, `produced_by` required, every link in
  `depends_on`/`supports`/`attacked_by`/`replies_to`/`shares_premise_with`/`passages`/
  `premises`/`conclusion`/`verified_by`/`disputes`/`supersedes`/`superseded_by`/`thinker`/
  `work` must resolve; a claim or argument must cite a passage), renders to `site/_build/`
  (gitignored) with relative paths so it works at a sub-path. `--check` for CI. Tested on a
  scratch map of four dummy nodes (not committed). Own tiny Markdown subset; PyYAML the only
  dependency.
- `site/static/style.css` (layout, four sizes, 66ch measure, passage beside text at ≥66rem,
  dark mode by system, print), `site/templates/` (base, node, index), `site/static/type.css`
  placeholder.
- Fonts, self-hosted and subset to Latin + polytonic Greek with features kept:
  EB Garamond + Source Sans 3 (A), Libertinus Serif + Sans (B), Alegreya + Alegreya Sans
  (C). All OFL. `site/fonts/README.md` has provenance. Rejected: Source Serif 4 (no polytonic
  Greek in the google/fonts build); Libertinus release WOFF2 (features stripped; subset from
  OTF instead).
- `site/specimens/{a,b,c,index}.html`, written by `site/specimens/make.py`: one mock node
  page, three types. Specimen text is the page's own reasoning plus four verse passages
  (Homer Il. 1.1–2, Vergil Aen. 1.1–3, Goethe Faust I 354–357, La Fontaine Fables I.1 1–4)
  with the project's own translations. No node, no claim attributed to anyone.
- `.github/workflows/site.yml`: check, build, deploy to GitHub Pages on push to `main`.
  Pushed in a separate commit; see the changelog for whether the push was accepted.

**Open asks.** 3 (choose the type; blocks Phase 1). 4 (mailbox; deferred by owner; blocks
Phase 2). 5 (enable Pages, set DNS at TransIP, custom domain; blocks public viewing). 6
(read the routine config back: connectors were visible in run 1 though recorded as `[]`).

**When Ask 3 is done:** copy the chosen `type-X.css` over `site/static/type.css`, delete
the two unused font directories and their `type-*.css`, record the choice in `DESIGN.md`
under *Open design asks* (that is a board decision transcribed, so it is permitted), and
drop `site/specimens/` from the published nav (keep the files; nothing is deleted).

**When Ask 5 (c) is confirmed:** add `--domain praemisse.com` to the build step in the
workflow so a `CNAME` file is emitted; verify https://praemisse.com/ serves.

**Before the first node (Phase 1), settle in `MODEL.md`-compatible form and record in the
changelog:** (1) how a new version lives inside the same file — proposed: a `versions:`
list in the front matter, newest first, each with `date`, `reason`, and the superseded
text; the page shows the current version and links the chain; (2) what the machine validity
check for `a-` nodes is — proposed: premises and conclusion as propositional/first-order
schemata in a `form:` field, checked by a small prover, with `checked` set only by the
tool; (3) how a Dispute node renders on its target's page; (4) a `t-`/`w-` node for Kant,
KrV and Prolegomena first, with the Akademie-Ausgabe scan as source. Phase 1 starts only
after Ask 3.

**Money.** 10.88 EUR incl. BTW spent in Q4 2026 of 200 EUR (`LEDGER.md`). Nothing spent in
run 1. The card used for the domain is still unreported.

**Tooling facts.** The cloud container has Python 3.11, PyYAML, Node 22 with a global
`playwright` and Chromium at `/opt/pw-browsers/chromium`; `pip install fonttools brotli`
works through the proxy; GitHub release and raw.githubusercontent.com downloads work, the
GitHub REST API returns 403 unauthenticated. There is no `gh` CLI. Git author is
`Claude <noreply@anthropic.com>`; commits carry the session trailer.

**Dropped from memory this run:** the founding-session details of the routine creation
(three default connectors attached on create, cleared with `clear_mcp_connections`), which
live in `ROUTINE.md` and the 2026-10-04 changelog; the list of rejected names.
