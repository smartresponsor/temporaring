from __future__ import annotations

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
