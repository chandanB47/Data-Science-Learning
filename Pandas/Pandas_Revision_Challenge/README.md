# 🐼 Pandas Revision Challenge — Days 01 to 06

## 🎯 Learning Objective

This revision challenge reviews and tests the Pandas concepts learned from **Day 01 to Day 06**.

The goal is not to memorize Pandas syntax. The goal is to understand how to inspect, select, filter, sort, count, and clean data using Pandas.

By completing this challenge, I should be able to independently:

- Create and work with Pandas Series.
- Create and understand DataFrames.
- Inspect a dataset.
- Select rows and columns.
- Filter data using conditions.
- Combine multiple filtering conditions.
- Sort and count data.
- Identify and handle missing values.
- Preserve the original dataset while cleaning data.

---

## 📚 Concepts Covered

### 1. Pandas Series

A **Series** is a one-dimensional labeled data structure.

```python
import pandas as pd

sales = pd.Series([15000, 22000, 18000, 25000])

print(sales)
```

A Series is similar to a single column of data.

---

### 2. Pandas DataFrame

A **DataFrame** is a two-dimensional tabular data structure containing rows and columns.

```python
data = {
    "Name": ["Amit", "Sneha", "Ravi"],
    "Age": [25, 28, 30],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(data)

print(df)
```

A DataFrame can contain multiple Series.

---

### 3. Data Inspection

Before analyzing a dataset, inspect its structure and contents.

Common methods include:

```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

These help answer questions such as:

- How many rows and columns are there?
- What are the column names?
- What data types are being used?
- Are there missing values?
- What does the numerical data look like?

---

### 4. Data Selection

Pandas allows selecting specific columns and rows.

#### Select one column

```python
df["Name"]
```

#### Select multiple columns

```python
df[["Name", "Age"]]
```

#### Select using `.loc[]`

`.loc[]` selects data using **labels**.

```python
df.loc[2:5]
```

#### Select using `.iloc[]`

`.iloc[]` selects data using **integer positions**.

```python
df.iloc[1:5, :3]
```

Remember: the ending position in `.iloc[]` slicing is excluded.

---

### 5. Filtering Data

Filtering allows us to select rows based on conditions.

```python
df[df["Salary"] > 60000]
```

The condition creates Boolean values (`True` or `False`), and Pandas returns rows where the condition is `True`.

#### Multiple conditions

Use `&` when **both conditions** must be true:

```python
df[(df["Age"] > 28) & (df["Salary"] >= 60000)]
```

Use `|` when **at least one condition** must be true:

```python
df[(df["Department"] == "Sales") | (df["Experience"] > 7)]
```

---

### 6. Sorting and Counting

Sort data using `sort_values()`.

#### Sort in ascending order

```python
df.sort_values("Salary")
```

#### Sort in descending order

```python
df.sort_values("Experience", ascending=False)
```

#### Sort by multiple columns

```python
df.sort_values(
    ["Department", "Salary"],
    ascending=[True, False]
)
```

Count values using `value_counts()`.

```python
df["Department"].value_counts()
```

By default, missing values are not included in the count.

To include missing values:

```python
df["Department"].value_counts(dropna=False)
```

---

### 7. Missing Data

Missing values are commonly represented as `NaN`.

#### Check for missing values

```python
df.isnull()
```

#### Count missing values

```python
df.isnull().sum()
```

#### Remove rows with missing values

```python
df_clean = df.dropna()
```

Creating a new DataFrame helps preserve the original dataset.

#### Fill missing values

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

#### Replace missing categorical values

```python
df["Department"] = df["Department"].fillna("Unknown")
```

---

## 🔄 Recommended Data Analysis Workflow

When working with a new dataset:

```text
Load or create the dataset
        ↓
Preview the data
        ↓
Check rows and columns
        ↓
Check column names and data types
        ↓
Identify missing values
        ↓
Generate statistical summaries
        ↓
Select and filter relevant data
        ↓
Sort and analyze the results
        ↓
Clean missing or incorrect data
        ↓
Continue with deeper analysis
```

---

## 🧠 Key Takeaways

- A **Series** stores one-dimensional labeled data.
- A **DataFrame** stores data using rows and columns.
- Data inspection should happen before analysis.
- `.loc[]` uses labels, while `.iloc[]` uses integer positions.
- Boolean conditions are used to filter rows.
- `&` means both conditions must be true.
- `|` means at least one condition must be true.
- `sort_values()` helps organize data for analysis.
- `value_counts()` helps analyze categorical data.
- Missing values should be investigated before removing or filling them.
- The original DataFrame should be preserved when performing major cleaning operations.

---

## 📝 Revision Challenge

Complete the accompanying **TASK.md** file without referring to previous solutions.

The challenge tests:

- Series and DataFrame basics
- Data inspection
- Data selection
- Filtering
- Sorting and counting
- Missing data
- Conceptual understanding

---

## 📂 Suggested Folder Structure

```text
Pandas/
│
├── Day-01-Pandas-Basics/
├── Day-02-Loading-and-Inspection/
├── Day-03-Data-Selection/
├── Day-04-Filtering/
├── Day-05-Sorting-and-Counting/
├── Day-06-Missing-Data/
│
└── Revision-Challenge/
    ├── README.md
    └── TASK.md
```

## ➡️ Next Step

After successfully completing this revision challenge, continue with the next topic in your Pandas learning roadmap.
