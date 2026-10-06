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

## How the model is applied

Settled by the operator on 2026-10-06, before the first node, as matters of method
(`BOARD.md`, tie-break). Enforced by `site/build.py --check`; nothing that fails it reaches
the site.

**Versions.** A revised node keeps its id and its file. The front matter carries
`versions:`, newest first, one entry per superseded version with `date`, `reason`, the
superseded `statement` and, when a dispute or attestation caused the change, `credit` (the
`d-` or `v-` id). The page shows the current version and lists the earlier ones at the same
address. `supersedes` / `superseded_by` are reserved for the rare case where a node is split
or merged and a new id is unavoidable.

**Statement.** Every claim, argument and comparison carries a one-sentence `statement`,
which is the text a dispute quotes and an attestation signs. The body explains; the
statement is the node.

**Validity.** An argument may carry a `form:` block: `atoms` (each with a one-line gloss),
`premises` (one formula per listed premise, in order) and `conclusion`, in propositional
logic. `tools/validity.py` decides by truth table whether the conclusion holds in every
assignment that satisfies the premises. A form that fails is a build error. `checked` is
allowed only on an argument whose form passes; a claim or comparison stays `draft` until a
human attests it, since there is nothing for a machine to check in a single sentence. The
check never says whether a premise is true or faithful; the page says so beside it.

**Disputes and attestations.** A `d-` node names its `target`, `disputant` (real name,
optional `affiliation`), `date`, `kind` (validity or fidelity), the `contested_claim` quoted
from the node, the `alternative`, at least one passage, optional `literature`, the
project's `reply`, the disputant's `counter` and a `ruling`, each with `date` and `text`,
and an `outcome`: published, argued, conceded, contested, resolved, escalated. A `v-` node
names its `target`, `attester`, `date`, `statement` and optionally `sides_with` (a reading).
The target's page renders every dispute and attestation on it in full. The target's
`disputes` and `verified_by` lists must equal the set of nodes targeting it; `attested`
needs one attestation on file, `established` two; `contested: true` exactly while a dispute
on it has outcome contested.
