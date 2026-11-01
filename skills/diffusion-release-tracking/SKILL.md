---
name: diffusion-release-tracking
description: Analyze feature adoption through Rogers' Diffusion of Innovations and design evidence-based phased rollouts. Use when interpreting adopter behavior, deciding whether to expand a release cohort, or defining calibrated rollout criteria and stop conditions.
metadata:
  tags: ["product-management", "adoption", "phased-rollout", "feature-flags", "diffusion-of-innovations"]
---

# Diffusion Release Tracking

Use diffusion theory to interpret how different adopter groups respond. Use release engineering and product evidence to control exposure. Do not turn Rogers' population categories into universal rollout percentages or automatic go/no-go gates.

## Keep Two Models Separate

Rogers' classic categories describe an analytical distribution of adopters:

| Category | Approximate share in the model | Typical behavior |
|---|---:|---|
| Innovators | 2.5% | tolerate uncertainty and experiment |
| Early adopters | 13.5% | seek strategic advantage and influence others |
| Early majority | 34% | want evidence, compatibility, and lower risk |
| Late majority | 34% | adopt under social, economic, or operational pressure |
| Laggards | 16% | prefer established practice and may have valid constraints |

These percentages are not instructions to expose exactly that share of users. A rollout cohort is an operational control selected from system risk, sample size, customer commitments, and the ability to detect and reverse harm.

## Workflow

1. Define the feature's job, target segment, eligible population, and adoption event.
2. Separate:
   - exposure;
   - activation;
   - successful job completion;
   - repeat use or retention;
   - advocacy or reference behavior.
3. Establish product-specific baselines and minimum detectable effects.
4. Segment by relevant behavior or need, not by assigning users a permanent personality label.
5. Define each operational rollout stage with entry, success, guardrail, stop, and rollback criteria.
6. Collect enough observation time for the product's natural usage cadence.
7. Recommend expand, hold, reduce, or stop, with uncertainty and data-quality limits.

## Calibrated Rollout Card

```markdown
### Stage: [internal / opt-in / limited cohort / broader availability]

**Eligible population:** [definition]
**Exposure:** [count or percentage chosen for operational reasons]
**Observation window:** [based on usage cadence]

Entry criteria:
- [technical readiness]
- [support, documentation, compliance, or commercial readiness]

Success evidence:
- [activation relative to baseline]
- [job completion and repeat-value signal]

Guardrails:
- [reliability, safety, support load, complaints, cost]

Stop conditions:
- [specific harmful condition and decision owner]

Rollback:
- [feature flag/config/data recovery path and verification]
```

Thresholds must come from the product baseline, user research, risk tolerance, statistical design, service objectives, and capacity. Values such as a fixed 70% completion rate, NPS 20, 5% churn, or 3× headroom may be examples in a local plan, never universal defaults.

## Interpret Adoption

Look for evidence related to Rogers' five perceived attributes:

- relative advantage;
- compatibility with existing work and values;
- complexity;
- trialability;
- observability of results.

For movement from enthusiastic users to a pragmatic segment, investigate the whole product: onboarding, migration, documentation, support, procurement, integration, trust, and credible reference use. Treat “the chasm” as a strategic hypothesis to test, not a mathematically fixed point at 16% or 20% rollout.

## Recommendation Rules

- `EXPAND`: success evidence is credible, guardrails hold, rollback remains ready.
- `HOLD`: evidence is promising but underpowered, too recent, or operational readiness is incomplete.
- `REDUCE`: guardrails degrade but the feature can remain available to a smaller safe cohort.
- `STOP`: harm, invalid value hypothesis, or unrecoverable operational risk outweighs further exposure.

Do not average away a harmed segment. Report sample size, selection bias, novelty effects, missing data, and conflicting qualitative evidence.

## Output

```markdown
## Adoption and Rollout Review — [feature]

**Decision:** EXPAND / HOLD / REDUCE / STOP
**Operational stage:** [stage and exposure]
**Target segment:** [behavioral/needs definition]
**Adoption hypothesis:** [Rogers attributes expected to matter]

| Evidence | Baseline/criterion | Observed | Confidence | Interpretation |
|---|---|---|---|---|

**Guardrails:** [status and affected segments]
**Uncertainty:** [sample, timing, selection, instrumentation]
**Next action:** [owner, change, observation window]
**Stop/rollback condition:** [condition and mechanism]
```

## Sources

- Everett M. Rogers, *Diffusion of Innovations*
- Geoffrey A. Moore, *Crossing the Chasm* — use as a market strategy lens, not a universal rollout law
