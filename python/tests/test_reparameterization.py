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
