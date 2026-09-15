# Verdict semantics

Verdicts apply to a **specific implemented test under declared assumptions**.

## `falsified`

The tested claim of physical novelty is rejected by the current deterministic filter. A common
positive scalar tempo factor can be mathematically valid while still being falsified as novel
physics under the v0.1 reparameterization test.

## `survived`

The hypothesis passed one implemented falsification filter and should proceed to stronger
tests. It does **not** mean proved, experimentally validated, physically correct, or preferred
over established theory.

## `inconclusive`

The classifier cannot issue a justified positive or negative result under the available
assumptions or implemented rules.

## `outside_v0_1_scope`

This classification identifies an unsupported model class. Its verdict should ordinarily be
`inconclusive`; unsupported is not equivalent to false.

## Assumption conflicts

A contract-valid payload can still contain semantic assumptions contradicted by symbolic
content. Such cases are `inconclusive`, not survivors. For example, an active tempo factor that
simplifies identically to zero conflicts with a declared `tempo_positive = true` assumption and
is classified as `tempo_assumption_conflict`.

## Dynamically trivial tempo

If the complete baseline vector field is identically zero, component tempo factors cannot
change the stated dynamics. The v0.1 classifier therefore uses
`tempo_irrelevant_zero_vector_field` with status `falsified` for the novelty claim.

## Authority

Final verdicts for implemented experiments are produced by deterministic code. LLMs may
propose hypotheses, transformations, invariants, counterexamples, or experiments, but do not
certify proofs, conservation, stability, or final mathematical verdicts.
