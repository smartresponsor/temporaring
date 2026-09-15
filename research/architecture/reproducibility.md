# Reproducibility architecture

Chat history is not part of the mathematical state of an experiment. The scientific pipeline
must be replayable without the conversation that produced a hypothesis.

The intended chain is:

`immutable hypothesis -> versioned experiment -> code/dependency fingerprint -> deterministic run -> hashed evidence -> verdict`

For the v0.1 reparameterization experiment, replay must include the same symbolic simplification and active-component compatibility rules; changing those rules changes the experiment implementation even when the input hypothesis is byte-identical.

Symfony records lifecycle/provenance metadata. Python executes the scientific method. Git
identifies source code; dependency fingerprints identify the runtime; artifact hashes connect
evidence to the run that generated it.

Specifications, schemas, small fixtures, and documentation are source. Large/repeatable
generated evidence is not.

GPU, HPC, distributed execution, and neural surrogates should be introduced only when a
validated workload requires them.
