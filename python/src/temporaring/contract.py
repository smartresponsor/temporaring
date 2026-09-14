"""Typed contract mirror for the canonical System Tempo hypothesis schema."""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator


NonEmptyString = Annotated[str, StringConstraints(min_length=1)]


class TempoAssumptions(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    smooth: bool
    finite_dimensional: bool
    tempo_positive: bool


class TempoSystem(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    state_variables: list[NonEmptyString] = Field(min_length=1)
    parameters: list[NonEmptyString]
    base_vector_field: list[NonEmptyString] = Field(min_length=1)
    tempo_factors: list[NonEmptyString] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_dimensions(self) -> "TempoSystem":
        dimension = len(self.state_variables)
        if len(self.base_vector_field) != dimension:
            raise ValueError("base_vector_field must match state_variables dimension")
        if len(self.tempo_factors) not in (1, dimension):
            raise ValueError("tempo_factors must contain one global factor or one factor per state variable")
        return self


class TempoHypothesis(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    schema_version: Literal["1.0"]
    hypothesis_id: NonEmptyString
    title: NonEmptyString
    system: TempoSystem
    assumptions: TempoAssumptions
