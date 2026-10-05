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
| `templates/` | `base.html` (the one header and one footer), `node.html`, `index.html`. Plain `{{ name }}` substitution. |
| `static/style.css` | Layout and typographic rules shared by every page. |
| `static/type.css` | The chosen typeface (Ask 3). A placeholder until the owner chooses. |
| `static/type.css` | The chosen type: direction B, Libertine (Ask 3, 2026-10-05). |
| `fonts/` | Self-hosted, subset, OFL-licensed web fonts; see `fonts/README.md`. |
| `specimens/` | The three typographic specimen pages offered under Ask 3, and `make.py` which wrote them. Kept as the record; no longer built or published. |
| `_build/` | Output. Not committed. |

## Build and publish

Locally: `pip install -r site/requirements.txt && python3 site/build.py`, then open
`site/_build/index.html`. Every page uses relative paths, so the output works from a file,
from a sub-path and from the root of a domain.

Published by `.github/workflows/site.yml` with GitHub Pages on every push to `main`, once
the owner has enabled Pages (Ask 5). The workflow fails the build if any node fails the
check: an unresolved link or a claim without a passage never reaches the site.

## Addresses

Permanent (`CHARTER.md` P4, `DESIGN.md` 2): a node `a-foo` lives at `/a/foo/`; type indexes at
`/a/`, `/c/`, `/t/` and so on.
