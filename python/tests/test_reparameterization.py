from __future__ import annotations

from typing import Any, cast

import pytest
from pydantic import ValidationError

from temporaring.contract import TempoHypothesis
from temporaring.validator.reparameterization import classify_reparameterization


def test_common_positive_factor_is_pure_reparameterization() -> None:
    hypothesis = TempoHypothesis.model_validate(
        {
            "schema_version": "1.0",
            "hypothesis_id": "common",
            "title": "common",
            "system": {
                "state_variables": ["x", "y"],
                "parameters": [],
                "base_vector_field": ["y", "-x"],
                "tempo_factors": ["1 + x**2"],
            },
            "assumptions": {
                "smooth": True,
                "finite_dimensional": True,
                "tempo_positive": True,
            },
        }
    )

    result = classify_reparameterization(hypothesis)

    assert result.status == "falsified"
    assert result.classification == "pure_time_reparameterization"


def test_distinct_factors_survive_no_go_filter() -> None:
    hypothesis = TempoHypothesis.model_validate(
        {
            "schema_version": "1.0",
            "hypothesis_id": "relative",
            "title": "relative",
            "system": {
                "state_variables": ["x", "y"],
                "parameters": [],
                "base_vector_field": ["-x", "-y"],
                "tempo_factors": ["1 + x**2", "1 + y**2"],
            },
            "assumptions": {
                "smooth": True,
                "finite_dimensional": True,
                "tempo_positive": True,
            },
        }
    )

    result = classify_reparameterization(hypothesis)

    assert result.status == "survived"
    assert result.classification == "relative_tempo_candidate"


def test_symbolically_equal_component_factors_reduce_to_common_tempo() -> None:
    hypothesis = TempoHypothesis.model_validate(
        {
            "schema_version": "1.0",
            "hypothesis_id": "symbolic-common",
            "title": "symbolic common",
            "system": {
                "state_variables": ["x", "y"],
                "parameters": [],
                "base_vector_field": ["-x", "-y"],
                "tempo_factors": ["1 + x", "x + 1"],
            },
            "assumptions": {
                "smooth": True,
                "finite_dimensional": True,
                "tempo_positive": True,
            },
        }
    )

    result = classify_reparameterization(hypothesis)

    assert result.status == "falsified"
    assert result.classification == "pure_time_reparameterization"


def test_distinct_factors_without_positivity_are_inconclusive() -> None:
    hypothesis = TempoHypothesis.model_validate(
        {
            "schema_version": "1.0",
            "hypothesis_id": "relative-sign-indefinite",
            "title": "relative sign indefinite",
            "system": {
                "state_variables": ["x", "y"],
                "parameters": [],
                "base_vector_field": ["-x", "-y"],
                "tempo_factors": ["x", "y"],
            },
            "assumptions": {
                "smooth": True,
                "finite_dimensional": True,
                "tempo_positive": False,
            },
        }
    )

    result = classify_reparameterization(hypothesis)

    assert result.status == "inconclusive"
    assert result.classification == "sign_indefinite_relative_tempo"


def test_distinct_factor_on_inactive_component_does_not_create_relative_tempo() -> None:
    hypothesis = TempoHypothesis.model_validate(
        {
            "schema_version": "1.0",
            "hypothesis_id": "inactive-component",
            "title": "inactive component",
            "system": {
                "state_variables": ["x", "y"],
                "parameters": [],
                "base_vector_field": ["-x", "0"],
                "tempo_factors": ["1 + x**2", "1 + y**2"],
            },
            "assumptions": {
                "smooth": True,
                "finite_dimensional": True,
                "tempo_positive": True,
            },
        }
    )

    result = classify_reparameterization(hypothesis)

    assert result.status == "falsified"
    assert result.classification == "pure_time_reparameterization"


def test_reparameterization_reports_first_active_factor_when_leading_component_is_inactive() -> None:
    hypothesis = TempoHypothesis.model_validate(
        {
            "schema_version": "1.0",
            "hypothesis_id": "leading-inactive-component",
            "title": "leading inactive component",
            "system": {
                "state_variables": ["x", "y"],
                "parameters": [],
                "base_vector_field": ["0", "-y"],
                "tempo_factors": ["1 + x**2", "2 + y**2"],
            },
            "assumptions": {
                "smooth": True,
                "finite_dimensional": True,
                "tempo_positive": True,
            },
        }
    )

    result = classify_reparameterization(hypothesis)

    assert result.status == "falsified"
    assert result.classification == "pure_time_reparameterization"
    assert result.transformation == "d_tau = (2 + y**2) * dt"


def test_zero_vector_field_makes_component_tempo_dynamically_irrelevant() -> None:
    hypothesis = TempoHypothesis.model_validate(
        {
            "schema_version": "1.0",
            "hypothesis_id": "zero-vector-field",
            "title": "zero vector field",
            "system": {
                "state_variables": ["x", "y"],
                "parameters": [],
                "base_vector_field": ["0", "0"],
                "tempo_factors": ["1 + x**2", "1 + y**2"],
            },
            "assumptions": {
                "smooth": True,
                "finite_dimensional": True,
                "tempo_positive": True,
            },
        }
    )

    result = classify_reparameterization(hypothesis)

    assert result.status == "falsified"
    assert result.classification == "tempo_irrelevant_zero_vector_field"


def test_declared_positive_identically_zero_active_factor_is_inconclusive() -> None:
    hypothesis = TempoHypothesis.model_validate(
        {
            "schema_version": "1.0",
            "hypothesis_id": "positivity-conflict",
            "title": "positivity conflict",
            "system": {
                "state_variables": ["x"],
                "parameters": [],
                "base_vector_field": ["-x"],
                "tempo_factors": ["0"],
            },
            "assumptions": {
                "smooth": True,
                "finite_dimensional": True,
                "tempo_positive": True,
            },
        }
    )

    result = classify_reparameterization(hypothesis)

    assert result.status == "inconclusive"
    assert result.classification == "tempo_assumption_conflict"


def valid_hypothesis_payload() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "hypothesis_id": "contract",
        "title": "contract",
        "system": {
            "state_variables": ["x"],
            "parameters": [],
            "base_vector_field": ["-x"],
            "tempo_factors": ["1 + x**2"],
        },
        "assumptions": {
            "smooth": True,
            "finite_dimensional": True,
            "tempo_positive": True,
        },
    }


def test_contract_rejects_noncanonical_schema_version() -> None:
    payload = valid_hypothesis_payload()
    payload["schema_version"] = "2.0"

    with pytest.raises(ValidationError):
        TempoHypothesis.model_validate(payload)


def test_contract_requires_schema_required_fields_without_defaults() -> None:
    payload = valid_hypothesis_payload()
    system = cast(dict[str, Any], payload["system"])
    system.pop("parameters")

    with pytest.raises(ValidationError):
        TempoHypothesis.model_validate(payload)

    payload = valid_hypothesis_payload()
    assumptions = cast(dict[str, Any], payload["assumptions"])
    assumptions.pop("tempo_positive")

    with pytest.raises(ValidationError):
        TempoHypothesis.model_validate(payload)


def test_contract_rejects_empty_strings_and_scalar_coercion() -> None:
    payload = valid_hypothesis_payload()
    system = cast(dict[str, Any], payload["system"])
    system["state_variables"] = [""]

    with pytest.raises(ValidationError):
        TempoHypothesis.model_validate(payload)

    payload = valid_hypothesis_payload()
    assumptions = cast(dict[str, Any], payload["assumptions"])
    assumptions["smooth"] = 1

    with pytest.raises(ValidationError):
        TempoHypothesis.model_validate(payload)


def test_classifier_supports_allowlisted_mathematical_functions() -> None:
    payload = valid_hypothesis_payload()
    system = cast(dict[str, Any], payload["system"])
    system["base_vector_field"] = ["sin(x)**2 + cos(x)**2"]
    system["tempo_factors"] = ["exp(x)"]

    result = classify_reparameterization(TempoHypothesis.model_validate(payload))

    assert result.classification == "pure_time_reparameterization"
    assert result.status == "falsified"


def test_classifier_rejects_undeclared_symbols() -> None:
    payload = valid_hypothesis_payload()
    system = cast(dict[str, Any], payload["system"])
    system["tempo_factors"] = ["1 + z**2"]

    with pytest.raises(ValueError, match="undeclared symbol"):
        classify_reparameterization(TempoHypothesis.model_validate(payload))


@pytest.mark.parametrize(
    "expression",
    [
        "__import__('os').system('echo unsafe')",
        "open('unsafe.txt', 'w')",
        "x.__class__",
        "[x][0]",
    ],
)
def test_classifier_rejects_non_arithmetic_python_syntax(expression: str) -> None:
    payload = valid_hypothesis_payload()
    system = cast(dict[str, Any], payload["system"])
    system["tempo_factors"] = [expression]

    with pytest.raises(ValueError):
        classify_reparameterization(TempoHypothesis.model_validate(payload))
