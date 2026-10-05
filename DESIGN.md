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
