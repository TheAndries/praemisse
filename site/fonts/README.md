# site/fonts/

Self-hosted web fonts (DESIGN.md 8), every one under the SIL Open Font License 1.1, with the
licence text beside the files. Subset to Latin, Latin Extended, Greek and Greek Extended
(polytonic), general punctuation and a few symbol ranges, with all OpenType layout features
kept (small capitals, old-style figures, ligatures, kerning). Rebuilt with `pyftsubset`
(fontTools) from the sources below; nothing was redrawn.

| Directory | Family | Source | Version fetched 2026-10-05 |
|-----------|--------|--------|------|
| `ebgaramond/` | EB Garamond (variable, upright and italic) | google/fonts `ofl/ebgaramond` | main |
| `sourcesans3/` | Source Sans 3 (variable, upright and italic) | adobe-fonts/source-sans release `3.052R` (WOFF2 VF); OFL from google/fonts | 3.052 |
| `libertinus/` | Libertinus Serif (Regular, Italic, Semibold, Semibold Italic), Libertinus Sans (Regular, Italic, Bold) | alerque/libertinus release `v7.051` (static OTF, then subset) | 7.051 |
| `alegreya/` | Alegreya (variable, upright and italic) | google/fonts `ofl/alegreya` | main |
| `alegreyasans/` | Alegreya Sans (Regular, Italic, Medium) | google/fonts `ofl/alegreyasans` | main |

Three directions are offered under Ask 3: A = EB Garamond + Source Sans 3, B = Libertinus,
C = Alegreya + Alegreya Sans. Once the owner chooses, the two unused families are removed
from this directory and `site/static/type.css` is set to the chosen one.

Not used: Source Serif 4 (the google/fonts build lacks polytonic Greek); the Libertinus
release's own WOFF2 files (their OpenType feature tables are stripped — subset from the OTF).
