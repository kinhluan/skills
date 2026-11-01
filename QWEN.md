# Qwen Repository Context

This is a portable Agent Skills repository. Canonical sources live in the real `skills/` discovery directory.

When changing a skill:

```bash
make sync-manifest
make package
make check
```

Keep one authoritative `SKILL.md` per skill, below 500 lines. Put detailed material in directly linked `references/`. Do not add duplicate condensed files or installer lock state. Update router coverage/tests and all generated release artifacts with source changes.

See [README.md](README.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [skills.json](skills.json).
