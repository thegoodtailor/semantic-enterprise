# Brief — The Creole Redesign: CASL for the Agentic Era

**Status: GATED — awaiting Iman's rulings. No prose moves until gated.**
Date: 2026-08-27. Trigger: Iman — "it began with me saying 'wouldn't it be good to have
a version of CASL, to illustrate how pushouts work' but in a world of free text
understood by an AI. this COULD be a genuinely innovative piece of computer science —
instead we have yards of pseudo-LookML and boring stuff about how to do joins."

## 1. Diagnosis

The creole currently mixes two languages wearing one name. The *semantic* constructs —
prose `def` axioms, `assert` with `born_of`, bridges with declared losses, `trust`,
`populated by`, `standing`, `deprecated ... why` — are the innovation. The *mechanical*
constructs — `grain (order_id)`, `op cpty_of : Fill -> Counterparty asof (exec_ts)`,
cardinality clauses, join plumbing — are compile-target material (what LookML/schema.yml
already say) wearing algebra costume. From the Reflexive Loop onward the blocks get
longer and the mechanical fraction rises, so the reader experiences escalating
config-reading instead of escalating ideas. The pushout — the thing the notation was
invented to illustrate — never appears IN the notation at all; it lives in prose and
diagrams while the notation shows joins.

## 2. The idea, stated as the computer science it is

> **The creole is an algebraic specification language in the CASL lineage whose
> sentences are natural language.** Signatures stay small and formal (concepts, arrows,
> grains). Axioms are English prose. Satisfaction is operationalized by two interpreters:
> a *stochastic* one — the LLM that loads the prose as context and reasons under it —
> and a *deterministic* one — the executable `assert` fragment, refutation run on every
> scan. Structuring is inherited intact from the specification-composition calculus
> (Poernomo–Crossley–Wirsing): **rename, hide, and union-along-a-shared-subtheory — the
> pushout — as visible language constructs.** Semantics is *loose semantics disciplined
> by refutation*: a prose axiom admits many readings; the asserts cut the reading space;
> the calibration ledger measures the residual gap. In institution terms: Sen = English,
> and ⊨ splits into calibrated interpretation plus executable refutation.

Why it is genuinely new, said with the prior art on the table (goes in 15b):
- **CASL** had model-theoretic semantics nobody could afford to check; **OWL** had
  decidable semantics nobody could afford to write; the creole has prose semantics
  anyone can write and a refutation semantics machines can check.
- **Attempto ACE** and controlled natural languages translate English *into* logic —
  English as sugar, formal semantics primary. The creole keeps prose as the semantic
  carrier; the machine interprets, it does not translate.
- **Gherkin/BDD** is the executable-NL discipline (scenarios + step bindings) — kin on
  the refutation side, with no algebra: no signatures, no structuring, no pushouts.
- **LookML/MetricFlow/schema.yml** are the compile targets — the institution morphism
  out of the creole, not rivals to it.
The novel object is the combination: algebraic structuring over natural-language
sentences with a stochastic interpreter disciplined by deterministic refutation, and
drift between the two interpreters measured as a first-class quantity.

## 3. The pushout, finally in the syntax

The construct the whole notation was conceived for, as language (illustrative draft —
grammar wording is Iman's to tune):

```
spec TradingAndFinance =
  glue Trading with Finance along TradeIdentity
    // TradeIdentity: the sub-theory both domains sign — trade & account identity,
    // and the equality they agree on. The pushout apex, named.
    rename Finance.position  to booked_position   // polysemy survives by renaming,
                                                  // never by overwriting
    hide   Finance.gl_leg_detail                  // lost on the Trading side — and says so
    partial Trading.desk_assignment               // survives only where a desk is mapped
```

Three consequences: (a) morphism honesty stops being commentary and becomes operators —
a declared loss IS a `hide`, a partiality IS `partial`, resolution of polysemy IS
`rename`; (b) the mesh's commutativity check has a syntactic home (the `glue` block is
what it re-verifies); (c) the ch3 P&L composition and ch5's session each get a
three-line block instead of a paragraph of hand-waving.

## 4. The split: semantic core vs. binding layer

- **Semantic core** (the creole proper; what chapters show): `spec/domain`, concept
  names, prose `def` axioms, `assert`/`born_of`, `glue/along/rename/hide/partial`,
  `trust`, `populated by`, `standing`, `deprecated ... why`.
- **Binding layer** (appendix only, explicitly named as the compile-target surface):
  grains, `asof` arrows, cardinalities, join mechanics — shown ONCE, next to the
  schema.yml/LookML they compile to, labeled "bindings: where the creole touches an
  engine." The pseudo-LookML stops pretending to be the language.

## 5. Landing plan (on gate approval)

1. **ch4 "The Creole"** rewritten around §2: lineage paragraph (CASL → his calculus →
   sentences-in-English), the two-interpreter semantics in four sentences, the Trading
   example slimmed to semantic core, one `glue` block at Multi-Domain Composition.
2. **ch3**: the P&L register composition gets its three-line `glue` block (the worked
   pushout the chapter now does in prose).
3. **ch12 (Reflexive Loop)**: the four fund definitions STAY — under the new framing
   they are the showcase (prose axioms + refutation, exactly the thesis); any
   mechanical residue trimmed.
4. **10b / ch8 blocks**: already mostly semantic core; light trim.
5. **Appendix**: card split into "The Semantic Core" (one page, the language) and
   "The Binding Layer" (mechanics + compile-down, shown against real tool YAML once).
6. **15b**: the departure claim added to the Goguen section — sentences = English,
   satisfaction = calibrated interpretation + refutation — with the prior-art honesty
   (ACE, Gherkin) alongside; this is the book's second-edition-CS seed next to hocolim.
7. **Proposal**: differentiator #6 upgraded from "vendor-neutral notation" to the CS
   claim, one sentence.

## 6. Gates — Iman rules

//@ Q1 (the claim): §2 is a claim in YOUR field, stated on your behalf. Certify the
wording (especially "Sen = English, ⊨ splits into calibrated interpretation plus
executable refutation") or rewrite it in your own hand — this is hocolim-register.
//@ Q2 (syntax): approve `glue ... with ... along ...` + `rename/hide/partial` as the
structuring surface (CASL's and your calculus's operators, renamed for prose), or tune
the keywords.
//@ Q3 (the split): approve demoting grain/asof/cardinality to a named Binding Layer
in the appendix (chapters show semantic core only)?
//@ Q4 (ch12 fund definitions): keep all four as the showcase (my recommendation), or
thin to two in-chapter with two in the appendix?
//@ Q5 (scope of the claim): does the two-interpreter semantics claim stay a sober
paragraph in 15b, or does it deserve a short named subsection in ch4 ("What Kind of
Language Is This?") — my recommendation: both, one paragraph each, no more.
