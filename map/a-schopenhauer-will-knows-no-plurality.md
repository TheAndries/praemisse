---
id: a-schopenhauer-will-knows-no-plurality
type: argument
title: If the thing in itself is the will, the will apart from its appearance lies outside time and space and knows no plurality, because plurality is conditioned by time and space, which are no property of the thing in itself
thinker: t-schopenhauer
statement: "Because plurality is conditioned by time and space and thinkable only in them, and time and space are forms of our cognition and no property of the thing in itself, which as such is free of every form of cognition, if the thing in itself is the will, then the will, as such and considered apart from its appearance, lies outside time and space, since to be free of a form of cognition is to lie outside it and the will so considered is what the thing in itself is (the map's bridge), and accordingly knows no plurality, since what lies outside time and space has nothing of what is thinkable only in them (the map's second bridge)."
passages: [p-wwv1-s25-will-outside-time-and-space-knows-no-plurality]
premises:
  - claim: c-schopenhauer-plurality-conditioned-by-time-and-space-not-of-thing-in-itself
  - assumption: "If time and space are forms of our cognition and no property of the thing in itself, the thing in itself as such is free of every form of cognition, and the thing in itself is the will, then the will, as such and considered apart from its appearance, lies outside time and space (the map's bridge for the text's »so liegt er ... außer der Zeit und dem Raum«: to be free of a form of cognition is to lie outside it, and the will considered as the thing in itself is what the thing in itself is)"
  - assumption: "If plurality is thinkable only in time and space, and the will so considered lies outside time and space, then the will so considered knows no plurality (the map's bridge for the text's »demnach«)"
inference: conditional proof, modus ponens twice
conclusion: c-schopenhauer-will-apart-from-appearance-outside-time-and-space-knows-no-plurality
form:
  logic: propositional
  atoms:
    p: plurality is necessarily conditioned by time and space and thinkable only in them
    f1: time and space are forms of our cognition and no property of the thing in itself
    f2: the thing in itself as such is free of every form of cognition
    w: the thing in itself is the will
    o: the will, as such and considered apart from its appearance, lies outside time and space
    m: the will, so considered, knows plurality
  premises:
    - "p and f1 and f2"
    - "(f1 and f2 and w) -> o"
    - "(p and o) -> not m"
  conclusion: "w -> (o and not m)"
status: checked
verified_by: []
disputes: []
depends_on: [c-schopenhauer-plurality-conditioned-by-time-and-space-not-of-thing-in-itself]
supports: [c-schopenhauer-will-apart-from-appearance-outside-time-and-space-knows-no-plurality]
attacked_by: []
replies_to: []
shares_premise_with: []
produced_by: claude-fable-5-1, 2026-10-13
---
The argument is the first three sentences of § 25: plurality is conditioned by time and
space and thinkable only in them; time and space are shapes of the principle of sufficient
reason, only our form of cognition and no property of the thing in itself; »Ist nun dieses
Ding an sich ... der Wille; so liegt er, als solcher und gesondert von seiner Erscheinung
betrachtet, außer der Zeit und dem Raum, und kennt demnach keine Vielheit«.

What the form captures and what it leaves out. Premise 1 is the one claim, with its three
conjuncts p, f1 and f2; the text predicates »nur unsere Erkenntnißform, nicht Eigenschaft des
Dinges an sich« of our cognition a priori, and of time and space as its shapes, which f1
glosses. The antecedent w is not a premise: the text draws the conclusion
conditionally, with the antecedent qualified as what Schopenhauer believes he has shown
(§ 21, [c-schopenhauer-will-alone-is-thing-in-itself](../../c/schopenhauer-will-alone-is-thing-in-itself/)),
and the conclusion claim keeps the conditional; the passage's last sentence then asserts it
outright, »trifft daher ihn nicht«, and the antecedent is § 21's claim already in the map,
so the map keeps the conditional form and a reader may ask for the discharged argument; the form proves w → (o ∧ ¬m), the claim's
statement atom for atom, and not o ∧ ¬m. Premise 2 is the map's bridge for »so liegt er ...
außer der Zeit und dem Raum«: the text's step is the identification of the will with the thing in itself together with
»frei ist von aller Form der Erkenntniß«, and the bridge says that to be free of a form is
to lie outside it. Premise 3 is the map's bridge for »demnach«: what
lies outside time and space has nothing of what is thinkable only in them. Both are named
as the map's in the statement. The sentence's further step, »ist folglich einer«, from no
plurality to unity, is not formalized; § 23 states the unity and its sense
([c-schopenhauer-will-groundless-and-one](../../c/schopenhauer-will-groundless-and-one/)).
The check says nothing of whether time and space are our form of cognition, which is the
premise Schopenhauer shares with Kant ([c-kant-space-not-of-things-in-themselves](../../c/kant-space-not-of-things-in-themselves/))
nor of whether the thing in itself is the will. JGB 21's »conventioneller Fiktionen« are
cause and effect ([c-nietzsche-cause-and-effect-conventional-fictions](../../c/nietzsche-cause-and-effect-conventional-fictions/)),
and the map reads nothing of it onto space.
