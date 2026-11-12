# 🐼 Day 05 — Sorting and Counting Data

## 🎯 Learning Goal

Learn how to sort data and count the frequency of values in a Pandas DataFrame.

## 📚 Topics Covered

- Sorting data using `sort_values()`
- Sorting in ascending and descending order
- Sorting by multiple columns
- Counting values using `value_counts()`

## 🔑 Key Concepts

### 1. Sorting Data

Use `sort_values()` to arrange data based on one or more columns.

```python
df.sort_values("Salary")
```

By default, data is sorted in ascending order.

### 2. Sorting in Descending Order

Use `ascending=False` to sort from highest to lowest.

```python
df.sort_values("Salary", ascending=False)
```

### 3. Sorting by Multiple Columns

You can sort using multiple columns.

```python
df.sort_values(
    by=["City", "Salary"],
    ascending=[True, False]
)
```

This first sorts by `City` in ascending order and then sorts `Salary` in descending order within each city.

### 4. Counting Values

Use `value_counts()` to count how many times each unique value appears.

```python
df["City"].value_counts()
```

Example output:

```text
Bangalore    2
Mumbai       2
Delhi        2
```

### 5. Counting Including Missing Values

By default, missing values are excluded.

Use `dropna=False` to include them:

```python
df["City"].value_counts(dropna=False)
```

## 💡 Why This Matters

Sorting helps you identify:

- Highest and lowest values
- Top-performing products
- Highest-paid employees
- Data patterns and rankings

Counting helps you understand:

- Category distribution
- Customer locations
- Product frequency
- Common values in a dataset

## 🎯 Day 05 Outcome

By the end of this lesson, I should be able to:

- Sort data by one column
- Sort data in ascending and descending order
- Sort data using multiple columns
- Count unique values using `value_counts()`
- Use sorting and counting to answer basic data questions

## ➡️ Next Step

**Day 06 — Missing Data**
