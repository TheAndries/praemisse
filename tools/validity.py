#!/usr/bin/env python3
"""praemisse — the machine validity check for argument nodes (MODEL.md, status `checked`).

An argument node may carry a `form:` block in its front matter:

    form:
      logic: propositional
      atoms:
        a: space is intuited a priori, before the existence of the things in it
        s: space is a determination of things in themselves
      premises: ["a", "s -> not a"]
      conclusion: "not s"

The check asks one question only: is the conclusion true in every assignment of truth
values that makes every premise true? It is answered by exhaustive truth table, so it is
decidable, explainable and, for the handful of atoms an argument has, instant. It says
nothing about whether the premises are true or whether they are what the passage says —
that is fidelity, and only a human settles it (DISPUTES.md).

Syntax: atoms are lowercase identifiers; `not`/`¬`/`~`; `and`/`∧`/`&`; `or`/`∨`/`|`;
`->`/`→` (material conditional, right-associative); `<->`/`↔`; parentheses. Precedence,
tightest first: not, and, or, ->, <->. Up to 16 atoms.

    python3 tools/validity.py 'p' 'p -> q' -c 'q'      # valid
    python3 tools/validity.py 'p -> q' 'q' -c 'p'      # invalid, prints a countermodel
"""
from __future__ import annotations

import argparse
import itertools
import re
import sys
from dataclasses import dataclass

MAX_ATOMS = 16

_TOKEN = re.compile(r"\s*(?:(<->|↔|->|→|¬|~|∧|&|∨|\||\(|\))|([a-z][a-z0-9_]*))")
_WORDS = {"not": "¬", "and": "∧", "or": "∨"}
_SYMS = {"~": "¬", "&": "∧", "|": "∨", "->": "→", "<->": "↔"}


class FormError(ValueError):
    pass


def tokenize(s: str) -> list[str]:
    out: list[str] = []
    pos = 0
    s = s.strip()
    while pos < len(s):
        m = _TOKEN.match(s, pos)
        if not m or m.end() == pos:
            raise FormError(f"cannot read {s[pos:pos + 12]!r} in {s!r}")
        pos = m.end()
        op, atom = m.group(1), m.group(2)
        if atom in _WORDS:
            out.append(_WORDS[atom])
        elif atom:
            out.append(atom)
        else:
            out.append(_SYMS.get(op, op))
    return out


# Formulas are tuples: ('atom', name) | ('¬', f) | (op, f, g) for op in ∧ ∨ → ↔.

class _Parser:
    def __init__(self, tokens: list[str], src: str):
        self.t, self.i, self.src = tokens, 0, src

    def peek(self) -> str | None:
        return self.t[self.i] if self.i < len(self.t) else None

    def take(self, tok: str | None = None) -> str:
        cur = self.peek()
        if cur is None or (tok is not None and cur != tok):
            raise FormError(f"expected {tok or 'a formula'} in {self.src!r}")
        self.i += 1
        return cur

    def parse(self):
        f = self.iff()
        if self.peek() is not None:
            raise FormError(f"unexpected {self.peek()!r} in {self.src!r}")
        return f

    def iff(self):
        f = self.imp()
        while self.peek() == "↔":
            self.take(); f = ("↔", f, self.imp())
        return f

    def imp(self):
        f = self.disj()
        if self.peek() == "→":
            self.take(); return ("→", f, self.imp())
        return f

    def disj(self):
        f = self.conj()
        while self.peek() == "∨":
            self.take(); f = ("∨", f, self.conj())
        return f

    def conj(self):
        f = self.neg()
        while self.peek() == "∧":
            self.take(); f = ("∧", f, self.neg())
        return f

    def neg(self):
        if self.peek() == "¬":
            self.take(); return ("¬", self.neg())
        if self.peek() == "(":
            self.take(); f = self.iff(); self.take(")"); return f
        tok = self.take()
        if not re.fullmatch(r"[a-z][a-z0-9_]*", tok):
            raise FormError(f"expected an atom, got {tok!r} in {self.src!r}")
        return ("atom", tok)


def parse(s: str):
    return _Parser(tokenize(s), s).parse()


def atoms_of(f, acc: set[str] | None = None) -> set[str]:
    acc = set() if acc is None else acc
    if f[0] == "atom":
        acc.add(f[1])
    else:
        for g in f[1:]:
            atoms_of(g, acc)
    return acc


def ev(f, v: dict[str, bool]) -> bool:
    op = f[0]
    if op == "atom":
        return v[f[1]]
    if op == "¬":
        return not ev(f[1], v)
    a, b = ev(f[1], v), ev(f[2], v)
    if op == "∧":
        return a and b
    if op == "∨":
        return a or b
    if op == "→":
        return (not a) or b
    if op == "↔":
        return a == b
    raise FormError(f"unknown operator {op!r}")


def show(f) -> str:
    op = f[0]
    if op == "atom":
        return f[1]
    if op == "¬":
        g = show(f[1])
        return "¬" + (g if f[1][0] in ("atom", "¬") else f"({g})")
    return f"({show(f[1])} {op} {show(f[2])})"


@dataclass
class Verdict:
    valid: bool
    atoms: list[str]
    countermodel: dict[str, bool] | None
    rows: int

    def __str__(self) -> str:
        if self.valid:
            return f"valid: the conclusion holds in all {self.rows} assignments of {', '.join(self.atoms)} that satisfy the premises" if self.rows else "valid (no atoms)"
        cm = ", ".join(f"{k}={'T' if val else 'F'}" for k, val in self.countermodel.items())
        return f"invalid: premises true and conclusion false when {cm}"


def check(premises: list[str], conclusion: str) -> Verdict:
    """Does the conclusion follow from the premises in every assignment? Exhaustive."""
    ps = [parse(p) for p in premises]
    c = parse(conclusion)
    names = sorted(set().union(*(atoms_of(p) for p in ps), atoms_of(c)))
    if len(names) > MAX_ATOMS:
        raise FormError(f"{len(names)} atoms; the limit is {MAX_ATOMS}")
    rows = 0
    for bits in itertools.product((False, True), repeat=len(names)):
        v = dict(zip(names, bits))
        if all(ev(p, v) for p in ps):
            rows += 1
            if not ev(c, v):
                return Verdict(False, names, v, rows)
    return Verdict(True, names, None, rows)


def check_form(form: dict) -> tuple[Verdict | None, list[str]]:
    """Validate a node's `form:` block. Returns (verdict, errors). Errors are reasons the
    block is malformed, not reasons the argument is invalid; an invalid argument is a
    verdict with valid=False."""
    errors: list[str] = []
    if not isinstance(form, dict):
        return None, ["form must be a mapping"]
    if form.get("logic", "propositional") != "propositional":
        errors.append(f"form.logic {form.get('logic')!r} is not supported; only propositional")
    prem = form.get("premises")
    conc = form.get("conclusion")
    atoms = form.get("atoms")
    if not isinstance(prem, list) or not prem or not all(isinstance(p, str) for p in prem):
        errors.append("form.premises must be a non-empty list of formulas")
    if not isinstance(conc, str) or not conc.strip():
        errors.append("form.conclusion must be a formula")
    if not isinstance(atoms, dict) or not atoms or not all(isinstance(k, str) and isinstance(val, str) and val.strip() for k, val in atoms.items()):
        errors.append("form.atoms must map every atom to a one-line gloss")
    if errors:
        return None, errors
    try:
        verdict = check(prem, conc)
    except FormError as e:
        return None, [str(e)]
    used = set(verdict.atoms)
    glossed = set(atoms)
    if used - glossed:
        errors.append(f"atoms without a gloss: {', '.join(sorted(used - glossed))}")
    if glossed - used:
        errors.append(f"glossed atoms that no formula uses: {', '.join(sorted(glossed - used))}")
    return verdict, errors


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="truth-table validity check")
    ap.add_argument("premises", nargs="+")
    ap.add_argument("-c", "--conclusion", required=True)
    a = ap.parse_args(argv)
    try:
        v = check(a.premises, a.conclusion)
    except FormError as e:
        print("error:", e, file=sys.stderr)
        return 2
    print(v)
    return 0 if v.valid else 1


if __name__ == "__main__":
    sys.exit(main())
