# INBOX.md

Owner notes (`BOARD.md`), mail, and filed disputes and attestations (`DISPUTES.md`). The
owner pastes verbatim, with the date and source; a filing made through the forms on the
node pages is appended here verbatim by `.github/workflows/inbox.yml`, with its issue
number (`MODEL.md`, *Filing*). The operator handles every entry in its next run, records
the source, and moves it to `CHANGELOG.md` with what was done.

## 2026-10-11 — owner note: design brief for the operator

Source: the owner's document *praemisse design brief for the operator.md*, given to the
operator at the start of an owner-initiated session on 2026-10-11, with two static HTML
mockups beside it (`praemisse-mockup-a.html`, the edition; `praemisse-mockup-b.html`, the
apparatus), kept as the record in `site/specimens/mockup-a.html` and `mockup-b.html`. The
note carries an owner decision, the choice of direction A, logged in `BOARD.md` the same
day. Handled in the same session on branch `design`; the changelog entry of that session
records what was done with it. Verbatim:

---

# praemisse design brief for the operator

Oct 11, 2026 · @Andries

## Read this first

You are giving praemisse.com its colour, spacing, page grammar and menu, in this owner-initiated session, on a branch, under `DESIGN.md` as it stands. The type is already decided (Libertinus Serif and Sans, owner decision of 2026-10-05) and the ten principles already bind; this work adds the layer that was never decided and leaves everything else alone. The result is seven page templates built from `map/` by the existing build, one token file, and a board decision that records the owner's choice of direction A, the edition.

**How this sits under the board.** praemisse is a two-seat board. This brief is the owner's steer, filed as an owner note in `INBOX.md` at the start of the session. What it asks for is an *amendment* to `DESIGN.md`: a palette, a spacing scale, a page grammar and a menu, added under a new heading "Colour, space and pages", with the date and the decision reference in `BOARD.md`. The amendment is made at the end, after the owner has approved the comparison specimen; until then nothing in `DESIGN.md` changes.

**Off limits.** `map/` and everything in it; the data model in `MODEL.md`; the status vocabulary and how status is computed; the dispute protocol; the type choice and the fonts under `site/fonts/`; any prose that is rendered from the map; the build's inputs. Nothing from the "Not permitted" list in `DESIGN.md` is permitted here either: no cards, no hero, no sidebar, no icons where a word will do, no decorative illustration of philosophers, no reading-time badges, no engagement metrics shown to readers. If a design idea needs any of these, it is the wrong idea.

**What is not off limits.** The templates under `site/`, the stylesheets under `site/static/`, the build's output structure, the front page's content order, where the counts live, and the index pages' layout.

**Branch and files.** Branch `design`. Tokens in `site/static/tokens.css`; `type.css` stays as it is and is imported by `tokens.css`, not replaced. Page and component styles in `site/static/site.css`. Specimens under `site/specimens/`, which already holds the three type specimens from October; add to it, never delete from it. Small commits, messages written for a reader.

**References.** Two static HTML mockups of the front page, `praemisse-mockup-a.html` (the edition) and `praemisse-mockup-b.html` (the apparatus), next to this brief. A is the chosen direction; B is kept only as the reference for its grid treatment, should the owner ask for it after seeing the specimen. They are sketches of colour, proportion and order, not templates: they are set in a stand-in serif because the mockup tool could not load Libertinus, so take their tokens and their structure, set everything in Libertinus, write the production markup yourself, and where a mockup and this brief differ, this brief wins; where this brief and `DESIGN.md` differ, `DESIGN.md` wins.

## What this amendment adds, and what it leaves alone

Every principle in `DESIGN.md` is honoured as written; the table says how, so you can check each page against it.

| Principle | What it already fixes | What this brief adds |
| --- | --- | --- |
| 1 Passage beside the claim | Side by side on wide screens, one tap away on a phone | The passage pair component and the two-column node layout with its breakpoint |
| 2 One node, one page, one address | No tabs, modals, accordions | The seven templates and the URL scheme stay; the index pages get a contents-list layout |
| 3 Typography does the work | Serif body, sans labels, 60–75 ch, four sizes at most | The four sizes as tokens, the measure at 66ch, leading, old-style figures, small caps for status |
| 4 Status visible and plain | Words, one place, never colour alone | The status word component, its fixed place on every template; *contested* gets the one warning colour beside the word |
| 5 Comparison pages are the showpiece | The most design care | The comparison grid, built and shown first as the specimen the owner chooses from |
| 6 Graph is navigation | Lists of links on every node | The dependency lists component, same place on every node |
| 7 Quiet chrome | One header, one footer, no sidebar, no hero, no cards | The running head, the menu of five words, the colophon footer; nothing else |
| 8 Fast and plain | Static, under a second, fonts self-hosted | A weight budget and a verification step; no new scripts |
| 9 Original language visible | Script beside translation | The passage pair always shows both, original first |
| 10 Looks older than it is | 1996 and 2036 | Paper, ink, one accent, rules; no shadows, no rounded panels, no gradients |

Left alone on purpose: the fonts and `type.css`; the dark-mode rule (follows the system; the palette below gives it values); the counts, which are kept but moved from the front page to the colophon; the words draft, checked, attested, established, contested.

One thing the brief changes that a reader will notice: the front page stops being a dashboard. The nine counters leave the top of the page and become one line in the colophon. The comparison becomes the first thing on the page. If the board wants the counters kept at the top, that is a board decision; the brief recommends against it, since three thinkers and zero disputes advertise emptiness rather than a map.

## The direction, and the checkpoint

The owner chose direction A, the edition, on 2026-10-11, from the two mockups. Record it in `BOARD.md` as an owner decision at the start of the session. What he has not yet seen is A set in Libertinus on the real comparison page, so the checkpoint remains: build that one specimen first and stop.

**A, The edition.** Warm paper, oxblood accent, a centred running head with the wordmark in letterspaced small caps and the menu beneath it, a hairline rule. The reference is a critical edition: apparatus in the margin, a preface on the front page, quieter and warmer. The comparison grid has its column rules in the hairline colour and the thinkers' names in the serif.

**B, The apparatus.** Cool grey-white paper, slate-blue accent, a left-aligned running head with the menu at the right and a firm 2px rule. The reference is a reference work: a stronger grid, the thinkers' names in bold sans, column rules darker, the comparison grid and the dependency lists carrying the page. Better on screen; firmer.

**B is not built.** Its description stays above and its mockup stays beside this brief for one reason: the grid's rules, name weight and column spacing are their own tokens (`--grid-rule`, `--grid-name-weight`, `--grid-name-family`, `--grid-gap`), so if the owner looks at the specimen and asks for B's firmer grid on A's page, that is a token swap you can do in the same hour, not a rebuild.

**The specimen.** One file, `site/specimens/comparison-a.html`, rendering the real `/x/thing-in-itself/` comparison from the map with the real passages, status words and qualification line, in Libertinus, at 1280px and at phone width, light and dark. Published on the branch preview if there is one, else screenshots committed beside it. Then the ask: "Comparison specimen at \[address\]: yes, or what to change?" Nothing else is built until it is answered. On the yes, the amendment moves into `DESIGN.md` under "Colour, space and pages" with the date and the decision line.

## The design system

One file, `site/static/tokens.css`, imports `type.css` and holds every colour, size and spacing as a custom property. No template or stylesheet contains a hex value or a pixel size that is not a token. Four type sizes, as principle 3 requires; if a fifth seems needed, the layout is wrong, not the rule.

```css
/* praemisse — colour, space and pages. Direction A, the edition: owner decision 2026-10-11.
   Type is in type.css (owner decision 2026-10-05). */
@import url("type.css");

:root {
  /* type scale: four sizes, no more (DESIGN.md P3) */
  --size-1: 2.5rem;      /* page title, line-height 1.15 */
  --size-2: 1.6rem;      /* claim on a node page, comparison cell lead, 1.3 */
  --size-3: var(--body-size);  /* body, from type.css, with --body-leading */
  --size-4: 0.9rem;      /* labels, status, apparatus, colophon, 1.5 */

  --measure: 66ch;
  --page: 1120px;        /* comparison grid and node page; reading pages use --measure */
  --gutter: 2rem;        /* 1.25rem under 640px */
  --s-1: 0.5rem; --s-2: 1rem; --s-3: 1.5rem; --s-4: 2.5rem; --s-5: 3.5rem; --s-6: 5rem;

  /* paper and ink */
  --paper: #F5EFE3; --ink: #1F1B16; --ink-2: #4A4238; --muted: #6B6257;
  --rule: #D8CDBB; --rule-strong: #1F1B16;
  --accent: #7A2E2B;          /* links, running-head mark */
  --contested: #7A2E2B;       /* the one warning colour; always beside the word */
  --head-align: center;
  --head-rule: 1px solid var(--rule);

  /* the grid's own levers, kept separate so a firmer grid is a swap, not a rebuild */
  --grid-rule: var(--rule);
  --grid-name-weight: 400;
  --grid-name-family: var(--serif);
  --grid-gap: 1.25rem;
}
@media (prefers-color-scheme: dark) { :root {
  --paper: #1B1813; --ink: #EAE2D3; --ink-2: #C9BFAE; --muted: #9A9083;
  --rule: #3A342B; --rule-strong: #EAE2D3; --accent: #D08A86; --contested: #D08A86;
}}

/* If the owner asks for B's grid on A's page, this block and nothing else:
   --grid-rule: var(--ink); --grid-name-weight: 700; --grid-name-family: var(--sans); --grid-gap: 1.5rem; */
```

Rules for using them:

- **`data-palette` is set on `<html>` by the build** from one value in the site config. Only palette A exists, and the attribute stays, so a future palette change is one block and one value.
- **One accent, one warning, and they may be the same colour.** The accent carries links and the wordmark's small-caps rule; the warning carries only the word *contested* and the mark beside a contested node in lists. Nothing else on the site is coloured. If A and B both end up with the same hue for both, that is fine: the word does the work, as principle 4 requires.
- **Figures:** old-style (`font-variant-numeric: oldstyle-nums`) in running text and the colophon; lining and tabular only inside the comparison grid's reference line.
- **Small caps** (`font-variant: small-caps`, real ones from Libertinus, never synthesised) for status words and the wordmark only, letterspaced 0.06–0.08em.
- **Rules, not boxes.** A section is separated by a hairline in `--rule`; the running head and the colophon by `--rule-strong`. No borders around content, no fills behind text, no rounded corners, no shadows.
- **Italic is a tool, not a style:** original-language passages, work titles, the qualification line. Never for emphasis in rendered prose.
- **Dark mode** follows the system; same layout, the pairs above verified at 4.5:1 for body and 3:1 for the status small caps at `--size-4`, ratios recorded in `DESIGN.md`.
- **Nothing is animated.** No transitions, no hover motion; a link underlines on hover and that is all.

## Components

Eleven components build every page. Each is one block of markup produced by the build and one block of classes in `site.css`. Build them once in `site/specimens/components.html`, showing each light and dark.

**Running head.** The one header. Wordmark "praemisse" in the serif, small caps, letterspaced, `--size-2`; beneath it (A) or beside it at the left (B) the one-line description "a map of the arguments of philosophy" in `--size-4` sans `--muted`. The menu follows. A `--rule` hairline under it in A, a 2px `--rule-strong` in B (`--head-rule` token). It does not stick; a reader scrolls back.

**Menu.** Five words in the sans, `--size-4`, letterspaced 0.04em: Thinkers · Works · Comparisons · Disputes · About. Centred under the wordmark (A) or at the right of the running head (B); `--head-align` drives both. The current section is marked by a hairline underline in `--accent`, never by weight alone. On a phone the five words fit on one line at 390px; verify, and if not, reduce the letterspacing, never hide a word.

**Section label.** A `--size-4` sans label in `--muted`, uppercase, letterspaced 0.14em, above a group: Comparisons, Start here, Thinkers, Depends on. It is the only uppercase text on the site.

**Contents list.** The layout of every index: a list with no bullets, each entry a hairline above, the name at the left in the serif and a `--size-4` sans note at the right (dates, a count, a status word). The last entry has a hairline below. No columns, no cards, no thumbnails.

**Status word.** The word in sans small caps, letterspaced, `--size-4`, in `--ink`; *contested* in `--contested`. On a node it sits in the apparatus note; in a list it sits in the right-hand note; in the running head of a comparison it sits in the section label line. Always a word; a colour is never the only carrier.

**Apparatus note.** The margin: `--size-4`, sans for labels and serif italic for text, `--ink-2`. On a wide screen a right column of `minmax(0, 2fr)` beside a `minmax(0, 3fr)` text column; under 720px it moves beneath the text, indented by `--s-3`, with a hairline above, in the same type, so it still reads as apparatus. Holds the status word, the source reference, the passage link and, on a comparison, the qualification.

**Passage pair.** The original first, in its script, in serif italic; the translation beneath in serif roman, `--ink-2`; the reference line in `--size-4` sans. Greek, Latin, German and French are shown as text with `lang` set; never transliterated. On a node page it is the apparatus column; on a passage page it is the page.

**Comparison grid.** One column per thinker, `grid-template-columns: repeat(N, minmax(0, 1fr))`, `--grid-gap`. Header row: the thinker's name in `--grid-name-family` at `--grid-name-weight`, dates in `--muted` after it, a `--rule-strong` above and a `--grid-rule` below. Each cell: the statement at `--size-2` serif, the passage's key term in italic, then the reference and the status word in `--size-4` sans. Column rules in `--grid-rule`. More than three thinkers: the grid scrolls sideways inside its own box on narrow screens, with the first column sticky. Under 720px the grid is rebuilt by CSS as a stack ordered by question, each thinker's cell under a repeated name in `--size-4`, so the three answers to one question stay together.

**Dependency lists.** Four section labels on every node: Depends on, Supports, Attacked by, Replies to, each followed by a contents list of the linked nodes with their status word at the right. An empty relation is omitted, not shown as "none". They sit under the claim and the apparatus, full width, in that order.

**Dispute exchange.** The contested node quoted at the top with its passage pair; then each turn as a dated, signed block: the name and date in `--size-4` sans, the text in serif at `--size-3`, a hairline between turns, no indentation and no bubbles. The model's single reply is marked "the map replies" in the same way as a human turn. The status line says *contested* until the protocol says otherwise.

**Colophon.** The one footer, above a `--rule-strong`. Two lines in `--size-4` sans `--muted`: the counts ("The map today · 3 thinkers · 5 works · 48 passages · …" with old-style figures, each count a link to its index) and the licence line ("data CC BY-SA 4.0 · code MIT · no account, no advertising, no cookies, no tracking beyond a page count · source"). Same on every page; the counts are regenerated by the build.

## Template by template

Seven templates and the index pages. Every page: running head, the template's body, colophon. Nothing else. Prose that is rendered from the map is not rewritten here; only its order and its setting change.

**1. Front page (`/`).** Reading width (`--measure`), centred.

1. Title: "A map of the arguments of philosophy" at `--size-1`, regular weight. Under it the one-paragraph description from today's page, set as a lead in serif italic `--ink-2`.
2. The status paragraph (draft, checked, attested, established, contested) as today, with the five words set as status words inline.
3. Section label *Comparisons*, then each comparison as an entry: title at `--size-2`, the thinkers in italic, one line of description, a `--size-4` line with the status word and its qualification. A `--rule-strong` above the first and a hairline between entries. With one comparison this is one entry; the layout must look right at one, three and twenty.
4. Section label *Start here*, then a numbered list of up to three nodes with a one-line note each. The nodes are chosen by the operator and listed in the site config (a `start_here` list of node ids); if the list is empty, the section is omitted.
5. Section label *Thinkers*, then a contents list: name, dates at the right.
6. Section label *To dispute a node*, then two sentences from `DISPUTES.md` and a link to the protocol.

The nine counts leave this page for the colophon.

**2. Comparison (`/x/<slug>/`).** Page width `--page`. Section label line: "Comparison · \<status word>, \<qualification if any>". Title at `--size-1`. The question as a lead in italic. The comparison grid. Beneath it, for each row of the grid, the full passage pairs in a two-column node layout so that a reader can go from the cell to the text without leaving the page; each pair anchored (`#kant-1`) and linked from its cell. Then the dependency lists for the comparison as a whole, if the model has them. This template gets the most care and is built first.

**3. Node: claim or argument (`/c/<id>/`, `/a/<id>/`).** Page width `--page`, two columns on wide screens: text column with the section label (Claim or Argument, and for an argument its premises, inference and conclusion as a numbered list), the claim at `--size-2`, and the rendered prose at `--size-3`; apparatus column with the status word, the source (work, section, line), the passage pair for the passage the node is tied to, and a link to the passage page. Under both columns, full width: the dependency lists. On a phone the apparatus follows the claim, before the prose, and returns to the same spot via the anchor, as principle 1 requires.

**4. Thinker (`/t/<slug>/`) and Work (`/w/<slug>/`).** Reading width. Title, dates (thinker) or thinker and year (work), one paragraph if the map has one, then contents lists under section labels: Works, Comparisons, Arguments, Claims, with a status word or a count at the right of each entry. No portrait, no illustration.

**5. Passage (`/p/<id>/`).** Reading width. Section label "Passage · \<work> · \<reference>", then the passage pair at `--size-3` with the original given room, then a contents list of the nodes tied to this passage.

**6. Dispute (`/d/<id>/`).** Reading width. Section label "Dispute · \<status word>", the contested node quoted with its passage pair, then the dispute exchange. The attestation record, if any, as the last block in the same form.

**7. About (`/about/`) and the colophon.** Reading width. The project's description, the status vocabulary explained once in full, the licences, the board and how to reach it, how to dispute, the source. The counts live in the colophon on every page, so About does not repeat them.

**Index pages (`/t/`, `/w/`, `/p/`, `/c/`, `/a/`, `/r/`, `/x/`, `/d/`, `/v/`).** Title ("Claims", with the count after it in `--muted`), one line on what the list is, then one contents list, sorted as the build sorts them today, each entry with its status word at the right. The five indexes not in the menu are reached from the colophon counts and from each other through a `--size-4` line under the title: "Thinkers · Works · Passages · Claims · Arguments · Readings · Comparisons · Disputes · Attestations". An empty index says in one sentence that nothing is here yet; it does not show a zero in large type.

## Phone, print, performance and accessibility

The reader is in a chair with time, or on a phone in bed. Both get the same text in the same order; only the columns move.

- **Breakpoints:** one, at 720px. Above it, the two-column node and comparison layouts; below it, one column, the apparatus beneath the claim, the grid stacked by question, `--gutter` at 1.25rem, `--size-1` at 2rem. Test at 390px, 768px and 1280px.
- **Body text never below 17px on a phone** and never below `--body-size` on a desktop; the four sizes scale together, not separately.
- **No horizontal scroll of the page** at any width. The only thing that scrolls sideways is a comparison grid with more than three thinkers, inside its own box.
- **JavaScript off:** every page complete and readable. The site has no scripts on the reading path today and gains none. The phone "one tap away" for the passage is an anchor link, not a script.
- **Weight:** a node page under 120 KB transferred including fonts on first visit; the fonts are cached, so a second page is under 30 KB. Verify with the browser's network panel and record it.
- **Speed:** first render under one second on a throttled 3G profile for a node page. Static files, no render-blocking stylesheet beyond `tokens.css` and `site.css`, fonts with `font-display: swap`.
- **Keyboard:** reading order is tab order; links are distinguishable by underline, not colour alone; focus is a 2px `--ink` outline offset 2px; a skip link to the main text is the first focusable element.
- **Contrast:** every pair, light and dark, at 4.5:1 for body and 3:1 for small caps at `--size-4` and for the accent underline. Measured, not eyeballed; ratios in `DESIGN.md`.
- **Language:** `lang="en"` on the page; `lang` set on every original-language passage (`el`, `la`, `de`, `fr`) so screen readers and hyphenation behave; `hyphens: auto` on body text, `hyphens: manual` on passages.
- **Headings:** one `h1`, section labels are `h2` even though they are small; nothing skips a level. The comparison grid is a `table` with `th` cells for the thinkers, so a screen reader reads it as a table; the stacked phone layout is the same table restyled.
- **Print:** `@media print` removes the menu and colophon counts, keeps the wordmark and the licence line, sets black on white, keeps the two-column layout on A4 landscape for a comparison and goes to one column otherwise, and prints the URL of each linked node after it in `--size-4`. A printed node page should look like a page from an edition.
- **Dark mode** follows the system and nothing else; no toggle.

## How to work

Comparison specimens first, the owner's choice second, the rest third. Nothing merges to `main` and nothing changes in `DESIGN.md` until the owner has chosen in a browser.

1. **Read before writing.** The whole of `site/`, the build, `DESIGN.md`, `MODEL.md`, `BOARD.md`, the October type specimens, and the two mockups. File this brief as an owner note in `INBOX.md`, dated, and log the owner's choice of direction A in `BOARD.md`. Write the first draft of the "Colour, space and pages" section as a separate file `site/DESIGN-amendment.md` (not yet in `DESIGN.md`) holding the token table, the component list and the template list. Commit.
2. **Tokens and components.** `tokens.css`, `site.css`, and `site/specimens/components.html` showing every component light and dark, 390px and 1280px, set in Libertinus from `site/fonts/`. Commit.
3. **Specimen checkpoint.** Build the comparison template and render `/x/thing-in-itself/` from the real map into `site/specimens/comparison-a.html`. Publish the branch to a preview if the host builds non-production branches; otherwise commit screenshots at 390px and 1280px, light and dark, beside it. File a non-blocking ask: "Comparison specimen at \[address\]: yes, or what to change?" Stop. Do not build the other templates until it is answered.
4. **Record the approval.** On the yes: apply any token change he asked for in `tokens.css` only, move `site/DESIGN-amendment.md` into `DESIGN.md` under "Colour, space and pages" with the date and the owner's decision line, and log it in `BOARD.md`. One commit, named for the decision.
5. **The other templates,** in this order: node (claim and argument), front page, thinker and work, passage, the index pages, dispute, about. One commit per template. Rebuild the whole site after each and check that no page's URL changed.
6. **Verification,** all of it, before the merge ask:
   - Screenshots of one page per template at 390px and 1280px, light and dark, under `site/specimens/`.
   - Weight and speed numbers for a node page and the comparison page, from the network panel and a throttled run, in `DESIGN.md`.
   - Contrast ratios for every pair in the chosen palette, in `DESIGN.md`.
   - Every URL that existed before the branch still answers 200; the list and the result in `DESIGN.md`.
   - A keyboard-only pass through the front page, a node and the comparison; a screen-reader pass through the comparison grid and one passage pair; each described in three lines in `DESIGN.md`.
   - A print of a node page and of the comparison to PDF, committed under `site/specimens/`.
   - A check against the "Not permitted" list in `DESIGN.md`, item by item, written as a line each: "carousels: none".
7. **Merge ask.** File a blocking ask: "Design branch complete; verification in `DESIGN.md`; merge?" Merge only on a yes. Then the routine inherits the templates and `DESIGN.md` binds.

**Done means:** seven templates and the index pages built by the existing build, one palette in `tokens.css` and no hex outside it, four type sizes, no scripts on the reading path, the counts in the colophon and not on the front page, every principle in the table above checkable on a page, the owner's choice recorded in `DESIGN.md` and `BOARD.md`, verification numbers written down, the owner's yes recorded.

**Scope discipline.** You will want to improve rendered prose, the status rules, the data model and the dispute protocol while you are in the templates. Do not. Write each as a note in `INBOX.md` or a line in `PLAN.md` for a scheduled run. The only copy you write here is copy this brief gives you; everything else is rendered from the map or copied from the governing files.

## What to ask the owner, and how

Two asks, through `ASKS.md`, each one question answerable in a minute. The owner has said he cares how this site looks and has taste; the asks are where that taste enters, so make the specimens worth looking at and keep everything else to yourself.

| When | Ask | Blocking? |
| --- | --- | --- |
| After step 3 | Comparison specimen at \[address\]: yes, or what to change? | Yes, for everything after the comparison template |
| After step 6 | Design branch complete; verification in `DESIGN.md`. Merge? | Yes |

Decide everything else yourself from this brief and `DESIGN.md`, and record each decision in `site/DESIGN-amendment.md` (later `DESIGN.md`) with one line of reasoning. Things you do not ask about: pixel values, spacing, the exact sort of an index, which three nodes go under *Start here* (choose them and list them; the owner can change the list), how the grid stacks on a phone, the wording of a section label. Things you do not decide: anything that changes a principle in `DESIGN.md`, a URL, the type, the status vocabulary, or the counts' return to the front page; these go to the board as a note, and the current state stays until the board decides.

If the owner answers the first ask with a change to a colour or a spacing, make it in `tokens.css` only and do not reopen the direction. If he asks for a different direction, stop and file a note in `INBOX.md` saying what it would take; do not build it without a decision line in `BOARD.md`.

---

## 2026-10-19 — owner note: the design brief filed, the four reservations accepted

Source: the owner's message at the start of an owner-initiated session on 2026-10-19 (the
operator on `claude-fable-5-1`), handled in the same session on branch `design`; the
changelog entry of that session records what was done with each instruction. The note the
owner asked to be filed, verbatim:

> Design brief filed as DESIGN-BRIEF-2026-10-11.md; direction A (the edition) chosen by the owner on 2026-10-11; the operator's four reservations in the 2026-10-12 changelog entry are accepted.

The same message answered the operator's question of 2026-10-12 (`CHANGELOG.md`, run 8;
Ask 8), note or motion, with *both*: the seven templates the brief describes are built
inside `DESIGN.md` as it stands, on the note; a palette, a spacing scale, a page grammar
and a menu added to `DESIGN.md` are a board matter, tabled as the motion *Colour, space and
pages* in `BOARD.md` at the specimen checkpoint, with the comparison specimen as its
exhibit, on which the owner votes when he answers the ask; until it passes `DESIGN.md` does
not change. The four accepted reservations are written into `site/DESIGN-amendment.md` in
the owner's words. The first stop remains the comparison specimen in Libertinus, filed as a
non-blocking ask with the motion beside it (Ask 11); nothing else is built until the owner
answers.

## 2026-10-19 — owner note: the specimen approved, "Yes to all"

Source: the owner, in the same owner session, after reading the comparison specimen and
its screenshots at 1280 and 390, light and dark. Asked the five questions of Ask 11 (the
look as a whole; A's hairline grid or B's firmer one; the first statement of a cell at the
claim size; the counts into the colophon; dark mode as shown), he answered: "Yes to all!"
He also said that the look of the site is his to decide, as aesthetics, and not a matter
for the board, which is for the direction of the project; and that the design should go on
without stopping again until the merge ask. Handled in the same session: the amendment moved
into `DESIGN.md`, the decision in `BOARD.md`, Ask 11 done, the remaining templates built.

## 2026-10-19 — owner note: Ask 12 answered (merge), and two notes for the next run

Source: the owner, in the same owner session, after reading the review of every template.
Ask 12: **merge.** Handled in the same session: `design` merged into `main`.

Two owner notes for the next scheduled run, not for the merge, in the owner's words:

> On the front page the lead starts at "broken into explicit premises", dropping the repeated title words.

> Subset the three Libertinus faces to the characters the map actually uses, target under 180 KB on first visit, as a separate decision with a before-and-after number.

Not handled in this session. The first is a copy change to `site/templates/index.html` (the
lead); the second touches `site/fonts/`, which the design brief put off limits to the design
work, and is to be taken as its own decision with the weight measured before and after
(`DESIGN.md`, *Verification*, gives the before: 357 KB for the three faces, 116 + 136 + 105).
