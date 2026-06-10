---
name: paper-audit
description: Audit a research paper against its public codebase to detect mismatches between claims and implementation. Use when reviewing papers with code, verifying reproducibility, or checking for implementation gaps. Inspired by Feynman's /audit workflow.
metadata:
  tags: ["research", "phd", "audit", "reproducibility", "code-review", "paper-verification"]
---

# Paper Audit

**Claims in the paper must match code in the repository.**

This skill audits research papers against their publicly available codebases to detect mismatches, missing implementations, and reproducibility issues. Inspired by Feynman's `/audit` workflow.

> "Trust but verify." — Russian proverb

---

## 1. When to Audit

Audit when:
- Reviewing a paper with an accompanying GitHub repository
- Planning to build on someone's method (verify it works first)
- Reviewing for a conference/journal (check reproducibility)
- Teaching (show students what to look for)

**Do NOT audit when:**
- No code is available (audit becomes impossible)
- Paper is purely theoretical (no implementation to check)
- You are the author (use `internal-critique` instead)

---

## 2. The Audit Protocol

### Step 1 — Paper Claim Extraction

Extract all verifiable claims from the paper:

| Claim ID | Section | Claim | Verifiable? |
|---|---|---|---|
| C1 | Method | "We use Adam optimizer with lr=0.001" | Yes |
| C2 | Method | "Batch size is 256" | Yes |
| C3 | Results | "Achieves 95.2% accuracy on ImageNet" | Yes |
| C4 | Method | "Our attention mechanism reduces complexity to O(n)" | Partial (need to read code) |
| C5 | Ablations | "Removing component X drops performance by 3%" | Yes |

**Claim types:**
- **Hyperparameter:** Learning rate, batch size, weight decay, architecture details
- **Architecture:** Layer counts, dimensions, activation functions, connectivity
- **Data:** Dataset version, preprocessing steps, augmentation pipeline
- **Metric:** Reported numbers with confidence intervals
- **Ablations:** Performance differences when components are removed

### Step 2 — Code Mapping

For each verifiable claim, locate the corresponding code:

```
Paper Claim → Code Location → Verification Result

Example:
C1: "Adam optimizer, lr=0.001"
  → Code: train.py:45: optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
  → Result: ✅ MATCH

C2: "Batch size is 256"
  → Code: config.yaml: batch_size: 128
  → Result: ❌ MISMATCH (paper says 256, code uses 128)

C3: "95.2% accuracy on ImageNet"
  → Code: README.md reports 94.8%
  → Result: ⚠️ DISCREPANCY (0.4% gap, possibly different eval protocol)
```

**Where to look:**
| Claim Type | Likely Code Location |
|---|---|
| Hyperparameters | `config.yaml`, `args.py`, `train.py` top-level constants |
| Architecture | `model.py`, `network.py`, `architecture/` folder |
| Data preprocessing | `data.py`, `dataset.py`, `preprocess.py` |
| Training loop | `train.py`, `trainer.py`, `main.py` |
| Evaluation | `eval.py`, `test.py`, `metrics.py` |
| Ablations | `ablation.py`, `experiments/`, `scripts/` |

### Step 3 — Mismatch Classification

| Severity | Type | Description | Example |
|---|---|---|---|
| 🔴 **Critical** | Missing implementation | Code doesn't implement claimed method | Paper claims "novel attention mechanism" but code uses standard softmax |
| 🔴 **Critical** | Wrong hyperparameters | Key hyperparameters differ | Paper reports lr=0.001 but code uses lr=0.01 |
| 🟡 **Major** | Partial implementation | Only part of the method is implemented | Multi-scale feature extraction claimed but only single-scale in code |
| 🟡 **Major** | Different evaluation protocol | Metrics computed differently | Paper uses top-5 accuracy, code computes top-1 |
| 🟡 **Major** | Missing ablations | Claimed ablations not in code | Paper shows ablation table but no ablation scripts |
| 🟢 **Minor** | Documentation mismatch | README or comments wrong | README says Python 3.8+ but code uses 3.10 syntax |
| 🟢 **Minor** | Hardcoded values | Values not configurable | Batch size hardcoded instead of in config |
| 🔵 **Note** | Implementation detail | Different but equivalent approach | Paper describes loop, code uses vectorized operation |

### Step 4 — Reproducibility Check

Attempt to run the code (if environment permits):

```bash
# 1. Environment setup
pip install -r requirements.txt  # Check: are all dependencies listed?

# 2. Data availability
# Check: is data downloadable? Is preprocessing script provided?

# 3. Run training
python train.py --config config.yaml  # Check: does it run without errors?

# 4. Run evaluation
python eval.py --checkpoint model.pth  # Check: can you reproduce reported numbers?
```

**Reproducibility score:**
| Score | Criteria |
|---|---|
| 5/5 | Runs out-of-the-box, reproduces numbers exactly |
| 4/5 | Runs with minor fixes, numbers within 0.5% |
| 3/5 | Runs with significant fixes, numbers within 1-2% |
| 2/5 | Runs but numbers don't match (>2% gap) |
| 1/5 | Doesn't run, missing dependencies or data |
| 0/5 | No code provided |

---

## 3. Audit Report Template

```markdown
## Paper Audit: [Paper Title] by [Authors]

**Paper:** [arXiv/DOI link]
**Code:** [GitHub/repo link]
**Audit Date:** YYYY-MM-DD
**Auditor:** [Name/Agent]

### Claim Verification Matrix

| ID | Claim | Code Location | Result | Notes |
|---|---|---|---|---|
| C1 | Adam, lr=0.001 | train.py:45 | ✅ Match | Exact match |
| C2 | Batch size 256 | config.yaml:3 | ❌ Mismatch | Code uses 128 |
| C3 | 95.2% ImageNet | README.md | ⚠️ Discrepancy | README reports 94.8% |

### Mismatches Found

#### 🔴 Critical (0 found)
[None / list]

#### 🟡 Major (1 found)
1. **Different batch size** (C2)
   - Paper: 256
   - Code: 128
   - Impact: Could affect convergence and final performance
   - Recommendation: Clarify which was used for reported results

#### 🟢 Minor (1 found)
1. **README outdated** (C3)
   - README reports 94.8% but paper claims 95.2%
   - Possibly different evaluation protocol or checkpoint

### Reproducibility Score: 3/5

**What worked:**
- Code structure is clean and modular
- Dependencies are mostly listed

**Blockers:**
- Missing preprocessing script for custom dataset
- Hardcoded paths in config files

**Time to reproduce:** Estimated 4-6 hours (with fixes)

### Recommendations

1. **For authors:** Update README with correct hyperparameters and results
2. **For users:** Use batch_size=128 for fair comparison, or ask authors which was used
3. **For reviewers:** Flag batch size discrepancy in review

### Verdict

- [ ] **Reliable** — Claims match code, reproducible
- [ ] **Mostly reliable** — Minor discrepancies, reproducible with fixes
- [x] **Use with caution** — Major discrepancies, needs clarification
- [ ] **Not reproducible** — Critical mismatches or missing code
```

---

## 4. Common Audit Patterns

### Pattern 1: The "Cherry-picked" Result

**Symptom:** Paper reports best run, code shows multiple runs with variance.

**Detection:**
```python
# In code: results/ folder has multiple runs
# run_1: 94.1%, run_2: 94.8%, run_3: 95.2%, run_4: 94.5%
# Paper reports: 95.2% (best run, not average)
```

**Verdict:** Not necessarily dishonest, but should report mean ± std.

### Pattern 2: The "Missing Ablation"

**Symptom:** Ablation table in paper, no ablation code in repo.

**Detection:**
```bash
# Search for ablation scripts
find . -name "*ablation*" -o -name "*ablate*"
# No results found
```

**Verdict:** Major concern. How were ablation numbers computed?

### Pattern 3: The "Different Method"

**Symptom:** Paper describes complex method, code uses simple baseline.

**Detection:**
```python
# Paper: "We propose a novel hierarchical attention mechanism..."
# Code: model.py uses nn.MultiheadAttention (standard PyTorch)
```

**Verdict:** Critical mismatch. Method is not implemented as described.

### Pattern 4: The "Undocumented Preprocessing"

**Symptom:** Results don't match, preprocessing steps differ.

**Detection:**
```python
# Paper: "We normalize images to [0,1]"
# Code: transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
```

**Verdict:** Major concern. Different preprocessing → different results.

---

## 5. Tools for Auditing

### Manual Audit
- Read paper claims → Find code → Compare
- Best for: Deep understanding, thorough verification
- Time: 2-4 hours per paper

### Semi-Automated Audit
- Use `grep` / `ripgrep` to find claim keywords in code
- Use `diff` to compare configs
- Best for: Quick checks, large codebases
- Time: 30-60 minutes per paper

### Automated Audit (future)
- Parse paper PDF for claims (NLP extraction)
- Parse code for hyperparameters and architecture
- Auto-compare and flag mismatches
- Best for: Batch auditing, systematic reviews
- Time: 5-10 minutes per paper (after setup)

---

## 6. Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| Code verification | `sota-survey` | Find papers with code to audit |
| Reproducibility check | `experiment-tracking` | Run and compare experiments |
| Issue severity | `internal-critique` | Severity grading system |
| Paper quality | `publication-strategy` | Decide if paper is trustworthy enough to cite |

---

## References

- [Feynman /audit](https://github.com/companion-inc/feynman) — Paper vs codebase mismatch audit
- [Papers With Code](https://paperswithcode.com/) — Database of papers and their code
- [ML Reproducibility Challenge](https://paperswithcode.com/rc2022) — Community effort to reproduce ML papers
