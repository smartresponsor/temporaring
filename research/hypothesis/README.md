# Canonical hypothesis fixtures

This directory contains small source-controlled System Tempo hypotheses used as deterministic
research fixtures.

`common-positive.json` represents a common positive tempo factor. Expected result:
`pure_time_reparameterization / falsified`.

`relative-tempo.json` represents distinct component tempo factors. Expected result:
`relative_tempo_candidate / survived`.

`survived` means only that the hypothesis passed the common-scalar no-go filter; it does not
prove physical novelty.

Both fixtures conform to [`../schema/hypothesis.schema.json`](../schema/hypothesis.schema.json).
New fixtures should remain small, interpretable, and tied to one explicit expected behavior.
