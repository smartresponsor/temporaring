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
