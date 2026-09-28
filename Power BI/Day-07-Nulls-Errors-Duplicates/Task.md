# 📋 Power BI — Day 07 TASK: Nulls, Errors & Duplicates

**Level:** Beginner  
**Day:** 7 of 30  
**Phase:** Level 2 — Power Query & Data Preparation  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`

# 🎯 Objective

Today you will practice:

1. Identify and handle **null values**
2. Identify and handle **errors**
3. Identify and remove **unwanted duplicates**
4. Validate the cleaned dataset

---

# 🛠️ Task 1 — Open Power Query

1. Open your Day 6 `.pbix` file.
2. Save a new copy as:

```text
Day07_Nulls_Errors_Duplicates.pbix
```

3. Go to:

**Home → Transform data**

4. Open the relevant table/query.

### 📸 Screenshot

```text
01-null-check.png
```

---

# 🔎 Task 2 — Identify Null Values

Inspect the dataset before changing anything.

Check important columns such as:

- `CustomerID`
- `City`
- `Product`
- `Quantity`
- `UnitPrice`
- `NetSales`

Use **Column Quality** if needed.

Record your observations:

| Column | Null Found? | What does it mean? | Action |
|---|---|---|---|
| CustomerID | | | |
| City | | | |
| Product | | | |
| Quantity | | | |
| UnitPrice | | | |
| NetSales | | | |

### If no nulls exist

Write:

> No null values found in this column.

Do not invent a cleaning result.

### 📸 Screenshot

```text
01-null-check.png
```

---

# 🧹 Task 3 — Handle Null Values

If null values exist:

1. Select the affected column.
2. Decide why the value is missing.
3. Choose an appropriate cleaning method.
4. Apply the transformation.
5. Check the result.

Possible actions include:

- Replace Values
- Replace null with a meaningful value such as `Unknown`
- Replace with a numeric value only when justified
- Remove rows when the missing value makes the record unusable

### ⚠️ Rule

Do not replace every null with `0`.

The correct action depends on the meaning of the column.

### 📸 Screenshot

```text
02-null-handling.png
```

---

# ⚠️ Task 4 — Identify Errors

Use **Column Quality** and look for the **Errors** category.

For each error, identify:

- Column name
- Error type/message
- Possible reason

Example:

```text
Column: Quantity
Error: Data conversion error
Possible reason: Invalid text value in a numeric column
```

### If there are no errors

Write:

> No errors found in the current dataset.

Do not create a fake error just to complete the checklist.

### 📸 Screenshot

```text
03-error-check.png
```

---

# 🛠️ Task 5 — Handle Errors

If errors are present:

1. Select the affected column.
2. Investigate the error.
3. Use an appropriate option such as:
   - Replace Errors
   - Remove Errors
4. Confirm the result.
5. Check that the column still has the correct data type.

### Decision rule

Use **Remove Errors** when the record is unusable.

Use **Replace Errors** when a valid replacement can be justified.

### 📸 Screenshot

```text
04-error-handling.png
```

---

# 🔁 Task 6 — Identify Duplicate Rows

Decide what defines a duplicate before removing anything.

Consider a business key such as:

- `OrderID`
- Or an appropriate combination of columns if one order can contain multiple records

### Important

A repeated `OrderID` does **not** automatically mean the row is a duplicate.

One order may legitimately contain multiple products or records.

Record your observation:

| Check | Result |
|---|---|
| Column(s) used to identify duplicates | |
| Duplicate rows found? | |
| Rows removed | |
| Reason | |

### 📸 Screenshot

```text
05-duplicate-check.png
```

---

# 🗑️ Task 7 — Remove Unwanted Duplicates

If true duplicate rows are found:

1. Confirm they are genuinely duplicated.
2. Select the appropriate column(s).
3. Use:

**Home → Remove Rows → Remove Duplicates**

4. Check the resulting row count.
5. Make sure valid records were not accidentally removed.

### If no duplicates exist

Write:

> No duplicate records found.

Do not remove valid records just to demonstrate the feature.

### 📸 Screenshot

```text
06-duplicates-removed.png
```

---

# ✅ Task 8 — Final Data Validation

Validate the cleaned dataset.

### Check Nulls
- Are expected missing values handled?
- Are important fields still missing?

### Check Errors
- Are errors resolved?
- Are data types still correct?

### Check Duplicates
- Were only genuine duplicates removed?
- Is the row count reasonable?

### Check Data Integrity

Review:

- `OrderID`
- `OrderDate`
- `CustomerID`
- `Quantity`
- `UnitPrice`
- `NetSales`

Complete:

| Validation | Result |
|---|---|
| Nulls checked | |
| Errors checked | |
| Duplicates checked | |
| Rows before cleaning | |
| Rows after cleaning | |
| Data types valid | |
| Final status | |

### 📸 Screenshot

```text
07-final-validation.png
```

---

# 🧠 Task 9 — Knowledge Check

Answer these in your notes.

### Q1. What is `null` in Power Query?

```text
__________________________________________________
```

### Q2. Why should we not replace every null with 0?

```text
__________________________________________________
```

### Q3. What is the difference between a null and an error?

```text
__________________________________________________
```

### Q4. Why should you investigate an error before removing it?

```text
__________________________________________________
```

### Q5. Does a repeated OrderID always mean the row is a duplicate?

```text
__________________________________________________
```

### Q6. What should you check before removing duplicates?

```text
__________________________________________________
```

### Q7. Why is validation important after data cleaning?

```text
__________________________________________________
```

---

# 💾 Save Your Work

```text
Power BI/
└── Day-07-Nulls-Errors-Duplicates/
    ├── README.md
    ├── TASK.md
    ├── Day07_Nulls_Errors_Duplicates.pbix
    └── Screenshots/
```

---

# ✅ Day 7 Completion Checklist

- [x] I checked for null values.
- [x] I understood what missing values represented.
- [x] I handled nulls appropriately.
- [x] I checked for errors.
- [x] I investigated errors before cleaning them.
- [x] I handled errors appropriately.
- [x] I checked for duplicates.
- [x] I identified what actually defines a duplicate.
- [x] I removed only unwanted duplicates.
- [x] I validated the cleaned data.
- [x] I saved the PBIX file.
- [x] I captured all required screenshots.
- [x] I am ready for Day 8.

---

# 🚀 Next

**Day 8 — Rename, Split & Replace Columns**

Do not start Day 8 until Day 7 has been completed and reviewed.
