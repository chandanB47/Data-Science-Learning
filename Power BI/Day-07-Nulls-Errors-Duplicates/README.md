# 📊 Power BI — Day 07: Nulls, Errors & Duplicates

**Level:** Beginner  
**Day:** 7 of 30  
**Phase:** Level 2 — Power Query & Data Preparation  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`

## 🎯 Day 7 Goal

Learn to identify and handle common data-quality problems in Power Query:

- Missing values / `null`
- Errors
- Duplicate rows
- Data-quality validation after cleaning

The goal is to understand **why** a value is missing or invalid before deciding how to clean it.

## 📚 Topics

### 1. Null Values
- Identify missing values
- Understand what `null` means
- Replace nulls when appropriate
- Know when a null should remain null

### 2. Errors
- Identify error cells
- Understand common causes
- Replace or remove errors appropriately
- Validate the column after fixing errors

### 3. Duplicates
- Identify duplicate records
- Decide what defines a true duplicate
- Remove unwanted duplicates
- Avoid deleting legitimate repeated records

### 4. Validation
After cleaning, verify:
- Nulls are handled appropriately
- Errors are resolved
- Unwanted duplicates are removed
- Important columns remain valid
- Row-count changes are understood

## 🛠️ Tools

- Power BI Desktop
- Power Query Editor
- `PowerBI_Master_Sales_Dataset_1500.csv`

## 📁 Expected GitHub Structure

```text
Power BI/
└── Day-07-Nulls-Errors-Duplicates/
    ├── README.md
    ├── TASK.md
    ├── Day07_Nulls_Errors_Duplicates.pbix
    └── Screenshots/
        ├── 01-null-check.png
        ├── 02-null-handling.png
        ├── 03-error-check.png
        ├── 04-error-handling.png
        ├── 05-duplicate-check.png
        ├── 06-duplicates-removed.png
        └── 07-final-validation.png
```

## ✅ Day 7 Deliverables

- Check the dataset for null values
- Practice handling missing values
- Check for errors
- Practice resolving/removing errors
- Check for duplicate records
- Remove only unwanted duplicates
- Validate the cleaned table
- Save the Day 7 `.pbix` file
- Capture the required screenshots
- Update your GitHub folder

## 📸 Screenshot Checklist

| # | Screenshot | Required |
|---|---|---|
| 01 | Null check | ✅ |
| 02 | Null handling | ✅ |
| 03 | Error check | ✅ |
| 04 | Error handling | ✅ |
| 05 | Duplicate check | ✅ |
| 06 | Duplicates removed | ✅ |
| 07 | Final validation | ✅ |

## 🧠 Important Rule

Do **not** blindly replace every null with `0`, `"Unknown"`, or another value.

The correct treatment depends on the meaning of the column.

A repeated `OrderID` also does not automatically mean a duplicate: one order may legitimately contain multiple records.

## 🎓 Expected Learning Outcome

After Day 7, you should be able to explain:

> I can identify nulls, errors, and duplicates in Power Query, apply an appropriate cleaning method, and validate the dataset after cleaning.

## ➡️ Next Day

**Day 8 — Rename, Split & Replace Columns**
