# PHP/Python boundary

The canonical v0.1 transport is:

```text
Symfony
  -> immutable hypothesis JSON
  -> python -m temporaring.runner
  -> machine-readable JSON result
  -> Symfony
```

Symfony Process executes the repository-local Python environment by default, with
`TEMPO_PYTHON` available as an execution override.

JSON Schema is the canonical structural hypothesis contract; Pydantic is the Python
implementation mirror plus semantic validation. The mirror enforces the same required fields,
literal schema version, non-empty canonical strings, closed objects, and strict scalar types,
then adds the documented cross-field dimension checks. The deterministic classifier adds
scientific semantic checks such as active-component selection, symbolic tempo-factor
compatibility, and obvious positivity contradictions; those are experiment logic rather than
structural schema rules. PHP must not create a divergent scientific-input schema.

Expression strings cross a hostile-data boundary even for repository-authored fixtures. Python
therefore parses them with the allowlisted arithmetic/function grammar documented by the
hypothesis contract and resolves names only from declared state variables and parameters plus
the canonical mathematical constants. Unsupported syntax is an execution/validation failure,
not a scientific verdict.

Runner stdout is machine-readable result data. Process failure or malformed JSON is an
execution failure, not a scientific verdict. Symfony also validates the stable result envelope
before it becomes an internal DTO: schema/hypothesis identity, verdict status, classification,
reason, optional transformation, invariant list, and bootstrap provenance must have their
declared scalar/list shapes. A syntactically valid JSON object with a missing or mistyped result
field is therefore also an execution-contract failure rather than a successful scientific run.
