# 🐼 Day 07 — Pandas Revision Challenge ( Day 3 to 6 ) Includes

## 🎯 Learning Objective

Review and apply the Pandas concepts learned in Days 01–06.

By completing this challenge, I should be able to independently:

- Create and work with Series.
- Create and understand DataFrames.
- Load a CSV dataset.
- Inspect a dataset.
- Understand columns and data types.
- Generate basic statistical summaries.

---

## 📚 Concepts to Review

### 1. Pandas Series

A Series is a one-dimensional labeled data structure.

```python
import pandas as pd

sales = pd.Series([100, 200, 300, 400])

print(sales)
```

---

### 2. Pandas DataFrame

A DataFrame is a two-dimensional tabular data structure with rows and columns.

```python
data = {
    "Name": ["Amit", "Sneha", "Ravi"],
    "Age": [25, 28, 30],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)

print(df)
```

---

### 3. Loading Data

Use `read_csv()` to load a CSV dataset.

```python
df = pd.read_csv("data.csv")
```

---

### 4. Inspecting Data

Use these methods when working with a new dataset:

```python
df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()
```

---

## 🔄 Recommended Data Analysis Workflow

When you receive a new dataset:

```text
Load the dataset
       ↓
Preview the data
       ↓
Check rows and columns
       ↓
Check data types and missing values
       ↓
Review statistical summaries
       ↓
Start analysis
```

---

## 🧠 Key Takeaways

- A Series stores one-dimensional labeled data.
- A DataFrame stores tabular data using rows and columns.
- `read_csv()` loads CSV files.
- Inspection helps you understand a dataset before analysis.
- `info()` and `describe()` provide important information about the data.

## ➡️ Next Step

After completing this revision challenge, move to **Day 08 — Column Selection**.
