# PHP/Python boundary

The canonical v0.1 transport is:

```text
Symfony
  -> immutable hypothesis JSON
  -> python -m temporaring.runner
  -> strict JSON result
  -> Symfony
```

Symfony Process executes the repository-local Python environment by default, with
`TEMPO_PYTHON` available as an execution override.

JSON Schema is the conceptual canonical hypothesis contract; Pydantic mirrors it in Python.
PHP must not create a divergent scientific-input schema.

Runner stdout is machine-readable result data. Process failure or malformed JSON is an
execution failure, not a scientific verdict.
