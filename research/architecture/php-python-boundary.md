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

JSON Schema is the canonical structural hypothesis contract; Pydantic is the current Python
implementation mirror plus semantic validation. The current runner validates through Pydantic
and does not yet guarantee exact JSON-Schema parity. PHP must not create a divergent
scientific-input schema.

Runner stdout is machine-readable result data. Process failure or malformed JSON is an
execution failure, not a scientific verdict.
