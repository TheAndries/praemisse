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
| `checked` | On an argument: machine-checked for validity (the inference is sound given the premises), fidelity unchecked. On a comparison: reviewed by a named human short of attestation, with the qualification shown in the status line (*Checked comparisons*, below). |
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
A comparison may instead be `checked` on a qualified human review (*Checked comparisons*,
below).

**Links between claims.** `depends_on` on a claim names the argument that establishes it.
It may instead name a claim when the text draws the one from the other by a step the map
has not formalized as an argument (Kant's "also", "denn", "mithin"); the body then quotes
the connective and the line, and a reader who wants the step checked may ask for it to be
made an argument. `supports` is the converse.

**Readings.** A `r-` node names the claim or argument it reads in `reading_of`, carries a
one-sentence `statement` of the reading, cites the passages it rests on and lists in
`literature` the works that hold it, by author, title, year and chapter. The page renders
the target, the literature, the passages and the body, which says what the reading holds,
what tells against it and what depends on it. The map does not pick a reading (`CHARTER.md`
P9); readings carry no status, since there is nothing for a machine to check and nothing
for a human to attest but the fidelity of the quotations, which may be disputed as on any
node.

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

**Attacks and converses.** `supports` is the converse of `depends_on`, and the build
checks that the two agree on every node. `attacked_by` on a node lists the nodes whose
statement denies what its statement says; each attacker names the node in `replies_to`,
so the two fields are converses and the build checks that they agree. An attack is set only against what the
target *states*, not its topic: Schopenhauer attacks Kant's derivation of the thing in
itself while accepting Kant's conclusion, so no attack is set on the conclusion. The
attacker's body quotes the sentence that names the target or says that none does and
what the link rests on instead. Setting or removing a link on an existing node does not
supersede a version, since the statement is unchanged; the changelog records it. Settled
by the operator on 2026-10-09, the first time an attack link was set.

**Comparisons.** An `x-` node sets two or more thinkers side by side on one question. It
carries `question` (one sentence), `thinkers` (the `t-` ids, in the order of the columns),
`statement` (the one sentence a dispute quotes), `rows` (each a `question`, `positions`
keyed by thinker id and listing that thinker's claims or arguments, and an optional
short `note` saying who aligns and where they part, and, where a cell's claim has readings,
how the row reads under each), `shared` (each a `premise` in
one sentence, the `claims` of different thinkers that assert it, and the passages where
each does) and `passages`, the spans the body quotes. The page renders the rows as a table,
one column per thinker, each cell the statements with their ids, status words and passage
references; a thinker with no position in a row is shown as having none in the map, never
supplied by the operator, and the row's note says whether that thinker's text on the
question is absent from the map or silent. `shares_premise_with` is set between two claims only when both
statements assert the same proposition, possibly among others, or one asserts it and the
other expressly keeps that thinker's assertion of it, and the comparison's `shared` entry
names the proposition and the passage of each; the field is symmetric, and the build checks
that every pair in a `shared` entry names each other, that every pair in the map is named
by some comparison, that a `shared` entry's passages are cited by its claims, that every
»...« quotation in a comparison's body or notes is inside a listed passage, and that the
body links every reading of a claim in the table. A comparison stays
`draft` until a human attests it (there is no form to check) or reviews it as *Checked
comparisons* below allows; its body says what depends
on each reading where a cell's claim has `r-` nodes, and lists what the map does not yet
contain. Settled by the operator on 2026-10-10, before the first comparison.

**Checked comparisons.** A comparison may carry `checked` when a named human has read its
claims and readings against the project's translations and ordered or approved what is on
the page, without attesting it: an attestation (`v-`) is a reading against the passage in
the original, and this is less. The node must then carry `status_note`, a clause or two in
plain words saying who reviewed what and what was not verified, and the status line shows
it after the word; the build refuses `checked` on a comparison without the note and the
note on anything else. The page's own text says the same in full. A claim or argument
gets no such status: a claim is `draft` until attested, an argument `checked` only by its
form. Owner decision of 2026-10-10 (`BOARD.md`), given on the first comparison, so that
later comparisons can use the same status.

**Quotations.** A claim may carry `quotes:`, a list of the load-bearing sentences, each
with `passage` (one of the claim's own passages), `original` and `translation`. The build
checks that each is a verbatim substring, whitespace aside, of that passage's `original`
and `translation` (P1), and the page shows the two side by side under the statement, with
the reference, so that a reader who will compare the original with the English finds both
in front of them without going to the passage list. The quotation adds nothing the
passage does not already carry; it is the passage's sentence brought up to the claim.
Settled by the operator on 2026-10-10 on the owner's request in the review of the first
comparison; set on the sentences that review named (B xxvi, Prolegomena § 32, Anhang ZA
II 534–535, WWV I §§ 21–22, JGB 16, »Die ›Vernunft‹ in der Philosophie« 6 fourth
proposition, Fabel stages 5–6) and on the shared-premise sentences on space.
