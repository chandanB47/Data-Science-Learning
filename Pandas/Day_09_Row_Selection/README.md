# 🐼 Day 09 — Row Selection with `.loc[]` and `.iloc[]`

## 🎯 Learning Objectives

By the end of this lesson, I will be able to:

- Select rows using `.loc[]`.
- Select rows using `.iloc[]`.
- Understand the difference between labels and positions.
- Select multiple rows from a DataFrame.

---

## 📊 Example Dataset

```python
import pandas as pd

data = {
    "Name": ["Amit", "Sneha", "Ravi", "Priya", "Kiran"],
    "Age": [25, 28, 30, 27, 32],
    "Department": ["Sales", "IT", "HR", "IT", "Finance"],
    "Salary": [50000, 60000, 55000, 65000, 70000]
}

df = pd.DataFrame(data)

print(df)
```

---

## 🔹 Selecting Rows with `.loc[]`

`.loc[]` selects data using **labels**.

```python
df.loc[0]
```

This selects the row with the index label `0`.

### Select Multiple Rows

```python
df.loc[0:2]
```

This selects rows with labels `0`, `1`, and `2`.

> **Important:** When slicing with `.loc[]`, the ending label is included.

---

## 🔹 Selecting Rows with `.iloc[]`

`.iloc[]` selects data using **integer positions**.

```python
df.iloc[0]
```

This selects the first row.

### Select Multiple Rows

```python
df.iloc[0:3]
```

This selects rows at positions `0`, `1`, and `2`.

> **Important:** When slicing with `.iloc[]`, the ending position is excluded.

---

## ⚠️ Key Difference

| Method | Selects Using | Example |
|---|---|---|
| `.loc[]` | Labels | `df.loc[0:2]` |
| `.iloc[]` | Integer positions | `df.iloc[0:3]` |

With the default index (`0, 1, 2...`), both methods may appear similar. The difference becomes clearer when the DataFrame has custom index labels.

---

## 🧠 Custom Index Example

```python
df.index = ["A", "B", "C", "D", "E"]

print(df)
```

Now you can use:

```python
df.loc["A"]
```

But:

```python
df.iloc[0]
```

still selects the first row by its position.

---

## 🧠 Key Takeaways

- `.loc[]` uses **index labels**.
- `.iloc[]` uses **integer positions**.
- `.loc[]` includes the ending label when slicing.
- `.iloc[]` excludes the ending position when slicing.

## ➡️ Next Step

Complete the exercises in `TASK.md`.

Next: **Day 10 — Boolean Filtering**.
