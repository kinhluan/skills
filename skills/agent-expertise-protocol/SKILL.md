---
name: agent-expertise-protocol
description: Design or review governance rules for expert agents, including authority boundaries, uncertainty, handoffs, escalation, and evidence standards. Use when defining agent roles or clarifying which actions require user approval; it is not automatically active outside an invoked governance task.
metadata:
  tags: ["agent-governance", "authority", "expertise", "handoff", "evidence"]
---

# Agent Expertise Protocol

Use this skill to create or audit an agent-governance policy. A skill cannot make itself globally mandatory; durable repository-wide rules belong in the host's instruction or policy mechanism.

## Principles

1. **Outcome over persona:** State the useful capability and boundary; do not require ceremonial role declarations.
2. **Evidence over authority:** Support claims with inspected artifacts, current primary sources, or explicit reasoning.
3. **Calibrated uncertainty:** Distinguish fact, inference, recommendation, and unknown.
4. **Scoped autonomy:** Take normal, reversible implementation steps inside the user's requested scope. Ask when authority, target, or consequential outcome materially expands.
5. **User ownership:** Preserve user data and decisions; never confuse a framework default with permission.
6. **Minimal coordination:** Add handoffs or specialists only when they improve correctness or throughput.

## Authority Model

| Action | Default treatment |
|---|---|
| read, search, inspect, calculate | proceed within scope |
| local reversible implementation requested by user | proceed and verify |
| formatting or generated artifacts required by the change | proceed |
| external message, issue, PR, commit publication, deployment | require explicit request or unambiguous workflow authority |
| destructive, irreversible, financial, access-control, or production action | verify exact target and obtain required approval |
| material scope or strategy change | present evidence and request a decision |

Do not force a user through a prescribed research, product, or architecture sequence when they ask for a bounded downstream task. Mention missing prerequisites only when they affect correctness, safety, or the requested outcome.

## Expertise Contract

For each role or skill, define:

```yaml
capability: what the agent can reliably do
triggers: requests and contexts that should activate it
inputs: evidence or artifacts needed
outputs: concrete artifact or decision
boundaries: adjacent work it should route or decline
authority: permitted read/write/external actions
verification: evidence required before claiming completion
```

Keep “when to use” in skill metadata. Put procedural details in the body and large domain references in directly linked files.

## Cross-Domain Work

1. Identify the parts that need distinct expertise.
2. Keep one accountable outcome and shared facts.
3. Route only the part that benefits from another skill or agent.
4. Pass the minimum relevant artifact, not a prewritten conclusion.
5. Reconcile conflicting advice through evidence, tradeoffs, and the user's objective.

No agent role becomes the final arbiter merely by being labeled architect, security, product, or reviewer.

## Escalate When

- the exact target or authorization cannot be resolved;
- a new action would affect external people, production, money, permissions, or publication;
- two plausible options materially change the result;
- required evidence is unavailable and guessing would be risky;
- an instruction conflict cannot be safely reconciled.

An escalation should contain the known facts, the blocked decision, options with consequences, and the smallest question needed.

## Quality Audit

- [ ] Trigger and output are concrete.
- [ ] Claims are sourced or explicitly marked as inference.
- [ ] Actions remain inside granted scope.
- [ ] The policy distinguishes local work from external mutation.
- [ ] Uncertainty and missing verification are visible.
- [ ] Handoffs preserve context without duplicating ownership.
- [ ] No fixed framework is treated as universally mandatory.
- [ ] Completion requires evidence, not a confident narrative.

## Related Resources

- [Master Framework](../../docs/master-framework.md) for optional ecosystem context.
- [`kinhluan-router`](../kinhluan-router/SKILL.md) for on-demand skill selection.
- [`collaborative-engineering-agent`](../collaborative-engineering-agent/SKILL.md) for bounded delivery coordination.
