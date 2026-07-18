---
name: problem-discovery
description: Test whether a specific real-world problem is important enough to address before defining a solution or MVP. Use when evaluating product demand, refining a target segment, planning discovery research, or deciding whether to build, defer, pivot, or stop.
metadata:
  tags: ["product-discovery", "problem-validation", "customer-research", "market-evidence", "decision-making"]
---

# Problem Discovery

Reduce uncertainty about a problem, not prove a favored solution. Define disconfirming evidence and decision criteria before collecting data.

## Frame the Hypothesis

```text
[Specific segment] experiences [observable problem]
in [situation/frequency], causing [measurable consequence].
They currently use [alternative/workaround], which fails because [evidence].
```

Record:

- target decision and deadline;
- riskiest assumptions;
- existing alternatives, including doing nothing;
- evidence that would increase or decrease confidence;
- ethical, legal, accessibility, and privacy constraints.

## Triangulate Evidence

Select methods that observe different failure modes:

| Evidence | Best use | Common limitation |
|---|---|---|
| interviews/contextual inquiry | past behavior, workflow, consequence, language | recall and recruitment bias |
| support/search/usage data | frequency and behavioral friction | instrumentation and survivorship bias |
| diary or field study | recurring context over time | participant burden |
| prototype/usability test | comprehension and task feasibility | does not prove demand |
| landing-page or concierge test | behavioral commitment to a proposition | traffic quality and novelty |
| purchasing/procurement evidence | budget, authority, switching constraints | long cycles and small samples |
| competitor/alternative analysis | current solutions and underserved needs | estimated revenue/traffic can be unreliable |
| labor or process data | cost of manual work in B2B settings | poor fit for many consumer/novel problems |

Use at least two independent sources when practical. Interviews are valuable but not automatically required or sufficient. Recruit the intended segment; distinguish users, buyers, administrators, and affected non-users.

Do not deceive participants about a nonexistent product, take payment without clear terms, expose private data, or manufacture scarcity. A concierge or Wizard-of-Oz test must disclose material limitations and provide consent/refund handling.

## Calibrate Sample and Thresholds

Choose sample size from the decision, expected heterogeneity, desired precision, recruitment feasibility, and analysis plan. Values such as “5–10 interviews,” “100 survey responses,” “5% conversion,” or “40% rating 7+” may be planning examples, not universal validation rules.

For conversion or survey estimates, report numerator, denominator, recruitment channel, interval/uncertainty, exclusions, and segment differences. Compare against a relevant baseline or alternative. Do not infer a market from clicks alone.

Use bottom-up market sizing where possible:

```text
reachable eligible accounts × plausible adoption × evidence-based annual value
```

Disclose every source and assumption. There is no universal minimum SOM for “valid” VC-backed or bootstrapped problems.

## Synthesize

Rate each assumption separately:

- `supported`: convergent evidence with credible coverage;
- `uncertain`: evidence is sparse, biased, or conflicting;
- `contradicted`: observed behavior conflicts with the hypothesis;
- `untested`: no suitable evidence.

Then choose:

- `PROCEED`: enough evidence for the next cheapest solution/JTBD test;
- `NARROW`: a specific segment or situation is supported;
- `LEARN`: run a named study to resolve a decision-critical uncertainty;
- `PIVOT`: reformulate the problem from contradicted assumptions;
- `STOP`: consequence or reachable demand does not justify further investment.

Confidence is not a vote count. Preserve negative cases and explain why sources disagree.

## Output

```markdown
## Problem Discovery Decision — [initiative]

**Decision:** PROCEED / NARROW / LEARN / PIVOT / STOP
**Segment and situation:** [...]
**Problem hypothesis:** [...]

| Assumption | Evidence for | Evidence against | Bias/limit | Status |
|---|---|---|---|---|

**Current alternatives and switching cost:** [...]
**Estimated consequence/value:** [units and assumptions]
**Unknown that could reverse the decision:** [...]
**Next test:** [method, sample rationale, owner, stop rule]
**Kill criteria:** [...]
```

Route the supported problem to `business-product-leadership` for JTBD/solution framing, `product-ux-research` for study design, and `product-analytics` for instrumentation and experiments.
