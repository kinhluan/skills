# diffusion-release-tracking Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a guidance-only agent skill that tracks where a feature sits on Rogers' Diffusion of Innovations bell curve and produces a Go/No-Go release recommendation with a structured report.

**Architecture:** Phase-Gated Framework with 4 Release Gates (Innovator → Early Adopter → Chasm → Majority), each with explicit quant+qual signal criteria. Agent identifies current gate, collects signals, produces diagnosis + verdict + markdown report. Standalone skill, cross-referenced from `business-product-leadership`.

**Tech Stack:** Markdown (SKILL.md format), skills.json registry (JSON)

**Spec:** `docs/superpowers/specs/2026-05-07-rogers-diffusion-skill-design.md`

---

### Task 1: Create `SKILL.md`

**Files:**
- Create: `.agent-skills/diffusion-release-tracking/SKILL.md`

- [ ] **Step 1: Create the directory**

```bash
mkdir -p .agent-skills/diffusion-release-tracking
```

- [ ] **Step 2: Write SKILL.md**

Create `.agent-skills/diffusion-release-tracking/SKILL.md` with this exact content:

```markdown
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
```

- [ ] **Step 3: Verify file exists and content looks correct**

```bash
head -5 .agent-skills/diffusion-release-tracking/SKILL.md
wc -l .agent-skills/diffusion-release-tracking/SKILL.md
```

Expected: frontmatter visible, line count ~130

- [ ] **Step 4: Commit**

```bash
git add .agent-skills/diffusion-release-tracking/SKILL.md
git commit -m "feat: add diffusion-release-tracking SKILL.md

Phase-gated Rogers Diffusion framework with 4 release gates,
quant+qual signal criteria, Go/No-Go output format."
```

---

### Task 2: Create `SKILL.toon`

**Files:**
- Create: `.agent-skills/diffusion-release-tracking/SKILL.toon`

- [ ] **Step 1: Write SKILL.toon**

Create `.agent-skills/diffusion-release-tracking/SKILL.toon` with this exact content:

```markdown
---
name: diffusion-release-tracking
description: Track feature position on Rogers' bell curve. 4 Phase Gates with quant+qual criteria → Go/No-Go release verdict + structured report.
metadata:
  tags: ["product-management", "diffusion-of-innovations", "release", "feature-flags", "rogers"]
---
# Diffusion Release Tracking

4 Release Gates map Rogers' adoption curve to phased rollout decisions.

## Gates
- **Innovator Gate** (internal → opt-in): 0 P0 bugs, ≥70% job completion, ≤1% error rate, "usable" feedback
- **Early Adopter Gate** (opt-in → 5–20%): ≥30% activation, ≥25% D7 retention, aha moment confirmed, ≥1 organic advocate
- **Chasm Gate** (20% → 50%): retention curve flat week 3+, NPS ≥20, whole product ready, beachhead vertical dominated, ≥1 reference story with ROI
- **Majority Gate** (50% → 100%): churn ≤5% B2B/≤10% consumer, support manageable, infra handles 3× load, late-majority objections addressed

## Agent Flow
1. Identify current gate (ask user or infer from rollout %)
2. Collect signals for that gate only
3. Assess signals against thresholds
4. Produce: diagnosis + ✅ GO / ⚠️ CONDITIONAL GO / ❌ NO-GO + markdown report + next gate criteria

## Output
```markdown
## Rogers Diffusion Report — [Feature]
**Current Gate:** X | **Rollout:** Y%
### Signal Assessment
| Signal | Status | Detail |
|---|---|---|
### Diagnosis
### Recommendation
**[✅/⚠️/❌ VERDICT]** — action.
### Next Gate Criteria
- [ ] criterion
```

## Notes
- Thresholds are baselines — adjust for B2B/consumer/internal/regulated context
- Strategic context (JTBD, Chasm theory): use `business-product-leadership` skill
```

- [ ] **Step 2: Verify**

```bash
head -5 .agent-skills/diffusion-release-tracking/SKILL.toon
```

Expected: frontmatter visible

- [ ] **Step 3: Commit**

```bash
git add .agent-skills/diffusion-release-tracking/SKILL.toon
git commit -m "feat: add diffusion-release-tracking SKILL.toon

Compressed summary for context-limited invocations."
```

---

### Task 3: Update `business-product-leadership` cross-reference

**Files:**
- Modify: `.agent-skills/business-product-leadership/SKILL.md`
- Modify: `.agent-skills/business-product-leadership/SKILL.toon`

- [ ] **Step 1: Add cross-reference to SKILL.md**

In `.agent-skills/business-product-leadership/SKILL.md`, find the end of the **Strategic Implications** bullet list under the Diffusion of Innovations section (after "Do not build for Late Majority features until Early Majority is retained."). Add:

```markdown
- For active release tracking and Go/No-Go decisions per rollout phase, use the `diffusion-release-tracking` skill.
```

- [ ] **Step 2: Add cross-reference to SKILL.toon**

In `.agent-skills/business-product-leadership/SKILL.toon`, find the Diffusion of Innovations bullet. Append to that line:

```
 → For active tracking/Go-No-Go per gate, use `diffusion-release-tracking` skill.
```

- [ ] **Step 3: Verify both files mention diffusion-release-tracking**

```bash
grep "diffusion-release-tracking" .agent-skills/business-product-leadership/SKILL.md
grep "diffusion-release-tracking" .agent-skills/business-product-leadership/SKILL.toon
```

Expected: 1 match each

- [ ] **Step 4: Commit**

```bash
git add .agent-skills/business-product-leadership/SKILL.md .agent-skills/business-product-leadership/SKILL.toon
git commit -m "feat: cross-reference diffusion-release-tracking from business-product-leadership"
```

---

### Task 4: Register in `skills.json`

**Files:**
- Modify: `skills.json`

- [ ] **Step 1: Add registry entry**

In `skills.json`, find the `"skills"` array. Add this entry (maintain alphabetical order — after `"ddd-tactical"`, before `"docker-containerization"`):

```json
{
  "name": "diffusion-release-tracking",
  "path": "./.agent-skills/diffusion-release-tracking",
  "files": ["SKILL.md", "SKILL.toon"],
  "description": "Track feature adoption position on Rogers' bell curve with 4 phase-gated Go/No-Go release decisions",
  "tags": ["product-management", "diffusion-of-innovations", "release", "feature-flags", "rogers", "ship-release"]
},
```

- [ ] **Step 2: Verify JSON is valid**

```bash
cat skills.json | python3 -m json.tool > /dev/null && echo "valid JSON"
```

Expected: `valid JSON`

- [ ] **Step 3: Verify entry exists**

```bash
grep "diffusion-release-tracking" skills.json
```

Expected: 3 matches (name, path, description)

- [ ] **Step 4: Commit**

```bash
git add skills.json
git commit -m "feat: register diffusion-release-tracking in skills.json registry"
```

---

## Self-Review

**Spec coverage check:**
- ✅ SKILL.md — full guidance, 4 gates, signal criteria, output format
- ✅ SKILL.toon — compressed summary
- ✅ Cross-reference from business-product-leadership (both files)
- ✅ skills.json registry entry
- ✅ Threshold calibration notes (B2B/consumer/internal/regulated)
- ✅ Integration note linking to Ship≠Release workflow

**Placeholder scan:** None found.

**Consistency check:** `diffusion-release-tracking` name used consistently across SKILL.md, SKILL.toon, skills.json, and cross-references.
