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
then adds the documented cross-field dimension checks. PHP must not create a divergent
scientific-input schema.

Runner stdout is machine-readable result data. Process failure or malformed JSON is an
execution failure, not a scientific verdict.
