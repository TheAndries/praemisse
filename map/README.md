# map/

The map itself: one plain file per node, YAML front matter plus Markdown, readable without
any tool. Node types, ids, links, statuses and provenance are defined in [`../MODEL.md`](../MODEL.md),
which is binding, including its section *How the model is applied* (versions, statements,
the validity form, disputes and attestations). Everything in this directory is licensed
CC BY-SA 4.0 ([`../LICENSE-DATA`](../LICENSE-DATA)). Nothing here is ever deleted; nodes are
superseded in place and disputes are closed, both at their permanent address (`CHARTER.md` P4).

Passages quote public-domain editions by canonical reference. Kant is quoted from the
Bonner Kant-Korpus transcription of the Akademie-Ausgabe (korpora.org), cited by A/B page
where the work has one and always by AA volume:page.line; translations marked "the
project" are the project's own and may be disputed like anything else.

Every node is validated by `python3 site/build.py --check`: ids, types, statuses, every
link, a passage behind every claim and argument, and the validity form of every argument
marked `checked`. First nodes: 2026-10-06 (Kant on the thing-in-itself).
