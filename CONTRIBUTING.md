# Contributing

Thanks for improving the collection.

## Add or Change a Skill

1. Work in `skills/<skill-name>/`; this is the canonical source and platform discovery tree.
2. Keep the directory and frontmatter `name` identical, lowercase, and hyphenated.
3. Write a concrete `description` that explains capability and activation context.
4. Keep `SKILL.md` below 500 lines. Move detailed examples or domain references into `references/` and link every reference directly from `SKILL.md`.
5. Add a deterministic helper under the skill's `scripts/` only when repeated execution benefits from it; test it.
6. Add or update the route in `scripts/skill_router.py` and cover ambiguous behavior in `tests/`.
7. For a new skill, add one row to the matching group in the README **Skill Catalog**, and raise that group's count in its `<summary>`. The group must match the Fieldbook category (`classify` in `site/src/lib/catalog.mjs`).
8. For a release, set the same `version` in `skills.json`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and `gemini-extension.json`.
9. Run:

```bash
make sync-manifest   # skills.json, plus the skill count in the README and plugin manifests
make package
make check           # fails if a count, catalog row, route, or archive is out of date
make site-check      # when site code or categories changed
```

Never edit a skill count by hand: `make sync-manifest` owns the README header and badge and both plugin descriptions, and the tests derive the expected count from `skills/`.

Commit source, manifest, tests, and every changed `dist/*.skill` archive together.

## Frontmatter

```yaml
---
name: my-skill
description: What it does and the requests or contexts that should activate it.
metadata:
  tags: ["optional", "discovery", "tags"]
---
```

Do not add a second condensed copy of `SKILL.md`. Avoid skill-local README/changelog files; keep only runtime instructions and resources.

## Content Standard

- Use imperative, actionable language.
- Distinguish facts, inference, defaults, and examples.
- Verify current claims against primary documentation.
- State assumptions and authority boundaries for external, destructive, financial, publication, security, or production actions.
- Do not use fixed metric tiers, sample sizes, venue rankings, or business thresholds as universal rules.
- Include evidence, verification, and completion conditions.

## Pull Requests

Keep the change focused. Explain what changed, why, release impact, checks run, and any residual risk. Do not claim a check passed unless it ran.
