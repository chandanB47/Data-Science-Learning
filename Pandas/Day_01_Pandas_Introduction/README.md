# 🐼 Day 01 — Pandas Introduction

## 🎯 Learning Objectives

By the end of this lesson, I will be able to:

- Understand what Pandas is.
- Import the Pandas library.
- Understand the difference between a Series and a DataFrame.
- Create basic Series and DataFrames.

---

## 📌 What is Pandas?

**Pandas** is a Python library used for working with structured data.

It is commonly used for:

- Data cleaning
- Data analysis
- Data transformation
- Working with CSV and Excel files

Import Pandas using:

```python
import pandas as pd
```

---

## 📊 Pandas Series

A **Series** is a one-dimensional labeled data structure.

Example:

```python
import pandas as pd

sales = pd.Series([100, 200, 300, 400, 500])

print(sales)
```

Pandas automatically creates an index:

```text
0    100
1    200
2    300
3    400
4    500
```

---

## 📋 Pandas DataFrame

A **DataFrame** is a two-dimensional data structure with rows and columns.

Example:

```python
import pandas as pd

data = {
    "Name": ["Chandan", "Rahul", "Priya"],
    "Department": ["Sales", "IT", "HR"],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)

print(df)
```

---

## 🔍 Series vs DataFrame

| Feature | Series | DataFrame |
|---|---|---|
| Dimensions | One-dimensional | Two-dimensional |
| Structure | Single column | Rows and columns |
| Example | Sales values | Complete employee table |

---

## 🧠 Key Takeaways

- Pandas is used for working with structured data.
- A **Series** represents one-dimensional data.
- A **DataFrame** represents tabular data with rows and columns.
- Pandas is commonly imported as `pd`.

## ➡️ Next Step

Complete the exercises in `TASK.md` and write your solutions in `practice.ipynb`.
