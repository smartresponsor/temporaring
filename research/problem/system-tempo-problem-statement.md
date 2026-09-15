# System Tempo problem statement

## Status

System Tempo is a **speculative research framework**, not an established physical theory.
This document separates philosophical motivation, mathematical formulation, and candidate
physical claims so that one category cannot silently substitute for another.

## Philosophical motivation

The project asks whether ordinary metric time must always be treated as a fundamental,
independent, uniformly advancing entity, or whether measured time can sometimes be modeled
as a local metric attached to the evolving regime of a system.

The motivating perspective is that an observer is itself a process embedded in a physical
system. A perfectly external observer equipped with an independent universal clock is not an
operational object available to an experiment. This motivates questions about how clocks,
processes, and system evolution are compared. It does **not** establish new physics.

The phrase **system tempo** denotes a possible state-dependent rate associated with system
evolution. Claims that a system can be relatively “faster” or “slower” remain philosophical
or physical hypotheses until an operational comparison is defined.

## Mathematical starting point

For an autonomous finite-dimensional system,

```text
dX/dt = F(X)
```

introduce `Gamma = Gamma(X, p, ...)`:

```text
dX/dt = Gamma(X, p, ...) F(X, p, ...).
```

If `dt/dtau = Gamma^-1`, then by the chain rule `dX/dtau = F(X)` wherever the transformation is regular. The notation alone does not
make `Gamma` physical. The decisive question is whether it changes an invariant or
operationally measurable relation, or only changes how an unchanged trajectory is traversed.

## First scientific problem

The first strict problem is the **Temporal Reparameterization No-Go Problem**:

> Determine whether a proposed tempo factor can be removed by a legitimate change of time
> parameter without changing physically relevant observables.

For a common positive scalar multiplying the complete vector field, the baseline expectation
is preserved state-space orbits. Such a model is not new physics solely because traversal
speed changes.

## Candidate route to nontriviality

For interacting subsystems, a dimensionless relation such as `R_AB = Gamma_A / Gamma_B` may
be relevant when it is symbolically nontrivial on dynamically active components and no single
global reparameterization removes both factors while preserving couplings and observables.
The v0.1 active-factor compatibility filter can detect the first obstruction, but global coupled
compatibility remains a research question rather than a conclusion.

## Open questions

- What exact invariant distinguishes System Tempo from time reparameterization?
- Can a symbolically nontrivial active-component ratio `Gamma_A / Gamma_B` be operationally measured?
- Under what couplings can distinct subsystem tempos not be removed globally?
- What is the minimal physically meaningful clock or reference subsystem?
- Does physical novelty require multiple interacting clocks?
- Which dimensionless observables would change?
- What happens at `Gamma = 0` or when `Gamma` changes sign?
- Are singular tempo factors parameterization failures or physical transitions?
- Can one global `tau` exist across interacting subsystems?
- How should non-autonomous forcing be treated?
- When does tempo coupling modify phase-space geometry rather than traversal speed?
- Which candidate models can be falsified symbolically before numerical simulation?
