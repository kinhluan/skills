---
name: scheduling-algorithms
description: Model, select, implement, or evaluate scheduling algorithms for operating systems, workflows, clusters, cloud resources, and real-time systems. Use for queues, DAG scheduling, preemption, fairness, deadlines, makespan, utilization, or scheduling research.
metadata:
  tags: ["scheduling", "optimization", "real-time", "distributed-systems", "algorithms"]
---

# Scheduling Algorithms

Model the scheduling problem before naming an algorithm. The same label can hide different arrival, precedence, resource, and preemption assumptions.

## Problem Contract

Record:

- jobs/tasks and arrival process;
- resource types, capacity, affinity, and heterogeneity;
- processing-time knowledge and uncertainty;
- precedence/DAG and communication cost;
- preemption, migration, replication, and failure rules;
- deadlines, priorities, fairness, and admission control;
- online/offline decision timing;
- primary objective and guardrails.

Typical objectives include response time, waiting time, slowdown, deadline misses, makespan, throughput, utilization, energy, cost, and fairness. Define units and aggregation; improving one can harm another.

## Select a Family

| Conditions | Candidate family |
|---|---|
| general-purpose interactive queue | round robin, priority aging, multilevel feedback |
| known short jobs | shortest-job/remaining-time variants |
| hard real-time uniprocessor | rate-monotonic or earliest-deadline-first with schedulability analysis |
| precedence-constrained heterogeneous workflow | list scheduling such as HEFT and domain-specific variants |
| independent cluster jobs | bin packing, backfilling, fair-share, dominant-resource fairness |
| large combinatorial offline problem | mathematical programming or bounded heuristic/metaheuristic |
| uncertain dynamic environment | robust/stochastic/online control; ML only with a safe baseline and fallback |

Check assumptions and complexity against workload scale. Do not use a metaheuristic or reinforcement learner merely because the search space is large.

## Evaluation

1. Use trace-driven and synthetic workloads that expose relevant regimes.
2. Compare with simple, strong, and domain-standard baselines under the same simulator, resource budget, stopping rule, and information access.
3. Separate tuning data from evaluation data.
4. Report distributions, tail behavior, and constraint violations, not only means.
5. Run sensitivity and ablation for workload mix, load, estimation error, failures, and hyperparameters.
6. Choose independent-run count through a power/precision or variance analysis.
7. Include scheduler overhead and scalability.

For hard real-time claims, provide a proof or accepted schedulability analysis; simulation alone cannot establish worst-case guarantees. For learned schedulers, test out-of-distribution load, unsafe actions, reward hacking, reproducibility, and deterministic fallback.

## Implementation Checks

- deterministic tie-breaking where required;
- bounded queue/memory growth;
- monotonic time and consistent units;
- starvation prevention and priority inversion handling;
- cancellation, retry, and idempotency;
- concurrent state synchronization;
- observable decision reasons and workload metrics;
- replayable traces and configuration.

## Output

```markdown
## Scheduling Design — [system]

**Problem model:** [online/offline, resources, arrivals, precedence]
**Objective/guardrails:** [...]
**Chosen family:** [algorithm and satisfied assumptions]
**Rejected alternatives:** [tradeoffs]
**Complexity/overhead:** [...]
**Failure and fallback:** [...]
**Evaluation protocol:** [workloads, baselines, metrics, uncertainty]
```

Read [references/detailed-guide.md](references/detailed-guide.md) only for the relevant algorithm family or implementation example. Verify formulas and citations against primary sources before using them in research claims.
