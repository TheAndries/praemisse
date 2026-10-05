# site/fonts/

Self-hosted web fonts (DESIGN.md 8), every one under the SIL Open Font License 1.1, with the
licence text beside the files. Subset to Latin, Latin Extended, Greek and Greek Extended
(polytonic), general punctuation and a few symbol ranges, with all OpenType layout features
kept (small capitals, old-style figures, ligatures, kerning). Rebuilt with `pyftsubset`
(fontTools) from the sources below; nothing was redrawn.

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
