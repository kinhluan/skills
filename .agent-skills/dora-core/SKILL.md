---
name: dora-core
description: DORA (DevOps Research and Assessment) Core Model for measuring and improving software delivery performance. Use this skill to assess team performance tier, identify capability gaps, and connect delivery metrics to product release strategy.
metadata:
  tags: ["dora", "devops", "delivery-performance", "metrics", "deployment-frequency", "lead-time", "change-failure-rate", "mttr"]
---

# DORA Core Model

DORA measures **how fast and how safely** a team delivers software. It is the bridge between product strategy (what to build, when to release) and technical execution (how to build it reliably).

---

## The 4 Key Metrics

| Metric | What it measures |
|---|---|
| **Deployment Frequency (DF)** | How often code is deployed to production |
| **Lead Time for Changes (LT)** | Time from code commit to running in production |
| **Change Failure Rate (CFR)** | % of deployments causing a production incident |
| **Time to Restore (MTTR)** | Time to recover from a production failure |

---

## Performance Tiers

| Tier | Deployment Frequency | Lead Time | Change Failure Rate | MTTR |
|---|---|---|---|---|
| **Elite** | On-demand (multiple/day) | < 1 hour | 0–5% | < 1 hour |
| **High** | 1/day – 1/week | 1 day – 1 week | 6–15% | < 1 day |
| **Medium** | 1/week – 1/month | 1 week – 1 month | 16–30% | 1 day – 1 week |
| **Low** | 1/month – 1/6 months | 1 month – 6 months | 16–30% | > 1 week |

**Elite and High performers** deploy 973× more frequently and have 6,570× faster recovery than Low performers (DORA 2023 State of DevOps).

---

## Key Capabilities (The Drivers)

DORA research identifies capabilities that predict high performance. Focus on these highest-impact ones:

### Technical Capabilities
| Capability | Impact | Integration |
|---|---|---|
| **Loosely Coupled Architecture** | #1 predictor of high DF | `c4-model` L2 container boundaries, `ddd-core` Bounded Contexts |
| **Trunk-Based Development** | Reduces integration debt | Short-lived branches, feature flags |
| **Continuous Integration** | Reduces LT and CFR | Automated test on every commit |
| **Test Automation** | Reduces CFR | Unit + integration tests in CI |
| **Deployment Automation** | Reduces LT | One-click or auto deploy to prod |
| **Shifting Left on Security** | Reduces CFR | Security checks in CI, not post-deploy |
| **Monitoring & Observability** | Reduces MTTR | Metrics, logs, traces in production |
| **Database Change Management** | Reduces CFR | Schema migrations versioned and automated |

### Process Capabilities
| Capability | Impact |
|---|---|
| **Working in Small Batches** | Directly reduces LT and CFR |
| **Streamlining Change Approval** | Manual approval gates are the #1 LT killer |
| **Team Experimentation** | Faster learning → better product decisions |
| **Customer Feedback** | Shorter feedback loop → less wasted work |

### Cultural Capabilities
| Capability | Impact |
|---|---|
| **Generative Culture (Westrum)** | High trust, blameless postmortems → faster MTTR |
| **Psychological Safety** | Teams that can surface problems fix them faster |
| **Learning Culture** | Continuous improvement on all 4 metrics |

---

## DORA Assessment: How to Use

1. **Measure current tier** — ask for each of the 4 metrics in the last 30 days
2. **Identify the bottleneck metric** — which metric is worst relative to its tier?
3. **Map to capability** — use the table above to find the root capability gap
4. **Prioritize** — fix the bottleneck capability first; others are downstream

### Quick Diagnostic Questions
- "How often do you deploy to production?" → Deployment Frequency tier
- "How long from `git commit` to live in prod?" → Lead Time tier
- "What % of deploys caused a hotfix or rollback in the last quarter?" → CFR tier
- "When production broke last, how long to restore?" → MTTR tier

---

## Integration with Other Skills

### → `diffusion-release-tracking`
Deployment Frequency is a **prerequisite signal** before advancing Rogers Gates:
- **Elite/High DF** (daily+): can iterate rapidly through Innovator → Early Adopter gates
- **Medium DF** (weekly): gate advancement is slower; plan for longer validation windows
- **Low DF** (monthly): cannot run proper phased rollouts — fix DF first before attempting Rogers gate strategy

### → `collaborative-engineering-agent`
| DORA Metric | CEA Practice |
|---|---|
| Lead Time ↓ | Atomic PRs (<200 lines), trunk-based dev reduces integration bottleneck |
| CFR ↓ | Dialectical Review Engine (DRE) catches issues before merge |
| MTTR ↓ | Automated fix-branch workflow, observability tooling |

### → `c4-model` + `ddd-core`
- **Loosely Coupled Architecture** (DORA's #1 capability) is achieved through:
  - C4 L2: independent deployable containers with clear API boundaries
  - DDD: Bounded Contexts with anti-corruption layers prevent cascade failures
- Conway's Law applies: if the org structure is tightly coupled, the architecture will be too — and DF suffers

### → `business-product-leadership`
| DORA Tier | Product Strategy Implication |
|---|---|
| Elite | Deploy on-demand → rapid MVP validation, tight Rogers feedback loop |
| High | Weekly deploys → manageable Early Adopter gate iteration |
| Medium | Monthly deploys → must plan Rogers gate windows months in advance |
| Low | Cannot run agile product strategy — delivery is the bottleneck |

---

## Anti-Patterns

- **Measuring DF but ignoring CFR** — high DF with high CFR = fast failure, not fast delivery
- **Using DF as a vanity metric** — deploying to staging doesn't count; production only
- **Manual change approval gates** — DORA research shows this is the single biggest LT killer, with no measurable CFR improvement
- **Optimizing MTTR with more process** — MTTR is reduced by observability and psychological safety, not more approval steps
- **Treating DORA as a report card** — metrics are diagnostic tools, not performance reviews
