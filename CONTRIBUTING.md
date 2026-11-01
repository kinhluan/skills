# Contributing

Thanks for improving the collection.

## Add or Change a Skill

1. Work in `skills/<skill-name>/`; this is the canonical source and platform discovery tree.
2. Keep the directory and frontmatter `name` identical, lowercase, and hyphenated.
3. Write a concrete `description` that explains capability and activation context.
4. Keep `SKILL.md` below 500 lines. Move detailed examples or domain references into `references/` and link every reference directly from `SKILL.md`.
5. Add a deterministic helper under the skill's `scripts/` only when repeated execution benefits from it; test it.
6. Add or update the route in `scripts/skill_router.py` and cover ambiguous behavior in `tests/`.
7. Run:

```bash
make sync-manifest
make package
make check
```

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
