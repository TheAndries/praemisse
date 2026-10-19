# site/

The build pipeline that renders `map/` into a static site, and nothing else. The site obeys
[`../DESIGN.md`](../DESIGN.md) (binding) and `CHARTER.md` P6–P8: static files, no frameworks on the
reading path, no cookies, no tracking beyond an aggregate count, self-hosted fonts, and
prose rendered from the nodes rather than written by hand. Code here is MIT ([`../LICENSE`](../LICENSE)).

## Layout

| Path | What |
|------|------|
| `build.py` | The whole pipeline: read `map/*.md`, validate against `MODEL.md`, render to `_build/`. `python3 site/build.py --check` validates only. |
| `requirements.txt` | PyYAML. Nothing else. |
| `templates/` | `base.html` (the running head, the menu, the colophon), `comparison.html`, `node.html` (claim, argument, reading), `measure.html` (thinker, work, passage, dispute, attestation), `index.html` (the front page), `about.html`. Plain `{{ name }}` substitution. |
| `site.yaml` | Design-layer settings: the palette set on `<html>`, the front page's `start_here` list. Added 2026-10-11. |
| `static/tokens.css` | Every colour, size and spacing as a custom property; imports `type.css`. Direction A, the edition (`DESIGN.md`, Colour, space and pages; owner decisions 2026-10-11 and 2026-10-19). |
| `static/site.css` | Page and component styles, all from the tokens. |
| `static/type.css` | The chosen type: direction B, Libertine (Ask 3, 2026-10-05). |
| `fonts/` | Self-hosted, subset, OFL-licensed web fonts; see `fonts/README.md`. |
| `specimens/` | The three typographic specimen pages offered under Ask 3 (`a.html`, `b.html`, `c.html`, `make.py`); the two mockups the owner gave with the design brief of 2026-10-11 (`mockup-a.html`, `mockup-b.html`); the components (`components.html`), the comparison specimen (`comparison-a.html`, written by `build.py --specimen x-thing-in-itself PATH`), the screenshots of every template and the two print PDFs of the verification (`DESIGN.md`). Kept as the record; not published. |
| `_build/` | Output. Not committed. |

## Build and publish

Locally: `pip install -r site/requirements.txt && python3 site/build.py`, then open
`site/_build/index.html`. `python3 site/build.py --specimen <node id> <path>` writes one node's page as a
specimen with relative paths for `site/specimens/`. Every page uses relative paths, so the output works from a file,
from a sub-path and from the root of a domain.

Published by `.github/workflows/site.yml` with GitHub Pages on every push to `main`, once
the owner has enabled Pages (Ask 5). The workflow fails the build if any node fails the
check: an unresolved link or a claim without a passage never reaches the site.

## Addresses

Permanent (`CHARTER.md` P4, `DESIGN.md` 2): a node `a-foo` lives at `/a/foo/`; type indexes at
`/a/`, `/c/`, `/t/` and so on.
