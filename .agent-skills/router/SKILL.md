---
name: router
description: Dispatch to the right kinhluan-skill based on user intent. Trigger when user says "dùng skill phù hợp", "use right skill", "kinhluan skills", or when multiple skills could apply and you need to pick one.
metadata:
  tags: ["routing", "dispatch", "meta", "orchestration"]
---

# Kinhluan Skill Router

Dispatch to the correct kinhluan-skill using 3-layer cascade.

## Layer 1: Hook Hint (auto)
Check if `[skill-router]` hint appeared in context (UserPromptSubmit hook output).
If yes: use the suggested skill directly.

## Layer 2: Memory Recall
```
Invoke: memory-recall
Query: "kinhluan skill routing [topic keywords from user message]"
```
If memory returns a routing pattern → use it.

## Layer 3: Intent Matching

Map user intent → skill:

### Research Track
| Intent | Skill |
|--------|-------|
| Find papers, survey field | `kinhluan-skills:sota-survey` |
| Write research question | `kinhluan-skills:research-question` |
| Design experiment | `kinhluan-skills:research-design` |
| Write paper/chapter | `kinhluan-skills:paper-writing` |
| PhD thesis defense | `kinhluan-skills:defense-prep` |
| Write PhD proposal | `kinhluan-skills:phd-proposal` |
| Track experiments | `kinhluan-skills:experiment-tracking` |
| Self-review paper | `kinhluan-skills:internal-critique` |
| Track milestones/deadlines | `kinhluan-skills:milestone-tracker` |
| Choose publication venue | `kinhluan-skills:publication-strategy` |

### Architecture Track
| Intent | Skill |
|--------|-------|
| C4 overview (which level?) | `kinhluan-skills:c4-model` |
| System context diagram | `kinhluan-skills:c4-level1-context` |
| Container/service diagram | `kinhluan-skills:c4-level2-container` |
| Component/internal diagram | `kinhluan-skills:c4-level3-component` |
| Class/ER diagram | `kinhluan-skills:c4-level4-code` |
| Architecture decision | `kinhluan-skills:architecture-decision-records` |
| Evolutionary/fitness functions | `kinhluan-skills:evolutionary-architecture` |

### DDD Track
| Intent | Skill |
|--------|-------|
| Strategic DDD, bounded context | `kinhluan-skills:ddd-core` |
| Aggregate, entity, value object | `kinhluan-skills:ddd-tactical` |
| CQRS, event sourcing, saga | `kinhluan-skills:ddd-patterns` |

### DevOps Track
| Intent | Skill |
|--------|-------|
| Docker, Dockerfile | `kinhluan-skills:docker-containerization` |
| Kubernetes, k8s | `kinhluan-skills:kubernetes-orchestration` |
| DORA metrics, delivery | `kinhluan-skills:dora-core` |

### Strategy Track
| Intent | Skill |
|--------|-------|
| Validate problem/demand | `kinhluan-skills:problem-discovery` |
| Why build this? | `kinhluan-skills:why-strategic-rationale` |
| JTBD, product strategy | `kinhluan-skills:business-product-leadership` |
| Release tracking, diffusion | `kinhluan-skills:diffusion-release-tracking` |
| Competitive strategy | `kinhluan-skills:art-of-war-software-engineering` |

### ML Track
| Intent | Skill |
|--------|-------|
| Federated learning + DQN | `kinhluan-skills:federated-learning-dqn` |
| Scheduling algorithms, MLFQ | `kinhluan-skills:scheduling-algorithms` |

### Writing Track
| Intent | Skill |
|--------|-------|
| Vietnamese CS terms | `kinhluan-skills:vietnamese-cs-terminology` |
| Technical English, IEEE/ACM | `kinhluan-skills:technical-english-cs` |
| Vietnamese writing standards | `kinhluan-skills:vietnamese-writing-standard` |

### Dev Track
| Intent | Skill |
|--------|-------|
| Python project setup | `kinhluan-skills:python-development` |
| TypeScript/JavaScript | `kinhluan-skills:javascript-typescript` |
| Security audit | `kinhluan-skills:security-analysis` |

## Dispatch Protocol

1. Identify matched skill from above table
2. Announce: "Using `<skill>` to <purpose>"
3. Invoke: `Skill(<matched-skill>)`
4. Follow skill instructions

## Memory Integration

After completing a routed task:
- If routing was non-obvious or user confirmed it worked → trigger `memory-store`
- Store pattern: `"[user intent keywords] → [skill-name] — worked for [context]"`
- Future recalls will shortcut Layer 1-3 matching

## When Multiple Skills Match

Pick most specific:
- `c4-level1-context` > `c4-model` (more specific wins)
- `ddd-tactical` > `ddd-core` (if aggregate/entity mentioned)
- Ask user if genuinely ambiguous (>2 equally valid options)
