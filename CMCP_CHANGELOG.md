# CMCP_CHANGELOG

## 2026-09-11

- Bootstrapped canonical `temporaring` repository skeleton.
- Established Symfony control plane and Python scientific compute plane.
- Fixed canonical identities: `temporaring/tempo`, `App\\Temporaring\\`, `Tempo*`, and research concept `System Tempo`.

## 2026-09-12

- Materialized the System Tempo research problem as durable repository documentation.
- Documented the temporal-reparameterization no-go result and boundary cases.
- Defined candidate physical-novelty criteria centered on invariant and operational observables.
- Specified conservative v0.1 scope, hypothesis/experiment contracts, verdict semantics, and provenance requirements.
- Documented the Symfony control-plane / Python compute-plane architecture, persistence boundary, and reproducibility model.
- Added research and falsification roadmaps plus canonical terminology and open questions.
- No Git commit was created as part of this documentation materialization.
- Classified `config/reference.php` and `python/**/*.egg-info/` as generated artifacts and added ignore rules.
- Confirmed `.gating/` is intended by Gating as a consumer configuration surface, while the existing Temporaring tree contains an obsolete flat-root gate-pack v1 snapshot; the legacy runtime/package files remain untracked and must not be committed wholesale.
- Added current Gating consumer config plus `.gating/profile/component/temporaring.yaml`; the canonical gate now passes with 7 rules, 0 failures, and the database-prefix rule skipped because no Doctrine table declarations exist yet.
- Removed unrelated Cruding/Gating path-reference churn from `composer.lock`, preserving only the intended `symfony/process` runtime lock transition.
- Repaired the Composer `test` script to target `tests/`; PHPUnit now exits successfully and reports that no PHP tests exist yet.
- Restricted the Git-visible `.gating/` surface to current consumer config and `profile/component/temporaring.yaml`, preventing accidental commit of the obsolete bundled runtime snapshot.
- Added durable v0.1 research-task acceptance criteria, an explicit open-question backlog, architecture decision records, and scientific guardrails.
- Completed a final documentation consistency pass: preserved the corrected time-reparameterization relation and made the current JSON Schema/Pydantic parity debt explicit at the PHP/Python boundary and v0.1 task level.

## 2026-09-14

- Reconnaissance baseline: read repository guidance, README, Composer metadata, PHP control-plane source, Python compute contracts/tests, the complete `research/` specification contour, and current Git state.
- Read the required sibling contracts from Objecting, Cruding, Viewing, and Interfacing; confirmed Temporaring currently has no Entity/system-field surface, no generic CRUD controllers/routes, and no presentation implementation that should move into those helpers.
- Read Gating as executable enforcement and Canonization as the normative textual source. Consulted Canon000 (component prefix), Canon001 (technical-role-first tree), Canon002 (interface mirror), Canon007 (literal PSR-4 identity), Canon008 (Composer dependency integrity), Canon009 (component/host boundary), Canon012 (typed boundary contracts), and Canon043 (development Composer dependency versions).
- Target-to-canon mapping: `Tempo*` declarations remain under `App\\Temporaring\\` in role-first `Command`, `DTO`, `Service`, and `ServiceInterface` roots; the runner service/interface pair remains mirrored; no Host implementation dependency is present; decoded Python JSON remains a true dynamic boundary while PHP returns a typed `TempoRunResultDTO`; first-party path dependencies must be normalized to Canon043 `dev-master` identity.
- Market/maturity baseline: mature experiment-tracking systems separate experiment/run identity, immutable configuration/input, provenance/environment, and artifact evidence. Temporaring already follows that architectural direction; RC correctness is therefore prioritized over speculative platform breadth.
- RC-critical workstream selected: make the Pydantic hypothesis mirror structurally no more permissive than the canonical JSON Schema, retain the intentionally stricter semantic dimension checks, add regression tests for rejected contract drift, and normalize first-party local Composer dependencies to Canon043.
- Growth workstream deferred from RC: richer source/dependency fingerprints, experiment/run persistence and replay indexing, artifact comparison UX, and additional operational observability once the v0.1 deterministic contract is sealed.
- Material risk: the worktree entered this run with tracked deletions of `.gating/config/gate.yaml`, `.gating/config/output.yaml`, `.gating/config/severity.yaml`, and `.gating/profile/component/temporaring.yaml`. Those pre-existing user changes are not restored or overwritten by this run; the Composer `gating` script currently fails because `severity.yaml` is absent.
- Planned verification: Composer validation, PHP lint/static analysis/tests, Symfony YAML/container lint, Python contract regressions where an executable path is available, and Gating re-check with any pre-existing configuration blocker reported separately.
- RC implementation completed: sealed the strict Pydantic structural mirror, added negative contract regressions, normalized first-party `dev-master` path identities, exposed the reachable Collectioning/Tabling path closure, and registered their bundles so canonical Cruding services autowire in the standalone Temporaring host.
- Verification results: `bin/check-python.ps1` passed Pyright strict with 0 errors, pytest with 5 passing tests, and both canonical runner smokes; `composer validate --strict --check-lock`, `lint:php`, `lint:yaml`, `lint:container`, PHPStan level 8, and Composer audit all passed. PHPUnit executed successfully but reported `No tests executed!`, reflecting the current empty PHP test surface rather than a test failure.
- Gating remains externally blocked by the pre-existing deletion of `.gating/config/severity.yaml`; the gate exits 2 before rule evaluation. This run deliberately leaves all four pre-existing `.gating` deletions untouched.
