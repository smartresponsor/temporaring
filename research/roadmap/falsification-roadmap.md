# Falsification roadmap

Use the cheapest decisive test first.

1. Validate contract and assumptions; reject unsupported model classes explicitly.
2. Simplify the baseline vector field and tempo factors; restrict compatibility analysis to dynamically active components and test whether active `Gamma_i / Gamma_ref` ratios reduce to `1`.
3. For non-common survivors, investigate singularities, signs, invariant geometry, dimensionless ratios, relative phases/events, symmetries, conservation laws, known limits, and failure of one global reparameterization.
4. Only for survivors, integrate ODEs and run bounded parameter sweeps with explicit solver
   versions, tolerances, and provenance.
5. Monte Carlo, GPU, HPC, or learned surrogates require demonstrated scientific need.

A planning heuristic is
`C(H) = w1*N_variables + w2*N_equations + w3*N_parameters + w4*C_solver`.

The weights are not yet canonical. The invariant principle is to spend computation only after
cheap falsification opportunities are exhausted.
