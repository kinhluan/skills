---
name: architecture-review
description: Review C4 vs code, fitness functions, and architecture drift. Use when checking design-to-code sync, fitness-function coverage, or deciding whether a finding belongs to SE or SRE.
metadata:
  tags:
  - architecture
  - review
  - c4
  - fitness-functions
  - design-to-code
  - escalation
  version: 1.0.0
---

# Architecture Review (Solution Architect)

This is the **architect's** loop: does the running system still match the intended architecture, and are the guards (fitness functions, ADRs) still true?

It is not a pull-request nitpick, a quality gate, or an incident review.

| Concern | Owner | Do not do here |
|---------|-------|----------------|
| C4 vs code, wrong quantum, missing ADR, dead fitness function | **SA (this skill)** | — |
| Implementation, tests, PR correctness | SE (`code-review-pr`) | Do not review the diff as if you were the engineer |
| SLO burn, on-call, capacity, failover ops | SRE | Do not write runbooks or page anyone |
| Threat model, secrets, vuln class | SecOps | Do not claim a security review |
| Coverage / SAST / merge gate | QC | Do not "pass" architecture because CI is green |

Diagrams: `c4-model` and the L1–L3 skills. Fitness functions: `evolutionary-architecture` (do not reinvent them here). Decisions already made: read `architecture-decision-records` instead of relitigating. Why the system exists: `why-strategic-rationale`.

---

## When to run

- Before a change that is hard to undo (store, sync model, service split).
- After two milestones, if C4 has not been re-checked against the repo.
- Fitness functions that never fail, or characteristics with no automated check.
- An argument that should have been an ADR.

Timebox one sitting. If you cannot finish C4 L2 vs deployables + fitness + ADR gaps, split the review; do not invent a second process.

---

## Review loop

1. **Intent.** Which characteristics matter here (consistency, residency, team boundary, deploy independence)? If "why" is unclear, stop and use `why-strategic-rationale`.
2. **C4 vs code (Design-to-Code Sync).** Walk L1 actors/systems, L2 containers vs actual deployables, L3 components vs packages. Every name on the diagram must exist; every store/queue/service in the repo must appear or be explicitly out of scope.
3. **Fitness functions.** For each claimed characteristic: is there a check in CI or production, did it fail in the last 90 days (not theater), does a fail block merge? Details live in `evolutionary-architecture`.
4. **Decisions.** Hard-to-change choices without an accepted ADR are gaps. Accepted ADRs that the code contradicts are fails. Do not re-open an accepted ADR in this review.
5. **Verdict + escalate.** Pass / fail per check. Each fail has an owner (SA stays, or SE / SRE / SecOps / QC). Propose; the user decides.

---

## C4 vs code

**Pass**

- L2 container list matches deployables (services, databases, brokers, jobs).
- L3 components map to packages/modules; the Dependency Rule is enforced or clearly waived in an ADR.
- No orphan: a service in the repo with no C4 box, or a C4 box with no code/path.

**Fail**

- Diagram names a container the repo does not ship.
- Repo has a datastore, queue, or sync path C4 omits.
- Domain/application layers import infrastructure with no import-linter (or equivalent) contract.
- Team boundaries cut across a bounded context (`ddd-core`) without an ADR.

How to check: start from `c4-level2-container` and `c4-level3-component`, then list deployables (`Dockerfile`, Helm/Kustomize, compose, IaC modules) and top-level packages. Diff the two lists. Do not draw a new C4 from memory if a diagram already exists — update or fail it.

---

## Fitness functions

Use `evolutionary-architecture` for types (atomic / holistic / triggered / continuous) and examples. In this review, only ask:

| Question | Pass | Fail |
|----------|------|------|
| Does each claimed characteristic have a check? | Named test or probe | Characteristic is slogan-only |
| Has any check failed in ~90 days? | Yes, then fixed | Never fails (theater) |
| Does a fail block merge or page the right owner? | Yes | Warning-only, ignored |
| Count | 3–5 to start | None, or a zoo of 20 |

Do not add a fitness function in this skill. Record the gap and point at `evolutionary-architecture` for the author.

---

## ADRs and rationale

- Missing ADR for a choice that will last >6 months → fail, hand the write-up to `architecture-decision-records` (MADR).
- Code contradicts an **accepted** ADR → fail. The fix is code or a superseding ADR, not a review comment that re-argues the options.
- "Why this product" is not an architecture review. Send that to `why-strategic-rationale`.

---

## Escalation

| You found | Escalate to | Stop |
|-----------|-------------|------|
| Invariant specified, implementation wrong or untested | SE | Do not write the patch here unless asked |
| Structure is fine; runtime/SLO/failover is not evidenced | SRE | Do not invent monitors |
| Secret in repo, auth boundary missing as a *threat* | SecOps | Do not run an audit |
| Gate (coverage, SAST) is the question | QC | Do not waive a gate |
| C4/code/fitness/ADR | Stay (SA) | — |

If two owners apply, split the findings. Do not blend an architecture fail into a QC comment.

---

## Output (one sitting)

```
Scope: <system / PR / service>
Intent: <characteristics under review>
C4 vs code: PASS/FAIL — <one line>
Fitness: PASS/FAIL — <one line>
ADRs: PASS/FAIL — <missing or contradicted>
Escalate: <none | SE/SRE/SecOps/QC + why>
User decides: <what you will not do until they say so>
```

Propose the next ADR or fitness function. Do not merge, page, or rewrite QC/SRE/SecOps/PhD skills from here.

---

## Ecosystem

- `c4-model` / L1–L3 — diagrams this review diffs against code
- `evolutionary-architecture` — write and wire fitness functions
- `architecture-decision-records` — capture or supersede decisions
- `clean-architecture` / `ddd-core` / `ddd-tactical` — Dependency Rule and bounded contexts
- `why-strategic-rationale` — why the system exists
- `code-review-pr` — SE owns the diff after you escalate
