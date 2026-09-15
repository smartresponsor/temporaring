# System Tempo research specifications

This tree is the durable research specification for **System Tempo**, the research/physical concept investigated by the **Temporaring** engineering component.

The project is falsification-first. A common positive scalar tempo factor multiplying an autonomous vector field often changes only traversal speed, not the state-space trajectory. Component-wise factors are compared only on dynamically active baseline components before any relative-tempo survivor is admitted. “Time runs differently” is therefore not enough for new physics.

## Reading order

1. [`problem/system-tempo-problem-statement.md`](problem/system-tempo-problem-statement.md)
2. [`problem/temporal-reparameterization-no-go.md`](problem/temporal-reparameterization-no-go.md)
3. [`problem/physical-novelty-criteria.md`](problem/physical-novelty-criteria.md)
4. [`specification/v0.1-scope.md`](specification/v0.1-scope.md)
5. [`specification/hypothesis-contract.md`](specification/hypothesis-contract.md)
6. [`specification/experiment-contract.md`](specification/experiment-contract.md)
7. [`specification/verdict-semantics.md`](specification/verdict-semantics.md)
8. [`specification/provenance-contract.md`](specification/provenance-contract.md)
9. [`architecture/research-platform.md`](architecture/research-platform.md)
10. [`architecture/php-python-boundary.md`](architecture/php-python-boundary.md)
11. [`architecture/persistence-boundary.md`](architecture/persistence-boundary.md)
12. [`architecture/reproducibility.md`](architecture/reproducibility.md)
13. [`tasks/v0.1-research-task.md`](tasks/v0.1-research-task.md)
14. [`tasks/open-research-questions.md`](tasks/open-research-questions.md)
15. [`decisions/architecture-decisions.md`](decisions/architecture-decisions.md)
16. [`decisions/scientific-guardrails.md`](decisions/scientific-guardrails.md)
17. [`roadmap/research-roadmap.md`](roadmap/research-roadmap.md)
18. [`roadmap/falsification-roadmap.md`](roadmap/falsification-roadmap.md)
19. [`notes/terminology.md`](notes/terminology.md)

Canonical flow: `Hypothesis -> Model -> Experiment -> Run -> Evidence -> Verdict`.

Hypothesis is the central research object. LLMs may propose or mutate hypotheses, but deterministic code owns implemented scientific verdicts.

Source-controlled material includes specifications, schemas, small canonical fixtures, and documentation. Generated numerical evidence belongs under `artifacts/` rather than Git history.
