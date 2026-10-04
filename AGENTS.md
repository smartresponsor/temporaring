# Temporaring repository guidance

Follow the platform Canonization and Gating repositories as the authoritative architecture and executable enforcement sources.

- PHP baseline: 8.4+.
- Symfony baseline: 8.1+ within Symfony 8.x.
- Root namespace: `App\\Temporaring\\`.
- Technical role comes before subject in `src/`.
- Do not introduce `src/Domain`, Port/Adapter/Adaptor, or subject-first trees.
- Component-owned PHP types use the `Tempo*` subject prefix when applicable.
- Component-owned YAML filenames use the `tempo_` prefix unless they are framework/vendor bootstrap files.
- Keep Python scientific execution isolated under `python/` and deterministic at the PHP/Python boundary.
- Generated research evidence belongs under `artifacts/` and must not be treated as source code.
## Platform Canon Precedence

For work under `D:\PhpstormProjects\www`, authoritative platform rules live in the Canonization repository. Gating is the executable mirror for objectively guardable rules. This `AGENTS.md` is an agent-facing projection or local supplement and must not override or contradict Canonization.

If a local instruction conflicts with current Canonization, follow Canonization and synchronize this file. Local instructions may narrow scope or add repository-specific constraints only when they remain compatible with Canonization.
