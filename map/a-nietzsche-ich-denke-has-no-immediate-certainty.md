---
id: a-nietzsche-ich-denke-has-no-immediate-certainty
type: argument
title: "The state expressed in \"I think\" has no immediate certainty, because settling what it is presupposes a comparison with other states I know in myself"
thinker: t-nietzsche
statement: "Because \"I think\" presupposes that I compare my momentary state with other states I know in myself in order to settle what it is, that state refers back to other knowledge, and so has for me at any rate no immediate certainty."
passages: [p-jgb-16-ich-denke-presupposes-comparison]
premises:
  - claim: c-nietzsche-ich-denke-presupposes-comparison
  - assumption: "If \"I think\" presupposes that I compare my momentary state with other states I know in myself, then my momentary state refers back to other knowledge (the map's identification of the comparison with the sentence's »dieser Rückbeziehung auf anderweitiges `Wissen`«, which the demonstrative warrants)"
  - assumption: "If my momentary state refers back to other knowledge, it has for me no immediate certainty (the sentence's »wegen«, which gives the back-reference as the reason; the general principle is instanced here, not stated)"
inference: modus ponens, twice
conclusion: c-nietzsche-ich-denke-has-no-immediate-certainty
form:
  logic: propositional
  atoms:
    c: "\"I think\" presupposes that I compare my momentary state with other states I know in myself, in order to settle what it is"
    b: "my momentary state refers back to other knowledge"
    g: "my momentary state has for me immediate certainty"
  premises:
    - "c"
    - "c -> b"
    - "b -> not g"
  conclusion: "not g"
status: checked
verified_by: []
disputes: []
depends_on: [c-nietzsche-ich-denke-presupposes-comparison]
supports: [c-nietzsche-ich-denke-has-no-immediate-certainty]
attacked_by: []
replies_to: []
shares_premise_with: []
produced_by: claude-fable-5-1, 2026-10-09
---
The argument is one sentence of JGB 16, in the philosopher's mouth: »Genug, jenes `ich
denke` setzt voraus, dass ich meinen augenblicklichen Zustand mit anderen Zuständen, die
ich an mir kenne, vergleiche, um so festzusetzen, was er ist: wegen dieser Rückbeziehung
auf anderweitiges `Wissen` hat er für mich jedenfalls keine unmittelbare `Gewissheit`.«

What the form captures and what it leaves out. Premise 1 is the first half of the
sentence. Premise 2 is the map's identification: the sentence's »dieser Rückbeziehung auf
anderweitiges `Wissen`« names, by its demonstrative, the comparison just described, and
the map reads the comparison as a back-reference to other knowledge. Premise 3 is the
»wegen«: the back-reference is given as the reason for the lack of immediate certainty,
and the map reads that reason as a conditional holding in this instance; the sentence
does not state the general principle that whatever refers back to other knowledge lacks
immediate certainty, and the map does not attribute it. Both assumptions are the map's
and a reader may dispute either. The grammatical subject of »hat er ... keine unmittelbare
`Gewissheit`« is »meinen augenblicklichen Zustand« (»was er ist«), not »jenes `ich
denke`«, which is neuter; the atoms and the conclusion claim speak of the state
accordingly, and JGB 17 says the same of the »Ich«
([c-nietzsche-es-denkt-already-an-interpretation](../../c/nietzsche-es-denkt-already-an-interpretation/)).
The form does not cover the ground of premise 1, the sentence before (»wonach sollte ich
abmessen, dass, was eben geschieht, nicht vielleicht `Wollen` oder `Fühlen` sei?«), nor
the »Reihe von verwegenen Behauptungen« the aphorism lists before that. The aphorism
opens with Schopenhauer's »ich will« as a second alleged immediate certainty
([c-nietzsche-schopenhauer-ich-will-a-superstition](../../c/nietzsche-schopenhauer-ich-will-a-superstition/))
and does not run this analysis for it; the conclusion here is about »ich denke« alone.
