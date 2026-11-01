---
name: art-of-war-software-engineering
description: Evaluate a major software or product initiative across alignment, timing, technical terrain, accountable leadership, and delivery method. Use for build/buy/partner decisions, strategic timing, resource allocation, or a go/hold/stop review before committing substantial effort.
metadata:
  tags: ["strategy", "initiative-review", "build-vs-buy", "risk", "resource-allocation"]
---

# Art of War for Software Engineering

Use Sun Tzu's five factors as a mnemonic for structured due diligence, not as a source of scientific thresholds. Make assumptions visible and calibrate the decision to the initiative's cost, reversibility, and evidence.

## Five Parallel Factors

| Factor | Software interpretation | Evidence |
|---|---|---|
| Tao — alignment | shared outcome, user value, incentives, explicit non-goals | strategy, problem evidence, stakeholder understanding |
| Heaven — conditions | timing, regulation, ecosystem, competition, dependencies | dated market/technology evidence and uncertainty |
| Earth — terrain | architecture, legacy constraints, skills, data, build/buy landscape | code/runtime audit, dependency map, vendor options |
| Command — leadership | accountable owner, decision rights, capability, conflict resolution | named owner, authority, capacity, escalation path |
| Method — operating system | delivery, testing, observability, security, learning cadence | current five-metric DORA baseline, controls, feedback loops |

Assess all five against the same initiative. A factor can be `supported`, `uncertain`, `constrained`, or `contradicted`; numeric scores are optional and must have a locally defined rubric.

## Workflow

1. Define the decision, options, deadline, sunk costs to ignore, and what is reversible.
2. Gather evidence for every factor and label inference separately.
3. Identify the two assumptions most capable of reversing the decision.
4. Compare options, including:
   - build;
   - buy/managed service;
   - partner;
   - adapt an existing capability;
   - defer or stop.
5. Test the riskiest assumption with the cheapest credible probe.
6. Decide `GO`, `CONDITIONAL GO`, `HOLD`, or `STOP`, with owner, review date, and exit criteria.

Do not default every generic subdomain to SaaS. Evaluate strategic control, regulation, data residency, switching cost, reliability, integration, total cost, vendor health, and exit plan. Likewise, do not default to building merely because the team can.

## Factor Prompts

### Tao

- Can affected people state the outcome and non-goals consistently?
- Is the user/problem evidence stronger than internal enthusiasm?
- What incentive could cause local optimization against the outcome?

### Heaven

- Which facts are time-sensitive and verified as of what date?
- What window closes if delayed, and what improves by waiting?
- Which external dependency can invalidate the plan?

### Earth

- What code, data, organizational, or vendor boundary dominates cost?
- Is the proposed boundary independently changeable and operable?
- What migration and exit paths exist?

### Command

- Who owns the decision and the operating outcome?
- Does that owner have authority, capacity, and relevant expertise?
- How are cross-team conflicts resolved?

### Method

- What is the service-level DORA baseline across change lead time, deployment frequency, failed deployment recovery time, change fail rate, and deployment rework rate?
- Can the team test, observe, reverse, and learn from a small release?
- Which constraint should one improvement experiment target?

Avoid historical universal DORA tiers and broad incident MTTR when assessing current delivery performance.

## Decision Matrix

```markdown
| Factor | Status | Evidence | Reversal assumption | Mitigation/experiment |
|---|---|---|---|---|
| Tao | | | | |
| Heaven | | | | |
| Earth | | | | |
| Command | | | | |
| Method | | | | |
```

Choose a decision rule before scoring. For high-consequence initiatives, one contradicted non-negotiable may outweigh several strong factors. For reversible experiments, uncertainty may justify a small probe rather than a stop.

## Output

```markdown
## Strategic Assessment — [initiative]

**Decision:** GO / CONDITIONAL GO / HOLD / STOP
**Options considered:** [...]
**Evidence date:** [...]

### Five-factor assessment
[matrix]

**Decisive constraint:** [...]
**Assumption most likely to reverse decision:** [...]
**Next experiment/mitigation:** [owner, cost, deadline, success/stop rule]
**Review trigger:** [...]
**Residual risk:** [...]
```

Route deep problem validation to `problem-discovery`, architecture evidence to `c4-model`, delivery measurement to `dora-core`, and adoption analysis to `diffusion-release-tracking`.
