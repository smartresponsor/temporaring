# Architecture decisions

This document records current design decisions so future implementation does not silently drift from the research architecture.

## Repository and execution boundary

Symfony/PHP and Python live in the same `temporaring` repository. Python is a bounded compute subsystem under `python/`, not a separate repository or network service.

Symfony is the control plane and owns orchestration, lifecycle, persistence, commands/APIs, artifact references, and policy concerns.

Python is the deterministic scientific compute plane. It owns symbolic and numerical scientific work and must remain independently runnable from immutable inputs.

## Transport and persistence

The v0.1 PHP/Python boundary is local subprocess execution through Symfony Process with machine-readable JSON input/output governed by the research contracts. HTTP, gRPC, daemons, and distributed workers are deferred.

Python does not write directly to the application database. Symfony owns persistent state and stores run metadata, verdicts, provenance, and artifact references.

## Contract authority

The canonical scientific input contract is machine-readable JSON Schema. Pydantic mirrors that contract in Python. PHP must not define a divergent scientific schema.

## Tooling placement

Pyright configuration belongs in the root of the same Symfony repository while Python source and its virtual environment remain under `python/`.

## Research authority

`Hypothesis` is the central scientific object. `Agent` and `Prompt` are auxiliary orchestration concepts and cannot become authorities for mathematical verdicts. Symbolic compatibility and assumption-conflict decisions belong to deterministic experiment code and must remain replayable from immutable input.

## Generated evidence

Specifications, schemas, small fixtures, and documentation are source-controlled. Generated scientific evidence belongs in `artifacts/` or future object storage, referenced by immutable hashes and metadata.

## Deferred complexity

GPU/HPC, queues, remote workers, neural surrogates, and agent swarms are introduced only after a measured workload demonstrates the need.
