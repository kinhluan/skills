# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A publishable **skills.sh-format** library of modular AI agent skills. Skills are installed as the Claude Code plugin `kinhluan-skills` and used in other projects via `kinhluan-skills:<skill-name>`. The repo also serves as a Gemini CLI extension and `npx skills` package.

## Key Commands

```bash
make validate    # Validate all skills against skills.sh standard
make package     # Build .skill distribution files into dist/
make help        # List all targets
```

Validation requires the external script at `/Users/luan.bui/.agents/skills/skill-creator/scripts/quick_validate.py`. Packaging uses `package_skill.py` from the same path.

## Repository Structure

```
.agent-skills/     # Source for all skills (symlinked as skills/)
  <skill-name>/
    SKILL.md       # Primary AI instructions — YAML frontmatter required
    SKILL.toon     # Condensed mirror of SKILL.md for context efficiency
dist/              # Pre-built .skill packages (committed, not gitignored)
skills.json        # Central manifest (skills.sh format) — update when adding skills
skills-lock.json   # Hash lock for installed skills
.claude-plugin/
  plugin.json      # Claude Code plugin manifest
gemini-extension.json  # Gemini CLI extension manifest
docs/              # Supplementary guides linked from README
```

## Skill Anatomy

Every skill must have:

1. **`SKILL.md`** with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: What this skill does and when to trigger it.
   metadata:
     tags: ["tag1", "tag2"]
   ---
   ```

2. **`SKILL.toon`** — same content, highly condensed (key patterns, rules, snippets only).

## Adding a New Skill

1. Create `.agent-skills/<skill-name>/SKILL.md` and `SKILL.toon`.
2. Add an entry to `skills.json` under `"skills"` array.
3. Run `make validate` — skill must pass.
4. Run `make package` — updates `dist/`.
5. Commit both source and `dist/` changes.

## Plugin Registration (Claude Code)

The plugin manifest at `.claude-plugin/plugin.json` registers skills under the `kinhluan-skills` namespace. Skills surface in Claude Code as `kinhluan-skills:<skill-name>`.

## Skill Categories

| Category | Prefix pattern | Examples |
|----------|---------------|---------|
| Architecture | `c4-*`, `ddd-*` | `c4-model`, `ddd-core`, `ddd-tactical` |
| Business/Strategy | — | `business-product-leadership`, `dora-core`, `diffusion-release-tracking` |
| Research/PhD | — | `sota-survey` → `research-question` → `paper-writing` → `defense-prep` |
| DevOps/Tech | — | `docker-containerization`, `kubernetes-orchestration`, `security-analysis` |
| Writing/Language | — | `vietnamese-cs-terminology`, `technical-english-cs` |

## Skill Auto-Routing System

3-layer cascade để trigger đúng skill:

### Layer 1 — Hook (automatic)
`scripts/skill_router.py` chạy qua UserPromptSubmit hook. Outputs `[skill-router]` hint vào Claude context. Keyword-based matching.

### Layer 2 — Router Skill
`kinhluan-skills:router` — dispatch skill, reads memory + matches intent table. Trigger khi user nói "dùng skill phù hợp" hoặc intent không rõ.

### Layer 3 — Memory Learning
Sau task thành công: `memory-store` pattern `"[intent keywords] → [skill-name]"`. Future prompts shortcut qua Layer 1.

### Quick Trigger Index

| User says / context | Invoke skill |
|---------------------|-------------|
| survey, literature, papers | `kinhluan-skills:sota-survey` |
| research question, RQ, hypothesis | `kinhluan-skills:research-question` |
| experiment design, methodology | `kinhluan-skills:research-design` |
| write paper, thesis chapter, LaTeX | `kinhluan-skills:paper-writing` |
| thesis defense, committee, bảo vệ | `kinhluan-skills:defense-prep` |
| C4 diagram (general) | `kinhluan-skills:c4-model` |
| context diagram, level 1 | `kinhluan-skills:c4-level1-context` |
| container/service diagram, level 2 | `kinhluan-skills:c4-level2-container` |
| component diagram, level 3 | `kinhluan-skills:c4-level3-component` |
| bounded context, ubiquitous language | `kinhluan-skills:ddd-core` |
| aggregate, entity, value object | `kinhluan-skills:ddd-tactical` |
| CQRS, event sourcing, saga | `kinhluan-skills:ddd-patterns` |
| docker, Dockerfile | `kinhluan-skills:docker-containerization` |
| k8s, kubernetes | `kinhluan-skills:kubernetes-orchestration` |
| DORA, deployment frequency | `kinhluan-skills:dora-core` |
| validate problem, demand | `kinhluan-skills:problem-discovery` |
| why build, value proposition | `kinhluan-skills:why-strategic-rationale` |
| JTBD, product strategy | `kinhluan-skills:business-product-leadership` |
| federated learning, DQN | `kinhluan-skills:federated-learning-dqn` |
| scheduling, MLFQ | `kinhluan-skills:scheduling-algorithms` |
| dịch thuật ngữ, Vietnamese terms | `kinhluan-skills:vietnamese-cs-terminology` |
| technical English, IEEE/ACM writing | `kinhluan-skills:technical-english-cs` |
| security, vulnerability, OWASP | `kinhluan-skills:security-analysis` |
