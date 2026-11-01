---
name: dora-core
description: Measure and improve software delivery performance with DORA's current five-metric throughput and instability model. Use when baselining one application or service, diagnosing delivery friction, selecting improvement experiments, or reviewing metric instrumentation.
metadata:
  tags: ["dora", "devops", "delivery-performance", "metrics", "continuous-improvement"]
---

# DORA Core

Use DORA metrics as a diagnostic system for continuous improvement, not as targets, rankings, or individual performance measures. Apply them to one application or service at a time and compare that service with its own historical baseline.

## Current Five-Metric Model

### Throughput

| Metric | Definition |
|---|---|
| Change lead time | Time from a change being committed to version control until it is successfully deployed to production |
| Deployment frequency | Number of production deployments in a period, or elapsed time between deployments |
| Failed deployment recovery time | Time to recover from a deployment that fails and requires immediate intervention |

### Instability

| Metric | Definition |
|---|---|
| Change fail rate | Proportion of deployments requiring immediate intervention, such as rollback or hotfix |
| Deployment rework rate | Proportion of deployments that are unplanned work caused by a production incident |

Do not substitute broad incident MTTR for failed deployment recovery time. Incidents unrelated to a production change are operational reliability data, not this DORA delivery metric.

## Establish Measurement Boundaries

Before calculating anything, record:

- service or application;
- production environment;
- deployment event definition;
- observation window and time zone;
- change-to-deployment correlation method;
- what qualifies as immediate intervention;
- how incident-driven deployments are identified;
- missing or censored data.

Keep numerator and denominator events inspectable. Do not blend services with materially different delivery systems or risk profiles.

## Baseline Workflow

1. Start with a conversation or DORA Quick Check if event data is not readily available.
2. Select a representative window. Use a longer window for low-frequency services and disclose seasonality or freezes.
3. Calculate all five metrics together.
4. Visualize distributions and trends, not only averages:
   - median and upper percentile for durations;
   - count and interval for frequency;
   - numerator, denominator, and confidence interval for rates.
5. Map the delivery path from commit to production and locate the largest wait state, batch, or recovery constraint.
6. Form one capability hypothesis, choose a small improvement experiment, and define a guardrail metric.
7. Re-measure the same service and window definition. Record confounders rather than claiming causality from correlation alone.

## Diagnostic Questions

- Where does work wait longest between commit and production?
- Which deployment steps require handoffs or large batches?
- Which failure classes cause immediate intervention?
- How often is deployment work unplanned incident rework?
- Can the team restore a failed deployment safely with rollback, roll-forward, or feature controls?
- Do test, observability, architecture, and approval practices address the observed constraint?

Typical experiments include smaller batches, reliable continuous integration, deployment automation, safer database changes, improved test feedback, observability, and loosely coupled delivery boundaries. Select an experiment from evidence; do not assume one practice is universally the primary cause.

## Interpretation Guardrails

- Do not use historical `Elite/High/Medium/Low` cutoffs as universal service-level objectives.
- Do not compare unrelated services or rank teams.
- Do not optimize deployment count while ignoring instability.
- Do not set a single metric as a goal; this invites gaming under Goodhart's law.
- Do not count staging activity as production deployment.
- Do not claim speed and stability are an inherent tradeoff.
- Pair delivery metrics with product outcomes, reliability objectives, and team well-being.

## Output

```markdown
## DORA Delivery Assessment — [service]

**Window:** [start–end, timezone]
**Boundary:** [production service and deployment definition]
**Data quality:** [coverage, missing events, assumptions]

| Factor | Metric | Result | Prior baseline | Evidence |
|---|---|---:|---:|---|
| Throughput | Change lead time | | | |
| Throughput | Deployment frequency | | | |
| Throughput | Failed deployment recovery time | | | |
| Instability | Change fail rate | | | |
| Instability | Deployment rework rate | | | |

**Primary constraint:** [observed wait/failure/rework pattern]
**Capability hypothesis:** [testable hypothesis, not asserted cause]
**Experiment:** [small change, owner, duration]
**Guardrails:** [stability/product/team measures]
**Next review:** [date and unchanged measurement definition]
```

## Sources

- [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- [History of DORA's software delivery metrics](https://dora.dev/insights/dora-metrics-history/)
- [DORA capability catalog](https://dora.dev/capabilities/)
