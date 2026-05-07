# Design Spec: `diffusion-release-tracking` Skill

**Date:** 2026-05-07  
**Status:** Approved  
**Author:** luan.bui

---

## Overview

A guidance-only agent skill that helps Product Owners track where a feature sits on Rogers' Diffusion of Innovations bell curve, then produce a Go/No-Go release recommendation backed by a structured report. Covers the full lifecycle: Ship → Innovator → Early Adopter → Chasm → Early Majority → scale.

Standalone skill. Cross-referenced from `business-product-leadership`.

---

## Approach: Phase-Gated Framework

4 Release Gates map directly onto the Rogers adoption curve and the Ship≠Release phased rollout workflow:

```
[Ship] → [Innovator Gate] → [Early Adopter Gate] → [Chasm Gate] → [Majority Gate]
           ~2.5%               ~16%                   16→50%          50→100%
           flag on             opt-in beta             beachhead        scale
```

Agent flow per invocation:
1. Identify which gate the feature is currently at (ask user or infer from context)
2. Collect signals for that gate only — mix of quantitative + qualitative
3. Assess signals against thresholds
4. Produce: diagnosis + verdict + structured markdown report + next gate criteria

---

## Signal Criteria per Gate

### Innovator Gate (internal dogfood → opt-in beta)

| Signal | Type | Go Threshold |
|---|---|---|
| P0/P1 bug count | Quant | 0 P0, ≤2 P1 |
| Core job completion rate | Quant | ≥70% |
| Internal team feedback | Qual | "Usable, no blockers" |
| Dark launch error rate | Quant | ≤1% |

### Early Adopter Gate (opt-in → 5–20% rollout)

| Signal | Type | Go Threshold |
|---|---|---|
| Feature activation rate | Quant | ≥30% of exposed users |
| Day-7 retention | Quant | ≥25% |
| "Aha moment" confirmed | Qual | ≥5 user interviews confirm it |
| Organic advocate signal | Qual | ≥1 user shares/recommends unprompted |

### Chasm Gate (20% → 50%) — most critical

| Signal | Type | Go Threshold |
|---|---|---|
| Retention curve shape | Quant | Flattening after week 3, not still dropping |
| NPS or CSAT | Quant | NPS ≥20 or CSAT ≥4/5 |
| Whole product gaps | Qual | Docs, onboarding, support sufficient for non-early-adopter |
| Beachhead vertical | Qual | 1 niche segment dominated before expanding |
| Reference story | Qual | ≥1 customer case study with real ROI numbers |

### Majority Gate (50% → 100%)

| Signal | Type | Go Threshold |
|---|---|---|
| Monthly churn | Quant | ≤5% B2B, ≤10% consumer |
| Support ticket volume | Quant | Manageable with current team size |
| Scalability headroom | Quant | Infrastructure handles 3× current load |
| Pricing/standards fit | Qual | Late majority objections addressed |

---

## Output Format

```markdown
## Rogers Diffusion Report — [Feature Name]
**Date:** YYYY-MM-DD
**Current Gate:** [Gate Name]
**Rollout:** X% of users

### Signal Assessment
| Signal | Status | Detail |
|---|---|---|
| [signal] | ✅/⚠️/❌ | [threshold + actual value or observation] |

### Diagnosis
[2–4 sentences: current gate position, which criteria met/missing, key risk.]

### Recommendation
**[✅ GO / ⚠️ CONDITIONAL GO / ❌ NO-GO]** — [one-sentence action].
[Follow-up: what to fix before next gate, if applicable.]

### Next Gate Criteria
- [ ] [criterion 1]
- [ ] [criterion 2]
...
```

**Verdict levels:**
- `✅ GO` — All criteria met, release to next phase
- `⚠️ CONDITIONAL GO` — Majority met, expand rollout cautiously while fixing gaps
- `❌ NO-GO` — Critical criteria missing, do not expand rollout

---

## Files to Create

| File | Purpose |
|---|---|
| `.agent-skills/diffusion-release-tracking/SKILL.md` | Full guidance, gates, criteria, output format |
| `.agent-skills/diffusion-release-tracking/SKILL.toon` | Compressed summary for context-limited invocations |

## Cross-Reference

Add to `business-product-leadership/SKILL.md` under the Diffusion of Innovations section:
> For active release tracking and Go/No-Go decisions, use the `diffusion-release-tracking` skill.

Add to `skills.json` registry with tags: `["product-management", "diffusion-of-innovations", "release", "feature-flags", "rogers"]`

---

## Out of Scope

- Code execution, data fetching, or analytics API integration (guidance only)
- Automatic threshold calibration per product type (thresholds are explicit defaults, agent notes when context warrants adjustment)
- Bass model computation or bell curve plotting
