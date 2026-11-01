# Kinhluan Skills

A portable collection of 64 agent skills for software delivery, architecture, security, product leadership, and academic research.

The repository follows the [Agent Skills specification](https://agentskills.io/specification) and can be consumed as a Claude Code plugin, Gemini CLI extension, or skills-compatible source.

## Highlights

- Current five-metric DORA delivery assessment
- C4 Levels 1–4 with container and deployment views kept distinct
- Strategic and tactical DDD, Clean Architecture, and ADRs
- Language, Docker, Kubernetes, API, cloud, and container security workflows
- Product discovery, analytics, UX research, adoption, and strategy
- End-to-end research workflow from SOTA survey to publication and defense
- Authorized security assessment with explicit safety boundaries
- Portable prompt router with tested specificity ranking

See [skills.json](skills.json) for the complete, generated catalog.

## Installation

### Claude Code

```text
/plugin marketplace add kinhluan/skills
/plugin install kinhluan-skills
/reload-plugins
```

Skills are exposed as `kinhluan-skills:<skill-name>`.

### Gemini CLI

```bash
gemini extensions install https://github.com/kinhluan/skills
```

### Skills-compatible agents

```bash
npx skills add kinhluan/skills
```

## Repository Layout

```text
skills/              canonical skill sources and platform discovery root
hooks/hooks.json     portable Claude plugin router hook
scripts/             validation, routing, manifest, and packaging tools
tests/               router regression tests
dist/                committed deterministic .skill archives
skills.json          generated publication manifest
```

Each skill has one authoritative `SKILL.md`. Detailed material belongs in directly linked `references/`; deterministic helpers belong in `scripts/`; output templates/assets belong in `assets/`. The repository intentionally does not maintain a second condensed copy of each skill.

## Development

Install the validation dependency:

```bash
python3 -m pip install -r requirements-dev.txt
```

Then use:

```bash
make sync-manifest  # regenerate skills.json from skills/
make validate       # validate metadata, links, routes, and release config
make test           # run router regression tests
make package        # rebuild deterministic dist/*.skill archives
make check          # validate + test + verify committed archives
```

CI runs `make check`. Release versions in `skills.json`, Claude plugin metadata, the marketplace entry, and `gemini-extension.json` must match.

## Fieldbook

The repository includes a source-driven Astro site in `site/`. It presents the
skill library as the **Kinhluan Fieldbook**, with Ngũ Sự as a strategic lens,
active pursuits, outcome-oriented learning paths, full skill pages, and
client-side catalog search.

```bash
make site-install
make site-dev
make site-check
```

Skill pages are generated directly from `skills.json` and
`skills/*/SKILL.md`; do not maintain a second copy of skill content in the site.
The `Deploy Fieldbook` workflow publishes the static build to GitHub Pages after
changes reach `main`. Repository maintainers must select **GitHub Actions** as
the Pages source once in repository settings.

## Design Principles

- Keep `SKILL.md` under 500 lines and use progressive disclosure.
- Put triggering context in `description`.
- Prefer current primary documentation for time-sensitive claims.
- Treat thresholds as calibrated decisions, not universal laws.
- Keep local implementation authority separate from external or consequential actions.
- Validate generated manifests and archives rather than editing them by hand.

## License

[MIT](LICENSE)
