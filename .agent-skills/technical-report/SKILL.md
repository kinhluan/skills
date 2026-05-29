---
name: technical-report
description: Write technical reports — experiment reports, system design documents, code documentation, and internal research memos. Use when documenting technical work that doesn't fit paper format.
metadata:
  tags: ["research", "phd", "technical-report", "documentation", "experiment-report", "system-design"]
  version: 1.0.0
  triggers:
    - "technical report"
    - "experiment report"
    - "system design document"
    - "code documentation"
    - "research memo"
    - "báo cáo kỹ thuật"
    - "tài liệu thiết kế"
---

# Technical Report

**Purpose:** Document technical work in detail — experiments, systems, code, and internal research.

**When to use:**
- Writing experiment reports (detailed results)
- Documenting system architecture
- Writing code documentation
- Creating internal research memos
- Preparing supplementary materials

**Links to:**
- `experiment-tracking` — experiment data
- `research-design` — methodology
- `thesis-writing` — thesis integration
- `paper-writing` — paper format
- `docker-containerization` — deployment docs
- `kubernetes-orchestration` — infrastructure docs

---

## Report Types

### 1. Experiment Report

```markdown
# Experiment Report: [Experiment Name]

**Date:** [YYYY-MM-DD]
**Author:** [Name]
**Version:** [v1.0]

## 1. Objective
[What question does this experiment answer?]

## 2. Setup

### 2.1 Hardware
- GPU: [type] × [count]
- RAM: [size]
- Storage: [type/size]

### 2.2 Software
- Python: [version]
- PyTorch: [version]
- CUDA: [version]

### 2.3 Dataset
| Property | Value |
|----------|-------|
| Name | [dataset] |
| Size | [N samples] |
| Train/Val/Test | [split ratios] |
| Preprocessing | [steps] |

### 2.4 Hyperparameters
| Parameter | Search Range | Final Value | Selection |
|-----------|--------------|-------------|-----------|
| learning_rate | [1e-4, 1e-2] | 1e-3 | grid search |
| batch_size | [16, 32, 64] | 64 | validation loss |

## 3. Method
[Brief description of what was tested]

## 4. Results

### 4.1 Main Results
| Method | Accuracy | F1 | Latency |
|--------|----------|-----|---------|
| Baseline | 85.2±0.3 | 84.1±0.4 | 12ms |
| Ours | 87.1±0.2 | 86.3±0.3 | 15ms |

### 4.2 Ablation
| Configuration | Accuracy | Δ |
|---------------|----------|---|
| Full | 87.1±0.2 | — |
| w/o Module A | 85.8±0.3 | -1.3 |
| w/o Module B | 86.2±0.2 | -0.9 |

### 4.3 Statistical Analysis
- Test: paired t-test
- p-value: 0.002 (significant at α=0.05)
- Seeds: 5 (42, 123, 456, 789, 1024)

## 5. Analysis
[Interpretation of results, patterns observed]

## 6. Conclusions
[Key takeaways, next steps]

## 7. Reproducibility
- Code: [URL or "available upon request"]
- Data: [URL or "see Section 2.3"]
- Random seeds: [list]
```

### 2. System Design Document

```markdown
# System Design: [System Name]

**Version:** [v1.0]
**Status:** [Draft/Review/Final]
**Last Updated:** [Date]

## 1. Overview
[1 paragraph: what the system does, why it exists]

## 2. Requirements

### 2.1 Functional Requirements
- FR1: [requirement]
- FR2: [requirement]

### 2.2 Non-Functional Requirements
- NFR1: Performance — [specification]
- NFR2: Scalability — [specification]
- NFR3: Reliability — [specification]

## 3. Architecture

### 3.1 High-Level Design
[Architecture diagram]

### 3.2 Component Design
| Component | Responsibility | Interface |
|-----------|---------------|-----------|
| [comp1] | [what it does] | [API/events] |
| [comp2] | [what it does] | [API/events] |

### 3.3 Data Flow
[Sequence diagram or flowchart]

## 4. API Design

### 4.1 Endpoints
| Method | Path | Description |
|--------|------|-------------|
| GET | /api/v1/[resource] | [description] |
| POST | /api/v1/[resource] | [description] |

### 4.2 Data Models
```typescript
interface [Model] {
  id: string;
  field: type;
}
```

## 5. Database Design
[ER diagram, schema]

## 6. Deployment
[Infrastructure, Docker, K8s config]

## 7. Testing Strategy
[Unit, integration, e2e tests]

## 8. Monitoring
[Metrics, alerts, dashboards]

## 9. Security
[Authentication, authorization, data protection]

## 10. Future Work
[Planned improvements]
```

### 3. Code Documentation

```markdown
# [Module Name] Documentation

## Overview
[What this module does]

## Installation
```bash
pip install [package]
```

## Quick Start
```python
from module import Class

# Initialize
obj = Class(param1=value1)

# Use
result = obj.method(input)
```

## API Reference

### Class: `ClassName`

#### `__init__(self, param1, param2)`
**Description:** Initialize the class.

**Parameters:**
| Name | Type | Default | Description |
|------|------|---------|-------------|
| param1 | str | required | [description] |
| param2 | int | 10 | [description] |

**Example:**
```python
obj = Class(param1="value", param2=20)
```

#### `method(self, input)`
**Description:** [what it does]

**Parameters:**
| Name | Type | Description |
|------|------|-------------|
| input | np.ndarray | [description] |

**Returns:**
| Type | Description |
|------|-------------|
| dict | [description] |

**Raises:**
| Exception | Condition |
|-----------|-----------|
| ValueError | [when] |

**Example:**
```python
result = obj.method(np.array([1, 2, 3]))
```

## Configuration
| Variable | Default | Description |
|----------|---------|-------------|
| DEBUG | False | Enable debug mode |

## Changelog
### v1.0.0 (YYYY-MM-DD)
- Initial release
```

### 4. Research Memo

```markdown
# Research Memo: [Topic]

**Date:** [YYYY-MM-DD]
**Author:** [Name]
**Status:** [Draft/Reviewed]

## Context
[Why this memo exists, what triggered it]

## Key Observations
1. [Observation 1]
2. [Observation 2]
3. [Observation 3]

## Analysis
[Detailed analysis of observations]

## Implications
[What this means for the research]

## Action Items
- [ ] [Action 1]
- [ ] [Action 2]

## References
[Related papers, experiments, discussions]
```

---

## Report Quality Checklist

### Content
- [ ] Clear objective statement
- [ ] Sufficient detail for reproduction
- [ ] Results with mean ± std (min 3 seeds)
- [ ] Statistical significance tests
- [ ] Honest limitations acknowledged

### Format
- [ ] Consistent notation
- [ ] Figures with captions
- [ ] Tables with captions
- [ ] References formatted
- [ ] Version number
- [ ] Date

### Technical
- [ ] Code snippets tested
- [ ] Commands verified
- [ ] Links working
- [ ] Version numbers accurate

---

## Integration Flow

```
experiment-tracking (data)
    ↓
technical-report (this skill)
    ├── Experiment Report → advisor/committee
    ├── System Design → team/collaborators
    ├── Code Documentation → users/developers
    └── Research Memo → self/team
    ↓
thesis-writing (integrate into thesis)
    ↓
paper-writing (extract for paper)
    ↓
conference-paper (present findings)
    ↓
progress-report (summarize for advisor)
```
