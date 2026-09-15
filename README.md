# Temporaring

Temporaring is the engineering component for the **System Tempo** research program.

The repository intentionally separates orchestration from scientific computation:

- `src/` — Symfony/PHP control plane;
- `python/` — deterministic scientific compute plane;
- `research/` — hypotheses, models, experiment specifications, datasets, and constraints;
- `artifacts/` — generated evidence and run outputs.

Canonical identity:

- repository: `temporaring`;
- component: `Temporaring`;
- research concept: `System Tempo`;
- Composer package: `temporaring/tempo`;
- PHP namespace: `App\\Temporaring\\`;
- subject prefix: `Tempo*`.

The first research target is to classify when a System Tempo factor is a pure time reparameterization and when it survives that no-go filter as a candidate for stronger invariant or operational analysis.

## Research documentation

The durable scientific and engineering specification lives under [`research/`](research/README.md).
Start there for the problem statement, temporal-reparameterization no-go test, physical-novelty
criteria, v0.1 contracts, architecture boundaries, reproducibility requirements, and the
falsification-first roadmap.
