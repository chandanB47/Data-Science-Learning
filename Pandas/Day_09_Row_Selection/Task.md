# 📝 Day 09 — Row Selection Practice

## Dataset

Use the following dataset:

```python
import pandas as pd

data = {
    "Name": ["Amit", "Sneha", "Ravi", "Priya", "Kiran"],
    "Age": [25, 28, 30, 27, 32],
    "Department": ["Sales", "IT", "HR", "IT", "Finance"],
    "Salary": [50000, 60000, 55000, 65000, 70000]
}

df = pd.DataFrame(data)
```

---

## Task 1 — Display the Dataset

Print the complete DataFrame.

---

## Task 2 — Select One Row with `.loc[]`

Select the row with index label `0`.

**Question:** Which employee does this represent?

---

## Task 3 — Select Multiple Rows with `.loc[]`

Select rows from label `1` to `3`.

**Question:** How many rows are returned?

---

## Task 4 — Select One Row with `.iloc[]`

Select the first row using `.iloc[]`.

---

## Task 5 — Select Multiple Rows with `.iloc[]`

Select the first three rows using:

```python
df.iloc[0:3]
```

**Question:** Why does this return three rows?

---

## Task 6 — Compare `.loc[]` and `.iloc[]`

Run:

```python
df.loc[0:2]
```

and:

```python
df.iloc[0:2]
```

Compare the results.

**Question:** Why are the results different?

---

## ⭐ Challenge — Custom Index

Change the DataFrame index to:

```python
["EMP101", "EMP102", "EMP103", "EMP104", "EMP105"]
```

Then:

1. Select the employee with label `EMP102` using `.loc[]`.
2. Select the same employee using `.iloc[]`.
3. Select the first three employees using both methods.

### Challenge Question

In your own words, explain:

**When would you use `.loc[]` and when would you use `.iloc[]`?**

---

## ✅ Completion Checklist

- [ ] I can select a row using `.loc[]`.
- [ ] I can select rows using `.iloc[]`.
- [ ] I understand labels vs positions.
- [ ] I understand why `.loc[0:2]` and `.iloc[0:2]` return different results.
- [ ] I completed the custom index challenge.
