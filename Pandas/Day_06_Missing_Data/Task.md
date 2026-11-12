# 📝 Day 06 — Missing Data Practice

## 📌 Setup

Create the following DataFrame:

```python
import pandas as pd
import numpy as np

data = {
    "Name": ["Amit", "Sneha", "Ravi", "Priya", "Kiran"],
    "Age": [25, np.nan, 28, np.nan, 32],
    "City": ["Bangalore", "Mumbai", np.nan, "Delhi", "Mumbai"],
    "Salary": [50000, 60000, np.nan, 55000, 70000]
}

df = pd.DataFrame(data)

print(df)
```

---

## Task 1 — Identify Missing Values

Display the DataFrame showing which values are missing using:

```python
isnull()
```

---

## Task 2 — Count Missing Values

Find the number of missing values in each column.

---

## Task 3 — Check Available Values

Use `notnull()` to display which values are available.

---

## Task 4 — Remove Missing Data

Create a new DataFrame by removing rows that contain missing values.

> Do not overwrite the original DataFrame.

---

## Task 5 — Fill Missing Age Values

Fill missing values in the `Age` column using the **mean age**.

---

## Task 6 — Fill Missing City Values

Replace missing values in the `City` column with:

```text
Unknown
```

---

## 🎯 Challenge Questions

Answer in your own words:

1. What does `isnull()` return?
2. What is the difference between `dropna()` and `fillna()`?
3. Why can blindly removing missing data be a problem?
4. When might filling a missing value be better than removing the row?

---

## ✅ Completion Checklist

- [ ] Created the DataFrame
- [ ] Identified missing values using `isnull()`
- [ ] Counted missing values
- [ ] Used `notnull()`
- [ ] Used `dropna()`
- [ ] Used `fillna()`
- [ ] Completed the challenge questions
