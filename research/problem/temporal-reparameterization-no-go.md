# Temporal Reparameterization No-Go

## Purpose

This is the first falsification filter for System Tempo v0.1. It prevents a change of
parameter from being misidentified as a new physical effect.

## Baseline statement

Consider a smooth autonomous system:

```text
dX/dt = Gamma(X) F(X)
```

on a region where `Gamma(X) > 0`. Along a trajectory define a monotonically increasing
parameter `tau` by `dtau = Gamma(X(t)) dt`. Wherever this transformation is regular:

```text
dX/dtau = F(X).
```

A common scalar under the declared positive-tempo assumption therefore generally changes traversal rate while preserving the state-space orbit. Under the current algebraic v0.1 test this is a **no-go case for physical novelty**; general global regularity and positivity proofs remain separate questions.

## Baseline invariants

The v0.1 classifier currently records:

- state-space orbits;
- fixed points;
- orbit topology.

This list is intentionally narrow and is not a theorem about every time-dependent observable.

## Local versus global transformation

The transformation is straightforward only where `Gamma` is sufficiently regular and
monotonicity is preserved. A local reparameterization does not guarantee one globally valid
time coordinate across an interacting system.

## Boundary cases

- `Gamma = 0`: local invertibility can fail; v0.1 does not decide whether this is only a
  parameterization singularity or a physical transition.
- Sign changes: `tau(t)` need not remain monotonic and flow orientation can reverse.
- Singular/non-smooth factors: poles or discontinuities require separate analysis.
- Multiple factors: for `dx_i/dt = Gamma_i F_i`, one scalar reparameterization removes all
  factors only under additional compatibility conditions.
- Coupled clocks: relative phases or event relations may survive one coordinate change.
- Non-autonomous forcing: explicit external-time dependence must be transformed consistently.

## v0.1 rule

A smooth finite-dimensional autonomous hypothesis with a common positive scalar tempo factor
is classified as `pure_time_reparameterization` with status `falsified`.

For component-wise factors, v0.1 first simplifies the baseline vector field and tempo factors
symbolically. Factors attached only to components whose baseline vector-field component is
identically zero are dynamically inactive and do not create a relative-tempo obstruction. If
the complete baseline vector field is identically zero, tempo factors cannot alter the stated
dynamics and the novelty claim is classified as `tempo_irrelevant_zero_vector_field` /
`falsified`.

For the remaining active components, compatibility is tested through symbolic factor ratios.
If every active `Gamma_i / Gamma_ref` simplifies to `1`, the factors reduce to one common tempo
and the common-tempo rule applies. This ratio test is an algebraic compatibility check for the
stated autonomous vector field; it does not by itself establish global regularity of `tau` over
all trajectories or domains. If active factors remain distinct and positivity is declared,
the hypothesis is classified as `relative_tempo_candidate` with status `survived`: one scalar
time reparameterization cannot remove all active component factors while keeping the stated
baseline vector field unchanged. If the distinct factors are not declared positive, zeros and
sign changes remain unresolved and the classifier returns `sign_indefinite_relative_tempo` with
an `inconclusive` verdict.

A declared positive active factor that simplifies identically to zero contradicts the declared
assumption. v0.1 reports `tempo_assumption_conflict` / `inconclusive` rather than converting that
contract-valid but semantically inconsistent input into a scientific survivor or falsification.

Here `falsified` means falsified **as a claim of physical novelty under this test**, not that
the equations are mathematically invalid. Likewise, `survived` records only failure of this
specific no-go test; it is not evidence of physical novelty.
