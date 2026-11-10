# 📝 Day 03 — Data Selection Practice

## 📌 Setup

Create the following DataFrame:

```python
import pandas as pd

data = {
    "Name": ["Amit", "Sneha", "Ravi", "Priya", "Kiran"],
    "Age": [25, 30, 28, 24, 32],
    "City": ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad"],
    "Salary": [50000, 60000, 55000, 48000, 70000]
}

df = pd.DataFrame(data)

print(df)
```

---

## Task 1 — Select One Column

Select and display the `Name` column.

---

## Task 2 — Select Multiple Columns

Select and display the `Name` and `Salary` columns.

---

## Task 3 — Select a Row Using `.loc[]`

Select the row with index label `2`.

---

## Task 4 — Select Multiple Rows Using `.loc[]`

Select rows from index `1` to `3`.

---

## Task 5 — Select a Row Using `.iloc[]`

Select the first row using `.iloc[]`.

---

## Task 6 — Select Rows and Columns

Using `.iloc[]`, select:

- The first 3 rows
- The first 2 columns

---

## 🎯 Challenge Question

Answer in your own words:

**What is the main difference between `.loc[]` and `.iloc[]`, and when would you use each one?**

```text

.loc[] selects data using labels or names,

.iloc[] selects data using integer positions.

- I would use .loc[] when I know the row or column label I want to select.

- I would use .iloc[] when I want to select data based on its numerical position in the DataFrame.
```

## Example :-

### Select using an index label
df.loc[2]

### Select using an integer position
df.iloc[2]


---

## ✅ Completion Checklist

- [x] Created the DataFrame
- [x] Selected a single column
- [x] Selected multiple columns
- [x] Used `.loc[]`
- [x] Used `.iloc[]`
- [x] Completed the challenge question
