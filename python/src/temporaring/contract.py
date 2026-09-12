"""Typed contract mirror for the canonical System Tempo hypothesis schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, model_validator


class TempoAssumptions(BaseModel):
    model_config = ConfigDict(extra="forbid")

    smooth: bool = True
    finite_dimensional: bool = True
    tempo_positive: bool = True


class TempoSystem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    state_variables: list[str] = Field(min_length=1)
    parameters: list[str] = Field(default_factory=list)
    base_vector_field: list[str] = Field(min_length=1)
    tempo_factors: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_dimensions(self) -> "TempoSystem":
        dimension = len(self.state_variables)
        if len(self.base_vector_field) != dimension:
            raise ValueError("base_vector_field must match state_variables dimension")
        if len(self.tempo_factors) not in (1, dimension):
            raise ValueError("tempo_factors must contain one global factor or one factor per state variable")
        return self


class TempoHypothesis(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: str
    hypothesis_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    system: TempoSystem
    assumptions: TempoAssumptions = Field(default_factory=TempoAssumptions)
