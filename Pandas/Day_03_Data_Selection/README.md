# 🐼 Day 03 — Data Selection

## 🎯 Learning Goal

Learn how to select specific columns and rows from a Pandas DataFrame.

## 📚 Topics Covered

- Selecting a single column
- Selecting multiple columns
- Selecting rows using `.loc[]`
- Selecting rows using `.iloc[]`

## 🔑 Key Concepts

### 1. Selecting a Single Column

```python
df["Name"]
```

This returns the values from one column.

### 2. Selecting Multiple Columns

```python
df[["Name", "Age"]]
```

Use a list inside the brackets to select multiple columns.

### 3. Selecting Rows with `.loc[]`

`.loc[]` selects data using labels.

```python
df.loc[0]
```

You can also select specific rows and columns:

```python
df.loc[0:2, ["Name", "Age"]]
```

### 4. Selecting Rows with `.iloc[]`

`.iloc[]` selects data using integer positions.

```python
df.iloc[0]
```

Example:

```python
df.iloc[0:3, 0:2]
```

## ⚠️ Important Difference

| Method | Selects Using |
|--------|---------------|
| `.loc[]` | Labels |
| `.iloc[]` | Integer positions |

## 💡 Why This Matters

Data selection is one of the most frequently used skills in data analysis. Before analyzing a dataset, you often need to select specific columns or rows relevant to your question.

## 🎯 Day 03 Outcome

By the end of this lesson, I should be able to:

- Select single and multiple columns
- Select rows using `.loc[]`
- Select rows using `.iloc[]`
- Understand the difference between label-based and position-based selection

## ➡️ Next Step

**Day 04 — Filtering Data using Conditions**
