"""Deterministic reparameterization classifier for System Tempo v0.1."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy

from temporaring.contract import TempoHypothesis


@dataclass(frozen=True)
class TempoClassification:
    classification: str
    status: str
    reason: str
    transformation: str | None
    invariants: tuple[str, ...]


def classify_reparameterization(hypothesis: TempoHypothesis) -> TempoClassification:
    """Classify whether tempo factors are a removable common scalar multiplier."""

    if not hypothesis.assumptions.smooth:
        return TempoClassification(
            classification="outside_v0_1_scope",
            status="inconclusive",
            reason="v0.1 requires smooth dynamics",
            transformation=None,
            invariants=(),
        )

    if not hypothesis.assumptions.finite_dimensional:
        return TempoClassification(
            classification="outside_v0_1_scope",
            status="inconclusive",
            reason="v0.1 is restricted to finite-dimensional ODE systems",
            transformation=None,
            invariants=(),
        )

    factors = hypothesis.system.tempo_factors
    if len(factors) == 1:
        common = True
    else:
        symbols = {
            name: sympy.Symbol(name)
            for name in (*hypothesis.system.state_variables, *hypothesis.system.parameters)
        }
        sympify = getattr(sympy, "sympify")
        simplify = getattr(sympy, "simplify")
        parsed: list[Any] = [sympify(expression, locals=symbols) for expression in factors]
        common = all(bool(simplify(expression - parsed[0]) == 0) for expression in parsed[1:])

    if common and hypothesis.assumptions.tempo_positive:
        factor = factors[0]
        return TempoClassification(
            classification="pure_time_reparameterization",
            status="falsified",
            reason="a positive common scalar tempo factor preserves state-space trajectories",
            transformation=f"d_tau = ({factor}) * dt",
            invariants=("state_space_orbits", "fixed_points", "orbit_topology"),
        )

    if common:
        return TempoClassification(
            classification="sign_indefinite_common_tempo",
            status="inconclusive",
            reason="common scaling is present but positivity was not assumed",
            transformation=None,
            invariants=(),
        )

    return TempoClassification(
        classification="relative_tempo_candidate",
        status="survived",
        reason="distinct component tempo factors can change vector-field direction and relative dynamics",
        transformation=None,
        invariants=(),
    )
