# Hypothesis contract

The canonical machine-readable contract is
[`../schema/hypothesis.schema.json`](../schema/hypothesis.schema.json), using JSON Schema
Draft 2020-12 and `schema_version = "1.0"`.

The Python Pydantic model is an implementation mirror. PHP must not invent an incompatible
scientific-input schema.

Required top-level fields are `schema_version`, `hypothesis_id`, `title`, `system`, and
`assumptions`.

`system` contains ordered `state_variables`, `parameters`, ordered `base_vector_field`
expressions, and `tempo_factors`. v0.1 permits one global factor or one factor per state
component.

`assumptions` contains `smooth`, `finite_dimensional`, and `tempo_positive`.
`tempo_positive` is currently a declared assumption, not a symbolic proof that the expression
is positive everywhere.

Runs should consume immutable hypothesis payloads. Scientific mutation should create a new
identity or preserve explicit parentage rather than silently editing evidence-generating input.
