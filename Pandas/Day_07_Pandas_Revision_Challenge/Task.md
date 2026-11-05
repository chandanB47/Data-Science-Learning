# 📝 Day 07 — Revision Challenge

## Part 1 — Series Practice

### Task 1

Create a Pandas Series containing the following monthly sales:

```text
1200, 1500, 1800, 2000, 2200
```

### Task 2

Print:

- The complete Series
- The first value
- The last value

---

## Part 2 — DataFrame Practice

Use the following data:

```python
data = {
    "Name": ["Amit", "Sneha", "Ravi", "Priya", "Kiran"],
    "Age": [25, 28, 30, 27, 32],
    "Department": ["Sales", "IT", "HR", "IT", "Finance"],
    "Salary": [50000, 60000, 55000, 65000, 70000]
}
```

### Task 3

Create a Pandas DataFrame using the data above.

### Task 4

Print the complete DataFrame.

### Task 5

Check the data type of each column.

---

## Part 3 — Data Inspection

Using your DataFrame, complete the following:

### Task 6

Display the first three rows.

### Task 7

Display the last two rows.

### Task 8

Find:

- Number of rows
- Number of columns

### Task 9

Display all column names.

### Task 10

Use `info()` to inspect the DataFrame.

### Task 11

Use `describe()` to generate a statistical summary.

---

## ⭐ Challenge

Answer these questions in your own words:
```
### 1. What is the difference between a Series and a DataFrame?
A Series is a one-dimensional structure that contains a single column of data. A DataFrame is a two-dimensional structure with rows and multiple columns.

### 2. Why should you inspect a dataset before analyzing it?
We inspect a dataset to understand its structure, columns, data types, missing values, and overall data before starting the analysis.

### 3. What information does df.info() provide?
df.info() provides information about the DataFrame, including column names, data types, non-null values, and memory usage.

### 4. What information does df.describe() provide?
df.describe() provides a statistical summary of numerical columns, including count, mean, standard deviation, minimum, maximum, and percentiles.

### 5. Which column has the highest average value in this dataset?
The Salary column has the highest average value.

From your dataset:
- Average Age = 28.4
- Average Salary = 60,000
```
---

## 🎯 Completion Check

You are ready for Day 08 if you can independently:

- [ ] Create a Series
- [ ] Create a DataFrame
- [ ] Load a CSV file
- [ ] Use `head()` and `tail()`
- [ ] Check `shape` and `columns`
- [ ] Understand `info()`
- [ ] Understand `describe()`
