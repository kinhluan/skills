---
name: diffusion-release-tracking
description: Track where a feature sits on Rogers' Diffusion of Innovations bell curve and produce a Go/No-Go release recommendation. Use this skill when deciding whether to expand a feature rollout, evaluating adoption signals, or planning phased release milestones.
metadata:
  tags: ["product-management", "diffusion-of-innovations", "release", "feature-flags", "rogers", "ship-release"]
---

# Diffusion Release Tracking

Track adoption position on Rogers' bell curve. Decide when to expand each Release phase.

## The 4 Release Gates

```
[Ship] → [Innovator Gate] → [Early Adopter Gate] → [Chasm Gate] → [Majority Gate]
           ~2.5%               ~16%                   16→50%          50→100%
         flag on / internal    opt-in beta             beachhead        scale
```

Agent flow:
1. Identify which gate the feature is currently at — ask user or infer from rollout %
2. Collect signals for **that gate only** — do not ask about other gates
3. Assess each signal against threshold
4. Produce diagnosis + verdict + markdown report + next gate criteria

---

## Gate 1: Innovator Gate
**From:** Ship (dark launch / internal flag on)
**To:** Opt-in beta / first external users (~2.5%)
**Question:** Is the feature stable and does it complete the core job?

| Signal | Type | Go Threshold |
|---|---|---|
| P0/P1 bug count | Quant | 0 P0, ≤2 P1 |
| Core job completion rate | Quant | ≥70% of attempts succeed end-to-end |
| Internal team feedback | Qual | "Usable, no blockers" from dogfood users |
| Dark launch error rate | Quant | ≤1% server errors on feature path |

---

## Gate 2: Early Adopter Gate
**From:** Opt-in beta
**To:** 5–20% phased rollout
**Question:** Is there retention signal and do users advocate for the feature?

| Signal | Type | Go Threshold |
|---|---|---|
| Feature activation rate | Quant | ≥30% of exposed users trigger the feature at least once |
| Day-7 retention | Quant | ≥25% of activators return and use the feature again by day 7 |
| "Aha moment" confirmed | Qual | ≥5 user interviews confirm the core value moment |
| Organic advocate signal | Qual | ≥1 user shares, recommends, or references the feature unprompted |

---

## Gate 3: Chasm Gate ← Most Critical
**From:** 20% rollout
**To:** 50% rollout
**Question:** Is the whole product ready for pragmatic, risk-averse users?

The Chasm (Moore) is where most products die. Early Adopters tolerate rough edges; Early Majority demands a complete solution — docs, support, onboarding, proof.

| Signal | Type | Go Threshold |
|---|---|---|
| Retention curve shape | Quant | Curve flattening after week 3, not still declining |
| NPS or CSAT | Quant | NPS ≥20 or CSAT ≥4/5 |
| Whole product gaps | Qual | Docs, onboarding, and support sufficient for a non-technical user |
| Beachhead vertical | Qual | 1 niche segment dominated completely before expanding to adjacent segments |
| Reference story | Qual | ≥1 customer case study with real ROI numbers, not just quotes |

---

## Gate 4: Majority Gate
**From:** 50% rollout
**To:** 100% rollout
**Question:** Are unit economics and infrastructure ready for full scale?

| Signal | Type | Go Threshold |
|---|---|---|
| Monthly churn | Quant | ≤5% for B2B, ≤10% for consumer |
| Support ticket volume | Quant | Resolvable with current team without backlog growth |
| Scalability headroom | Quant | Infrastructure handles 3× current peak load |
| Pricing/standards fit | Qual | Late Majority objections (price, compliance, standards) addressed |

---

## Output Format

After collecting signals, produce this report:

```markdown
## Rogers Diffusion Report — [Feature Name]
**Date:** YYYY-MM-DD
**Current Gate:** [Gate Name]
**Rollout:** X% of users

### Signal Assessment
| Signal | Status | Detail |
|---|---|---|
| [signal name] | ✅/⚠️/❌ | [threshold vs actual value or observation] |

### Diagnosis
[2–4 sentences: current position on bell curve, which criteria are met or missing, primary risk to expansion.]

### Recommendation
**[✅ GO / ⚠️ CONDITIONAL GO / ❌ NO-GO]** — [one-sentence action].
[If not full GO: what to fix before next gate.]

### Next Gate Criteria
- [ ] [criterion 1]
- [ ] [criterion 2]
```

**Verdict levels:**
- `✅ GO` — All gate criteria met. Expand rollout to next phase.
- `⚠️ CONDITIONAL GO` — Majority met. Expand cautiously (hold at current %) while fixing gaps.
- `❌ NO-GO` — Critical criteria missing. Do not expand rollout. Address gaps first.

---

## Threshold Calibration Notes

Default thresholds are reasonable baselines. Agent should flag when context warrants adjustment:
- **B2B enterprise:** Day-7 retention threshold may be lower (usage is weekly/monthly by nature)
- **Internal tooling:** Advocate signal may be irrelevant; focus on job completion and error rate
- **Consumer viral product:** Organic advocate signal is more critical, weight it higher
- **Regulated industry:** Whole product gap check must include compliance/security sign-off

---

## Integration with Ship≠Release Workflow

This skill operationalizes the Agile Delivery principle from `business-product-leadership`:
- **Ship** = code behind feature flag (before Innovator Gate)
- **Release** = advancing through gates by turning flags on for wider cohorts

For strategic context on JTBD, market positioning, and The Chasm theory, use the `business-product-leadership` skill.

## DORA Prerequisite: Deployment Frequency

Before attempting phased gate advancement, assess DORA Deployment Frequency tier (use `dora-core` skill):

| DORA DF Tier | Gate Strategy |
|---|---|
| **Elite** (on-demand) | Full gate strategy applies — iterate rapidly per gate |
| **High** (daily–weekly) | Gate iteration feasible — allow longer validation windows |
| **Medium** (weekly–monthly) | Plan gate windows months in advance; reduce gate count |
| **Low** (monthly+) | **Fix DF first.** Cannot run meaningful phased rollouts at this cadence |

Low Deployment Frequency is a delivery bottleneck that makes Rogers gate validation impossible — by the time you gather signal, the market window has shifted.
