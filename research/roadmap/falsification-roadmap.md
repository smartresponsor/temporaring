# Falsification roadmap

Use the cheapest decisive test first.

1. Validate contract and assumptions; reject unsupported model classes explicitly.
2. Simplify tempo factors; test common-scalar reparameterization, singularities, signs,
   symmetries, conservation laws, and known limits.
3. Search for invariant geometry, dimensionless ratios, relative phases/events, and failure of
   one global reparameterization.
4. Only for survivors, integrate ODEs and run bounded parameter sweeps with explicit solver
   versions, tolerances, and provenance.
5. Monte Carlo, GPU, HPC, or learned surrogates require demonstrated scientific need.

A planning heuristic is
`C(H) = w1*N_variables + w2*N_equations + w3*N_parameters + w4*C_solver`.

The weights are not yet canonical. The invariant principle is to spend computation only after
cheap falsification opportunities are exhausted.
