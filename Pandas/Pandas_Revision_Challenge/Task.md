# 📝 Pandas Revision Challenge — Tasks

## 🎯 Objective

Test your understanding of the Pandas concepts covered in **Days 01–06**.

Try to complete all tasks without looking at previous notes or solutions.

---

# Part 1 — Series and DataFrame Basics

## Task 1 — Create a Series

Create a Pandas Series containing these quarterly sales values:

```text
15000, 22000, 18000, 25000
```

---

## Task 2 — Access Series Values

Print:

- The complete Series
- The first value
- The last value

---

## Task 3 — Create and Display the DataFrame

Use the following dataset:

```python
import pandas as pd
import numpy as np

data = {
    "Employee": ["Arjun", "Meera", "Rahul", "Divya", "Vikram", "Neha", "Rohan", "Pooja"],
    "Age": [26, 31, np.nan, 29, 35, 27, np.nan, 32],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales", np.nan],
    "Experience": [2, 7, 4, 5, np.nan, 3, 6, 8],
    "Salary": [45000, 72000, 55000, 60000, 85000, np.nan, 58000, 78000]
}

df = pd.DataFrame(data)
```

Display the complete DataFrame.

---

# Part 2 — Data Inspection

## Task 4

Display the first **4 rows** of the DataFrame.

## Task 5

Display the last **3 rows** of the DataFrame.

## Task 6

Find the number of:

- Rows
- Columns

## Task 7

Display all column names.

## Task 8

Check the data type of every column.

## Task 9

Use `info()` to inspect the DataFrame.

## Task 10

Use `describe()` to generate a statistical summary.

---

# Part 3 — Data Selection

## Task 11

Select only the `Employee` column.

## Task 12

Select the following columns:

- `Employee`
- `Department`
- `Salary`

## Task 13

Using `.loc[]`, select rows with index labels **2 to 5**.

## Task 14

Using `.iloc[]`, select the **first 3 rows**.

## Task 15 — Challenge

Using `.iloc[]`, select:

- Rows at positions **1 to 4**
- The first **3 columns**

⚠️ Remember: the ending position in `.iloc[]` is excluded.

---

# Part 4 — Filtering Data

## Task 16

Display employees whose salary is greater than **60,000**.

## Task 17

Display employees who work in the **IT** department.

## Task 18

Display employees who:

- Are older than 28
- Have a salary greater than or equal to 60,000

Use the `&` operator.

## Task 19

Display employees who:

- Work in the Sales department
- **OR** have more than 7 years of experience

Use the `|` operator.

---

# Part 5 — Sorting and Counting

## Task 20

Sort the DataFrame by `Salary` from lowest to highest.

## Task 21

Sort the DataFrame by `Experience` from highest to lowest.

## Task 22

Sort the DataFrame by:

1. `Department` in ascending order
2. `Salary` in descending order

## Task 23

Count how many employees belong to each department.

### Bonus

Include missing department values in your count.

---

# Part 6 — Missing Data

## Task 24

Display which values are missing in the DataFrame.

## Task 25

Count the missing values in each column.

## Task 26

Create a new DataFrame called `df_clean` by removing rows containing missing values.

**Do not modify the original `df`.**

## Task 27

Fill missing `Age` values using the mean age.

## Task 28

Replace missing `Department` values with `"Unknown"`.

---

# ⭐ Final Challenge — Test Your Understanding

## Question 1 — Series vs DataFrame

### What is the difference between a Series and a DataFrame?

**Answer:**

A **Series** is a one-dimensional labeled data structure, similar to a single column of data.

A **DataFrame** is a two-dimensional data structure with rows and columns. A DataFrame can contain multiple Series.

**Example:** In an employee dataset, the `Salary` column is a Series, while the complete employee table is a DataFrame.

---

## Question 2 — `.loc[]` vs `.iloc[]`

### What is the difference between `.loc[]` and `.iloc[]`?

**Answer:**

`.loc[]` selects data using **labels or names**.

`.iloc[]` selects data using **integer positions**.

For example:

```python
# Selects rows using index labels
df.loc[2:5]

# Selects rows using integer positions
df.iloc[2:5]
```

An important difference is that `.iloc[]` follows normal Python slicing, so the ending position is excluded.

---

## Question 3 — Boolean Filtering

### What happens when you filter a DataFrame using a Boolean condition?

For example:

```python
df[df["Salary"] > 60000]
```

Explain what happens to the rows that meet and do not meet the condition.

**Answer:**

When we filter a DataFrame using a Boolean condition, Pandas checks each row and produces either `True` or `False`.

- Rows where the condition is `True` are included in the result.
- Rows where the condition is `False` are excluded.

In the example above, only employees with a salary greater than `60,000` are returned.

The original DataFrame remains unchanged unless we explicitly modify it.

---

## Question 4 — `&` vs `|`

### What is the difference between `&` and `|` when filtering data?

**Answer:**

`&` means **AND**. Both conditions must be `True` for a row to be selected.

`|` means **OR**. At least one condition must be `True` for a row to be selected.

For example:

```python
# Both conditions must be True
df[(df["Age"] > 25) & (df["Salary"] > 60000)]

# At least one condition must be True
df[(df["Age"] > 25) | (df["Salary"] > 60000)]
```

---

## Question 5 — Using `dropna()`

### Why might `dropna()` be a bad choice for some datasets?

**Answer:**

`dropna()` removes rows or columns containing missing values. This can be a bad choice because it may remove useful data.

For example, if many rows contain only one missing value, using `dropna()` could remove a large amount of valuable information and affect the analysis.

Before using `dropna()`, we should understand why the data is missing and decide whether removing or filling the missing values is the better option.

---

## Question 6 — Keeping the Original DataFrame

### You have a dataset with 100,000 rows. Why is it a good practice to keep the original DataFrame unchanged?

Think about:

- Data safety
- Recovering from mistakes
- Comparing original and cleaned data

**Answer:**

Keeping the original DataFrame unchanged protects the raw data.

If we make a mistake while cleaning or transforming the data, we can return to the original dataset. It also allows us to compare the original data with the cleaned version and understand what changes were made.

For example:

```python
df_clean = df.dropna()
```

This creates a new cleaned DataFrame while keeping the original `df` unchanged.

This is especially important when working with a large dataset, such as one containing **100,000 rows**, where incorrectly modifying or losing data can be difficult to recover.

---

## 🎯 Key Takeaways

- A **Series** is one-dimensional, while a **DataFrame** has rows and columns.
- `.loc[]` uses labels, while `.iloc[]` uses integer positions.
- Boolean filtering returns rows where the condition is `True`.
- `&` means **AND**, while `|` means **OR**.
- `dropna()` can cause unnecessary data loss if used without analysis.
- Keeping the original DataFrame unchanged protects your raw data and makes it easier to recover from mistakes.

---

# 🎯 Completion Checklist

You should be able to independently:

- [ ] Create a Series
- [ ] Create and inspect a DataFrame
- [ ] Check rows, columns, and data types
- [ ] Use `head()`, `tail()`, `info()`, and `describe()`
- [ ] Select columns and rows
- [ ] Understand `.loc[]` and `.iloc[]`
- [ ] Filter data using one or multiple conditions
- [ ] Use `&` and `|` correctly
- [ ] Sort data using `sort_values()`
- [ ] Count categorical values using `value_counts()`
- [ ] Identify missing values
- [ ] Use `dropna()` and `fillna()` appropriately
- [ ] Preserve the original DataFrame while cleaning data

---

## ➡️ Next Step

After completing this revision challenge, review any mistakes you made before moving to the next topic in your Pandas learning roadmap.
