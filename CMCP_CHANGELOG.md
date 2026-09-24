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

