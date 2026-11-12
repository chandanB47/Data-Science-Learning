# 📝 Day 05 — Sorting and Counting Data Practice

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

## Task 1 — Sort by Salary

Sort the DataFrame by `Salary` from lowest to highest.

---

## Task 2 — Sort by Salary Descending

Display the employees from the highest salary to the lowest salary.

---

## Task 3 — Sort by Multiple Columns

Sort the DataFrame by:

1. `City` in ascending order
2. `Salary` in descending order

---

## Task 4 — Count Cities

Count how many people belong to each city.

---

## Task 5 — Find the Most Common City

Use `value_counts()` to identify which city appears most frequently.

---

## 🎯 Challenge Questions and Answers

### 1. What is the difference between ascending and descending sorting?

Ascending sorting arranges data from the lowest to the highest value, or from A to Z. Descending sorting arranges data from the highest to the lowest value, or from Z to A.

### 2. Why would you sort data using multiple columns?

Sorting by multiple columns helps organize data based on more than one condition. For example, we can first sort employees by city and then sort their salaries within each city.

### 3. What does `value_counts()` do?

`value_counts()` counts how many times each unique value appears in a column.

### 4. How can sorting help during data analysis?

Sorting helps organize data and makes it easier to identify patterns, compare values, and find the highest or lowest values.

---

## ✅ Completion Checklist

- [ ] Created the DataFrame
- [ ] Sorted data in ascending order
- [ ] Sorted data in descending order
- [ ] Sorted using multiple columns
- [ ] Used `value_counts()`
- [ ] Completed the challenge questions
