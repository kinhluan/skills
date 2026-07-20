---
name: sota-survey
description: Conduct a rigorous state-of-the-art literature survey, scoping a question, searching primary scholarly sources, screening studies, extracting comparable evidence, synthesizing disagreements, and identifying defensible gaps. Use for literature reviews, related-work maps, or current-paper searches.
metadata:
  tags: ["research", "literature-review", "evidence-synthesis", "sota", "scholarly-search"]
---

# SOTA Survey

Build a traceable evidence map rather than a ranked list of famous papers. Search current sources when the user asks for recent work, and cite primary papers for claims about methods or results.

## Protocol

### 1. Scope

Record:

- research question and decision the survey informs;
- population/domain, intervention or method, comparators, outcomes, and context where applicable;
- inclusion/exclusion criteria;
- languages, publication types, and date coverage;
- databases and search date;
- treatment of preprints, grey literature, theses, replications, and negative results.

Do not default to “last five years” if seminal work is needed. Use a justified end date equal to the actual search date.

### 2. Search

Combine:

1. concept synonyms and controlled vocabulary;
2. multiple scholarly databases appropriate to the field;
3. backward and forward citation searching;
4. key author, dataset, method, and venue searches;
5. trial, dataset, code, or preprint registries when relevant.

Save exact queries, filters, result counts, API/database versions, and export files. Deduplicate by stable identifiers first, then bibliographic similarity.

Venue rankings, author h-index, and citation counts may assist discovery but must not be treated as a universal quality order or exclusion threshold. Rankings measure different constructs and coverage; new, interdisciplinary, replication, and negative work can be important before accumulating citations.

### 3. Screen

Use at least title/abstract and full-text stages. Record one exclusion reason per full-text exclusion. For systematic reviews, use independent screening or a documented conflict-resolution process when resources allow.

Stop snowballing based on a documented saturation rule and search budget, not a claim of completeness merely because one iteration found nothing.

### 4. Extract

For each included work capture:

| Field | Content |
|---|---|
| identity | DOI/stable ID, version, venue, year |
| question | problem and claimed contribution |
| method | design, assumptions, intervention/model |
| evidence | datasets, sample, baselines, metrics, uncertainty |
| result | effect/estimate with units and conditions |
| validity | limitations, bias, leakage, confounders |
| reproducibility | code, data, configuration, license |
| relevance | connection to the survey question |

Never compare headline scores unless datasets, splits, preprocessing, metric definitions, resource budgets, and evaluation protocols are compatible.

### 5. Appraise

Choose a design-appropriate appraisal tool or explicit rubric. Evaluate evidence directly:

- construct and outcome validity;
- sample and benchmark representativeness;
- baseline fairness;
- statistical and practical uncertainty;
- leakage, selective reporting, and multiplicity;
- robustness and external validity;
- artifact availability and reproducibility.

Do not infer quality solely from prestige, citation count, author reputation, or journal quartile.

### 6. Synthesize

Build a taxonomy from observed approaches. Separate:

- findings that are directly comparable;
- findings that agree under different conditions;
- genuine contradictions;
- missing evidence;
- methodological and deployment constraints.

Quantify consensus only when the sampling frame and coding rule justify it. Otherwise describe the balance and strength of evidence rather than using an arbitrary percentage.

A defensible gap must state who or what is affected, what evidence is missing, why existing work does not answer it, and what study could close it. “Few papers” alone is not a contribution.

## Output

```markdown
## SOTA Survey — [question]

**Search date:** [date, timezone]
**Coverage:** [databases, dates, publication types]
**Protocol:** [criteria and saved query/artifact]
**Flow:** retrieved N → deduplicated N → screened N → included N

### Taxonomy
[approaches and representative primary papers]

### Evidence Matrix
| Study | Method | Data/context | Comparator | Outcome | Result/uncertainty | Validity | Artifact |
|---|---|---|---|---|---|---|---|

### Agreement and Disagreement
[claims, supporting evidence, conflicting evidence, boundary conditions]

### Gaps
| Missing evidence | Why it matters | Existing limitation | Study needed |
|---|---|---|---|

### Limitations of this survey
[coverage, language, access, screening, date, publication bias]
```

Use [references/gap-matrix-template.md](references/gap-matrix-template.md) when a reusable comparison artifact is helpful. Route question formulation to `research-question`, experiment planning to `research-design`, and manuscript synthesis to `paper-writing`.
