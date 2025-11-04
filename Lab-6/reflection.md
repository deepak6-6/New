# Reflection – Lab 6: Fuzz Testing

**Name:** Deepak Kuna  
**SRN:** PES2UG23CS293  
**Section:** E

---

### 1. How did Hypothesis help?
Hypothesis automatically generated edge-case inputs like `None`, empty strings, and invalid numbers that caused hidden crashes. It helped find bugs faster than manual testing.

### 2. How would you use Fuzzing in CI/CD Pipelines?
I would include Hypothesis tests in CI pipelines (like GitHub Actions) so that every commit runs fuzz tests automatically to ensure input safety.

### 3. What do you observe from screenshots SS2 and SS4?
Before fixing, several inputs caused exceptions (SS2). After fixing, all Hypothesis tests passed (SS4), showing improved robustness and input handling.
