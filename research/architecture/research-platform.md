# Research platform architecture

Temporaring contains two execution planes in one repository.

## Symfony/PHP control plane

Symfony owns orchestration, persistent application state, run lifecycle, artifact references,
policy/presentation concerns, and command/API entry points.

## Python deterministic compute plane

Python owns scientific contract validation, symbolic classification, numerical solvers when
justified, and deterministic evidence generation. It must remain independently runnable.

Python stays under `python/` in this repository; it is not a separate service or repository.
The v0.1 boundary is a local subprocess, not HTTP, gRPC, or a daemon.

The architecture must allow scientific results to be reproduced without an LLM. Agents may
propose or mutate hypotheses but are auxiliary to deterministic scientific execution.
