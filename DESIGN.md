# DESIGN.md

**Status: binding under `CHARTER.md` P7. Amendable only by board decision.**

The site is a place to read. Everything below follows from that.

## Principles

1. **The passage is always beside the claim.** On a wide screen the node's text and its
   source passage sit side by side; on a phone the passage is one tap away and returns to
   the same spot. The reader never has to trust the map without the text in view.
2. **One node, one page, one permanent address.** Nothing is hidden in a tab, a modal or an
   accordion. Pages are linkable, printable and readable with JavaScript off.
3. **Typography does the work.** A text serif with real italics for body and passages, a
   restrained sans for labels and status, generous measure (60–75 characters), generous
   leading, a hierarchy of at most four sizes. No icons where a word will do.
4. **The status is visible and plain.** Draft, checked, attested, established, contested —
   as words, in one consistent place on every node, never as a colour alone.
5. **Comparison pages are the showpiece.** A page that sets Kant, Schopenhauer and
   Nietzsche side by side on the thing-in-itself is the thing a reader cannot get anywhere
   else; it gets the most design care.
6. **The graph is navigation, not decoration.** "Depends on", "Supports", "Attacked by",
   "Replies to" are lists of links on every node. A visual graph, if built, is a secondary
   view and never the landing page.
7. **Quiet chrome.** One header, one footer, no sidebar, no hero, no cards, no cookie banner
   (no cookies), no newsletter interrupt, no "share" buttons. Dark mode follows the system.
8. **Fast and plain.** Static files. Loads in under a second on a weak connection. No
   frameworks on the reading path. Fonts self-hosted, with system fallbacks.
9. **Original language visible.** Greek, Latin, German, French shown in their script
   beside the translation, never only as a transliteration.
10. **It should look older than it is.** The reference points are a well-set scholarly
    edition and the better university presses, not a startup. The site should look like
    it could have existed in 1996 and still look right in 2036.

## Not permitted

Ads of any kind. Pop-ups. Infinite scroll. Autoplay. Carousels. Skeleton loaders. "You may
also like." Reading-time badges. Engagement metrics shown to readers. Stock imagery.
Decorative illustration of philosophers.

## Open design asks

The owner cares about the look and has taste. Before the first page is built, the operator
shows him three typographic directions (a specimen page each, no content) and he chooses.
That choice is recorded here and becomes binding.

**Chosen, 2026-10-05, by the owner (owner decision, `BOARD.md`): direction B, Libertine.**
Libertinus Serif for text and Libertinus Sans for labels, both self-hosted under the OFL,
at the size and leading set in `site/static/type.css`. The three specimens remain in
`site/specimens/` as the record of what was offered; they are no longer published. The
unused families were removed from `site/fonts/`.

## Colour, space and pages

**Binding, owner decision of 2026-10-19 (`BOARD.md`), after the owner approved the comparison
specimen set in Libertinus (`site/specimens/comparison-a.html`, Ask 11; the design brief of
2026-10-11, `DESIGN-BRIEF-2026-10-11.md`).** Written on branch `design` under the ten
principles as they stand; the type (2026-10-05) is unchanged. Every decision the operator took
on its own is listed under *Decisions*, each with its one line of reasoning. The four
reservations of 2026-10-12 are accepted by the owner and bind.

### The direction

Direction A, *the edition*, chosen by the owner on 2026-10-11 from two mockups (`BOARD.md`;
the mockups are kept as `site/specimens/mockup-a.html` and `mockup-b.html`). Warm paper, ink,
one oxblood accent, hairline rules; a centred running head with the wordmark in letterspaced
small caps and the menu beneath it; the comparison grid with its column rules in the hairline
colour and the thinkers' names in the serif. The reference is a critical edition: text,
apparatus in the margin, the sources in full. Direction B, *the apparatus*, is not built; its
grid survives as four tokens so that a firmer grid is a swap, not a rebuild.

### The operator's four reservations, accepted

Run 8 (`CHANGELOG.md`, 2026-10-12) named four things in the mockups the operator would not
carry over as they stood. The owner accepted all four on 2026-10-19 (`INBOX.md`), in these
words, which bind this work:

1. Mockup copy is illustrative and no rendered prose is rewritten, so the word "behind"
   does not travel.
2. Status words come from `MODEL.md` and the map, so no claim shows checked.
3. The status explanation on the front page is the map's own text, including the
   comparison sense of checked.
4. Fonts are Libertinus from `site/fonts/`, never Google.

### Tokens

One file, `site/static/tokens.css`, imports `type.css` (the type, owner decision 2026-10-05)
and holds every colour, size and spacing as a custom property. No template or stylesheet
carries a hex value or a pixel size that is not a token. `data-palette` is set on `<html>` by
the build from `site/site.yaml`; only palette `a` exists.

| Token | Light | Dark | Used for |
|-------|-------|------|----------|
| `--size-3` | `clamp(var(--body-size), 0.8125rem + 0.47vw, 1.4rem)`: 19px on a phone and at 1280, 22px at 1920 and above; `--body-leading` (1.45) | | body, passages, statements; the front page's lead (since 2026-10-19) |
| `--size-1` | `--size-3` × 2.105 (× 1.684 under 720px): 40px at 1280, 46px at 1920, 32px on a phone; leading 1.15 | | the page title |
| `--size-2` | `--size-3` × 1.347: 25.6px at 1280, 29.7px at 1920; leading 1.3 | | the claim on a node page, the lead statement of a comparison cell, the wordmark |
| `--size-4` | `--size-3` × 0.758: 14.4px at 1280, 16.7px at 1920; leading 1.5 | | labels, status words, apparatus, references, menu, colophon |
| `--measure` | 60ch (66ch until 2026-10-19): 530px at 1280, 614px at 1920, lines of 62–69 characters | | reading pages and the text column |
| `--page` | 1120px | | the comparison grid and the two-column node layout |
| `--gutter` | 2rem (1.25rem under 640px) | | the page's side gutter |
| `--s-1` … `--s-6` | 0.5, 1, 1.5, 2.5, 3.5, 5rem | | every vertical space |
| `--paper` | `#F5EFE3` | `#1B1813` | the page |
| `--ink` | `#1F1B16` | `#EAE2D3` | text, status words, the strong rule |
| `--ink-2` | `#4A4238` | `#C9BFAE` | leads, translations, apparatus text |
| `--muted` | `#6B6257` | `#9A9083` | labels, dates, colophon |
| `--rule` | `#D8CDBB` | `#3A342B` | hairlines between sections and entries |
| `--rule-strong` | `--ink` | `--ink` | under the running head, above the colophon, above a grid |
| `--accent` | `#7A2E2B` | `#D08A86` | links in running text, the current menu word's underline |
| `--contested` | `#7A2E2B` | `#D08A86` | the word *contested*, and only that word |
| `--head-align`, `--head-rule` | center, 1px `--rule` | | the running head (B would be left, 2px `--rule-strong`) |
| `--grid-rule`, `--grid-name-weight`, `--grid-name-family`, `--grid-gap` | `--rule`, 400, `--serif`, 1.25rem | | the comparison grid; B's values are in a comment in the file |

Contrast ratios, measured (WCAG 2 relative luminance, computed from the hex values above on
2026-10-11), all above 4.5:1 for text and 3:1 for the small caps and the accent underline:

| Pair | Light | Dark |
|------|-------|------|
| `--ink` on `--paper` | 14.95:1 | 13.75:1 |
| `--ink-2` on `--paper` | 8.62:1 | 9.73:1 |
| `--muted` on `--paper` | 5.22:1 | 5.64:1 |
| `--accent` on `--paper` (links, the current menu word; also `--contested`) | 8.14:1 | 6.46:1 |
| `--rule` on `--paper` (a hairline, not text) | 1.37:1 | 1.44:1 |

Rules for using them: one accent and one warning, which may be the same hue, and nothing else
on the site is coloured; old-style figures in running text and the colophon, lining and tabular
only in the grid's reference line; real small caps from Libertinus for the status words and the
wordmark, never synthesised; rules, not boxes (no borders around content, no fills behind text,
no rounded corners, no shadows); italic for original-language passages, work titles and the
qualification line, never for emphasis in rendered prose; dark mode follows the system; nothing
animated.

### Components

Eleven, each one block of markup from the build and one block of classes in `site/static/site.css`,
all shown light and dark in `site/specimens/components.html`.

1. **Running head.** The wordmark *praemisse* in serif small caps at `--size-2`, the line
   *a map of the arguments of philosophy* in `--size-4` sans `--muted`, the menu, a hairline. Centred. Does not stick.
2. **Menu.** Five words in `--size-4` sans, letterspaced 0.04em: Thinkers · Works · Comparisons ·
   Disputes · About. The current section carries a hairline underline in `--accent`. One line at 390px.
3. **Section label.** `--size-4` sans `--muted`, uppercase, letterspaced 0.14em; an `h2`. The only uppercase text on the site.
4. **Contents list.** No bullets; a hairline above each entry and below the last; the name at the
   left in the serif, a `--size-4` sans note at the right.
5. **Status word.** Sans small caps, letterspaced, `--size-4`, in `--ink`; *contested* in `--contested`.
   Always the word; never a colour alone.
6. **Apparatus note.** `--size-4`, sans labels and serif italic text in `--ink-2`; the right column
   (`minmax(0, 2fr)` beside `minmax(0, 3fr)`) above 720px, beneath the text with a hairline above below it.
   On a claim, argument, passage, reading or comparison it also carries the two filing links
   of run 12 (*Dispute this node*, *Attest this node*), in the same setting.
7. **Passage pair.** The original first, in its script, serif italic, `lang` set; the translation in
   serif roman `--ink-2`; the reference line in `--size-4` sans. Never transliterated.
8. **Comparison grid.** A `table`: one column per thinker, `th` cells for the thinkers with their
   dates; each row's question a `th scope="rowgroup"` across the width; each cell its statements,
   the first at `--size-2`, with reference and status word in `--size-4` sans. Stacks by question under 720px.
9. **Dependency lists.** Depends on, Supports, Attacked by, Replies to (and Shares a premise with,
   which the model also carries): a section label and a contents list each; an empty relation is omitted.
10. **Dispute exchange.** The contested node with its passage pair, then dated, signed turns with a
    hairline between; the project's reply marked *the map replies* in the same form.
11. **Colophon.** Above a `--rule-strong`: the counts line, each count a link to its index, in
    old-style figures; the licence line. The same on every page; the counts come from the build.

### Templates

Seven templates and the index pages, each running head, body, colophon and nothing else. Prose
rendered from the map is not rewritten; only its order and setting change.

1. **Front page.** Reading width. Title, the description as an italic lead, the status paragraph,
   *Comparisons* (one entry per comparison, title at `--size-2`), *Start here* (up to three nodes
   from `start_here` in `site/site.yaml`; omitted if empty), *Thinkers* (a contents list), *To
   dispute a node*. The counts leave this page for the colophon. The status paragraph is the map's
   own text, including the comparison sense of checked (reservation 3).
2. **Comparison.** Page width. The label line *Comparison · status, qualification*, the title, the
   question as an italic lead, the statement, the grid, then *The texts, by row*: for each row the
   passage pairs of that row in the text column (3fr), grouped by thinker, each passage once and
   anchored by its id, and the row's note in the apparatus column (2fr) with a link back to that
   row of the grid; then the premises shared, the body, the dependency lists, the apparatus note.
3. **Node (claim, argument).** Page width, two columns: the label, the claim at `--size-2`, the
   argument's premises and conclusion, the quotations, the prose; the apparatus column with the
   status word, source, passage pairs; the dependency lists full width beneath.
4. **Thinker, Work.** Reading width; title, dates or thinker and year, the facts, contents lists.
5. **Passage.** Reading width; the label *Passage · work · reference*, the pair, the nodes tied to it.
6. **Dispute.** Reading width; the label *Dispute · status*, the node quoted, the exchange, the record.
7. **About.** Reading width; the description, the status vocabulary, the licences, the board, how to dispute.
- **Index pages.** Title with the count in `--muted`, one line on the list, a `--size-4` line
  naming all nine indexes, one contents list with status words at the right; an empty index says so in one sentence.

### Decisions taken by the operator

Each from the brief and `DESIGN.md`, with its reasoning in one line.

- *The lead statement of a cell at `--size-2`, the rest at `--size-3`.* The brief sets the cell
  statement at `--size-2` and names it the "cell lead"; cells hold one to three statements of 11 to
  92 words, and three at `--size-2` in a third of the page would make a row a screen tall.
- *Each passage is shown once, under the first row that cites it, anchored by its id; a later cell
  links to that anchor.* Nine of the 34 citations in the grid repeat a passage shown in an earlier
  row, and repeating 1,200 words would cost weight and reading without adding a text.
- *The row's note moves from inside the grid to the apparatus column beside that row's passages.*
  The brief's cell holds statement, reference and status, so the grid stays a grid; the note is the
  map's commentary on the row and sits where an edition puts commentary, in the margin of the sources.
- *In the texts section the passages take the text column (3fr) and the note the apparatus column
  (2fr), not the other way round.* The passages are the text of that section, 7,000 words of it;
  in the 2fr column they ran to 37,000px, in the 3fr column at the measure to 23,000px.
- *The six passages the comparison lists but no cell cites follow the rows as a last group,
  "Cited in the shared premises and the text".* The body quotes them (P1), so they must be on the page.
- *The label line above the title is a `p`, not an `h2`.* It is the title's kicker, not a section;
  an `h2` before the `h1` would read as a heading out of order.
- *Links in running text are `--accent` with an underline; links in a list or a grid cell, where
  every entry is a link, are `--ink` with no underline until hover or focus.* The brief asks for
  underline rather than colour alone, which is a rule about links inside text; a list of links
  needs no mark on each.
- *The grid cell's statement is plain text; the type word (Claim, Argument) in the reference line
  links to the node.* A statement of 50 words as one underlined link would be noise; the word says
  what kind of node it opens.
- *The thinker's full name in the grid header, with the dates after it.* The map has `name`,
  not a surname field, and the model is off limits.
- *The grid has no key term per cell.* The brief shows one; the model has no field for it and the
  operator writes no copy that is not rendered from the map; noted for `PLAN.md`.
- *`site/site.yaml` holds the palette and the `start_here` list.* The brief asks for a site config
  with both; it is a design-layer input, not a build input in the sense the brief protects.
- *Specimens are not published; the owner opens the file from the branch or reads the screenshots.*
  GitHub Pages deploys `main` only, so there is no branch preview.
- *The committed screenshots show the head, the grid and the first row of texts (6,600px at 1280,
  12,600px at 390), not the whole page.* The whole page is 38,700px at 1280 and 66,000px at 390,
  and four full-page PNGs weigh 33 MB; the HTML file beside them is the whole page.
- *The weight budget of the brief (a node page under 120 KB with fonts) cannot be met with the
  fonts as they are.* The seven Libertinus files weigh 100–136 KB each, 820 KB in all, and a page
  needs at least the serif roman, serif italic and sans roman; the fonts are off limits to this
  work, so the measured numbers are recorded and the gap goes to the board as a note.
- *The build's `--specimen ID PATH` writes one node's page with the specimen's relative paths.*
  The brief asks for the real comparison rendered by the existing build, not a copy made by hand.

- *The filing links of run 12 (`main`, 2026-10-18), Dispute this node and Attest this node,
  render inside the apparatus note of the comparison, in the apparatus setting.* They are the
  map's route for a reader's filing (`MODEL.md`, Filing), and the apparatus note is where the
  page already says what the node is and who produced it; the build's splice of a second
  paragraph now carries the note's class.
- *The specimen was re-rendered on 2026-10-19 from the map as merged from `main`.* The brief
  asks for the real page, and the real page grew by two rows and twenty-odd cells between
  2026-10-11 and 2026-10-19 (seven rows, 227 nodes); the grid alone is now 10,800px tall at
  1280px, which is the map's height and not the template's, and whether a cell of three
  statements wants a tighter setting is the owner's to say at the ask.
- *The screenshots show the head, the grid and the first passage pair, as 64-colour PNGs.*
  With seven rows the earlier clip (head, grid, the whole first row of texts) ran to 18,500px
  and 3.9 MB a file; the first pair shows the component, and 64 colours keep the text legible
  at a fifth of the weight (0.7–0.9 MB a file; the whole page is 71,000px at 1280 and
  121,000px at 390).

### Decisions taken at step 5 (the other templates, 2026-10-19)

- *The node page's title is set at `--size-2`, the claim size, and its statement at `--size-3`.*
  The brief names "the claim at `--size-2`" and no title; a node's title is itself a sentence of
  up to thirty words, and at `--size-1` it would run to four lines before the statement.
- *The apparatus column of a node holds the status word, the thinker, every passage the node
  cites as a passage pair at `--size-4`, and the readings of the node.* The brief lists the
  status, the source and the passage; the pair at the small size keeps the column shorter than
  the text beside it on most pages, and the pair's reference line is the link to the passage page.
- *The prose and the dependency lists sit beneath both columns, full width at the measure.*
  On a phone the apparatus then follows the claim and precedes the prose, as the brief and P1
  require, with no jump link and no script.
- *Thinker, work, passage, dispute and attestation pages share one template, `measure.html`:
  a kicker, the title, a top block, the prose, the contents lists, the apparatus note.* They
  differ only in what fills the top block and the lists.
- *The one line under an index title is taken from `MODEL.md`, Node types.* The brief asks
  for a line on what the list is and the operator writes no copy of its own; the model's own
  description of each type is that line.
- *The note at the right of an index entry is the status word where the node has one, else
  the fact that places it: a thinker's dates, a work's thinker and year, a passage's work, a
  reading's thinker, a dispute's outcome, an attestation's date.* The brief asks for a status
  word; the types without one need something at the right or the list reads as unfinished.
- *An empty index says "No dispute is in the map yet", in that form for each type.*
- *Start here lists three checked arguments, one per thinker, each the first step of its
  chain on the thing in itself (`site/site.yaml`); the note at the right is the type and the
  status word.* The brief leaves the choice to the operator and the owner may change the list.
- *The front page's lead is the description from the old front page, verbatim, which opens
  with the same words as the new title above it.* The brief fixes both; the repetition is a copy
  matter the brief forbids this work to settle, and it is noted in `PLAN.md` for a run.
- *The dispute and attestation templates are built but no page of either kind exists to
  render; the dispute exchange is shown as a form in `site/specimens/components.html`.* The
  first real filing (Ask 10) will be the first test, and the operator checks the page then.
- *`site/static/style.css` is removed; every page is styled from `tokens.css` and `site.css`.*
- *The specimens of the templates are screenshots of the first 3,000px of each page, as
  64-colour PNGs.* A whole page runs to 11,000px (the claims index) and a full-page PNG to 3 MB.

### Type on wide screens and the fonts (owner decisions, 2026-10-19, branch `design-type`)

**A. Fluid type (2026-10-19).** At 1920px the reading column was sized as at 1280px and the
page sat as a small block in an empty field. The body size `--size-3` is now
`clamp(var(--body-size), 0.8125rem + 0.47vw, 1.4rem)`: 19px on a phone and at 1280, rising to
22px at 1920 and no further; `--size-1`, `--size-2` and `--size-4` are derived from it by the
ratios they had (2.105, 1.347, 0.758; 1.684 for the title under 720px), so the four-size rule
(P3) holds at every width and the leading is unchanged. The owner's formula was
`1rem + 0.45vw`, which gives 21.8px at 1280 and would have enlarged the approved 1280 setting;
the slope and intercept were set so that the sizes the owner named hold (19px at 1280, 22px at
1920, never below today's on a phone), and the changelog says so. The measure is 60ch on every
reading-width page and in the text column of the node and comparison pages, whose page width
is unchanged: the owner asked for 68ch and for 62–70 characters a line, and in Libertinus the
ch unit (the zero) is wider than the average letter, so 68ch gave lines of 75 characters and
60ch gives 62–69. Hyphenation is automatic below 720px and manual at 720px and above for body
and lead text; passages are manual at every width. The front page's lead is roman, at
`--size-3`, in `--ink-2`; italic stays everywhere this section names it.

**B. The front page's lead (2026-10-19).** It starts at "Broken into explicit premises",
dropping the words that repeated the title above it; nothing else in the description changed,
and the description on About and in the metadata is as it was (`BOARD.md`).

**C. The fonts (2026-10-19).** The brief's bar on `site/fonts/` was lifted by the owner for this
one purpose. `tools/subset_fonts.py` subsets each face in `site/fonts/libertinus/full/` (the
faces as fetched and subset on 2026-10-05, kept unpublished) to the characters the map and the
templates use (106 on 2026-10-19) plus Basic Latin, Latin-1, Latin Extended-A, Greek and
Coptic, General Punctuation, the arrows and the logical symbols (858 code points), with every
OpenType layout feature kept; the small capitals, old-style and lining figures, ligatures and
kerning the templates use were checked present in every subset. Polytonic Greek (Greek
Extended) is not in the ranges and enters through the map scan when a passage uses it. The
build fails if a rendered page carries a character the subsets lack
(`site/build.py`, `check_font_coverage`), so the script is rerun when the map grows.

| Face | Before (2026-10-05 subset) | After (2026-10-19) | Glyphs before | Glyphs after |
|------|-------:|------:|------:|------:|
| `LibertinusSerif-Regular.woff2` | 113 KB | 50 KB | 1745 | 809 |
| `LibertinusSerif-Italic.woff2` | 133 KB | 57 KB | 1697 | 806 |
| `LibertinusSans-Regular.woff2` | 103 KB | 44 KB | 1685 | 782 |
| `LibertinusSerif-Semibold.woff2` | 111 KB | 48 KB | 1689 | 806 |
| `LibertinusSerif-SemiboldItalic.woff2` | 129 KB | 58 KB | 1675 | 804 |
| `LibertinusSans-Italic.woff2` | 115 KB | 51 KB | 1676 | 779 |
| `LibertinusSans-Bold.woff2` | 97 KB | 44 KB | 1595 | 760 |
| the three faces a node page needs | 357 KB | 151 KB | | |
| all seven | 800 KB | 352 KB | | |

**The checks of 2026-10-19,** all passed before the merge of `design-type`:
- Screenshots at 1920px, first screen, light and dark, under `site/specimens/`:
  `front-1920-*.png`, `claim-1920-*.png`, `comparison-1920-*.png`, 41–93 KB each.
- Body size, computed in Chromium: 19px at 390, 19.0px at 1280, 22.0px at 1920.
- Characters per line on the front page at 1920, measured on the lead's rendered lines:
  69, 65, 67 (a capacity of 69 at an average advance of 8.92px in a 614px column).
- Contrast of the lead, `--ink-2` on `--paper`: 8.62:1 light, 9.73:1 dark.
- No character falls back: the build's coverage check passes on all 238 pages, and every
  text element on the comparison page computes to Libertinus Serif or Libertinus Sans.
- A node page on first visit: 3.1 KB of HTML and 7.0 KB of stylesheets gzipped with the three
  faces, 151 KB, is **161 KB**, under 180 KB; the budget of 120 KB in the brief remains unmet.

### Verification

Done on 2026-10-19 on branch `design`, on the map as merged from `main` that day (227 nodes),
with Playwright's Chromium 1280px and 390px, light and dark; the scripts are not part of the
site.

**Screenshots,** one page per template, under `site/specimens/`: `front`, `node` (a claim),
`argument`, `thinker`, `work`, `passage`, `index` (the claims), `about`, each at 1280 and 390,
light and dark, the first 3,000px; the comparison as `comparison-a-*` (its head, grid and first
passage pair) and the components as `components-*`. No dispute or attestation exists to render.

**Weight,** measured on the built files; GitHub Pages serves text gzipped, fonts as they are.

| Page | HTML raw | HTML gzip | Stylesheets gzip (tokens, type, site) | Fonts on first visit |
|------|---------|-----------|------------------|------------------|
| Node (`/c/kant-space-a-priori/`) | 9.2 KB | 3.1 KB | 6.6 KB | 357 KB (serif regular and italic, sans regular); 471 KB where the page uses a semibold |
| Argument (`/a/kant-appearance-requires-thing-in-itself/`) | 10.9 KB | 3.6 KB | 6.6 KB | the same |
| Front page | 5.5 KB | 2.0 KB | 6.6 KB | the same |
| Comparison (`/x/thing-in-itself/`) | 217 KB | 62 KB | 6.6 KB | 574 KB (all seven faces) |

The brief's budget of a node page under 120 KB on first visit is not met and cannot be met
with the fonts as they are: the three faces a page needs weigh 357 KB, and the fonts are off
limits to this work (`PLAN.md` §5, the weight risk). The second page is 10 KB with the fonts
cached, inside the brief's 30 KB.

**Speed,** Chromium with its *Fast 3G* profile (1.6 Mbit/s down, 150 ms round trip) against a
local server, cold cache: first contentful paint 0.59 s on the front page and 0.68 s on the
comparison (the text renders in the fallback face and swaps, `font-display: swap`); the load
event, which waits for the fonts, 2.5 s on the front page and 4.4 s on the comparison; the node
page with the fonts cached loads in 1.0 s. The brief's "first render under one second" holds;
"loads in under a second on a weak connection" (P8) holds for the text and not for the fonts.

**Contrast,** every pair, light and dark, in the table under *Tokens* above: `--ink` 14.95:1
and 13.75:1, `--ink-2` 8.62:1 and 9.73:1, `--muted` 5.22:1 and 5.64:1, `--accent` 8.14:1 and
6.46:1 on `--paper`; all above 4.5:1 for text and 3:1 for the small caps and the accent underline.

**Every URL that existed before the branch still answers.** The build of `origin/main`
(`cf1a115`) and the build of the branch, the same day and map, each write 238 pages; the two
lists of paths are identical (227 nodes, 9 indexes, the front page, About). Nothing moved.

**Keyboard,** on the front page, a claim and the comparison: the first Tab lands on the skip
link, then the wordmark and the five menu words, then the links in reading order; every stop
shows the 2px `--ink` outline (`outline-style: solid`, `outline-width: 2px` on each of the
first twelve stops, checked by script); 26, 29 and 332 focusable elements, all links, no
tabindex anywhere. Links in running text are underlined, not coloured alone.

**Screen reader,** a structural pass over the comparison grid and a passage pair, by script,
not by a screen reader: the page has one `h1`, a heading order that skips no level, a `nav`
labelled *Sections*, a `main` the skip link targets, `lang="en"` on the page; the grid is a
`table` with `th scope="col"` for the three thinkers and their dates, seven `tbody` groups each
opened by a `th scope="rowgroup"` carrying the row's question; every passage pair sets
`lang="de"` on the original and `lang="en"` on the translation. Under 720px the same table is
restyled, not rebuilt, and its header row stays in the tree for a reader. A pass with a real
screen reader has not been made.

**Print,** `site/specimens/print-node.pdf` (the argument page, A4 portrait, one column) and
`print-comparison.pdf` (A4 landscape, the grid, the texts in two columns), from Chromium with
`@media print`: black on white, the menu and the counts removed, the wordmark and the licence
line kept, the site path printed after every linked node.

**Not permitted** (`DESIGN.md`), item by item: ads: none. Pop-ups: none. Infinite scroll:
none; every index is one page. Autoplay: none; nothing plays. Carousels: none. Skeleton
loaders: none; no script runs. "You may also like": none. Reading-time badges: none.
Engagement metrics shown to readers: none; the counts in the colophon count nodes, not
readers. Stock imagery: none. Decorative illustration of philosophers: none; no image on the
site. Also checked: no hex value and no pixel size outside `tokens.css`; four sizes and no
fifth in `site.css`; no `<script>` in any template or page; the counts on no front page but
in the colophon; body text 19px; the menu on one line at 390px; no horizontal scroll at 390
or 1280 on any template (scroll width equal to the viewport on every screenshot).
