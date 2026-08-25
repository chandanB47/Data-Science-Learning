# 🧹 Day 02 — Text Functions & Data Standardization

Welcome to **Day 02** of my **Excel & Advanced Excel** learning journey.

Today’s focus is on using Excel text functions to **clean, extract, combine, and standardize text data** commonly found in real-world datasets.

> 📊 **Module:** Excel for Data Science & Analytics
> 📅 **Day:** 02
> 📚 **Topic:** Text Functions & Data Standardization
> 💼 **Business Exercise:** Customer Data Standardization
> 📁 **Dataset:** `Sales_data 10K.xlsx`

---

## 🎯 Learning Objectives

By the end of Day 02, I should be able to:

* Clean inconsistent text data.
* Remove unnecessary spaces and non-printing characters.
* Extract text from different positions within a string.
* Standardize names using proper capitalization.
* Combine values from multiple cells.
* Split text using delimiters.
* Extract useful information from customer and email data.
* Understand the importance of text standardization in data analysis.
* Prepare cleaner data for filtering, reporting, and lookup operations.

---

# 📚 Topics Covered

## 1. `TRIM`

Removes unnecessary spaces from text.

### Syntax

```excel
=TRIM(text)
```

### Example

```excel
=TRIM(A2)
```

If the cell contains:

```text
  Rahul Sharma  
```

The result becomes:

```text
Rahul Sharma
```

### Business Use

Useful for cleaning customer names, product names, addresses, and other text fields containing accidental spaces.

---

## 2. `CLEAN`

Removes non-printing characters from text.

### Syntax

```excel
=CLEAN(text)
```

### Business Use

Useful when data is imported from external systems and contains hidden or non-printing characters.

---

## 3. `TRIM` + `CLEAN`

These functions can be combined for basic text cleaning.

```excel
=TRIM(CLEAN(A2))
```

This helps remove:

* Unnecessary spaces
* Non-printing characters

---

## 4. `LEFT`

Extracts characters from the beginning of a text string.

### Syntax

```excel
=LEFT(text, number_of_characters)
```

### Example

```excel
=LEFT("CHANDAN",3)
```

Result:

```text
CHA
```

---

## 5. `RIGHT`

Extracts characters from the end of a text string.

### Syntax

```excel
=RIGHT(text, number_of_characters)
```

### Example

```excel
=RIGHT("CHANDAN",3)
```

Result:

```text
DAN
```

---

## 6. `MID`

Extracts characters from a specific position within a text string.

### Syntax

```excel
=MID(text, start_position, number_of_characters)
```

### Example

```excel
=MID("ANALYTICS",3,4)
```

Result:

```text
ALYT
```

---

## 7. `PROPER`

Converts text into proper capitalization.

### Syntax

```excel
=PROPER(text)
```

### Example

```excel
=PROPER("rahul sharma")
```

Result:

```text
Rahul Sharma
```

### Business Use

Useful for standardizing customer names, employee names, city names, and other text fields.

---

## 8. `CONCAT`

Combines text from multiple cells or values.

### Syntax

```excel
=CONCAT(A2,B2)
```

### Example

```excel
=CONCAT(A2," ",B2)
```

If:

```text
A2 = Rahul
B2 = Sharma
```

Result:

```text
Rahul Sharma
```

---

## 9. `TEXTSPLIT`

Splits text into multiple cells using a delimiter.

### Syntax

```excel
=TEXTSPLIT(text, column_delimiter)
```

### Example

```excel
=TEXTSPLIT("Rahul-Sharma-South","-")
```

Result:

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| Rahul    | Sharma   | South    |

Another example:

```excel
=TEXTSPLIT("Laptop-Electronics-55000","-")
```

Result:

| Column 1 | Column 2    | Column 3 |
| -------- | ----------- | -------- |
| Laptop   | Electronics | 55000    |

---

# 🏢 Real-World Scenario

Real-world business data is rarely perfectly standardized.

For example, the following values may represent the same customer:

```text
"  Rahul Sharma"
"RAHUL SHARMA"
"rahul sharma"
"Rahul Sharma  "
```

Although they look similar to a human, inconsistent text can cause problems with:

* 🔎 Lookups
* 📊 Grouping
* 🔢 Counting
* 🔍 Filtering
* 📈 Reporting
* 🧹 Data quality

As a Data Analyst, text standardization is an important part of preparing data for analysis.

---

# 📊 Master Dataset

The same **10K master dataset** is used throughout the Excel learning module.

Important customer fields include:

```text
Customer_ID
Customer_Name
City
Region
Email
```

The dataset contains intentional text-quality issues such as:

* Extra spaces
* Different capitalization
* Inconsistent text formatting
* Missing customer names
* Customer information requiring standardization

The purpose is to simulate realistic data-cleaning situations.

---

# 💼 Day 02 Business Exercise

### Scenario

You are working as a **Junior Data Analyst**.

Customer information has been collected from multiple sources and contains inconsistent formatting.

Before the data is used for reporting and lookup operations, management wants the customer information cleaned and standardized.

---

## 📝 Task 1 — Clean Customer Names

Create a new column:

```text
Clean_Customer_Name
```

Use:

```excel
=TRIM(CLEAN(Customer_Name_Cell))
```

Apply the formula to the required customer records.

---

## 📝 Task 2 — Standardize Customer Names

Create:

```text
Proper_Customer_Name
```

Convert the cleaned names into proper capitalization.

Example:

```text
rahul sharma
```

Expected:

```text
Rahul Sharma
```

---

## 📝 Task 3 — Extract First Name

Create:

```text
First_Name
```

Extract the first name from the standardized customer name.

Example:

```text
Rahul Sharma
```

Expected:

```text
Rahul
```

### Challenge

Do **not** assume that every first name has the same number of characters.

---

## 📝 Task 4 — Extract Last Name

Create:

```text
Last_Name
```

Example:

```text
Rahul Sharma
```

Expected:

```text
Sharma
```

### Challenge

The formula should work with names of different lengths.

---

## 📝 Task 5 — Create Customer Label

Create:

```text
Customer_Label
```

Expected format:

```text
CUST100001 - Rahul Sharma
```

Combine:

* Customer ID
* `" - "`
* Proper customer name

Use `CONCAT`.

---

## 📝 Task 6 — Extract Email Username

Create:

```text
Email_Username
```

Example:

```text
rahul.sharma10001@example.com
```

Expected:

```text
rahul.sharma10001
```

Use appropriate text functions.

---

## 📝 Task 7 — Extract Email Domain

Create:

```text
Email_Domain
```

Example:

```text
rahul.sharma10001@example.com
```

Expected:

```text
example.com
```

Use appropriate text functions.

---

## 📝 Task 8 — TEXTSPLIT Challenge

In a temporary area, enter:

```text
Rahul-Sharma-South
```

Use `TEXTSPLIT` to separate the values into three columns:

```text
Rahul | Sharma | South
```

Then test:

```text
Laptop-Electronics-55000
```

Split it into:

```text
Laptop | Electronics | 55000
```

---

# 🧠 Formula Practice

Practice each function individually before attempting the business exercise.

```excel
=TRIM(A2)
```

```excel
=CLEAN(A2)
```

```excel
=TRIM(CLEAN(A2))
```

```excel
=LEFT(A2,3)
```

```excel
=RIGHT(A2,3)
```

```excel
=MID(A2,2,5)
```

```excel
=PROPER(A2)
```

```excel
=CONCAT(A2," ",B2)
```

```excel
=TEXTSPLIT(A2,"-")
```

> ⚠️ These examples are for practice. The business exercise should be solved independently.

---

# ❓ Business Questions

After completing the practical exercise, answer these questions:

1. Why is text standardization important in data analysis?
2. What problems can unnecessary spaces cause?
3. What is the difference between `TRIM` and `CLEAN`?
4. What is the difference between `LEFT`, `RIGHT`, and `MID`?
5. When would you use `PROPER`?
6. When would `CONCAT` be useful?
7. When would `TEXTSPLIT` be useful?
8. Why is using a fixed number of characters a poor approach for extracting names?
9. How can text cleaning improve lookup accuracy?
10. Why should the original/raw data generally be preserved before cleaning?

---

# 📋 Formula Cheat Sheet

| Function    | Purpose                          | Example              |
| ----------- | -------------------------------- | -------------------- |
| `TRIM`      | Remove unnecessary spaces        | `=TRIM(A2)`          |
| `CLEAN`     | Remove non-printing characters   | `=CLEAN(A2)`         |
| `LEFT`      | Extract from the beginning       | `=LEFT(A2,3)`        |
| `RIGHT`     | Extract from the end             | `=RIGHT(A2,3)`       |
| `MID`       | Extract from a specific position | `=MID(A2,2,5)`       |
| `PROPER`    | Standardize capitalization       | `=PROPER(A2)`        |
| `CONCAT`    | Combine text                     | `=CONCAT(A2," ",B2)` |
| `TEXTSPLIT` | Split text using a delimiter     | `=TEXTSPLIT(A2,"-")` |

---

# ✅ Day 02 Completion Checklist

* [ ] Understand why text cleaning is important
* [ ] Practice `TRIM`
* [ ] Practice `CLEAN`
* [ ] Practice `TRIM` + `CLEAN`
* [ ] Practice `LEFT`
* [ ] Practice `RIGHT`
* [ ] Practice `MID`
* [ ] Practice `PROPER`
* [ ] Practice `CONCAT`
* [ ] Practice `TEXTSPLIT`
* [ ] Clean customer names
* [ ] Standardize customer names
* [ ] Extract first names
* [ ] Extract last names
* [ ] Create customer labels
* [ ] Extract email usernames
* [ ] Extract email domains
* [ ] Complete the business questions

---

# 📁 Day 02 Files

```text
Day_02_Text_Functions/
├── README.md
├── raw_data.xlsx
└── solution.xlsx
```

### File Description

| File            | Purpose                                      |
| --------------- | -------------------------------------------- |
| `README.md`     | Concepts, instructions, tasks, and questions |
| `raw_data.xlsx` | Original dataset used for practice           |
| `solution.xlsx` | Completed formulas and final results         |

---

# 🔜 Next: Day 03

## 📈 Math & Statistical Functions

Topics:

* `SUMIFS`
* `COUNTIFS`
* `AVERAGEIFS`
* `ROUND`
* `MEDIAN`
* `STDEV.S`
* Percentiles
* Regional Performance Analysis

---

## ⭐ Learning Principle

> **Learn → Practice → Analyze → Build → Document**

The goal is not simply to memorize Excel functions.

The goal is to understand **what a function does, when to use it, and how it solves a real business problem.**
