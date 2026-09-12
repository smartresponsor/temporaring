# Persistence boundary

Symfony owns persistent application state. The Python compute plane must not write directly to
the application PostgreSQL database.

Python receives explicit input, computes, and returns result data or artifact references. It
remains stateless relative to the application database.

Likely future persisted concepts include Hypothesis, Model, Experiment, ExperimentRun,
Constraint, Result, Verdict, Artifact, Dataset, AgentDecision, and ModelVersion. This is a
roadmap, not an instruction to create all entities prematurely.

Generated numerical output belongs under `artifacts/` for the current filesystem-backed phase.
The database should prefer metadata, hashes, provenance, and references. Object storage may
replace filesystem artifacts later.
