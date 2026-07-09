---
name: xquik-product-signals
description: Design source-backed public X signal workflows with Xquik for product discovery and release tracking. Use with JTBD, product analytics, or diffusion gates.
metadata:
  tags:
    - product-management
    - market-research
    - x-data
    - xquik
    - openapi
    - mcp
    - release-tracking
---

# Xquik Product Signals

Use Xquik as a source-backed input for product discovery, release tracking, and market signal analysis on public X data.

## Source Truth

Check these links before designing requests or agent workflows:

- Xquik API docs: https://docs.xquik.com/api-reference/overview
- Xquik OpenAPI: https://xquik.com/openapi.json
- Xquik MCP overview: https://docs.xquik.com/mcp/overview

Do not invent endpoint paths, request fields, response fields, rate behavior, or auth behavior. Verify them from source truth in the same task.

## When To Use

Use this skill when the user asks to:

- Track public launch, feature, category, or competitor signals on X
- Collect public posts, profile context, or keyword signals for JTBD research
- Build a release signal dashboard for Rogers diffusion gates
- Compare product language, objections, and adoption cues across public conversations
- Connect Xquik to an agent workflow through REST, webhooks, or MCP

## Signal Design Flow

1. Define the product question in one sentence.
2. Map it to a framework:
   - `business-product-leadership` for JTBD, MVP, and market framing.
   - `diffusion-release-tracking` for rollout gates and adoption signals.
   - `product-analytics` for funnels, cohorts, and experiment metrics.
   - `product-ux-research` for qualitative synthesis.
3. Select the X signal type: account, keyword, post, conversation, launch term, competitor term, or event.
4. Verify the Xquik endpoint or MCP tool against source truth.
5. Define the sample window, query terms, inclusion criteria, and exclusion criteria.
6. Separate observed signals from interpretation.
7. Produce a decision artifact with confidence, caveats, and next actions.

## Output Template

```markdown
## Xquik Product Signal Brief
**Product Question:** ...
**Framework:** JTBD / diffusion gate / analytics / UX research
**Xquik Surface:** REST API / webhook / MCP
**Source Links Checked:** ...
**Signal Scope:** accounts, keywords, posts, dates, exclusions

### Observed Signals
| Signal | Evidence | Product Meaning | Confidence |
|---|---|---|---|

### Decision
Recommendation: go / hold / research more
Reason:
Next action:
```

## Guardrails

- Keep Xquik opt-in and scoped to the user's stated product question.
- Do not use private account data unless the user explicitly authorizes it.
- Do not run write, scheduled, persistent, or bulk workflows without explicit approval.
- Do not store raw public content longer than the task requires unless the user asks.
- Do not treat social volume as product-market fit by itself.
- Do not mix competitor monitoring with harassment, evasion, or personal targeting.

## Quality Checks

- Source docs and OpenAPI were reachable.
- The requested endpoint or MCP tool exists in source truth.
- The sample definition is written down before analysis.
- Observations and interpretations are separated.
- The result maps back to a product decision, not vanity reporting.
