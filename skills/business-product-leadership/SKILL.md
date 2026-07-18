---
name: business-product-leadership
description: Frame product strategy and decisions across customer problems, Jobs-to-Be-Done, value propositions, MVP scope, product economics, experiments, pricing, go-to-market, and adoption. Use when a product owner or founder needs an evidence-based decision and accountable next step.
metadata:
  tags: ["product-strategy", "jtbd", "mvp", "experimentation", "pricing", "go-to-market"]
---

# Business and Product Leadership

Turn strategy into falsifiable choices. Frameworks organize evidence; they do not create universal thresholds or replace customer, financial, legal, and operational context.

## Decision Workflow

1. Define the decision, owner, deadline, target segment, and constraints.
2. State the problem evidence and current alternatives.
3. Frame the job:

```text
When [situation], [actor] wants to [progress],
so they can [outcome], despite [constraint].
```

4. Express a value proposition and the assumption most likely to invalidate it.
5. Select the smallest solution/prototype that can test the assumption.
6. Define success, guardrail, stop, and follow-up criteria from baseline data and risk.
7. Evaluate delivery capability, economics, adoption, and organizational ownership.
8. Decide build, buy, partner, adapt, defer, or stop.

Discovery and JTBD can iterate in either direction. Do not insist on a universal sequence when evidence already exists; maintain traceability from claims to observations.

## Product Evidence

Use multiple evidence types:

- observed customer behavior and qualitative research;
- product/support/search data;
- willingness and authority to switch or pay;
- competitive alternatives and switching cost;
- technical/operational feasibility;
- unit economics and cash constraints;
- legal, accessibility, privacy, and trust requirements.

Conversion, retention, CAC:LTV, NPS, sample sizes, or price points must be calibrated to the product, channel, usage cadence, margin, and uncertainty. Label illustrative numbers as examples.

## MVP

An MVP is the smallest coherent way to test a value/risk hypothesis, not a low-quality version of every planned feature. Specify:

- target segment and job;
- hypothesis and evidence needed;
- included/excluded scope;
- manual/automated boundaries;
- quality, safety, and support floor;
- measurement and observation window;
- kill/pivot criteria;
- migration path if the test succeeds.

## Build/Buy/Partner

Assess strategic differentiation, regulatory control, data locality, reliability, integration, customization, vendor health, switching/exit cost, and total lifecycle cost. Generic capability is not automatically “buy”; core capability is not automatically “build.”

## Ship and Release

- `ship`: deploy safely and reversibly.
- `release`: expose a value proposition to a defined cohort.
- `adopt`: users achieve and repeat the intended outcome.

Use `dora-core` for current service-level delivery metrics and `diffusion-release-tracking` for calibrated adoption/rollout decisions. Do not map historical DORA tiers or Rogers percentages directly to product gates.

## Output

```markdown
## Product Decision — [initiative]

**Decision:** [...]
**Owner/date:** [...]
**Segment and JTBD:** [...]
**Problem/value evidence:** [...]
**Riskiest assumption:** [...]
**Options considered:** [build/buy/partner/adapt/defer/stop]
**Experiment/MVP:** [...]
**Success, guardrail, stop criteria:** [...]
**Economics and constraints:** [...]
**Next action:** [owner, date, evidence]
```

Read [references/detailed-guide.md](references/detailed-guide.md) only for a relevant framework or template. Recalibrate every numerical example and verify time-sensitive market/tool claims before use.
