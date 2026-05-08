---
name: sota-survey
description: Survey State-of-the-Art literature on a research topic. Use when asked to find papers, survey a field, map the research landscape, identify gaps, or build a literature matrix. First step in any research workflow.
metadata:
  tags: ["research", "phd", "literature", "survey", "sota"]
  version: 1.0.0
  triggers:
    - "Survey SOTA on X"
    - "What are the latest papers on"
    - "Literature review on"
    - "Find papers about"
    - "Map the research landscape"
    - "What has been done on"
---

# SOTA Survey

Systematic literature mapping to identify what exists, what works, and where the gaps are.

## Workflow

### Step 1 — Define Scope
```
Topic: <research area>
Time range: last N years (default: 5)
Venues: top conferences/journals for this field
Keywords: [primary] + [secondary] + [negative exclusions]
```

### Step 2 — Search Strategy
Search in this order:
1. **arXiv** (cs.AI, cs.LG, cs.DC, etc.) — `arxiv.org/search`
2. **Semantic Scholar** — `api.semanticscholar.org`
3. **Google Scholar** — broad coverage
4. **Venue-specific** — NeurIPS, ICML, ICLR, CVPR, ACL, AAAI proceedings

Query pattern: `("term1" OR "term2") AND ("method" OR "approach") AND "domain"`

### Step 3 — Paper Triage (3-pass)
**Pass 1 — Title+Abstract** (2 min/paper): Keep if directly relevant  
**Pass 2 — Introduction+Conclusion** (10 min/paper): Extract key claims  
**Pass 3 — Full read** (30-60 min/paper): Extract method, results, limitations  

### Step 4 — Build Gap Matrix

| Paper | Problem | Method | Dataset | Metric | Result | Limitation |
|-------|---------|--------|---------|--------|--------|------------|
| Author et al. (year) | ... | ... | ... | ... | ... | ... |

### Step 5 — Synthesize

**Taxonomy** — group papers by approach/paradigm:
- Group A: [name] — papers [1,3,5]
- Group B: [name] — papers [2,4]

**Trend timeline:**
```
2019: early work on X
2021: shift to Y approach  
2023: dominated by Z
2025: open problems remain in W
```

**Gap analysis:**
- Gap 1: No work addresses [condition] in [domain]
- Gap 2: Methods assume [X] but real-world violates it
- Gap 3: Evaluated only on [benchmark], not [realistic setting]

## Output Format

```markdown
## SOTA Survey: [Topic]

**Coverage:** N papers, [year range], venues: [list]

### Taxonomy
...

### Key Findings
- State: [what works best today]
- Benchmark: [standard dataset/metric]
- Open problem: [what nobody has solved]

### Gap Table
| Gap | Why it matters | Potential approach |
...

### Top Papers to Read First
1. [Author et al. year] — [why: foundational/best result/closest to your work]
2. ...
```

## Tool Integration (optional)

If Semantic Scholar API available:
```bash
curl "https://api.semanticscholar.org/graph/v1/paper/search?query=<topic>&fields=title,year,citationCount,abstract"
```

If HuggingFace Papers available: search `hf_hub_query` with paper topic.

## Links to Other Skills
- Feeds into → `research-question` (use gaps found here to formulate RQ)
- Feeds into → `paper-writing` (Related Work section)
- Iterates with → `experiment-tracking` (as new baselines discovered)
