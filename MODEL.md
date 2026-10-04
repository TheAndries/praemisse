# MODEL.md

What is stored, and how. Plain files under `map/`, one file per node, YAML front matter
plus Markdown. Readable without any tool. Ids are stable forever; a changed node gets a
new version inside the same file, never a new id.

## Node types

| Type | Id prefix | What it is |
|------|-----------|-----------|
| Thinker | `t-` | A person. Dates, tradition, canonical editions used. |
| Work | `w-` | A text. Edition, reference scheme, source URL of the public-domain text. |
| Passage | `p-` | A located span of a work: canonical reference, original text, translation, translation licence. |
| Claim | `c-` | A position a thinker holds, stated in one sentence, tied to one or more passages. |
| Argument | `a-` | Premises (each a claim or an explicit assumption), an inference form, a conclusion (a claim). Tied to the passages where the argument is made. |
| Reading | `r-` | One interpretation of a contested claim or argument, with the literature that holds it. |
| Comparison | `x-` | Two or more thinkers on one question: which claims align, which premises are shared, where they diverge, with links. |
| Dispute | `d-` | Filed under `DISPUTES.md`. Node id, disputant, date, text, replies, outcome. |
| Attestation | `v-` | A named human's sign-off on a node against its passage. |

## Links

Every argument and claim carries: `depends_on`, `supports`, `attacked_by`, `replies_to`,
`shares_premise_with`. Links are node ids. The site renders them as lists; tooling checks
that every link resolves.

## Status

Every claim, argument and comparison has exactly one of:

| Status | Meaning |
|--------|---------|
| `draft` | Produced by the operator. No human has read it against the passage. |
| `checked` | Machine-checked for validity (the inference is sound given the premises). Fidelity unchecked. |
| `attested` | One named human has read it against the passage and signed off. |
| `established` | Two or more independent named humans have. |

plus an overlay flag `contested: true` while a dispute is in step 4 of `DISPUTES.md`.

## Provenance

Every node records `produced_by` (model and date), `verified_by` (list of attestation ids),
`superseded_by` / `supersedes` (version chain), and `disputes` (list). The site shows the
model that produced a draft. Readers may judge accordingly.

## Texts

Primary texts are taken from public-domain editions (Perseus, Wikisource, Gutenberg, the
Internet Archive, the Akademie-Ausgabe scans) and cited by canonical reference, never by
page of a modern edition. Modern translations are not stored. Where no public-domain
translation is adequate, the project renders its own, marks it as the project's, and shows
the original beside it. Contemporary (post-1929) arguments are formalized from a lawfully
read source, cited, and the source text is not reproduced.
