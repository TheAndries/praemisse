# CHANGELOG.md

Newest first. What was done, decided, and got wrong.

## 2026-10-07 — run 3: the critique of dogmatic metaphysics, and the two readings

Third scheduled run, on `main`, on the configured model `claude-fable-5-1` (the same the
last entry records; no handover). Read all governing files first.

**Steps 1–3.** No ask changed status since run 2; Ask 4 stays deferred by the owner and
blocks only Phase 2. `INBOX.md` empty: nothing to publish, reply to or record. No open
motion.

**Step 4, the nodes: 29 new, 3 revised.** Kant on the critique of dogmatic metaphysics and
the limits of reason, from the korpora.org text, fetched page by page (AA III 18–19,
202–203; AA IV 350–357). Eight passages: B xxviii–xxix (the same action in another
relation); B xxix–xxx ("Ich mußte also das Wissen aufheben"); A 235–236 / B 294–295 (the
island, the land of truth); A 236 / B 295 (the understanding's principles serve only
experience); Prolegomena §57 in four spans (the absurdity of cognizing beyond experience;
the still greater absurdity of admitting no things in themselves; *Grenzen* against
*Schranken*; metaphysics leads to limits). Seventeen claims, all `draft`. Two arguments,
both `checked`: *God, freedom and immortality cannot be assumed for practical use unless
speculative reason gives up its pretension to insight beyond experience* (k→e, e→x, a→¬x
⊢ a→¬k, B xxix–xxx) and *to admit no things in themselves is absurd* (n→g, g→u, ¬u ⊢ ¬n,
Prolegomena §57). Two reading nodes on "eben dieselben Gegenstände" (B xxvi), the first
use of the `r-` type: the two-aspect reading (Prauss 1974; Allison 2004, ch. 2) and the
two-object reading (Strawson 1966, Part Four; Guyer 1987, Part V; Van Cleve 1999, ch. 10),
each with the passages it rests on, what it holds, what depends on it and what tells
against it; the map picks neither (`CHARTER.md` P9). The claim they read now points to
them. Every passage's `original` was diffed word for word against the fetched text and its
line range confirmed by the same script; one slip (4:352.32 for 33) was caught that way
before the review. Translations are the project's own and marked. *Grenzen* is "limits"
and *Schranken* "bounds" throughout, following Kant's own definition at AA 4:352.21–25;
the one older passage that had "boundary" (B 308–309) is revised to match, with the
revision noted on the node.

**Method.** `MODEL.md`, *How the model is applied*, gains two paragraphs, as matters of
method: how a reading node is applied (`reading_of`, `statement`, `literature`, no
status) and what `depends_on` means between two claims (an argument, or a step the text
marks with "also", "denn", "mithin" that the map has not formalized). The build validates
`reading_of` as a link and renders a reading's target and literature in the facts list.

**The adversarial pass, and what it found.** A second agent was given the nodes, the
corpus files and the brief to break validity, fidelity, translation and line references;
it also fetched the five older AA pages the readings cite. It returned 33 findings; I
accepted all 33 and changed the nodes before commit.
- *Serious, validity.* My Prolegomena §57 argument had as its third premise "a careful
  critique guards the limits of reason", from the "wenn nicht" clause (4:351.10–12), and
  the form negated "the restricting principles become transcendent". But Kant says they
  *could* become so and that Hume's *Dialogues* are an example of it happening (4:351.09):
  the passage itself contradicts a factual premise that they do not. And the form's
  conclusion, "we do not admit no things in themselves", was not the conclusion claim,
  "it is absurd to admit no things in themselves". The absurdity can only come from a
  premise that the outcome is absurd, which is the map's, not Kant's wording. Rebuilt:
  premise 3 is a new claim, *it is absurd that the principles restricting reason to
  possible experience should themselves become transcendent*, whose body says in its
  first sentence that it is the map's reading and why; the critique clause is a standalone
  claim, restated as the counterfactual it is; and my sentence attributing the "greater
  absurdity" of 4:350.34 to the wrong thing is gone.
- *Moderate, validity.* The B xxx argument's form concluded ¬x→¬k, "if practical extension
  is not declared impossible, the pretension is removed", while its conclusion claim says
  "I cannot assume God, freedom and immortality unless ..."; the identity of "assuming
  them" with "practical extension not being impossible" was tacit. Added as an explicit
  assumption premise, a→¬x, named as the map's bridge; the form now concludes a→¬k, which
  is the claim. The argument's id had named a claim it does not support; renamed before
  commit, while ids are still free.
- *Moderate.* A `shares_premise_with` link that shared no premise node; conclusion claims
  without `depends_on` their argument; "would become transcendent" for "könnten";
  "set a goal to its pretensions" for "ihr Ziel setzte", which means to put a stop to
  them; the "Grenze"/"boundary" inconsistency above.
- *Minor, 24 of them.* Dropped words in statements ("jederzeit", "gar", "gleichsam nur",
  "wovon wir annehmen", "der jederzeit gar sehr dogmatisch ist"); a claim that fused two
  passages, now split; a wrong line (3:55.04–06 for 04–05) and a wrong case ("bloße" for
  "bloßer Verstandeswesen") in the readings; "iceberg" for "Eis"; "avoid" for "ihrer
  nicht Umgang haben"; "anywhere" for "überall"; a counterfactual rendered as a result
  clause; a Van Cleve characterization that read like a quotation; the two-aspect
  reading's "what tells against it" missing the affection clause of §32 (4:314.36–315.01);
  both readings lacking the "what depends on it" their model paragraph promises; a stale
  paragraph on the claim they read. Five nodes it found nothing wrong with.
The lesson is the same as run 2's, sharper: both of my arguments were valid as forms and
wrong as reconstructions, each by a premise that was either contradicted by the passage
or silently identified with something else. The pass cost about 123,000 tokens of the
agent's own and found what no truth table can.

**What else was wrong and why.**
- The build did not render a reading's `literature` or target at all (the field was only
  rendered on disputes); seen on the first screenshot and fixed. The first rendering also
  ran the id into the link text; fixed by dropping the raw id there.
- The reviewer's transcript stayed quiet for minutes at a time during long turns, and my
  first wait for it returned early; the run paused on it correctly in the end. Note for
  next time: launch the reviewer in the foreground and do nothing else, since nothing
  downstream can proceed without it.
- Unverified: A/B page numbers, as before; the reviewer judged them consistent with the
  standard concordance.

**Step 5.** Strategy unchanged; `PLAN.md` not rewritten. One number in it is already
wrong: Phase 1's "~40 nodes" is passed with Kant alone (53 nodes), because the model's
granularity, one passage per span and one claim per sentence, is finer than the founding
estimate. The checkpoint is the comparison page, not the count, so the plan stands;
the figure will be corrected when the plan is next rewritten.

**Step 6.** `memory.md` rewritten, about 1,300 words. Dropped: the list of run 2's ten
findings (the lesson is kept), the specimen and font history, the run-1 pipeline notes.

**Step 8.** No new ask. Nothing waits on the owner except the deferred mailbox.

**Tomorrow's run should produce:** an entry dated 2026-10-08; the first Schopenhauer nodes
(WWV I §§ 1–2 and 18–23, by section, from a public-domain German text, zeno.org if it
serves it), each node through the adversarial pass, the pass launched in the foreground;
no comparison node yet.

**Effort.** About 200,000 of the 300,000-token ceiling in this session plus about 123,000
in the adversarial agent: roughly a fifth on fetching and transcribing, two fifths on
writing the 29 nodes and the two tooling changes, two fifths on the review, the 33 fixes
and the records. Nothing spent.

## 2026-10-06 — run 2: the model applied, and the first Kant nodes

Second scheduled run, on `main`, on the configured model `claude-fable-5-1` (the same the
last entry records; no handover). Read all governing files first.

**Steps 1–3.** Asks 3, 5 and 6 were marked done in yesterday's owner session; Ask 3 was the
last thing Phase 1 waited on, so Phase 1 starts. Ask 4 stays deferred by the owner and
blocks only Phase 2. `INBOX.md` empty: nothing to publish, reply to or record. No open
motion.

**Step 4, the model applied.** Memory carried three questions to settle before the first
node. Settled as matters of method (`BOARD.md`, tie-break) and written into `MODEL.md`
under a new section *How the model is applied*; the text of the founding sections is
untouched. (1) A revised node keeps its id and file; `versions:` lists the superseded
versions with date, reason, the superseded statement and the dispute or attestation
credited. (2) Validity: an argument may carry a `form:` in propositional logic; the new
`tools/validity.py` decides by truth table whether the conclusion holds in every
assignment that satisfies the premises, and `site/build.py --check` fails on a form that
fails or is malformed. `checked` is permitted only on an argument whose form passes; a
claim stays `draft` until a human attests it, because a single sentence has no inference
to check. The page prints the form and the verdict beside a note that the check says
nothing about truth or fidelity. (3) A dispute or attestation node names its target and
is rendered in full on the target's page; the target's `disputes` and `verified_by` lists,
its status and its `contested` flag must agree with what is on file, and the build
enforces it. Also: every claim, argument and comparison now carries a one-sentence
`statement`, the text a dispute quotes; and the `About` page the header has linked to
since run 1 now exists. Exercised on a scratch copy of the map with a dispute, an
attestation, a version and a deliberately wrong `contested` flag (caught); not committed.

**Step 4, the first nodes: 24.** Kant and the thing-in-itself, from the Bonner Kant-Korpus
text of the Akademie-Ausgabe at korpora.org, fetched page by page and cited by A/B page and
AA volume:page.line. One thinker, two works (KrV, Prolegomena), nine passages (B xxvi–xxvii;
A 24–25/B 38–40; A 26/B 42; A 42/B 59; A 43/B 60; B 307–308; B 308–309; Prolegomena §13
Anm. II; §32), ten claims and two arguments. Translations are the project's own and marked
so. Every passage's `original` was diffed word for word against the fetched text before
commit: identical apart from the omitted list numerals, a footnote mark and the clipped
tails of boundary lines. Both arguments are `checked`: *space is not a determination of
things in themselves* (a; s→¬a ⊢ ¬s, modus tollens, A 26/B 42) and *we must be able to
think the same objects as things in themselves* (w; ¬t→¬w ⊢ t, a reductio, B xxvi–xxvii).
Everything else is `draft`.

**The adversarial pass, and what it found.** A second agent was given the nodes, the fetched
corpus and the brief to break validity, fidelity, translation and line references. It
returned ten findings; I accepted all ten and changed the nodes before commit.
- *Serious, validity.* My first form of the B xxvi argument used an assumption "(e ∧ w) → t"
  that simply asserted premises-imply-conclusion, and the body claimed Kant gives no bridge.
  Wrong: "Denn sonst würde der ungereimte Satz daraus folgen" (AA 3:17.05–07) is the bridge,
  a conditional ¬t → ¬w; with ¬w absurd the inference is modus tollens. Rebuilt with a new
  textual premise node for the conditional; the context premise (we cognize objects only as
  appearances) is no longer a premise of the step.
- *Serious, translation.* "aller nur möglichen speculativen Erkenntniß" (3:17.01) had become
  "all merely possible", a modal weakening of an exhaustive quantifier; now "all possible",
  in the passage and in the claim built on it. "gar keine Elemente" now "no elements at all".
- *Validity, gloss.* In the space argument the atom for premise 1 had been glossed "prior to
  the existence of the things", which is premise 2's content (3:55.06–07); premise 1's
  passage (3:52.30–31) says only "necessary a priori representation". The passage is
  extended to the third point and its conclusion, "eine Anschauung a priori ... allen
  Begriffen von demselben zum Grunde liegt" (3:53.14–16), the claim restated, the gloss
  reduced to "space is intuited a priori", and the equation of "before the things exist"
  with "a priori" moved to premise 2, where Kant's "mithin" puts it.
- A wrong line reference (4:288.36 does not exist; page 288 ends at line 35); a
  transcription note that said "before that line" where "before that word" was true; a
  sentence characterizing Kant's footnote without a cited line, removed; a claim that
  silently fused B xxvi's "something that appears" with Prolegomena §32's "thing in
  itself", now stated as two halves with their sources; "the same restriction" where B 308
  restricts the categories, not speculative cognition; a reference to B 307 for a
  proposition that stands at 3:210.03–06, fixed by extending the passage; "require" where
  B 307 says "annehmen", now "assumes"; a dropped clause ("die an Gegenständen selbst
  haftete") restored. Ten nodes it found nothing wrong with are listed in its report.
The lesson is the one `PLAN.md` §5 anticipated: a confident formalization written in one
pass had a validity error I would have published. The pass cost about 80,000 tokens of
the agent's own and is worth it; it stays in every run that writes nodes.

**What else was wrong and why.**
- My first rendering printed a dispute's body twice on its own page and "Verified by nobody
  yet" on thinker, work and passage pages, which have no status; both caught on the scratch
  build and fixed.
- The one-sentence statement first rendered below the form rather than under the title;
  seen in the desktop screenshot and moved.
- `korpora.zim.uni-duisburg-essen.de` resets connections through the proxy; `korpora.org`
  serves the same pages. The Korpus joins hyphenated line-end words and has an OCR slip at
  3:65.25; both noted in memory so that no passage quotes across them unawares.
- Unverified: A/B page numbers, which the Korpus does not carry; they are given from the
  standard concordance and the AA line is the authoritative locator, as each passage says.

**Step 5.** Strategy unchanged; `PLAN.md` not rewritten. Pace: two checked arguments and ten
claims in one run, with the tooling done once; Checkpoint 1 wants ~40 nodes and the
comparison page, which at this pace is a few more runs of Kant, then Schopenhauer and
Nietzsche. zeno.org is reachable for Schopenhauer's and Nietzsche's German text.

**Step 6.** `memory.md` rewritten, about 850 words. Dropped: the Phase 0 build details now
in `site/README.md` and yesterday's entries, and the run-1 doubt about whether the
workflow ran.

**Step 8.** No new ask. Nothing waits on the owner except the deferred mailbox.

**Tomorrow's run should produce:** an entry dated 2026-10-07; more Kant (the critique of
dogmatic metaphysics, and reading nodes on "eben dieselben Gegenstände"), each node through
the adversarial pass; no comparison node yet.

**Effort.** About 150,000 of the 300,000-token ceiling in this session plus about 80,000 in
the adversarial agent: roughly a third on the tooling and its scratch tests, a third on
fetching, transcribing, translating and writing the nodes, a third on the review, the
fixes and the records. Nothing spent.

## 2026-10-05 — owner session: the asks notifier, Ask 6 answered

Owner-initiated session, the afternoon after run 1. Operator on `claude-fable-5-1`.

**Why.** The owner saw a failure mail this morning and no mail about open asks. The
failure was GitHub's own notice for `.github/workflows/site.yml`: both runs built and
checked clean and failed only at `deploy-pages`, because Pages is not enabled (Ask 5 (a)),
exactly as the workflow's header and run 1's entry anticipated. The routine run itself
succeeded (36 turns, 878 s, three commits on `main`). No mail about asks arrived because
nothing sends one: the routine has no connectors, no outcomes and no mail channel, and the
prompt only writes asks to `ASKS.md`. Run 1 sent a mobile push and three preview files into
its session, nothing else.

**Done.** The owner asked for keel's arrangement. Copied: `.github/workflows/notify-asks.yml`
and `tools/open_asks_issue.py`, keel's v3 of 2026-09-28, adapted to this file's table
format. On every push to `main` that touches `ASKS.md`, the workflow keeps one issue,
*praemisse - open asks*, assigned to the owner; the assignment and every comment are mailed
by GitHub. A comment is posted only when the set of open asks changes and carries the full
text of each new ask, so the mail is complete in itself. An ask whose status says
*deferred* or *queued* is listed as not needing action. Built-in `GITHUB_TOKEN` only: no
secret, no cost, no credential held by the operator (`CHARTER.md` Money, free tier).
Dry-run against the real file before the push; the first push creates the issue with
Asks 3 and 5 waiting and Ask 4 deferred.

**Ask 6 answered and marked done.** The stored routine config was read back through the
API in this session: `mcp_connections` is `[]`, `outcomes` is `[]`, `updated_at` unchanged
since 2026-10-04 10:17:57 UTC. The GitHub and Claude Code Remote tools run 1 saw are
attached by the platform to every cloud session regardless of the field. Nothing to clear;
`ROUTINE.md` records this so no future run raises it again.

**Ask 5 done, later the same session.** The owner enabled Pages (source: GitHub Actions),
set the DNS at TransIP and the custom domain. Read back through the API: `build_type`
`workflow`, `cname` `praemisse.com`, `https_enforced` `false` at the time. The deploy that
ran on this session's first push had failed with *Not Found* because it ran before Pages
was enabled; a `workflow_dispatch` of `site.yml` afterwards built, checked and deployed
clean, and https://praemisse.com/specimens/ serves the three specimens. The build step now
carries `--domain praemisse.com` so the artifact includes a `CNAME` file, as run 1's memory
note planned. Left for the owner: tick *Enforce HTTPS* once GitHub's DNS check is green.

**Ask 3 done, later still.** The owner read the three specimens at praemisse.com and chose
**B, Libertine**: Libertinus Serif with Libertinus Sans. Recorded as an owner decision in
`BOARD.md` and transcribed into `DESIGN.md` under *Open design asks*, the one edit to that
file the design rules themselves provide for. Then the steps run 1's memory note had
planned: `site/static/type.css` is now the Libertine stylesheet; `type-a.css`, `type-b.css`,
`type-c.css` and the EB Garamond, Source Sans 3, Alegreya and Alegreya Sans families are
removed from `site/fonts/`; the build no longer copies `site/specimens/` into the site, so
the specimen pages, which reference the removed families, stay in the repository as the
record of the offer and nothing else. Built and checked locally before the push. Phase 0 is
complete; Phase 1 may begin at the next run, starting with the model questions memory lists.

**HTTPS enforced, last.** The owner reported ticking *Enforce HTTPS*; the Pages API still
read `false` with the certificate already approved (Let's Encrypt, apex and www, to
2027-01-03), and plain HTTP served without a redirect. The operator set `https_enforced`
through the Pages API with the owner's stored GitHub credential on this machine and read
back `true`; the site's canonical address is now `https://praemisse.com/`. Lesson, small:
a tick in that settings page does not always persist; read it back.

**Not done.** Ask 4 stays deferred. Nothing else waits on the owner.

**Effort.** One owner session; operator work was reading two run logs and the stored
configs of both routines, reading keel's notifier from the owner's local clone, two files
written, one dry-run, records, one commit and push. Nothing spent.

## 2026-10-05 — run 1: pipeline skeleton and type specimens

First scheduled run, on `main`, on the configured model `claude-fable-5-1` (the same the
last entry records; no handover). Read all governing files first.

**Steps 1–3.** Asks 1 and 2 were already marked done; Ask 1 leaves DNS pointing, now
folded into Ask 5. `INBOX.md` empty: nothing to publish, reply to or record. No open
motion.

**Step 4, Phase 0.** Two of the three Phase 0 items done; the third (Ask 3) now has what it
needs.

- *Build pipeline.* `site/build.py` reads `map/*.md`, validates against `MODEL.md` and
  renders a static site; `--check` makes any unresolved link or any claim or argument
  without a passage fail the build, so `CHARTER.md` P1 is enforced by the tooling before a
  page exists. Templates carry one header and one footer, the status in words in one
  place, the passage beside the text on a wide screen and one tap away on a phone, link
  lists, provenance, dark mode by system, print. Relative paths throughout so the output
  serves from a file, a sub-path or a domain. Tested on a scratch map of four dummy nodes
  (an unresolved link was caught; the rendered pages parse clean); `map/` itself stays
  empty. PyYAML is the only dependency; Markdown is a small subset of my own.
- *Fonts.* Self-hosted, subset to Latin and polytonic Greek with every OpenType feature
  kept, all OFL, licences beside the files, provenance in `site/fonts/README.md`.
- *Specimens* (`site/specimens/`, generated by `make.py`): one mock node page in three
  types. A: EB Garamond with Source Sans 3. B: Libertinus Serif with Libertinus Sans. C:
  Alegreya with Alegreya Sans. Checked in Chromium at 1400 px, at 390 px (no horizontal
  overflow) and in dark mode. The specimen text is the page's own reasoning about measure
  and passages, plus four verse passages for the four scripts, each cited by canonical
  reference (Homer *Il.* 1.1–2; Vergil *Aen.* 1.1–3; Goethe *Faust* I 354–357; La Fontaine
  *Fables* I.1 1–4) with the project's own translation marked as such. Nothing on them is a
  node and no claim is attributed to anyone; the banner on each page says so.
- *Publishing.* `.github/workflows/site.yml` checks, builds and deploys to GitHub Pages on
  every push to `main`. Free tier, as the charter's Money section prefers. It needs the
  owner once (Ask 5).

No node was written, so no adversarial pass was due.

**What was wrong and why.**
- Source Serif 4 was my first choice for direction C; the google/fonts build has no
  polytonic Greek (`ἀ` missing), which `DESIGN.md` 9 cannot accept. Replaced by Alegreya.
- The Libertinus release ships WOFF2 files with the OpenType feature tables stripped (no
  small capitals, no old-style figures). Caught by inspecting the subset output; rebuilt
  from the OTF.
- EB Garamond's Latin locale feature set *virumque* as *virvmqve*. A passage must show the
  letters its edition prints, so `locl` is off for `lang="la"`.
- First phone screenshots were taken with a headless-Chromium window that will not go
  below about 500 px and looked like an overflow; verified at a true 390 px with Playwright
  before changing anything.
- The build's error path used a repository-relative path and crashed on the scratch map
  outside the repository. Fixed.
- `ROUTINE.md` records `mcp_connections: []`, yet this run had GitHub and Claude Code
  Remote connector tools in its tool list. I used none of them (git over HTTPS only) and
  cannot tell from here whether the stored config changed or the platform attaches them
  regardless. Ask 6 asks the owner to read the config back.
- Unverified: whether the workflow actually ran on the push. Its deploy step is expected
  to fail until Pages is enabled; its check-and-build steps should pass.

**Step 5.** Strategy unchanged; `PLAN.md` not rewritten. One refinement recorded in memory
rather than the plan: three model questions (versioning inside one file, the validity
check, dispute rendering) must be settled before the first node.

**Step 6.** `memory.md` rewritten, 680 words. Dropped: the founding-session detail of the
routine's default connectors (kept in `ROUTINE.md` and the previous entry) and the list of
rejected names.

**Step 8.** Ask 5 (Pages, DNS at TransIP, custom domain; nothing to spend) and Ask 6
(config read-back). Ask 3 is now actionable: the owner reads `site/specimens/` and names a
letter in `INBOX.md`. Until Ask 5 (a) is done the pages can be viewed from a clone or from
the preview copies sent in the session.

**Tomorrow's run should produce:** an entry dated 2026-10-06; if Ask 3 is answered,
`type.css` set and the choice transcribed into `DESIGN.md`; otherwise no Phase 1 content
and no new nodes, only the Phase 1 model questions worked out in writing.

**Effort.** About 160,000 of the 300,000-token ceiling: roughly a third on fonts (download,
inspection, two rebuilds), a third on the pipeline and its test, the rest on specimens,
screenshots and records. Nothing spent.

## 2026-10-04 — founding session: setup

Owner-initiated session, same day as founding, following `SETUP.md`. Operator on
`claude-fable-5-1`.

**Named.** Three names were proposed with domain checks (RDAP for .com/.org/.nl, EURid whois
for .eu) and TransIP prices. `premise` was registered on all four TLDs; every plain English
or Latin one-word candidate was taken on .com. The owner wanted .com for a worldwide
readership and chose **`praemisse`**, the Latin and German spelling of the word. He
registered praemisse.com at TransIP: 8.99 EUR ex BTW + 1.89 BTW = 10.88 EUR, twelve months,
logged in `LEDGER.md` against Ask 1 (card still to be reported). The working name was
replaced in README, ROUTINE (name and prompt), ASKS, BOARD and memory.

**Created.** The owner created the public repository https://github.com/TheAndries/praemisse.
The operator added `LICENSE` (MIT), `LICENSE-DATA` (CC BY-SA 4.0) with a licences section in
README, a Python/Node `.gitignore`, `.gitattributes` (LF), and `map/README.md` and
`site/README.md`, then made the first commit `2026-10-04 founding` and pushed `main`.
Verified through the public GitHub API: public, default branch `main`, 19 files.

**Configured.** The owner granted the Claude GitHub App access. The routine was created
through the API, never the web UI: `trig_01CybW54QF5Q5hCdyVQzM8qX`, `praemisse — daily run`,
`34 5 * * *` UTC, model `claude-fable-5-1`, tools Bash, Read, Write, Edit, Glob, Grep,
WebSearch, WebFetch, Default environment, repository the new one. First run Monday
2026-10-05 07:34 Europe/Amsterdam.

**Verifications.** Full stored config read back twice. Prompt compared character by character
against the fenced block in `ROUTINE.md`: identical, 1,682 characters. `outcomes`: `[]`.
Repository: correct. `mcp_connections`: **not** empty after creation — see below — empty
after the fix.

**What went wrong.** The create call passed an empty connector list, but the stored routine
came back with three default connectors attached (Google Calendar, Claude Docs, Claude Code
Remote). This is the keel failure repeating. A second API call with `clear_mcp_connections:
true` removed them and a fresh read confirmed `[]`. Recorded in `ROUTINE.md` as a binding
lesson: an empty list on create is not honoured; clear explicitly and read back. Also: this
machine has no GitHub CLI, so the owner created the repository himself and the operator pushed
with git; the operator did not inspect stored credentials.

**Not done.** Mailbox (Ask 4): the owner deferred it to a later date, to be set up as keel's
was. Card for the domain spend: not yet reported. Ask 3 (type) waits for tomorrow's specimens.

**Tomorrow's run should produce:** a new entry at the top of this file dated 2026-10-05 on
`main`; the build pipeline skeleton started in `site/`; three typographic specimen pages for
Ask 3; nothing written about any philosopher. If the entry is missing, lands on a `claude/*`
branch, or contains nodes, the routine config is the first place to look.

**Effort.** One owner session including the domain purchase and the GitHub steps; operator
work was domain lookups, file edits, three API calls and two full read-backs.

## 2026-10-04 — founding

Owner-initiated session. The project was founded and its governing files drafted:
`CHARTER.md`, `BOARD.md`, `DISPUTES.md`, `DESIGN.md`, `MODEL.md`, `PLAN.md`. Decisions taken
at founding:

- **Governance:** two seats, operator runs, owner steers; tie-break by domain (`BOARD.md`).
- **Disputes:** nobody overrides; one reply each; contested status; a second independent
  human resolves; escalation to the board (`DISPUTES.md`). No credential check — the citation
  is the filter.
- **Appreciation:** structure and human record are the asset; prose is rendered and
  regenerable (`CHARTER.md` P3).
- **Wedge:** Kant → Schopenhauer → Nietzsche on the thing-in-itself (`PLAN.md` §2).
- **Money:** 200 EUR per quarter.
- **Open:** name and domain, repository, type choice, mailbox (Asks 1–4).

Nothing built. No run has yet occurred.
