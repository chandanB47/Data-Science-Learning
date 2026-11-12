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

## 🎯 Challenge Questions and Answers

### 1. What does `isnull()` return?

`isnull()` returns a Boolean result showing whether each value is missing. It returns `True` for missing values and `False` for available values.

### 2. What is the difference between `dropna()` and `fillna()`?

`dropna()` removes rows or columns that contain missing values. `fillna()` replaces missing values with a specified value, such as the mean, median, or a custom value.

### 3. Why can blindly removing missing data be a problem?

Blindly removing missing data can cause the loss of important information and reduce the size of the dataset. This may affect the accuracy and reliability of the analysis.

### 4. When might filling a missing value be better than removing the row?

Filling a missing value is better when the row contains useful information and removing it would result in losing valuable data. The missing value can be replaced with an appropriate value based on the data and the analysis.

---

## ✅ Completion Checklist

- [x] Created the DataFrame
- [x] Identified missing values using `isnull()`
- [x] Counted missing values
- [x] Used `notnull()`
- [x] Used `dropna()`
- [x] Used `fillna()`
- [x] Completed the challenge questions
