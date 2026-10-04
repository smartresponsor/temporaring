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

## 2026-09-15

- Fresh local reconnaissance confirmed `master` at `0280fba5bbaf4ed34ce5b751f4589399924a1fc8`, with no upstream configured and only the same four pre-existing tracked `.gating/` deletions dirty before this work.
- Confirmed the JSON Schema/Pydantic parity debt from the older transfer note is already closed in the authoritative local state: literal schema version, required fields, strict scalar types, closed objects, and regression coverage are present.
- Tightened the v0.1 relative-tempo compatibility classification: symbolically equivalent component factors remain removable common tempo; positive distinct factors remain `relative_tempo_candidate` / `survived`; distinct factors without a positivity assumption now return `sign_indefinite_relative_tempo` / `inconclusive` because zeros and sign changes remain unresolved.
- Corrected the root README so v0.1 no longer implies that a surviving factor already produces invariant observables; survivors are only candidates for stronger invariant or operational analysis.
- Added deterministic regressions for symbolic common-factor reduction and sign-indefinite distinct factors.
- `bin/check-python.ps1` passed with Pyright strict at 0 errors/warnings/informations, 11 pytest tests passing, and both canonical runner smoke fixtures returning their expected scoped verdicts.
- The four pre-existing `.gating/` deletions remain untouched and are excluded from the scope of this work.
- Extended the compatibility test to active baseline components using symbolic `Gamma_i / Gamma_ref` ratios; tempo factors attached only to identically zero baseline components no longer create false relative-tempo survivors.
- Added deterministic handling for an identically zero baseline vector field (`tempo_irrelevant_zero_vector_field` / `falsified`) and for declared positivity contradicted by an active factor simplifying to zero (`tempo_assumption_conflict` / `inconclusive`).

## 2026-09-16 — PHP executable-test baseline and RC revalidation

### Reconnaissance and canon mapping
- Re-read Temporaring root guidance, Composer/runtime source, the complete documented `research/` reading order (problem, specification, architecture, tasks, decisions, roadmaps, terminology), and required Objecting, Cruding, Viewing, Interfacing, Gating, and Canonization contracts.
- Consulted authoritative Canonization rules Canon000, Canon001, Canon002, Canon003, Canon007, Canon008, Canon018, Canon019, Canon020, Canon021, Canon022, Canon023, Canon024, Canon025, Canon026, Canon029, Canon030, Canon032, Canon033, Canon034, Canon036, Canon038, Canon039, Canon041, Canon043, Canon044, and Canon045 where applicable.
- Canon039 mapping: Temporaring contains executable production PHP but previously had no repository-owned PHPUnit config, no persistent coverage script, and `composer test` exited successfully with `No tests executed!`.
- RC-critical workstream: establish a real executable PHP regression/coverage contract without changing System Tempo scientific semantics. Growth remains richer run provenance, experiment persistence/replay indexing, artifact comparison, and additional deterministic experiments after v0.1 correctness is sealed.

### Material implementation
- Added repository-owned `phpunit.xml.dist` with `src/` as the explicit production coverage population.
- Added three PHP regressions for `TempoRunResultDTO::classification()` covering canonical classification, missing classification, and invalid non-string classification fallback.
- Updated Composer `test` to use the repository PHPUnit configuration and added persistent `test:coverage` output at `var/coverage/summary.txt`.
- Adjusted the coverage invocation from unsupported PHPUnit-10 `--branch-coverage` to supported `--path-coverage`, preserving branch/path-aware php-code-coverage collection.

### Verification and boundaries
- `composer validate --strict`: PASS.
- PHP lint: PASS before the test addition; PHPUnit itself then caught an initially truncated new test file, which was repaired immediately.
- `composer test`: PASS, 3 tests / 3 assertions.
- `composer phpstan`: PASS, 7 files / 0 errors.
- `composer lint:yaml`: PASS, 5 files.
- `composer lint:container`: PASS.
- `composer test:coverage`: PASS with PHPUnit 10.5.64 + Xdebug 3.5.1 and persistent coverage output.
- `composer gating` remains blocked before rule evaluation by the pre-existing deletion of `.gating/config/severity.yaml`; all four pre-existing tracked `.gating` deletions remain intentionally untouched.
- Canon041 remains a separate standalone-application tooling requirement to assess/close; this pass does not fabricate Playwright/UI coverage for a repository that currently has no established browser UI test surface.

## 2026-09-16 — Canon041 browser/application test-tooling closure

### Canon mapping and decision
- Read Canon041 and Canon042 together. Canon041 is a hard standalone-Symfony tooling contract: Symfony Test Pack, Panther, repository-local Playwright dependency/config, and reproducible PHPUnit/Playwright execution paths. Canon042 is a separate runtime warning contract when explicit behavioral/UI coverage inventories are missing; it forbids treating passing test counts as a fabricated coverage percentage.
- RC-critical work therefore closes Canon041 tooling only. No synthetic browser workflow or invented UI denominator is created for the current Temporaring repository, which has no established interactive product UI surface. Canon042 evidence remains measurable post-RC debt until real functional/behavioral/UI surfaces exist and can be inventoried honestly.

### Material implementation
- Upgraded PHPUnit from the incompatible 10.5 line to `^11.5.55`; Composer resolved 11.5.56.
- Added `symfony/test-pack ^1.2` and `symfony/panther ^2.2`; Composer resolved Test Pack 1.2.0 and Panther 2.4.0 plus BrowserKit/CSS Selector/WebDriver test dependencies.
- Added repository-local `package.json`, `package-lock.json`, `@playwright/test ^1.54.0`, `playwright.config.js`, and standard `npm test -> test:e2e` execution. The Playwright command intentionally permits zero browser tests until an actual UI surface is owned by Temporaring.
- Added `/test-results/` and `/playwright-report/` to `.gitignore`; generated browser-test output remains outside source history.
- Composer package-scoped dependency resolution refreshed the root lock to current compatible Symfony 8.1 patch packages and current local first-party path-package references; no sibling repository source was modified by this run.

### Verification
- `composer validate --strict --check-lock`: PASS.
- `composer test`: PASS on PHPUnit 11.5.56, 3 tests / 3 assertions.
- `composer test:coverage`: PASS with Xdebug 3.5.1 and persistent path/branch-aware summary.
- `composer phpstan`: PASS, 0 errors.
- `composer lint:yaml`: PASS, 5 files.
- `composer lint:container`: PASS after one Console MCP timeout retry; the successful retry reports a valid container.
- `npm test`: PASS through Playwright configuration with no fabricated browser tests.
- `npm audit`: PASS, 0 vulnerabilities.
- `composer audit`: PASS, no security advisories.
- `composer gating`: still exits 2 before rule evaluation because pre-existing `.gating/config/severity.yaml` is deleted. The four pre-existing `.gating` deletions remain untouched and are not part of this commit.

## 2026-09-17 — RC coverage, quality, and executable-canon closure

### Reconnaissance and market baseline
- Re-read Temporaring guidance, README, Composer manifests, PHP runtime/test surfaces, and the existing execution journal; preserved the four pre-existing tracked `.gating/` deletions as external state.
- Reused the required Objecting, Cruding, Viewing, Interfacing, Gating, and Canonization contour already read for this repository and mapped the current pass to Canon029, Canon030, Canon039, Canon040, Canon041, Canon042, Canon043, Canon044, and Canon045.
- Current reproducible-research practice emphasizes machine-readable environments/dependencies, deterministic reruns, and separation of source from generated evidence/provenance. Temporaring's `src/`, `python/`, `research/`, and `artifacts/` split already follows that direction; RC work therefore stayed on reproducibility and executable acceptance rather than speculative experiment-platform breadth.

### Material implementation
- Added `TempoRuntimeCoverageTest` covering the command success and invalid-input contracts, a real PHP-to-Python execution of the canonical `common-positive.json` hypothesis, and fail-closed missing-hypothesis behavior.
- Raised persistent PHP coverage from lines 8.33% / methods 28.57% / branches 100% to lines 90.91% / methods 85.71% / branches 84.62%, closing Canon040 without synthetic assertions.
- Added repository-owned `phpstan.neon`, Composer PHP-CS-Fixer check/fix scripts, and explicit schema validation/migration-currentness scripts using isolated in-memory SQLite test DSNs.
- Added repository-owned `config/tempo_gating_profile.yaml` and `config/tempo_gating_rules.yaml`; the Gating command now executes the installed `gating/gate` policy directly and does not restore or depend on the deleted legacy `.gating` consumer files.

### Verification and residual debt
- `composer validate --strict --check-lock`: PASS.
- `composer cs:check`: PASS after line-ending normalization of the new test.
- `composer phpstan`: PASS, 0 errors.
- `composer test:coverage`: PASS, 7 tests / 13 assertions; Canon040 PASS at 90.9% lines, 85.7% methods, 84.6% branches.
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings, pytest 11/11, both canonical runner smoke fixtures returned expected scoped verdicts.
- `composer schema:parity`: PASS; Doctrine mapping is valid and migrations report up to date on the isolated test contour.
- `composer gating`: PASS with 36 rules, 0 failures, 1 warning, 4 skipped. The sole warning is Canon042 because no honest behavioral/UI coverage inventory exists yet.
- The four pre-existing `.gating/` deletions remain untouched and excluded from this pass.

## 2026-09-24 — scientific expression boundary hardening

### Reconnaissance baseline
- Re-read the repository guidance, root README/Composer manifests, complete documented `research/` reading order, PHP control plane, Python compute plane, tests, schema, Gating profile/rule set, and current Git state.
- Current worktree entered this run with unrelated/concurrent changes in `.gating/README.md`, `composer.json`, `composer.lock`, `composer.prod.json`, and untracked `.gating/config/`; this pass does not absorb or overwrite those changes.
- Read the mandatory sibling responsibility contracts from Objecting, Cruding, Viewing, and Interfacing and confirmed this hardening remains inside Temporaring's deterministic scientific-compute boundary: no Entity/system-field, generic CRUD, rendering, shell, or navigation ownership moves into Temporaring.
- Read Canonization as the normative textual source and Gating as executable enforcement. Consulted Canon018 directly for package/namespace identity and Canon012 for typed dynamic-boundary handling; existing role-first `App\\Temporaring\\` PHP structure remains unchanged and applicable canon stays authoritative over local historical patterns.
- Code Memory scope discovery reports no declared `memory:scope:resolve` Composer script, so no repository memory graph is available through the declared contract in this workspace.

### Market and maturity baseline
- Mature durable-workflow systems separate lifecycle orchestration from execution history/replay, while temporal-modeling practice distinguishes audit/history semantics from workflow state. Temporaring therefore keeps workflow/event-store concerns outside its bounded responsibility.
- SymPy's current documentation explicitly warns that `sympify()` evaluates string input and must not be used with unsanitized input. Temporaring currently feeds hypothesis expressions from JSON directly into `sympify()`, making the expression parser both a security boundary and a scientific-integrity boundary.
- RC-critical workstream: replace eval-backed string parsing with a deterministic allowlisted arithmetic/function parser constrained to declared state variables and parameters; add regression coverage and document the expression grammar.
- Growth workstream remains separate: richer provenance/dependency fingerprints, persisted run/replay indexing, artifact comparison UX, and stronger coupled-system/global-reparameterization experiments.

### Canon mapping and implementation
- Canon011: unsupported or malformed expressions fail observably as validation/execution errors; no scientific success-like fallback is introduced.
- Canon012: raw JSON remains a dynamic ingress boundary, while Pydantic models and the dedicated expression parser establish the typed/validated internal contract before classification.
- Canon017: updated the hypothesis contract and PHP/Python boundary documentation to describe the actual restricted expression grammar and fail-closed behavior.
- Canon018: package identity remains `temporaring/tempo`, PHP root remains `App\\Temporaring\\`, and no PHP naming/tree migration was required.
- Objecting, Cruding, Viewing, and Interfacing manifests/contracts were checked where present; the selected change is non-applicable to their owned entity/system-field, generic CRUD, rendering, and shell surfaces. Temporaring and Interfacing have no root `MANIFEST.json`; no manifest was invented.
- Added `python/src/temporaring/expression.py`: an AST-based, eval-free parser with bounded input/AST size, declared-symbol resolution, arithmetic operators, canonical constants, and an explicit one-argument mathematical-function allowlist.
- Routed both base-vector-field and tempo-factor parsing through that parser. Added regressions for supported functions, undeclared symbols, imports/system calls, file calls, attribute access, and subscripting.
- Added `/.console-mcp/` to `.gitignore` because guarded verification creates local execution metadata that is not repository source.

### Verification and residual debt
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings/informations, pytest 17/17, and both canonical runner smoke fixtures returned their expected v0.1 verdicts.
- `composer validate --strict --check-lock`: PASS.
- `composer cs:check`: PASS.
- `composer phpstan`: PASS, 0 errors.
- `composer test`: PASS, 7 tests / 13 assertions.
- `composer lint:yaml`: PASS, 7 YAML files valid.
- `composer lint:container`: PASS.
- `composer schema:parity`: PASS; Doctrine mapping valid and migrations up to date on isolated in-memory SQLite test DSNs.
- `composer audit`: PASS; no security vulnerability advisories found.
- Initial `composer gating` bootstrap failed before rule evaluation because installed vendor metadata still exposed the prior `Gating\\Gate\\` autoload while the already-current lock records `App\\Gating\\`. A source-preserving `composer install --no-scripts` synchronized generated vendor state to the existing lock.
- Re-run `composer gating`: PASS with 36 rules, 0 failures, 1 warning, 4 skipped. The only warning remains Canon042 (behavioral/UI coverage evidence missing); it is pre-existing, explicit, and unrelated to the scientific-expression boundary.
- No remote or upstream is configured on local `master`; publication cannot be performed without inventing repository integration state.

## 2026-09-25 — Canon042 measurable behavioral coverage closure

### Reconnaissance and market baseline
- Re-read the authoritative execution specification, repository guidance, root manifests, PHP command/runner/test surfaces, System Tempo problem/no-go/v0.1/roadmap documents, and the current orchestration journal. The worktree entered this pass with concurrent changes in `.gating/README.md`, `composer.json`, `composer.lock`, `composer.prod.json`, and untracked `.gating/config/`; those surfaces were preserved rather than absorbed.
- Re-read required Objecting, Cruding, Viewing, Interfacing, Gating, and Canonization contracts. Consulted Canon018, Canon019, Canon041, Canon042, Canon043, and Canon052 directly; Canon042 was the only executable Gating warning at baseline.
- Market comparison: mature experiment systems such as MLflow and DVC make run inputs/results/artifacts and reproducibility metadata explicit. Temporaring already separates research specification, deterministic compute, and generated evidence; RC therefore stays focused on measurable acceptance evidence rather than adding a tracking SaaS layer.
- RC-critical workstream: close Canon042 with a reproducible repository-owned application-surface inventory that measures the existing CLI and deterministic classification workflow without inventing browser/UI surfaces.
- Growth workstream remains post-RC: richer run provenance/dependency fingerprints, persisted experiment/run replay indexing, artifact comparison UX, and stronger coupled-system/global-reparameterization research.

### Material implementation
- Added `tools/qa/tempo-behavioral-ui-coverage.js`. The producer fails closed if the canonical `tempo:hypothesis:run` declaration or its functional/integration regressions drift, then writes schema `behavioral-ui-coverage-v2` evidence under `var/coverage/behavioral-ui.json`.
- Changed repository-local `npm test` to run the complete behavioral evidence workflow: PHPUnit, Playwright execution, then deterministic evidence production.
- Inventoried functional `command:tempo:hypothesis:run`, behavioral/critical `workflow:hypothesis-classification`, and an explicitly empty UI denominator because Temporaring currently owns no interactive browser surface.

### Verification and integration state
- First npm gate exposed a truncated producer tail with a Node syntax error; repaired it and re-ran the full workflow.
- `npm test`: PASS; PHPUnit 7 tests / 13 assertions, Playwright execution PASS with no invented UI tests, evidence emitted as functional 1/1, behavioral 1/1, UI 0/0, critical 1/1.
- `composer gating`: PASS with 36 rules, 0 failures, 0 warnings, 4 skipped; Canon042 now passes at 100% for every applicable dimension, with UI 0/0 treated as an explicit empty denominator.
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings/informations, pytest 17/17, and both canonical runner smoke fixtures returned expected v0.1 verdicts.
- `composer cs:check`: PASS; `composer phpstan`: PASS; `composer test`: PASS; `composer lint:php`: PASS; `composer schema:parity`: PASS; `composer validate --strict --check-lock`: PASS.
- Local `master` HEAD is `8c79582c8b05249f2327c5c9a05022f3a3d49c8e`; no `origin` or upstream is configured, so push/PR publication remains factually unavailable. Concurrent pre-existing dirty files remain outside this pass.

## 2026-09-26 — PHP/Python result-envelope hardening

### Reconnaissance and baseline
- Re-read the authoritative execution specification, repository guidance, current research architecture/task contracts, PHP runner/DTO/tests, Python contract/runner/classifier, Composer/package scripts, current Git state, and the existing orchestration journal.
- Re-read the required Objecting, Cruding, Viewing, Interfacing, Gating, and Canonization contours. Normative Canonization files consulted directly for this pass include Canon001, Canon002, Canon012, Canon019, Canon021, Canon022, Canon043, and Canon045; the broader configured rule set remains executable through Temporaring Gating.
- Target-to-canon mapping: `Command/`, `DTO/`, `Service/`, and mirrored `ServiceInterface/` already satisfy Canon001/002; no alternative layer taxonomy or generic CRUD surface exists (Canon019/021); the decoded Python JSON is a legitimate dynamic boundary, but its stable result envelope must become a validated typed internal contract under Canon012.
- Market/maturity baseline: mature experiment platforms track run inputs, metadata, outputs/artifacts, and reproducibility context; DVC similarly makes experiment pipeline dependencies/outputs explicit. Temporaring already owns deterministic local execution and provenance bootstrap, so RC correctness is prioritized over adding a tracking SaaS or distributed execution layer.
- RC-critical workstream selected: fail closed when Python returns syntactically valid JSON with a missing or mistyped stable result field. Growth remains persisted run indexing/replay, richer dependency fingerprints, artifact comparison UX, and broader scientific experiments.
- Pre-existing dirty state was preserved: `.gating/README.md`, `composer.json`, `composer.lock`, `composer.prod.json`, and untracked `.gating/config/` were present before this pass and are not treated as this pass's implementation.

### Material implementation
- Hardened `TempoRunResultDTO` so the stable Python result envelope is validated at construction: schema version, hypothesis ID, status, classification, reason, optional transformation shape, invariant list, and bootstrap provenance.
- Removed the former `classification() -> "unknown"` fallback; malformed result contracts now raise an execution error instead of being representable as a successful internal run.
- Added negative PHPUnit regressions for missing/non-string classification and incomplete provenance.
- Updated the PHP/Python boundary documentation to state that syntactically valid but structurally malformed result JSON is an execution-contract failure.

### Verification
- `composer lint:php`: PASS.
- `composer cs:check`: PASS; 0 fixable files.
- `composer phpstan`: PASS; 0 errors.
- `composer test`: PASS; 12 tests / 25 assertions.
- `composer test:coverage`: PASS; Canon040 evidence is lines 94.5%, methods 87.5%, branches 92.6%, all above canonical thresholds.
- `composer lint:yaml`: PASS; 7 YAML files valid.
- `composer lint:container`: PASS.
- `composer schema:parity`: PASS; Doctrine mapping valid and migrations up to date on isolated test DSNs.
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings/informations, pytest 17/17, and both canonical runner fixtures returned their expected v0.1 envelopes.
- Symfony runtime smoke `tempo:hypothesis:run research/hypothesis/common-positive.json --env=test`: PASS through the real PHP/Python boundary with `pure_time_reparameterization`.
- `npm test`: PASS; PHPUnit 12/25, Playwright execution succeeded with the repository's explicit empty UI denominator, and behavioral evidence regenerated as functional 1/1, behavioral 1/1, UI 0/0, critical 1/1.
- `composer validate --strict --check-lock`: PASS.
- Composer audit: PASS; no vulnerability advisories. npm audit at high threshold: PASS; 0 vulnerabilities.
- Final `composer gating`: PASS with 36 rules, 0 failures, 0 warnings, 4 intentional skips; Canon040 and Canon042 are fresh and green.
- No browser/mobile/UI implementation changed, so screenshot/visual-flow evidence is not applicable to this pass.
- Git integration scope is limited to the five owned files from this pass; the pre-existing Composer/Gating dirty state is excluded. No `origin` or upstream is configured, so publication is factually unavailable.

## 2026-09-28 — RC security false-positive remediation

### Reconnaissance baseline
- Read the authoritative engine specification, repository guidance, Composer/Gating manifests, existing CMCP journal, current Git state, and the supplied CanonScanning security/Inspecting reports.
- Preserved pre-existing dirty state in `.gating/README.md`, `composer.json`, `composer.lock`, `composer.prod.json`, and untracked `.gating/config/`; no destructive cleanup, stash, reset, or sibling-repository mutation is permitted.
- Verified required application dependencies Objecting, Cruding, Viewing, and Interfacing are declared as development path/symlink dependencies and production package dependencies; read their available root contracts together with Gating and Canonization references.
- Consulted Canon034 (generated/local state stays outside source history) and Canon052 (consumer `.gating/` is artifact-only; normative Gating configuration belongs in canonical application configuration).
- Fresh Inspecting evidence for fingerprint `87c8f5d0db58511f56cebc1a0fb1912b9d80180f7da1941a6eb0cd01fd06815b` reported zero PHP-structure findings; the analyzer envelope also records a Semgrep timeout, so only the successful PHP-structure result is reused as GREEN evidence.
- Fresh security evidence was RED solely because `security.secret_leak` scanned `python/.venv/Lib/site-packages/pydantic/types.py`, i.e. installed virtual-environment dependency code already excluded by `.gitignore`.

### RC-critical workstream
- Keep secret scanning enabled while excluding only the repository-local generated Python virtualenv through the supported `component.secret_scan_excluded_paths` profile contract.
- Do not suppress evidence strings, disable the rule, patch Pydantic, or mutate the Gating owner repository.
- Growth work remains separate from RC: richer experiment provenance/replay/indexing, artifact comparison, UX, and additional operational observability.

### Canon mapping
- Canon034 -> `python/.venv/` remains ignored generated/local dependency state and must not become source history.
- Canon052 -> the scanner exception is owned by `config/tempo_gating_profile.yaml`, not consumer `.gating/` policy/config snapshots.
- Gating `GateSecretLeakRule` -> `secret_scan_excluded_paths` is merged with default exclusions while `secret_scan: enabled` remains active.

### Material implementation
- Added `python/.venv/**` to `component.secret_scan_excluded_paths` in `config/tempo_gating_profile.yaml`; no source-security scope outside that generated dependency tree is reduced.

### Verification and acceptance
- Initial full `composer gating` exposed a real dependency-closure blocker after the security profile repair: current Viewing/Cruding require `failing/failure`, but Temporaring did not yet declare/register it.
- Added `failing/failure` as a development path/symlink dependency, production package dependency, and standalone Symfony bundle; also closed production Collectioning/Tabling parity required by the current platform baseline.
- Normalized `.gating/` to Canon052 artifact-only topology and restored its consumer-boundary README; executable/normative configuration remains under Symfony `config/` and the Gating package.
- Applied Canon055 neutral platform terminology in `AGENTS.md`.
- `composer gate`: PASS, 9 rules, 0 failed, 0 warning; `security.secret_leak` PASS with 444 files scanned.
- `composer gating`: PASS, 36 rules, 0 failed, 0 warning, 4 intentional skips.
- `composer validate --strict --check-lock`: PASS.
- `composer cs:check`: PASS; 0 fixable files.
- `composer phpstan`: PASS; 0 errors.
- `composer test`: PASS; 12 tests / 25 assertions.
- `composer lint:yaml`: PASS; 7 YAML files.
- `composer lint:container`: PASS.
- `composer schema:parity`: PASS; Doctrine mapping valid and migrations up to date on isolated SQLite test DSNs.
- `npm test`: PASS; Playwright path executed with the explicit UI denominator and regenerated behavioral coverage evidence (functional 1/1, behavioral 1/1, UI 0/0, critical 1/1).
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings/informations, pytest 17/17, and both canonical runner fixtures returned expected v0.1 envelopes.
- Composer audit: PASS; no security vulnerability advisories.
- Post-mutation Inspecting report `D--PhpstormProjects-www-temporaring-20260928-102820.json`: PASS for executed analyzers with 0 findings, PHPStan 0 errors, and clean PHP-structure metrics. Semgrep is not claimed GREEN because it was not present in the successful analyzer set.
- No browser/mobile/UI implementation changed, so screenshot or visual-flow evidence is not applicable.
- Composer/lock changes that pre-dated this execution window were reviewed and retained only where they form a coherent, tested RC dependency/tooling state; the incorrect pre-existing `.gating/README.md` replacement was repaired instead of committed.

## 2026-09-29 — Canon052 consumer-artifact remediation

### Baseline and evidence
- Upstream CanonScanning Gating report was RED on the consumer `.gating/` topology; fresh Inspecting PHP-structure evidence contained zero findings, while Semgrep timed out and is not claimed as GREEN evidence.
- Baseline local `master` HEAD was `89aa638349e7e14099eb6ee7fec9f3cc1ab08f44`, with no upstream configured. The only Git-visible dirty path was `.gating/README.md`, replaced by the Gating package README.
- Required Objecting, Cruding, Viewing, and Interfacing runtime dependencies and local sibling path/symlink repositories are declared in the root Composer manifest.

### Canonization mapping
- Consulted Canon052 directly: consumer `.gating/` is artifact-only and must not contain copied Gating engine/policy/runtime trees.
- Consulted Canon045 for root local repository closure and Canon036 for documentation producer ownership; neither requires an application-source change for this remediation.
- Repository AGENTS remains authoritative for `App\\Temporaring\\`, Symfony 8/PHP 8.4, technical-role-first structure, and the prohibition on Domain/Port/Adapter/Adaptor trees.

### Market and workstreams
- Current reproducible-workflow practice represented by Nextflow, Snakemake, and DVC emphasizes reproducible execution, explicit versioned inputs/artifacts, and traceable lineage. Temporaring's scientific compute/control-plane separation remains directionally aligned.
- RC-critical workstream: restore the deterministic Gating consumer boundary and acceptance gates.
- Growth workstream: richer immutable run/environment fingerprints, portable provenance, and experiment lineage remain post-RC and do not block this Canon052 repair.

### Material implementation
- Preserved the entire contaminated `.gating/` tree non-destructively under `var/temporaring/2026-09-29/engine-20260930020513-temporaring-046d13/quarantine/gating-contamination/`.
- Recreated `.gating/README.md` as the minimal non-executable artifact-boundary document. No reset, clean, delete, or runtime restart was used.

### Verification
- `composer validate --strict --check-lock`: PASS.
- `composer gating`: PASS, 36 rules, 0 failures, 0 warnings, 4 intentional skips; Canon052 contamination is no longer reported.
- `composer cs:check`: PASS; `composer phpstan`: PASS with 0 errors.
- `composer test`: PASS, 12 tests / 25 assertions; `composer test:coverage`: PASS with Canon040 evidence at 94.5% lines, 87.5% methods, 92.6% branches.
- `composer lint:yaml`, `composer lint:container`, and `composer schema:parity`: PASS.
- `npm test`: PASS; behavioral evidence functional 1/1, behavioral 1/1, UI 0/0, critical 1/1. No user-observable UI changed, so screenshots are not applicable.
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings/informations, pytest 17/17, both canonical scientific smoke fixtures passed.
- Post-mutation Inspecting was attempted repeatedly through the standalone quality capability. Two long invocations exceeded the connector window; a bounded 30-second probe returned `INSPECTING_FAILED` with no stdout/stderr. The earlier long invocation also removed the tracked `.gating/README.md` as a side effect; the file was restored byte-for-byte and a subsequent bounded Inspecting probe left the worktree clean. Inspecting source confirms analyzer-local timeouts (Semgrep 60s, PHPStan/Rector 300s), while the orchestration call can terminate earlier without analyzer diagnostics. This is an Inspecting execution-plane blocker, not a Temporaring deterministic-gate failure; post-mutation Inspecting remains NOT_VERIFIED.
- Final Git inspection before commit: only `CMCP_CHANGELOG.md` is dirty; `.gating/README.md` is restored byte-for-byte to tracked canonical state. No origin/upstream is configured, so publication is unavailable without inventing remote state.

## 2026-10-03 — engine-20261003235424-temporaring-7e4996

### Baseline and canon mapping
- Re-read the authoritative task specification, repository guidance, current Composer/runtime source, research entrypoint, supplied CanonScanning reports, required Objecting/Cruding/Viewing/Interfacing contracts, Gating, and Canonization.
- Fresh upstream fingerprint `46d2ab90724b68c772305e6f6562cf1630e903e6cd62f1ceddf5ad9233125fc1`: Inspecting reports zero PHP-structure findings; Semgrep timed out and is not claimed GREEN. Gating is RED only on Canon052; Canon031 is a warning.
- Consulted normative Canon052 and Canon031. Canon052 requires consumer `.gating/` to be artifact-only while the installed `gating/gate` package owns executable policy/runtime. Canon031 requires >=70% meaningful class and contract-method PHPDoc coverage independently.
- Target-to-canon mapping remains Symfony-oriented: `App\\Temporaring\\`, role-first `Command`, `DTO`, `Service`, `ServiceInterface`, no `src/Domain`, Port/Adapter/Adaptor taxonomy, no component-local generic CRUD, and no local Objecting system-field or UI ownership.

### Market and workstreams
- Compared current experiment/reproducibility practice represented by MLflow, Sacred, DVC, and Snakemake: run metadata/configuration, provenance/artifacts, reproducible pipelines, and portable reporting are mature expectations.
- RC-critical workstream stays bounded to deterministic PHP/Python execution, provenance/result contracts, canonical packaging/Gating, documentation quality, tests, and diagnostics.
- Growth workstream remains separate: persisted experiment/run registry, comparisons/dashboard UX, distributed workflow scheduling, cache orchestration, richer portable reports, and additional scientific capability.

### Material implementation
- Preserved the complete contaminated consumer `.gating/` tree non-destructively at `var/temporaring/2026-10-03/engine-20261003235424-temporaring-7e4996/gating-contamination/` and recreated the tracked artifact-only `.gating/README.md`; no delete/reset/clean/stash operation was used.
- Added meaningful documentation for the exact Canon031 weak symbols in the command, result DTO, kernel, runner service, and service interface without changing behavior.
- Preserved the pre-existing `AGENTS.md` Canonization-precedence change as coherent in-scope guidance pending final Git reconciliation.

### Verification and acceptance
- `composer validate --strict --check-lock`: PASS.
- Initial post-mutation `composer gating`: 0 failures; Canon040 and Canon042 were stale-evidence warnings only. Regenerated PHPUnit and behavioral evidence, then re-ran Gating: PASS, 36 rules, 0 failures, 0 warnings, 4 intentional skips; coverage is 94.5% lines / 87.5% methods / 92.6% branches and behavioral evidence is functional 1/1, behavioral 1/1, UI 0/0, critical 1/1.
- `composer gate`: PASS, 10 rules, 0 failures, 0 warnings, 2 intentional skips; secret scan passed over 77 source files.
- `composer quality`: PASS; PHP-CS-Fixer reports no fixable files, PHPStan 0 errors, PHPUnit 12 tests / 25 assertions, repository gate GREEN.
- `composer lint:php`, `composer lint:yaml`, `composer lint:container`, and `composer schema:parity`: PASS.
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings/informations, pytest 17/17, and both canonical System Tempo smoke fixtures returned their expected result envelopes.
- Composer audit and npm audit at high severity: PASS, no vulnerability advisories/findings.
- Fresh post-mutation Inspecting report `D:\\PhpstormProjects\\www\\Inspecting\\.inspecting\\reports\\D--PhpstormProjects-www-temporaring-20261004-000617.json`: GREEN for executed analyzers, PHPStan 0 errors and PHP-structure 0 findings. Semgrep was not part of this successful run and is not claimed GREEN.
- No browser/mobile/UI implementation changed. Existing behavioral test tooling executed through `npm test`; visual screenshots are not applicable to this remediation.
- Post-verification worktree contains only the pre-existing `AGENTS.md` change plus this run's journal and five PHPDoc-only source changes; verifier-generated evidence remains under ignored `var/` surfaces.

## 2026-10-03 — engine-20261004031235-temporaring-76b164

### Reconnaissance and evidence reconciliation
- Resolved `D:\\PhpstormProjects\\www\\temporaring` through Console MCP; baseline `master` worktree was clean.
- Re-read target `AGENTS.md`, README, Composer/package manifests, current PHP source/tests, Gating profile/rules, research entrypoint plus provenance/PHP-Python/reproducibility/roadmap contracts, and the Python package manifest.
- Re-read required Objecting, Cruding, Viewing, Interfacing, Gating, and Canonization root contracts. Consulted authoritative Canon052 directly together with its executable Gating mirror; target-to-canon mapping remains `App\\Temporaring\\`, role-first Symfony structure, no Domain/Port/Adapter/Adaptor tree, no local generic CRUD, and consumer `.gating/` artifact-only.
- Compared mature experiment/reproducibility practice represented by MLflow and DVC: explicit run metadata, versioned inputs/configuration, provenance, and inspectable artifacts remain the relevant baseline. RC-critical work stays on deterministic execution, provenance/contracts, canonical tooling integration, tests, and diagnostics; persisted run registry/dashboard/distributed orchestration remain growth work.
- Reconciled supplied CanonScanning evidence: the 2026-09-29 Gating report is historical RED on Canon052, while current repository state no longer reproduces it. Supplied Inspecting evidence had zero PHP-structure findings with a Semgrep timeout; the newer local Inspecting report `D--PhpstormProjects-www-temporaring-20261004-000617.json` is GREEN for PHPStan and PHP-structure with zero findings.

### Verification and runtime classification
- `composer gating`: PASS, 36 rules, 0 failures, 0 warnings, 4 intentional skips; Canon040 remains 94.5% lines / 87.5% methods / 92.6% branches and Canon042 remains functional 1/1, behavioral 1/1, UI 0/0, critical 1/1.
- `composer quality`: PASS; PHP-CS-Fixer clean, PHPStan 0 errors, PHPUnit 12 tests / 25 assertions, repository gate 0 failures / 0 warnings.
- `npm test`: PASS; PHPUnit, Playwright execution, and behavioral evidence producer all completed successfully with no invented UI denominator.
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings/informations, pytest 17/17, and both canonical System Tempo smoke fixtures returned expected result envelopes.
- `composer lint:yaml`, `composer lint:container`, and `composer schema:parity`: PASS; Composer validate --strict --check-lock and Composer audit also PASS.
- Reuse-first runtime probe found no Console-MCP-managed PHP server on port 8000. An unmanaged listener answered HTTP 500, but target `var/log` was empty and target source has no matching request-id middleware signature; no restart was performed and this listener is not accepted as Temporaring behavioral evidence.
- No browser/mobile/UI implementation changed, so visual screenshots are not applicable; the repository's explicit UI denominator remains 0/0.

## 2026-10-03 — engine-20261004032853-temporaring-bac517

### Reconnaissance and evidence reconciliation
- Resolved `D:\\PhpstormProjects\\www\\temporaring` through Console MCP. Baseline `master` HEAD is `3b75d22192723cffd591d44109109687b7fb7a2f`, with a clean worktree and no configured upstream/remote.
- Read the authoritative task specification, target guidance/README/Composer/runtime source, research entrypoint, supplied CanonScanning Gating and Inspecting reports, and required Objecting, Cruding, Viewing, Interfacing, Gating, and Canonization contracts.
- Consulted normative Canon052 and Canon031 plus the executable Canon052 mirror. Current mapping remains `App\\Temporaring\\`, role-first Symfony structure, no `src/Domain`, Port/Adapter/Adaptor taxonomy, no component-local generic CRUD, and consumer `.gating/` artifact-only.
- The supplied 2026-09-29 Gating RED is historical for the current tree: `.gating/composer.json` is absent, `.gitignore` restricts `.gating/` to the non-executable boundary README, and fresh `composer gating` passes Canon052.
- Supplied Inspecting evidence reports zero PHP-structure findings; its Semgrep timeout remains non-GREEN analyzer evidence.

### Market and workstreams
- Mature experiment/workflow practice represented by MLflow, DVC, and Nextflow emphasizes versioned run inputs, explicit provenance, inspectable artifacts, reproducibility, and portable execution state.
- RC-critical workstream remains deterministic PHP/Python execution, result/provenance contracts, canonical Gating/package integration, tests, diagnostics, and reproducible verification.
- Growth workstream remains separate: persisted run registry/comparison UX, richer data/code/environment lineage, distributed workflow scheduling, and expanded System Tempo experiments.

### Current acceptance baseline
- `composer validate --strict --check-lock`: PASS.
- `composer gating`: PASS, 36 rules, 0 failures, 0 warnings, 4 intentional skips; Canon040 is 94.5% lines / 87.5% methods / 92.6% branches and Canon042 is functional 1/1, behavioral 1/1, UI 0/0, critical 1/1.
- `composer quality`: PASS; PHP-CS-Fixer clean, PHPStan 0 errors, PHPUnit 12 tests / 25 assertions, repository gate 0 failures / 0 warnings.
- No user-observable UI implementation changed in this execution window; visual evidence is not applicable unless a later mutation creates an interactive surface change.

### Final verification and integration
- `bin/check-python.ps1`: PASS; Pyright 0 errors/warnings/informations, pytest 17/17, and both canonical scientific smoke fixtures returned their expected result envelopes.
- `composer schema:parity`: PASS; Doctrine mapping is valid and migrations are up to date on isolated in-memory SQLite test DSNs.
- `npm test`: PASS; PHPUnit 12 tests / 25 assertions, Playwright execution succeeded with the explicit empty UI denominator, and behavioral evidence regenerated as functional 1/1, behavioral 1/1, UI 0/0, critical 1/1.
- Post-journal Inspecting report `D:\\PhpstormProjects\\www\\Inspecting\\.inspecting\\reports\\D--PhpstormProjects-www-temporaring-20261004-034210.json`: GREEN for executed analyzers; PHPStan 0 errors and PHP-structure 0 findings. Semgrep was not part of this successful run and is not claimed GREEN.
- No browser/mobile/UI implementation changed, so screenshot/visual-flow evidence is not applicable to this execution window.
- Final Git diff/status and coherent signed commit remain as the integration tail; no remote/upstream was configured at baseline, so publication must not be invented.


