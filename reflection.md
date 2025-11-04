# Reflection – Lab 5: Static Code Analysis

**Name:** Deepak Kuna  
**SRN:** PES2UG23CS293  
**Course:** UE23CS341A – Software Engineering  
**Lab:** 5 – Static Code Analysis  

---

### 1. Easiest vs Hardest Fixes
- **Easiest:** Fixing mutable default arguments (`logs=[]`) and using `with open()` for safe file operations.
- **Hardest:** Implementing proper input validation and handling exceptions without breaking logic flow.

### 2. False Positives
- Pylint reported naming convention issues and global variable warnings that were stylistic rather than functional bugs.

### 3. Integration into Workflow
- I would add Pylint, Flake8, and Bandit checks to a **GitHub Actions CI pipeline**.
- Also, I’d use a **pre-commit hook** locally so static checks run automatically before pushing changes.

### 4. Improvements Observed
- The code is now cleaner, safer, and more readable.
- Security improved by removing `eval()` and broad `except` blocks.
- Logging, docstrings, and f-strings made it more maintainable.

---
