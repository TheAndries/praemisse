# PLAN.md

Current strategy. Rewritten, with the date, whenever it changes. Last rewritten 2026-10-18,
run 12 (Phase 2 opened: the filing route settled and built; what follows). Earlier
versions: 2026-10-10 owner session (Checkpoint 1 answered; the comparison `checked` with a
qualification), 2026-10-10 run 6 (the comparison node exists; the node count corrected) and
2026-10-04 (founding), in the git history.

## §1. What this is, in one sentence

Build the Kant → Schopenhauer → Nietzsche chain on the thing-in-itself well enough that one
comparison page is better than anything a single specialist could have written, then open it
to dispute.

## §2. Why that wedge

Schopenhauer builds on Kant and attacks him explicitly; Nietzsche does the same to
Schopenhauer. The dependencies are stated in the texts, not reconstructed. Three thinkers,
one question, one dense, well-documented chain. All three are public domain in the original
and in older translations. If the comparison page works, the method is proven for the rest.

## §3. Phases

**Phase 0 — founding. Done 2026-10-05.** Name and domain (Ask 1). Public repository and
routine (Ask 2). Type chosen (Ask 3). Site live at praemisse.com (Ask 5). Build pipeline:
`map/` → static site, checked on every push.

**Phase 1 — the chain. Built 2026-10-06 to 2026-10-10; Checkpoint 1 answered 2026-10-10.** The founding
target of ~40 nodes was wrong by a factor of three: a claim per sentence of a passage and an
argument per inference step give 145 nodes for the three thinkers on this one question
(Kant 53, Schopenhauer 38, Nietzsche 53, and the comparison). Kant: the critique
of dogmatic metaphysics, appearance and thing in itself, the limits of knowledge (KrV,
Prolegomena, by Akademie page and line). Schopenhauer: the will as thing in itself, the
critique of Kant's derivation in the Anhang to WWV I (by §, ZA page as an aid). Nietzsche:
immediate certainty, the will as cause, the true world (JGB, GD, by aphorism; no Nachlass).
Nine arguments with validity checked by machine; two contested readings held open on Kant
(B xxvi) and on Nietzsche (JGB 36); the first attack links and the first shared-premise
links, with their conventions in `MODEL.md`. The comparison node `x-thing-in-itself` exists
since 2026-10-10; the owner read it the same day and ordered eight changes, applied in
the owner session, and it is `checked` with the qualification its status line shows, not
attested (147 nodes). Everything is `draft` or `checked`; nothing is claimed beyond that.

**Checkpoint 1 (answered 2026-10-10; Ask 7 done):** the owner read
https://praemisse.com/x/thing-in-itself/ against the project's translations, found nothing
that reads as fabrication, and gave eight decisions, all applied the same day
(`CHANGELOG.md`, the owner session of 2026-10-10): the page is `checked` with a
qualification, two readings were settled (Fabel stages 5–6 in Nietzsche's own voice), one
shared premise widened, one cell moved, and the load-bearing sentences now stand in German
beside the English inside the claims. The question in the ask's own words, whether the page
is better than what he could find elsewhere, was not answered in those words; no rethink of
the method was ordered, and the operator proceeds on that until the owner says otherwise in
`INBOX.md`. What follows, in order: the gaps the comparison page lists (Kant B xxvii–xxviii
and the rest of A 236–260 / B 295–315; Schopenhauer § 2, §§ 24–29, the Anhang on the
Aesthetic; Nietzsche JGB 15, 20, 21, 34), each added only where it adds a row or a cell;
then the second comparison the chain already supports, *the will* (Schopenhauer §§ 18–23
against Nietzsche JGB 19, 36, GD Irrthümer 3), built to the same convention and offered
for the same qualified review; quotations (`MODEL.md`, *Quotations*) set on the
load-bearing sentence of every claim a comparison cell cites, as the pages are touched. A
fourth thinker is no longer blocked by this checkpoint, but comes after those two.

**Phase 2 — first humans. Opened 2026-10-18.** The route into `INBOX.md` that depends on
nobody reading mail is settled in `MODEL.md`, *Filing*, and built: every claim, argument,
passage, reading and comparison page ends with *Dispute this node* and *Attest this node*,
each a link to an issue form with the node's id prefilled; a workflow carries the filing
verbatim into `INBOX.md`, commits it, posts a receipt, and, once the operator has published
the `d-` or `v-` node, posts its permanent address on the issue. The second comparison, on
the will, was built on 2026-10-15 and awaits the owner's qualified review (Ask 9). What
follows, in order: the owner tests the route once from a node page (Ask 10), so that the
first stranger's filing is not the first test; the operator reads `INBOX.md` every run and
handles a filing inside the deadlines of `DISPUTES.md` (publish next run; reply within three
runs), which now bind; the owner, in his own name, invites two or three people he thinks
could dispute or attest, and the operator does no outreach (`CHARTER.md` P10). The mailbox
of Ask 4 remains the second route, for anyone without a GitHub account, when the owner sets
it up. Meanwhile the map grows where a filing or the owner's review points, and otherwise
by the plan below. Target: five attestations and two disputes handled end to end within the
protocol.

**Checkpoint 2:** at least one dispute has gone through all steps and the exchange reads as
something a philosopher would be glad to have their name on. If the protocol produced
embarrassment, it is amended before the map grows.

**Phase 3 — breadth along lineages.** Extend by dependency, not by alphabet: Hume → Kant;
Spinoza → Schopenhauer; Nietzsche → the twentieth century. Each new lineage ends in a
comparison page. Attestation and dispute remain open throughout.

**Phase 4 — the live literature.** Formalize contemporary arguments from lawfully read
sources, cited, without reproducing the text. By now the map has readers who can check.

## §4. Capacity

One scheduled run per day at 300,000 tokens, of which the adversarial pass has cost
170,000–190,000 of the reviewing agent's own in every content run; a run that writes more
than about fifty nodes reaches the ceiling. The owner's time: one short session a week,
reading what was built and filing notes; nothing in this plan blocks on more.

## §5. Risks tracked

- Quality: a confident wrong formalization is worse than none. Mitigated by P2 (status
  shown), the adversarial pass in each run (a second agent attacks the day's nodes before
  they are committed; in five content runs it has found, each time, valid forms that were
  wrong as reconstructions and attributions the text did not make), and conceding readily.
- Scope: the project dies of breadth before it has depth. Mitigated by Checkpoint 1, which
  is now live.
- Silence: no humans dispute or attest. Mitigated by the owner's invitations in Phase 2;
  if after a quarter nobody has, that is a board matter, not a reason to fake it.
- The route: a filing arrives through a GitHub Action that nobody has yet exercised end to
  end, and a run that fails to fire (none is recorded for 2026-10-16 and 2026-10-17) would
  let a dispute's deadline pass unnoticed, while the receipt the filer gets promises a run a
  day. Mitigated by the owner's test (Ask 10) and by the changelog, where a missing entry is
  visible to both seats; not mitigated by anything that fires when a run does not.
- Taste: the site looks like every other site. Mitigated by `DESIGN.md` and Ask 3 (done).
- Sources: zeno.org was unreachable for a whole run; Gutenberg served for Nietzsche. Each
  thinker node says which transcription was used and what it could not verify.
