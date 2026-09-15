# Provenance and reproducibility contract

Every scientific verdict should be reproducible from immutable inputs and a sufficiently
specified execution environment without requiring the LLM that may have proposed a hypothesis.

Target run provenance includes:

- hypothesis hash and experiment hash;
- source-code commit SHA;
- Python version and dependency fingerprint;
- solver/classifier name and version;
- parameters and tolerances;
- random seed when stochastic work exists;
- input and output artifact hashes;
- timestamp.

The current runner already records input SHA-256, Python version, and SymPy version. That is a
bootstrap, not the final provenance model. Because v0.1 classifications depend on symbolic
simplification, the recorded SymPy version is part of scientific replay context rather than
incidental runtime metadata.

For LLM-originated hypotheses also record model identifier, prompt hash, parent hypothesis ID,
and mutation reason.

Replay must verify immutable inputs and environment, execute deterministic code, and compare
declared outputs without requiring live LLM access.
