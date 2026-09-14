# Hypothesis contract

The canonical machine-readable contract is
[`../schema/hypothesis.schema.json`](../schema/hypothesis.schema.json), using JSON Schema
Draft 2020-12 and `schema_version = "1.0"`.

The JSON Schema is the canonical structural contract. The Python Pydantic model is an implementation mirror plus semantic validation. PHP must not invent an incompatible
scientific-input schema.

Required top-level fields are `schema_version`, `hypothesis_id`, `title`, `system`, and
`assumptions`.

`system` contains ordered `state_variables`, `parameters`, ordered `base_vector_field`
expressions, and `tempo_factors`. v0.1 permits one global factor or one factor per state
component.

`assumptions` contains `smooth`, `finite_dimensional`, and `tempo_positive`.
`tempo_positive` is currently a declared assumption, not a symbolic proof that the expression
is positive everywhere.

Semantic constraints also require `base_vector_field` length to equal the number of state variables and `tempo_factors` to contain either one global factor or one factor per state variable. Those cross-field constraints are currently enforced by the Pydantic implementation rather than encoded in the JSON Schema itself.

The Python Pydantic mirror now matches the canonical structural requirements: required fields have no implicit defaults, `schema_version` is the literal `"1.0"`, canonical strings are non-empty, unknown fields are forbidden, and scalar coercion is disabled. Pydantic additionally enforces the documented cross-field dimension constraints, which remain semantic validation beyond the JSON Schema's structural contract.

Runs should consume immutable hypothesis payloads. Scientific mutation should create a new
identity or preserve explicit parentage rather than silently editing evidence-generating input.
