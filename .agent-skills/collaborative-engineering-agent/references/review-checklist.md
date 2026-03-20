# Dialectical Review Checklist (DRE)

## Phase A: Analysis
- [ ] What is the core responsibility of this change?
- [ ] Is it DRY? (Don't Repeat Yourself)
- [ ] Does it follow the project's architectural patterns?

## Phase B: Pushback (The Devil's Advocate)
- [ ] **Error Handling:** What if input is `null`? What if the network fails?
- [ ] **Performance:** Is there an $O(n^2)$ loop? Can we use a Map/Hash?
- [ ] **Security:** Are there hardcoded secrets? Is there a risk of SQL/Command injection?
- [ ] **Dependency:** Do we *really* need this new library? Can we do it with stdlib?

## Phase C: Fix & Rationale
- [ ] Does the fix address the *root cause*?
- [ ] Is the rationale documented clearly?
- [ ] Are the variable/method names descriptive?

## Phase D: Re-review & Verification
- [ ] Do all tests pass after the fix?
- [ ] Is the code more readable/maintainable now?
- [ ] Has the critique been fully satisfied?
