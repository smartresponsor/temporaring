# Experiment contract

The canonical research flow is:

`Hypothesis -> Model -> Experiment -> Run -> Evidence -> Verdict`

An Experiment defines a deterministic question asked of a model. It is distinct from the
hypothesis and from a concrete Run.

The initial experiment is temporal-reparameterization classification: under declared v0.1
assumptions, can the tempo factor be removed by one admissible reparameterization, or must the
hypothesis proceed to stronger analysis? For component-wise factors, the current deterministic
method first removes identically inactive baseline components and tests symbolic active-factor
compatibility through `Gamma_i / Gamma_ref` ratios before issuing a survivor verdict.

Future experiment records should include a stable identifier/version, hypothesis/model
reference, deterministic method identifier, assumptions/preconditions, parameters/tolerances,
expected evidence type, and explicit verdict semantics.

An Experiment is a specification; a Run is one execution in a concrete environment.
Re-running the experiment must not require an LLM.

Cheapest falsification comes first. A planning heuristic is
`C(H) = w1*N_variables + w2*N_equations + w3*N_parameters + w4*C_solver`; the weights are not
yet canonical, but the cost discipline is.
