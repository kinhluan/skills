---
name: kinhluan-router
description: Select the smallest set of relevant skills from the kinhluan collection. Use when the user asks to choose a skill, several domains overlap, or the correct specialist is unclear; route from current intent and evidence without forcing a universal workflow sequence.
metadata:
  tags: ["routing", "dispatch", "skill-selection", "orchestration"]
---

# Kinhluan Router

Route the user's current request, not an imagined full program. Prefer one primary skill and add a second only when it owns a distinct necessary part of the outcome.

## Routing Workflow

1. Extract the requested verb, artifact, domain, and completion condition.
2. Inspect relevant workspace evidence when it changes the choice.
3. Match skill descriptions and specific triggers.
4. Rank:
   - exact artifact/domain match;
   - specific skill over generic umbrella;
   - action skill over background framework;
   - current request over a presumed prerequisite chain.
5. Select up to three skills. State order only when their work is dependent.
6. If no skill materially improves the task, continue without one.

Do not require role declarations or ask permission merely to select an on-demand skill. Do not force problem discovery before a bounded code fix, SOTA survey before editing an existing paper, or C4 Level 1 before reviewing an existing Level 2 diagram unless missing context makes the requested task unreliable.

## Specificity Examples

| Request | Primary | Optional secondary |
|---|---|---|
| “audit this paper against its repository” | `paper-audit` | `research-design` for validity issues |
| “monitor new papers weekly” | `research-watch` | `sota-survey` for periodic synthesis |
| “Kubernetes container security” | `container-security` | `kubernetes-orchestration` |
| “review this PR” | `merge-request-review` | language/security skill if warranted |
| “SonarQube gate failed” | `code-quality-gate` | language skill |
| “Go concurrency leak” | `golang-development` | `security-analysis` only if relevant |
| “create research slides and figures” | `slide-automation` | `ai-figure-generation` |
| “should we build this?” | `art-of-war-software-engineering` | `problem-discovery` |

## Workflow-Aware Suggestions

Research, product, and architecture workflows are advisory context. Suggest a missing upstream artifact when it blocks interpretation:

- a statistical claim without a defined estimand;
- a rollout decision without exposure and guardrail data;
- a component diagram without a known container boundary;
- a deployment action without a target environment or rollback.

Otherwise honor the requested stage and note assumptions.

## Executable Router

The plugin hook uses [`scripts/skill_router.py`](../../scripts/skill_router.py) for lightweight prompt suggestions. Its routes are scored so longer, specific phrases beat generic keywords; short terms use word boundaries. The repository validator requires every published skill to have exactly one route, and regression tests cover ambiguous prompts.

Treat hook suggestions as hints. The agent still checks current context and may select a different skill with a short rationale.

## Output

```markdown
**Primary skill:** [name] — [why it owns the requested artifact]
**Secondary skill:** [name, only if needed] — [distinct role]
**Order:** [parallel or dependent]
**Assumption:** [only a fact that could change routing]
```
