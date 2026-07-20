# Repository Instructions

The canonical skill source and platform discovery root is the real `skills/` directory. Preserve unrelated work.

For any skill change:

1. Keep `SKILL.md` under 500 lines and link every `references/` file directly.
2. Put activation context in frontmatter `description`.
3. Update `scripts/skill_router.py` and regression tests when routing changes.
4. Run `make sync-manifest`, `make package`, then `make check`.
5. Commit source, `skills.json`, and every changed deterministic `dist/*.skill` package together.

Do not add `SKILL.toon`, skill-local README files, machine-specific paths, or `skills-lock.json`. Verify current technical/research claims against primary sources.

For Fieldbook changes:

1. Keep `skills.json` and `skills/*/SKILL.md` as the only skill-content source.
2. Preserve the `/skills` GitHub Pages base configured in `site/astro.config.mjs`.
3. Keep client-side interactions usable without accounts or external data services.
4. Run `make site-check` and keep internal links valid before publishing.
