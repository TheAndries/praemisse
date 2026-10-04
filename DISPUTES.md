# DISPUTES.md

How anyone argues with the map. This protocol is the reason the project appreciates: every
step produces a dated, named, permanent record that no model can generate after the fact.

**Status: binding under `CHARTER.md` P4. Amendable only by board decision.**

---

## What can be disputed

Any node (`MODEL.md`): a thinker's claim, an argument's premises or inference, a passage
mapping, a comparison. Two kinds of objection, and the node page says which one is open:

- **Validity** — the conclusion does not follow from the premises as stated. Checked by
  machine first; a human validity dispute must show the gap.
- **Fidelity** — this is not what the text says, or not what the thinker meant. Only humans
  can settle this.

## Who may dispute

Anyone, under their real name, with affiliation if they wish. No credential is checked.
The filter is the citation: a dispute without at least one passage reference is returned
with a one-line reason and is not published. Anonymous or pseudonymous disputes are not
accepted.

## What a dispute contains

1. The node's permanent id.
2. The claim being contested, quoted from the node.
3. The alternative reading, stated as precisely as the node states its own.
4. At least one passage, by canonical reference, that supports the alternative.
5. Optionally, secondary literature that argues the same.

Filed through the form on the node page (which writes to `INBOX.md` until a connector
exists), or by email to the project address.

## The process

**1. Published.** The operator publishes the dispute on the node's page in the next
scheduled run, verbatim, with the disputant's name and the date. It receives a permanent
address.

**2. One reply.** Within three scheduled runs the operator replies in writing, signed as the
project, citing passages. The reply does one of two things:
- **Concede.** The node is revised; the old version is superseded, not deleted; the dispute
  and reply stay attached; the disputant is credited on the node as the source of the
  correction.
- **Argue.** The reply states why the node's reading stands, with passages, and names the
  interpretive choice at stake if there is one.

**3. One counter.** The disputant may reply once more, by the same route. The operator does
not reply again.

**4. Status.** If not conceded, the node is marked **contested**. Its page shows both
readings, the exchange, and what depends on the node under each reading.

**5. Ruling.** A contested node leaves that status only when a second, independent, named
human files an attestation siding with one reading, citing the passage. That reading becomes
*attested*; the other stays on the page as a recorded minority reading. The operator rules
on whether the second human is independent (not the disputant, not a co-author, not
recruited for this) and records the ruling.

**6. Escalation.** If two independent humans side against the operator and it still does
not concede, the matter goes to `BOARD.md` as a motion and the owner decides. If the owner
sides with the humans, the node is revised and the operator's reading becomes the recorded
minority.

**7. Permanence.** Nothing is deleted. A closed dispute remains at its address with its full
exchange. A superseded node keeps its address and links forward.

## Attestations

The quieter half of the protocol. A named human who has read a node against its passage may
attest that it is faithful. One attestation moves a node from *checked* to *attested*; two
independent attestations make it *established* (`MODEL.md`). Attesters are credited on the
node and in the project's list of contributors. An attestation on a contested node counts as
siding with a reading (step 5).

## Conduct of the operator

- Replies are courteous, concrete and short. They cite; they do not lecture.
- A dispute is treated as a gift, in the reply's tone and in the changelog.
- The operator concedes readily when the text is against it. Conceding is not a failure; a
  node that was wrong and is now right is the project working.
- The operator never characterizes a disputant, their competence or their motives.
- The operator never contacts a disputant beyond the exchange above, except to answer a
  question they asked.
