# Day 09 — Python If / Else & Conditional Logic

📌 **Overview**

Day 09 covers **Conditional Statements and Control Flow**, the foundational decision-making mechanism in Python. Conditional execution directs program flow along specific branches based on whether a given expression evaluates to `True` or `False`.

In Data Science workflows, conditional logic governs data quality checks, missing value imputation rules, outlier filtering, business metric classification, and model threshold routing.

---

📚 **Topics Covered**

* Relational & Comparison Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
* Single-Branch Execution (`if`) and Binary Branching (`if` / `else`)
* Multi-Condition Decision Chains (`if` / `elif` / `else`)
* Logical Operators (`and`, `or`, `not`)
* Short-Circuit Evaluation and Defensive Checks
* Nested Conditional Structures
* String & Collection Membership Conditions (`in`, `not in`)
* Truth Value Testing (Truthy vs. Falsy objects)
* Ternary Conditional Expressions (`x if condition else y`)
* Practical Data Science Scenario: Row-Level Data Quality & Anomaly Triage

---

### 1. Multi-Branch Evaluation (`elif`)

Python evaluates branches sequentially from top to bottom. Once a condition evaluates to `True`, its corresponding block runs and the entire construct terminates.

```python
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"Grade: {grade}")  # Grade: A
