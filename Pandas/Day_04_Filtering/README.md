# 🐼 Day 04 — Filtering Data

## 🎯 Learning Goal

Learn how to filter rows in a Pandas DataFrame using conditions.

## 📚 Topics Covered

- Boolean filtering
- Comparison operators
- Filtering with a single condition
- Filtering with multiple conditions
- Using `&` and `|`

## 🔑 Key Concepts

### 1. Filtering with a Single Condition

Suppose we have a DataFrame:

```python
import pandas as pd

data = {
    "Name": ["Amit", "Sneha", "Ravi", "Priya"],
    "Age": [22, 28, 19, 30],
    "Salary": [30000, 50000, 25000, 60000]
}

df = pd.DataFrame(data)
```

To find people older than 25:

```python
df[df["Age"] > 25]
```

The condition:

```python
df["Age"] > 25
```

creates a Boolean result containing `True` and `False`.

Pandas returns only the rows where the condition is `True`.

### 2. Comparison Operators

| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### 3. Filtering with Multiple Conditions

Use `&` for **AND**:

```python
df[(df["Age"] > 20) & (df["Salary"] > 40000)]
```

Both conditions must be `True`.

Use `|` for **OR**:

```python
df[(df["Age"] < 20) | (df["Salary"] > 50000)]
```

At least one condition must be `True`.

> ⚠️ Always place each condition inside parentheses when using `&` or `|`.

## 💡 Why Filtering Matters

In real-world data analysis, you rarely analyze every row at once.

For example, you may need to:

- Find products with sales above a target
- Identify customers from a specific city
- Analyze employees with high salaries
- Find missing or unusual values

Filtering helps you focus on the data needed to answer a specific question.

## 🎯 Day 04 Outcome

By the end of this lesson, I should be able to:

- Filter data using a single condition
- Use comparison operators
- Filter data using multiple conditions
- Understand the difference between `&` and `|`
- Apply filtering to answer basic data questions

## ➡️ Next Step

**Day 05 — Sorting and Counting Data**
