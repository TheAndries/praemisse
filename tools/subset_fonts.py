#!/usr/bin/env python3
"""praemisse — subset the Libertinus faces to what the site renders (owner decision 2026-10-19).

    python3 tools/subset_fonts.py            rewrite site/fonts/libertinus/*.woff2 from full/
    python3 tools/subset_fonts.py --report   print the before-and-after table only, do not write

Reads every character under map/ and site/templates/, adds Basic Latin, Latin-1 Supplement,
Latin Extended-A, Greek and Coptic, General Punctuation, the arrows and the logical symbols the argument forms use, and subsets each face in
site/fonts/libertinus/full/ to that set with every OpenType layout feature kept (small
capitals, old-style and lining figures, ligatures, kerning), writing the result as the file type.css
loads, beside the full face in full/. Polytonic Greek (Greek Extended) is not in the ranges; a
passage that uses it brings its characters in through the map scan when the script is rerun. Rerun when the map grows; the build fails if a rendered page
carries a character the subsets lack (site/build.py, check_font_coverage).
Requires fontTools and brotli (site/requirements.txt). Nothing is redrawn; OFL 1.1 applies.
"""
from __future__ import annotations

import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "site" / "fonts" / "libertinus"
FULL = FONTS / "full"
SOURCES = [ROOT / "map", ROOT / "site" / "templates"]
RANGES = [  # (first, last) inclusive
    (0x0020, 0x007E),  # Basic Latin
    (0x00A0, 0x00FF),  # Latin-1 Supplement
    (0x0100, 0x017F),  # Latin Extended-A
    (0x0370, 0x03FF),  # Greek and Coptic
    (0x2000, 0x206F),  # General Punctuation (dashes, quotation marks, ellipsis, bullets)
    (0x2190, 0x2199),  # arrows (→ in the forms and the dependency lists)
]
SYMBOLS = "¬∧∨↔⊢⊬⊨⊭⊤⊥∀∃∴∵≠≤≥×÷−·•€£"  # the logic and the odd symbol the templates render


def used_characters() -> set[str]:
    chars: set[str] = set()
    for src in SOURCES:
        for p in src.rglob("*"):
            if p.suffix in (".md", ".html", ".yaml") and p.is_file():
                chars.update(p.read_text(encoding="utf-8"))
    return {c for c in chars if not c.isspace() and ord(c) >= 0x20}


def wanted() -> set[int]:
    cps = {ord(c) for c in used_characters()} | {ord(c) for c in SYMBOLS}
    for a, b in RANGES:
        cps.update(range(a, b + 1))
    return cps


def subset_face(src: Path, dst: Path, cps: set[int], write: bool = True) -> tuple[int, int, int, int]:
    before = src.stat().st_size
    font = TTFont(src)
    glyphs_before = font["maxp"].numGlyphs
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]      # keep every feature: smcp, c2sc, onum, lnum, tnum, pnum, liga, kern, ...
    opts.name_IDs = ["*"]             # keep the name table whole, licence and all
    opts.notdef_outline = True
    opts.glyph_names = False
    opts.hinting = False
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=sorted(cps))
    sub.subset(font)
    glyphs_after = font["maxp"].numGlyphs
    import io
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    data = buf.getvalue()
    glyphs_after = TTFont(io.BytesIO(data))["maxp"].numGlyphs
    if write:
        dst.write_bytes(data)
    return before, len(data), glyphs_before, glyphs_after


def main(argv=None) -> int:
    report_only = "--report" in (argv or sys.argv[1:])
    if not FULL.exists():
        sys.exit(f"{FULL} is missing: the full faces must sit there (see site/fonts/README.md)")
    cps = wanted()
    used = used_characters()
    print(f"{len(used)} distinct characters in map/ and site/templates/; {len(cps)} code points requested", file=sys.stderr)
    rows = []
    for src in sorted(FULL.glob("*.woff2")):
        b, a, gb, ga = subset_face(src, FONTS / src.name, cps, write=not report_only)
        rows.append((src.name, b, a, gb, ga))
    print("| Face | Before | After | Glyphs before | Glyphs after |")
    print("|------|-------:|------:|------:|------:|")
    for name, b, a, gb, ga in rows:
        print(f"| `{name}` | {b/1024:.0f} KB | {a/1024:.0f} KB | {gb} | {ga} |")
    tb = sum(r[1] for r in rows); ta = sum(r[2] for r in rows)
    print(f"| all seven | {tb/1024:.0f} KB | {ta/1024:.0f} KB | | |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
