---
name: academic-research-excellence
description: Core PhD Research Workflow. Use this skill for Literature Review, finding Research Gaps, LaTeX publication patterns (IEEE/ACM), and designing Ablation Studies.
metadata:
  tags: ["research-methodology", "phd-workflow", "latex", "scientific-writing"]
---

# Academic Research Excellence (PhD Workflow)

A professional framework for conducting high-impact AI research and scientific publishing.

## 📚 1. Literature Review & Gap Analysis
Use this workflow to identify where your contribution fits:
1.  **Selection:** Identify top 10 papers in the sub-field (last 3-5 years).
2.  **Synthesis:** Create a **Comparison Table** (Method, Data, Metrics, Limitations).
3.  **Gap Discovery:** Look for "Future Work" sections or common failures in existing methods (e.g., "Existing FL models fail under extreme non-IID data").
4.  **Positioning:** State clearly: *"While Paper A solves X, it ignores Y. Our method solves Y by doing Z."*

## ✍️ 2. Scientific Writing (LaTeX/Overleaf)
Patterns for professional publication:
- **Math Notations:** Use standard notation (e.g., $Q(s, a)$ for DQN).
- **IEEE/ACM Tables:** Use `booktabs` for clean, professional tables.
- **Algorithm Pseudo-code:** Use `algorithmicx` or `algorithm2e` for readable logic.

## 🧪 3. Experimental Design (PhD Standard)

### Ablation Studies
Prove your components matter. If your algorithm has 3 parts (A, B, C):
- Test Base.
- Test Base + A.
- Test Base + A + B.
- Test Base + A + B + C (Full).
*Goal: Show incremental improvement for each addition.*

### Sensitivity Analysis
Test how your algorithm performs when parameters change (e.g., change learning rate $\alpha$ from $0.001 \to 0.1$).

## 🎓 4. Thesis & Defense Preparation
- **Logical Flow:** Introduction -> Background -> Methodology -> Experiments -> Conclusion.
- **Storytelling:** Every experiment must answer a specific **Research Question (RQ)**.

## 🚫 Research Anti-Patterns
- **The "Hammer looking for a nail":** Applying a complex algorithm where a simple one works.
- **Vague Methodology:** Not providing enough detail for others to reproduce your results.
- **Lack of Baselines:** Not comparing against the current "State of the Art" (SOTA).
