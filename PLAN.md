# PLAN.md

Current strategy. Rewritten, with the date, whenever it changes. Last rewritten 2026-10-04
(founding).

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

**Phase 0 — founding (now).** Name and domain (Ask 1). Public repository and routine access
(Ask 2). Three typographic specimens for the owner to choose from (Ask 3). Build pipeline:
`map/` → static site. No content.

**Phase 1 — the chain.** Target: ~40 nodes. Kant: the critique of dogmatic metaphysics, the
distinction of appearance and thing-in-itself, the limits of knowledge (KrV, Prolegomena,
by Akademie page). Schopenhauer: the will as the thing-in-itself, the critique of Kant in
the appendix to WWV I (by section). Nietzsche: the rejection of the thing-in-itself, the
critique of Schopenhauer's will (Jenseits, Götzen-Dämmerung, Nachlass where unavoidable
and marked as such). Every argument with validity checked by machine. One comparison node:
*the thing-in-itself*. All `draft` or `checked`; nothing claimed beyond that.

**Checkpoint 1 (end of Phase 1):** the comparison page exists, the owner reads it against
the texts he knows, and says in writing whether it is better than what he could find
elsewhere. If no, the method is rethought before any breadth.

**Phase 2 — first humans.** The dispute form and the attestation form go live. The owner,
in his own name, invites two or three people he thinks could dispute or attest — Erasmus
contacts, a reading group, whoever he trusts. The operator does no outreach. Target: five
attestations and two disputes handled end to end within the protocol.

**Checkpoint 2:** at least one dispute has gone through all steps and the exchange reads as
something a philosopher would be glad to have their name on. If the protocol produced
embarrassment, it is amended before the map grows.

**Phase 3 — breadth along lineages.** Extend by dependency, not by alphabet: Hume → Kant;
Spinoza → Schopenhauer; Nietzsche → the twentieth century. Each new lineage ends in a
comparison page. Attestation and dispute remain open throughout.

**Phase 4 — the live literature.** Formalize contemporary arguments from lawfully read
sources, cited, without reproducing the text. By now the map has readers who can check.

## §4. Capacity

One scheduled run per day at 300,000 tokens. The owner's time: one short session a week,
reading what was built and filing notes; nothing in this plan blocks on more.

## §5. Risks tracked

- Quality: a confident wrong formalization is worse than none. Mitigated by P2 (status
  shown), the adversarial pass in each run (a second agent attacks the day's nodes before
  they are committed), and conceding readily.
- Scope: the project dies of breadth before it has depth. Mitigated by Checkpoint 1.
- Silence: no humans dispute or attest. Mitigated by the owner's invitations in Phase 2;
  if after a quarter nobody has, that is a board matter, not a reason to fake it.
- Taste: the site looks like every other site. Mitigated by `DESIGN.md` and Ask 3.
