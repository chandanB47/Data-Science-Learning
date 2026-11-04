# 📝 Day 02 — Practice Tasks

## Dataset

Use any CSV dataset for today's practice.

You can use a simple dataset containing information such as:

- Name
- Age
- City
- Salary

---

## Task 1 — Import Pandas

Import Pandas using the standard alias `pd`.

---

## Task 2 — Load the Dataset

Load your CSV file using:

```python
pd.read_csv()
```

Store the dataset in a variable named `df`.

---

## Task 3 — View the First Rows

Display the first five rows of the dataset.

**Question:** Why is `head()` useful when working with a new dataset?

---

## Task 4 — View the Last Rows

Display the last five rows of the dataset using `tail()`.

---

## Task 5 — Check Dataset Shape

Print the shape of the dataset.

Answer:

- How many rows does the dataset have?
- How many columns does the dataset have?

---

## Task 6 — View Column Names

Display all column names using `columns`.

---

## Task 7 — Inspect Dataset Information

Run:

```python
df.info()
```

Answer these questions:

1. What data types are present in your dataset?
2. Are there any missing values?

---

## Task 8 — Statistical Summary

Run:

```python
df.describe()
```

Observe the output and answer:

- Which numerical column has the highest average value?
- What is the maximum value in that column?

---

## ⭐ Challenge

Without looking at the previous examples, inspect a dataset using all of these methods:

```python
head()
tail()
shape
columns
info()
describe()
```

Write one short observation about what you learned from the dataset.
