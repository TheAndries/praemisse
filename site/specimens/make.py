#!/usr/bin/env python3
"""Writes the three typographic specimen pages for Ask 3 (DESIGN.md, last section).

Same page three times; only the type stylesheet differs. The page is a mock node page:
the layout the real pages will use, with specimen text. Nothing on it is a node and no
claim on it is attributed to anyone. The passages are verse, chosen for their letters,
cited by canonical reference; the translations are the project's own.

Run:  python3 site/specimens/make.py   (from the repository root or anywhere)
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent

DIRECTIONS = {
    "a": dict(
        name="A — Garamond",
        serif="EB Garamond", sans="Source Sans 3",
        designers="Georg Duffner and Octavio Pardo (serif); Paul D. Hunt, Adobe (sans)",
        licence="SIL Open Font License 1.1, both",
        weight="371 KB serif (upright and italic, variable), 168 KB sans, subset to Latin and Greek",
        character="The Aldine and French Renaissance book face, after Claude Garamont's romans and Robert Granjon's italics. Small x-height, long extenders, so it is set a step larger. The reference point is a well-printed classical text of the last century."),
    "b": dict(
        name="B — Libertine",
        serif="Libertinus Serif", sans="Libertinus Sans",
        designers="Philipp H. Poll; Khaled Hosny; Caleb Maclennan and contributors",
        licence="SIL Open Font License 1.1",
        weight="483 KB serif (four static faces), 313 KB sans (three), subset to Latin and Greek",
        character="The open-source academic text face of the last twenty years, grown out of Linux Libertine. Serif and sans from the same hand, so labels and text agree. The most complete Greek of the three. The reference point is a university-press monograph set in the 2000s."),
    "c": dict(
        name="C — Alegreya",
        serif="Alegreya", sans="Alegreya Sans",
        designers="Juan Pablo del Peral, Huerta Tipográfica",
        licence="SIL Open Font License 1.1, both",
        weight="225 KB serif (upright and italic, variable), 167 KB sans (three static faces), subset to Latin and Greek",
        character="A calligraphic humanist drawn for long literary texts, with a full polytonic Greek. Warmer and more rhythmic than A or B, and the most clearly of this century; the one most likely to still look right in 2036."),
}

PASSAGES = [
    dict(lang="grc", work="Homer, <cite>Iliad</cite>", ref="1.1–2", source="Perseus (Monro and Allen, 1920)",
         original="Μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος\nοὐλομένην, ἣ μυρί᾽ Ἀχαιοῖς ἄλγε᾽ ἔθηκε,",
         translation="Sing, goddess, the wrath of Peleus’ son Achilles, the ruinous wrath that laid countless griefs on the Achaeans,"),
    dict(lang="la", work="Vergil, <cite>Aeneid</cite>", ref="1.1–3", source="Perseus (Greenough, 1900)",
         original="Arma virumque cano, Troiae qui primus ab oris\nItaliam fato profugus Laviniaque venit\nlitora,",
         translation="Arms I sing, and the man who first from the shores of Troy came, a fugitive by fate, to Italy and the Lavinian coast,"),
    dict(lang="de", work="Goethe, <cite>Faust</cite> I", ref="354–357", source="Wikisource (Cotta, 1808)",
         original="Habe nun, ach! Philosophie,\nJuristerei und Medizin,\nUnd leider auch Theologie\nDurchaus studiert, mit heißem Bemühn.",
         translation="I have now, alas, studied philosophy, law and medicine, and sadly theology too, through and through, with ardent effort."),
    dict(lang="fr", work="La Fontaine, <cite>Fables</cite>", ref="I.1, 1–4", source="Wikisource (Barbin, 1668)",
         original="La Cigale, ayant chanté\nTout l’été,\nSe trouva fort dépourvue\nQuand la bise fut venue :",
         translation="The cicada, having sung all summer long, found herself quite destitute when the north wind came:"),
]

LINKS = [
    ("Depends on", [("c-0001", "A line of sixty to seventy-five characters keeps the eye’s place"), ("c-0002", "A claim without its passage in view asks to be trusted, not read")]),
    ("Supports", [("a-0003", "The passage sits beside the claim on a wide screen")]),
    ("Attacked by", [("a-0004", "A narrow measure wastes a wide screen")]),
    ("Replies to", [("d-0001", "A dispute, filed under the protocol, with its reply")]),
    ("Shares a premise with", [("a-0005", "A page is printed, not scrolled")]),
]

def passage_html(p):
    return f'''<div class="passage" lang="{p['lang']}">
  <p class="ref" lang="en"><span>{p['work']} {p['ref']}</span><span>{p['source']}</span></p>
  <p class="original verse" lang="{p['lang']}">{p['original']}</p>
  <p class="translation" lang="en">{p['translation']} <span class="by">— the project’s translation</span></p>
</div>'''

def links_html():
    out = []
    for title, items in LINKS:
        lis = "".join(f'<li><span class="id">{i}</span><a href="#">{t}</a></li>' for i, t in items)
        out.append(f'<div><h2>{title}</h2><ul>{lis}</ul></div>')
    return "\n".join(out)

def page(key, d):
    passages = "\n".join(passage_html(p) for p in PASSAGES)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Specimen {key.upper()} · praemisse</title>
<link rel="stylesheet" href="../static/style.css">
<link rel="stylesheet" href="../static/type-{key}.css">
</head>
<body>
<header class="site-header" id="top">
  <a class="wordmark" href="#">praemisse</a>
  <nav><a href="#">Thinkers</a> <a href="#">Works</a> <a href="#">Comparisons</a> <a href="#">Disputes</a> <a href="#">About</a></nav>
</header>
<main>
<p class="specimen-banner"><strong>Typographic specimen {d['name']}.</strong> {d['serif']} for text and passages, {d['sans']} for labels. This is the layout of a node page with specimen text. Nothing here is a node; no claim on this page is attributed to anyone. Compare with <a href="a.html">A</a>, <a href="b.html">B</a>, <a href="c.html">C</a>, or return to the <a href="index.html">list</a>.</p>

<p class="status"><span><span class="label">Argument</span></span> <span>Status: <span class="word">draft</span></span> <span>Produced by the operator, 2026-10-05</span> <span>Verified by nobody yet</span></p>

<div class="node">
<article class="node-text">
<h1>A page is for reading, so the passage stands beside the claim</h1>

<p class="jump"><a href="#passages">The passages</a></p>

<h2>The argument</h2>
<ol class="argument">
  <li><span class="n">P1</span><span><a href="#">A reader keeps their place in a line when it holds between sixty and seventy-five characters.</a></span></li>
  <li><span class="n">P2</span><span><a href="#">A claim is trusted rather than read when its passage is out of view.</a></span></li>
  <li><span class="n">P3</span><span class="assumption"><em>Assumption.</em> A page that serves both conditions at once serves reading better than one that serves either alone.</span></li>
  <li><span class="n">Form</span><span>From P1, P2 and P3, by setting the text at that measure and the passage beside it.</span></li>
  <li class="conclusion"><span class="n">C</span><span><a href="#">A node page sets its text at a measure of sixty to seventy-five characters with its passage beside it.</a></span></li>
</ol>

<h2>In prose</h2>
<p>The map breaks arguments into explicit premises, inferences and conclusions, each tied to the passage it comes from, each linked to every argument that depends on it or attacks it. A reader can see what a position commits them to, what it rests on, and where two thinkers share or contest a premise. Every node carries its status in words, in the same place, on every page: <span class="sc">draft</span>, <span class="sc">checked</span>, <span class="sc">attested</span>, <span class="sc">established</span>, and <span class="sc">contested</span> while a dispute is open.</p>
<p>Prose like this paragraph is rendered from the node and may be regenerated at any time; it is never the object of attestation or dispute. The structure and the passage mapping are. A sentence that cannot be traced to a passage is not written, and a node never appears more checked than it is. Anyone who can cite a text may dispute a node under their own name; nobody may overwrite one, and nothing is ever deleted.</p>
<p>References appear as the tradition writes them: Bekker 1094a1, Stephanus 507b, Akademie 4:289, B 311, WWV I §21, JGB 16, Ethica I p11, KSA 12:9[91]. Dates run 1781, 1818, 1886; figures 0123456789 in text, <span style="font-variant-numeric: lining-nums">0123456789</span> lining.</p>

<section class="links">
{links_html()}
</section>

<div class="meta">
  <p>Permanent address: praemisse.com/a/0000 · Produced by the operator (claude-fable-5-1), 2026-10-05 · Versions: 1 · Disputes: none · <a href="#">Dispute this node</a> · <a href="#">Attest to it</a></p>
</div>
</article>

<aside id="passages">
{passages}
<p class="return"><a href="#top">Back to the argument</a></p>
</aside>
</div>

<section class="specimen-notes">
<h2>About this direction</h2>
<dl>
  <dt>Text face</dt><dd>{d['serif']}</dd>
  <dt>Label face</dt><dd>{d['sans']}</dd>
  <dt>Designers</dt><dd>{d['designers']}</dd>
  <dt>Licence</dt><dd>{d['licence']}; self-hosted from <code>site/fonts/</code>, no third-party request</dd>
  <dt>Weight on the wire</dt><dd>{d['weight']}</dd>
  <dt>Character</dt><dd>{d['character']}</dd>
</dl>
<div class="alphabet">
  <span class="label">Roman</span>
  <p>ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz ÄÖÜ äöüß ÀÉÈÊÇ àéèêç fi fl ffi &amp; 0123456789 · ; : ! ? « » „“ ‘’ — –</p>
  <span class="label">Italic</span>
  <p><em>ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz äöüß àéèêç fi fl &amp; 0123456789 Ding an sich · volonté · la chose en soi · Wille zum Leben</em></p>
  <span class="label">Greek</span>
  <p lang="grc">ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ αβγδεζηθικλμνξοπρστυφχψω ἀἁἂἃἄἅἆἇ ᾠᾡᾧ ῥ ῾ ᾽ ἡ οὐσία, τὸ ὄν, ἡ ψυχή, ὁ λόγος, τὸ ἀγαθόν, ἡ ἀλήθεια</p>
  <span class="label">Small capitals</span>
  <p><span class="sc">Draft · Checked · Attested · Established · Contested</span></p>
  <span class="label">The four sizes</span>
  <p class="sizes"><b class="s1">Label 13 px</b> · <b class="s2">Body</b> · <b class="s3">Subhead</b> · <b class="s4">Title</b></p>
</div>
</section>
</main>
<footer class="site-footer">
  <p>praemisse · a map of the arguments of philosophy · data CC BY-SA 4.0, code MIT · no account, no advertising, no cookies, no tracking beyond a page count</p>
</footer>
</body>
</html>
'''

INDEX = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Typographic specimens · praemisse</title>
<link rel="stylesheet" href="../static/style.css">
</head>
<body>
<header class="site-header"><a class="wordmark" href="#">praemisse</a><nav><span>Typographic specimens for Ask 3</span></nav></header>
<main>
<div class="prose">
<h1>Three typographic directions</h1>
<p>Same page three times, in the layout every node page will use; only the type changes. Each is self-hosted, open-licensed, and carries polytonic Greek, German and French in their own script. Read each on a wide screen, on a phone, and in dark mode, and pick one. The choice is recorded in <code>DESIGN.md</code> and becomes binding.</p>
<ol>
  <li><a href="a.html">A — Garamond.</a> EB Garamond with Source Sans 3. The classical edition.</li>
  <li><a href="b.html">B — Libertine.</a> Libertinus Serif with Libertinus Sans. The academic monograph.</li>
  <li><a href="c.html">C — Alegreya.</a> Alegreya with Alegreya Sans. The literary book, of this century.</li>
</ol>
<p>What is the same on all three: one header, one footer, no sidebar; a measure of sixty to seventy-five characters; four sizes; the status in words in one place; the passage beside the claim on a wide screen and one tap away on a phone; links as lists; dark mode following the system; nothing that needs JavaScript. These follow <code>DESIGN.md</code> and are not up for choice here. What differs: the faces, their size and leading, and the character of the page.</p>
<p>To choose, write the letter in <code>INBOX.md</code> as an owner note, or mark Ask 3 done with the letter. Anything else you notice about the layout is welcome in the same note.</p>
</div>
</main>
<footer class="site-footer"><p>praemisse · specimens, 2026-10-05 · nothing on these pages is a node</p></footer>
</body>
</html>
'''

if __name__ == "__main__":
    for key, d in DIRECTIONS.items():
        (HERE / f"{key}.html").write_text(page(key, d), encoding="utf-8")
    (HERE / "index.html").write_text(INDEX, encoding="utf-8")
    print("wrote", ", ".join(f"{k}.html" for k in DIRECTIONS), "and index.html in", HERE)
