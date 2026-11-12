# 🐼 Day 06 — Missing Data

## 🎯 Learning Goal

Learn how to identify and handle missing values in a Pandas DataFrame.

## 📚 Topics Covered

- Identifying missing values
- `isnull()` and `notnull()`
- Counting missing values
- Removing missing values with `dropna()`
- Filling missing values with `fillna()`

## 🔑 Key Concepts

### 1. What Is Missing Data?

Missing data occurs when a value is not available in a dataset.

In Pandas, missing values are commonly represented as:

```python
NaN
```

For example:

| Name | Age | Salary |
|---|---:|---:|
| Amit | 25 | 50000 |
| Sneha | NaN | 60000 |
| Ravi | 28 | NaN |

---

### 2. Finding Missing Values

Use `isnull()` to check for missing values.

```python
df.isnull()
```

This returns `True` where data is missing and `False` where data is available.

To count missing values in each column:

```python
df.isnull().sum()
```

---

### 3. Finding Available Values

Use `notnull()` to check whether values are present.

```python
df.notnull()
```

---

### 4. Removing Missing Values

Use `dropna()` to remove rows containing missing values.

```python
df.dropna()
```

You can also remove columns containing missing values:

```python
df.dropna(axis=1)
```

> ⚠️ Be careful with `dropna()`. Removing too many rows can result in losing valuable data.

---

### 5. Filling Missing Values

Use `fillna()` to replace missing values.

```python
df["Age"] = df["Age"].fillna(25)
```

You can also fill missing values using the mean:

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

For text data, you might use:

```python
df["City"] = df["City"].fillna("Unknown")
```

## 💡 Why Missing Data Matters

Before analyzing a dataset, you need to understand whether data is missing.

Missing values can:

- Affect calculations and analysis
- Produce incorrect results
- Reduce the quality of insights

The correct way to handle missing data depends on the dataset and the reason the data is missing.

## 🎯 Day 06 Outcome

By the end of this lesson, I should be able to:

- Identify missing values using `isnull()`
- Count missing values
- Check available values using `notnull()`
- Remove missing data using `dropna()`
- Fill missing values using `fillna()`
- Choose an appropriate method for handling missing data

## ➡️ Next Step

**Day 07 — Duplicates & Data Types**
