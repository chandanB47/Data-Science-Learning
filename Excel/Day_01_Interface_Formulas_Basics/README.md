# 📊 Day 01 — Excel Basics & Formulas

Welcome to **Day 01** of my Excel & Advanced Excel learning journey.

Today I will build the foundation required for using Excel as a **data-analysis tool** rather than only as a spreadsheet.

> 🎯 **Module:** Excel for Data Science & Analytics  
> 📌 **Day:** 01  
> 📚 **Topic:** Excel Basics & Formulas  
> 💼 **Business Exercise:** Sales Transaction Analysis  
> 📊 **Dataset:** `Sales_data 10K.xlsx`

---

## 🎯 Learning Objectives

By the end of Day 01, I should be able to:

- Understand workbook, worksheet, rows, columns, cells, and ranges.
- Understand cell references.
- Write basic Excel formulas.
- Use arithmetic operators.
- Understand relative references.
- Understand absolute references using `$`.
- Use `SUM`.
- Use `AVERAGE`.
- Use `COUNT`.
- Use `MIN`.
- Use `MAX`.
- Calculate sales values from transaction data.
- Build a basic sales summary.

---

# 1. Excel Fundamentals

## Workbook

An Excel file is called a **Workbook**.

Example:

```text
Sales_data 10K.xlsx
```

A workbook can contain multiple worksheets.

---

## Worksheet

A worksheet is an individual sheet/tab inside an Excel workbook.

The master dataset contains multiple related sheets that will be useful throughout the 12-day course.

---

## Row

Rows run horizontally and are identified using numbers:

```text
1, 2, 3, 4, 5, ...
```

---

## Column

Columns run vertically and are identified using letters:

```text
A, B, C, D, E, ...
```

---

## Cell

A cell is the intersection of a row and a column.

Example:

```text
B5
```

means:

```text
Column = B
Row    = 5
```

---

## Range

A range is a group of cells.

Example:

```excel
B2:B100
```

means all cells from `B2` through `B100`.

Another example:

```excel
A2:F100
```

means the rectangular range from A2 through F100.

---

# 2. Formula Basics

Every Excel formula begins with:

```excel
=
```

### Addition

```excel
=A1+B1
```

### Subtraction

```excel
=A1-B1
```

### Multiplication

```excel
=A1*B1
```

### Division

```excel
=A1/B1
```

### Power

```excel
=A1^2
```

### Important

Excel uses `*` for multiplication.

Correct:

```excel
=A1*B1
```

Incorrect:

```excel
=A1xB1
```

---

# 3. Cell References

Instead of typing numbers directly into formulas, we can reference cells.

Suppose:

| Quantity | Unit Price |
|---:|---:|
| 2 | 55000 |

If Quantity is in `J2` and Unit Price is in `K2`:

```excel
=J2*K2
```

This calculates the gross sales value.

Using cell references makes formulas reusable across many rows.

---

# 4. Relative References

A relative reference changes when a formula is copied.

Example:

```excel
=J2*K2
```

When copied to the next row, Excel automatically changes it to:

```excel
=J3*K3
```

Then:

```excel
=J4*K4
```

This is called a **relative cell reference**.

### Example

If `J2` contains Quantity and `K2` contains Unit Price:

```excel
=J2*K2
```

can be dragged down for the entire dataset.

---

# 5. Absolute References

An absolute reference stays fixed when a formula is copied.

The `$` symbol is used to lock a reference.

Example:

```excel
=$H$1
```

Here both the column and row are locked.

### Reference types

| Reference | Meaning |
|---|---|
| `A1` | Relative reference |
| `$A$1` | Absolute reference |
| `A$1` | Row locked |
| `$A1` | Column locked |

For Day 01, the main focus is:

```excel
A1
```

and

```excel
$A$1
```

---

# 6. Core Excel Functions

## SUM

Adds numbers together.

```excel
=SUM(A2:A100)
```

### Business use

Calculate total sales, total quantity, total cost, etc.

---

## AVERAGE

Calculates the arithmetic mean.

```excel
=AVERAGE(A2:A100)
```

### Business use

Calculate average transaction value or average quantity.

---

## COUNT

Counts cells containing numbers.

```excel
=COUNT(A2:A100)
```

### Business use

Count the number of numeric transactions or records.

> `COUNT` counts numbers. It does not count ordinary text values.

---

## MIN

Returns the smallest numeric value.

```excel
=MIN(A2:A100)
```

### Business use

Find the smallest transaction, lowest price, lowest quantity, etc.

---

## MAX

Returns the largest numeric value.

```excel
=MAX(A2:A100)
```

### Business use

Find the largest transaction, highest price, highest quantity, etc.

---

# 7. Master Dataset

The same master dataset will be used throughout all 12 days.

Main sheet:

```text
Sales_Data
```

Important fields include:

| Field | Purpose |
|---|---|
| `Sale_ID` | Unique transaction identifier |
| `Sale_Date` | Transaction date |
| `Customer_ID` | Customer reference |
| `Customer_Name` | Customer name |
| `Product_ID` | Product reference |
| `Product` | Product name |
| `Category` | Product category |
| `Region` | Sales region |
| `Employee_ID` | Sales employee reference |
| `Quantity` | Quantity sold |
| `Unit_Price` | Price per unit |
| `Discount_Pct` | Discount percentage |
| `Payment_Mode` | Payment method |
| `Sales_Channel` | Sales channel |
| `Status` | Transaction status |

---

# 8. Day 01 Practical Exercise

## Scenario

You are working as a **Junior Data Analyst** for a retail company.

The company has thousands of sales transactions.

Management wants a basic sales summary.

Your job is to calculate transaction-level sales values and then summarize the dataset.

---

## Task 1 — Calculate Gross Sales

Create a new column called:

```text
Gross_Sales
```

Formula:

```text
Quantity × Unit Price
```

For the first data row, identify the correct Quantity and Unit Price cells and create the formula.

Then copy the formula down for all transactions.

---

## Task 2 — Calculate Total Gross Sales

Calculate the total Gross Sales using:

```text
SUM
```

Do not manually add individual cells.

---

## Task 3 — Calculate Average Gross Sale

Calculate the average transaction value using:

```text
AVERAGE
```

---

## Task 4 — Count Transactions

Use:

```text
COUNT
```

to determine the number of numeric Gross Sales values.

---

## Task 5 — Find Minimum Gross Sale

Use:

```text
MIN
```

to find the smallest Gross Sales value.

---

## Task 6 — Find Maximum Gross Sale

Use:

```text
MAX
```

to find the largest Gross Sales value.

---

## Task 7 — Total Quantity Sold

Calculate the total quantity sold using:

```text
SUM
```

---

## Task 8 — Average Quantity

Calculate the average quantity per transaction using:

```text
AVERAGE
```

---

## Task 9 — Highest Unit Price

Find the highest Unit Price using:

```text
MAX
```

---

## Task 10 — Lowest Unit Price

Find the lowest Unit Price using:

```text
MIN
```

---

# 9. Absolute Reference Challenge

The company has a standard discount rate of:

```text
5%
```

Enter the discount rate into a separate cell.

Create a new column:

```text
Discount_Amount
```

Calculate the discount amount for each transaction.

### Requirement

Your formula must use an **absolute cell reference** for the 5% discount rate.

For example, the formula should contain a reference in this form:

```excel
=$H$1
```

Do **not** type `5%` directly into every formula.

The purpose of this task is to understand why absolute references are useful.

---

# 10. Business Questions

After completing the formulas, determine:

1. What is the total gross sales?
2. What is the average gross sale?
3. How many transactions are there?
4. What is the minimum gross sale?
5. What is the maximum gross sale?
6. What is the total quantity sold?
7. What is the average quantity per transaction?
8. What is the highest unit price?
9. What is the lowest unit price?

---

# 11. Formula Cheat Sheet

| Formula | Purpose |
|---|---|
| `=A1+B1` | Addition |
| `=A1-B1` | Subtraction |
| `=A1*B1` | Multiplication |
| `=A1/B1` | Division |
| `=SUM(A2:A100)` | Total |
| `=AVERAGE(A2:A100)` | Average |
| `=COUNT(A2:A100)` | Count numeric values |
| `=MIN(A2:A100)` | Minimum |
| `=MAX(A2:A100)` | Maximum |
| `=A1` | Relative reference |
| `=$A$1` | Absolute reference |

---

# 12. What I Should Understand After Day 01

I should be able to explain:

### Question 1

What is a cell reference?

### Question 2

What is the difference between:

```text
A1
```

and

```text
$A$1
```

### Question 3

Why would an analyst use:

```excel
=J2*K2
```

instead of manually calculating every transaction?

### Question 4

What is the difference between:

```text
SUM
AVERAGE
COUNT
MIN
MAX
```

### Question 5

Why is an absolute reference useful when a value such as a tax rate or discount rate must remain fixed?

---

# 13. Day 01 Completion Checklist

- [ ] Understand workbook
- [ ] Understand worksheet
- [ ] Understand rows and columns
- [ ] Understand cells and ranges
- [ ] Use arithmetic formulas
- [ ] Use cell references
- [ ] Understand relative references
- [ ] Understand absolute references
- [ ] Use `SUM`
- [ ] Use `AVERAGE`
- [ ] Use `COUNT`
- [ ] Use `MIN`
- [ ] Use `MAX`
- [ ] Calculate Gross Sales
- [ ] Calculate Discount Amount
- [ ] Complete the sales summary
- [ ] Answer the business questions

---

# 📈 Learning Approach

The goal is not to memorize formulas.

The goal is to understand:

```text
Raw Business Data
        ↓
Cell References
        ↓
Formula
        ↓
Calculated Value
        ↓
Summary
        ↓
Business Insight
```

For example:

```text
Quantity × Unit Price
        ↓
    Gross Sales
```

This is the foundation for the more advanced Excel analysis that follows.

---

# 🔜 Next Day

**Day 02 — Text Functions**

Topics:

- `TRIM`
- `CLEAN`
- `LEFT`
- `RIGHT`
- `MID`
- `PROPER`
- `CONCAT`
- `TEXTSPLIT`
- Customer data standardization
- Practical data-cleaning exercise

---

## ⭐ Core Principle

> **Learn → Practice → Analyze → Build → Document**
