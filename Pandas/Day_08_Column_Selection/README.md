# 🐼 Day 08 — Column Selection

## 🎯 Learning Objective

Learn how to select one or multiple columns from a Pandas DataFrame.

By the end of this lesson, I will be able to:

- Select a single column.
- Select multiple columns.
- Understand the difference between a Series and a DataFrame.
- Use column selection for basic data analysis.

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

## 🔹 Selecting a Single Column

Use one pair of square brackets to select a single column.

```python
df["Name"]
```

This returns a **Pandas Series**.

You can check the type:

```python
type(df["Name"])
```

### Example

```python
salary = df["Salary"]

print(salary)
```

---

## 🔹 Selecting Multiple Columns

To select multiple columns, provide a list of column names.

```python
df[["Name", "Salary"]]
```

This returns a **Pandas DataFrame**.

You can check the type:

```python
type(df[["Name", "Salary"]])
```

---

## ⚠️ Important Difference

```python
df["Salary"]       # Returns a Series

df[["Salary"]]     # Returns a DataFrame
```

The extra square brackets make a difference.

| Selection | Result |
|---|---|
| `df["column"]` | Series |
| `df[["column"]]` | DataFrame |
| `df[["col1", "col2"]]` | DataFrame |

---

## 💡 Why Column Selection Matters

Real-world datasets can contain many columns.

For example:

```text
Customer_ID | Name | Age | City | Product | Sales | Profit
```

If you only want to analyze sales and profit, you can select:

```python
df[["Sales", "Profit"]]
```

This helps you focus on the information relevant to your analysis.

---

## 🧠 Key Takeaways

- Use `df["column"]` to select one column.
- A single selected column returns a **Series**.
- Use `df[["column1", "column2"]]` to select multiple columns.
- Multiple selected columns return a **DataFrame**.
- Column selection helps focus your analysis on relevant data.

## ➡️ Next Step

Complete the exercises in `TASK.md`.

Next: **Day 09 — Row Selection using `.loc[]` and `.iloc[]`**.
