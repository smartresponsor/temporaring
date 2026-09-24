"""Deterministic reparameterization classifier for System Tempo v0.1."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy

from temporaring.contract import TempoHypothesis
from temporaring.expression import parse_expression


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
    symbols = {
        name: sympy.Symbol(name)
        for name in (*hypothesis.system.state_variables, *hypothesis.system.parameters)
    }
    simplify = getattr(sympy, "simplify")

    if len(factors) == 1:
        active_factors = factors
    else:
        base_components: list[Any] = [
            parse_expression(expression, symbols)
            for expression in hypothesis.system.base_vector_field
        ]
        active_factors = [
            factor
            for factor, component in zip(factors, base_components, strict=True)
            if not bool(simplify(component) == 0)
        ]

        if not active_factors:
            return TempoClassification(
                classification="tempo_irrelevant_zero_vector_field",
                status="falsified",
                reason="the baseline vector field is identically zero, so tempo factors do not change the dynamics",
                transformation=None,
                invariants=("state_space_orbits", "fixed_points", "orbit_topology"),
            )

    parsed: list[Any] = [parse_expression(expression, symbols) for expression in active_factors]
    simplified = [simplify(expression) for expression in parsed]
    has_zero_factor = any(bool(expression == 0) for expression in simplified)

    if hypothesis.assumptions.tempo_positive and has_zero_factor:
        return TempoClassification(
            classification="tempo_assumption_conflict",
            status="inconclusive",
            reason="tempo_positive is declared but an active tempo factor simplifies identically to zero",
            transformation=None,
            invariants=(),
        )

    reference = simplified[0]
    if bool(reference == 0):
        common = all(bool(expression == 0) for expression in simplified[1:])
    else:
        compatibility_ratios = [simplify(expression / reference) for expression in simplified[1:]]
        common = all(bool(ratio == 1) for ratio in compatibility_ratios)

    if common and hypothesis.assumptions.tempo_positive:
        factor = active_factors[0]
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

    if not hypothesis.assumptions.tempo_positive:
        return TempoClassification(
            classification="sign_indefinite_relative_tempo",
            status="inconclusive",
            reason=(
                "distinct component tempo factors obstruct one common scalar reparameterization, "
                "but positivity was not assumed so zeros or sign changes remain unresolved"
            ),
            transformation=None,
            invariants=(),
        )

    return TempoClassification(
        classification="relative_tempo_candidate",
        status="survived",
        reason=(
            "positive distinct component tempo factors obstruct one common scalar "
            "reparameterization and may change vector-field direction or relative dynamics"
        ),
        transformation=None,
        invariants=(),
    )
