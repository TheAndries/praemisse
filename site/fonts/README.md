# site/fonts/

Self-hosted web fonts (DESIGN.md 8), every one under the SIL Open Font License 1.1, with the
licence text beside the files. Two sets. `libertinus/full/` holds the faces as fetched on
2026-10-05 and subset then to Latin, Latin Extended, Greek and Greek Extended (polytonic),
general punctuation and a few symbol ranges, with all OpenType layout features kept; the site
does not load them and the build does not publish them. `libertinus/*.woff2`, the files
`type.css` loads, are subset again from those on 2026-10-19 (owner decision) by
`tools/subset_fonts.py` to the characters the map and the templates use plus Basic Latin,
Latin-1, Latin Extended-A, Greek and Coptic, General Punctuation, the arrows and the logical
symbols, every layout feature kept (small capitals, old-style and lining figures, ligatures,
kerning): 800 KB to 352 KB for the seven, 357 KB to 151 KB for the three a page needs. Rerun
the script when the map grows; `site/build.py` fails if a rendered page carries a character
the subsets lack. Nothing was redrawn.

| Directory | Family | Source | Version fetched 2026-10-05 |
|-----------|--------|--------|------|
| `libertinus/` | Libertinus Serif (Regular, Italic, Semibold, Semibold Italic), Libertinus Sans (Regular, Italic, Bold) | alerque/libertinus release `v7.051` (static OTF, then subset) | 7.051 |

Three directions were offered under Ask 3: A = EB Garamond + Source Sans 3, B = Libertinus,
C = Alegreya + Alegreya Sans. The owner chose B on 2026-10-05 (`DESIGN.md`, `BOARD.md`);
the two unused families were removed from this directory in the same session and
`site/static/type.css` carries the chosen one. The specimen pages in `site/specimens/`
still reference the removed families and are kept only as the record of the offer.

Not used: Source Serif 4 (the google/fonts build lacks polytonic Greek); the Libertinus
release's own WOFF2 files (their OpenType feature tables are stripped — subset from the OTF).
