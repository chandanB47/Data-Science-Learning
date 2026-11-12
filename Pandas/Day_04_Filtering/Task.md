# 📝 Day 04 — Filtering Data Practice

## 📌 Setup

Create the following DataFrame:

```python
import pandas as pd

data = {
    "Name": ["Amit", "Sneha", "Ravi", "Priya", "Kiran", "Anjali"],
    "Age": [25, 30, 22, 28, 35, 24],
    "City": ["Bangalore", "Mumbai", "Delhi", "Bangalore", "Mumbai", "Delhi"],
    "Salary": [50000, 65000, 40000, 55000, 75000, 45000]
}

df = pd.DataFrame(data)

print(df)
```

---

## Task 1 — Filter by Age

Display all people whose age is greater than 25.

---

## Task 2 — Filter by City

Display all people who live in `Bangalore`.

---

## Task 3 — Filter by Salary

Display all people with a salary greater than or equal to `55000`.

---

## Task 4 — Multiple Conditions Using AND

Display people who:

- Are older than 25
- Have a salary greater than `50000`

Use the `&` operator.

---

## Task 5 — Multiple Conditions Using OR

Display people who:

- Live in `Delhi`
- OR have a salary greater than `70000`

Use the `|` operator.

---

# 🎯 Challenge Questions and Answers

## 1. What happens when you use a Boolean condition to filter a DataFrame?

A Boolean condition checks each row and returns either `True` or `False`. When used to filter a DataFrame, Pandas displays only the rows where the condition is `True`.

## 2. What is the difference between `&` and `|` when filtering data?

The `&` operator means **AND**, so both conditions must be `True` for a row to be selected.

The `|` operator means **OR**, so at least one condition must be `True` for a row to be selected.

## 3. Why should each condition be placed inside parentheses?

Each condition should be placed inside parentheses to ensure that Python evaluates the comparison conditions correctly before applying the `&` or `|` operator. This helps avoid errors caused by operator precedence.

---

## ✅ Completion Checklist

- [x] Created the DataFrame
- [x] Filtered using one condition
- [x] Used comparison operators
- [x] Used `&` for multiple conditions
- [x] Used `|` for multiple conditions
- [x] Completed the challenge questions
