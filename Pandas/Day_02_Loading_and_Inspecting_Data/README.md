# 🐼 Day 02 — Loading and Inspecting Data

## 🎯 Learning Objectives

By the end of this lesson, I will be able to:

- Load a CSV file using Pandas.
- View the first and last rows of a dataset.
- Check the number of rows and columns.
- View column names.
- Understand basic information about a dataset.
- Generate statistical summaries.

---

## 📂 Loading Data

Real-world data is commonly stored in files such as CSV or Excel files.

Pandas can load a CSV file using `read_csv()`.

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

Here, `df` stores the dataset as a Pandas DataFrame.

---

## 👀 Viewing Data

### `head()`

Displays the first five rows by default.

```python
df.head()
```

You can also specify the number of rows:

```python
df.head(3)
```

### `tail()`

Displays the last five rows by default.

```python
df.tail()
```

---

## 📐 Checking Dataset Size

Use `shape` to check the number of rows and columns.

```python
df.shape
```

Example output:

```text
(100, 5)
```

This means the dataset has:

- 100 rows
- 5 columns

---

## 🏷️ Viewing Column Names

Use `columns` to see all column names.

```python
df.columns
```

---

## ℹ️ Understanding Dataset Information

Use `info()` to get information about:

- Column names
- Data types
- Non-null values
- Memory usage

```python
df.info()
```

---

## 📊 Statistical Summary

Use `describe()` to generate a statistical summary of numerical columns.

```python
df.describe()
```

It can show values such as:

- Count
- Mean
- Standard deviation
- Minimum
- Maximum
- Percentiles

---

## 🔄 Basic Data Inspection Workflow

When working with a new dataset, start with:

```python
df.head()
df.shape
df.columns
df.info()
df.describe()
```

This helps you understand the dataset before performing cleaning or analysis.

---

## 🧠 Key Takeaways

- Use `pd.read_csv()` to load CSV files.
- Use `head()` and `tail()` to preview data.
- Use `shape` to check dataset dimensions.
- Use `info()` to understand columns and data types.
- Use `describe()` to summarize numerical data.

## ➡️ Next Step

Complete the exercises in `TASK.md` using a CSV dataset.
