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

A common positive scalar therefore generally changes traversal rate while preserving the
state-space orbit. Under the current test this is a **no-go case for physical novelty**.

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

Here `falsified` means falsified **as a claim of physical novelty under this test**, not that
the equations are mathematically invalid.
