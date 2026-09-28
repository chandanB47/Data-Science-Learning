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
| CustomerID | No | No missing values | No action |
| City | No | No missing values | No action |
| Product | No | No missing values | No action |
| Quantity | No | No missing values | No action |
| UnitPrice | No | No missing values | No action |
| NetSales | No | No missing values | No action |


### 📌 Observation

> No null values found in the checked columns.

### ✅ Result

No null-value cleaning was required because the dataset contains no missing values in these columns.

---

## 🧹 Task 3 — Handle Null Values

### Result

No null values were found in the checked columns.

Therefore, no null-value transformation was required.

| Column | Null Found? | Action |
|---|---|---|
| CustomerID | No | No action |
| City | No | No action |
| Product | No | No action |
| Quantity | No | No action |
| UnitPrice | No | No action |
| NetSales | No | No action |

> No null values were found, so the dataset was left unchanged.



---

## ⚠️ Task 4 — Identify Errors

### Result

No errors found in the current dataset.

| Column | Errors Found? |
|---|---|
| CustomerID | No |
| City | No |
| Product | No |
| Quantity | No |
| UnitPrice | No |
| NetSales | No |

> No errors were found in the current dataset.

---

## 🛠️ Task 5 — Handle Errors

### Result

No errors were found in the current dataset.

Therefore, no error-handling transformation was required.

| Check | Result |
|---|---|
| Errors found | No |
| Replace Errors | Not required |
| Remove Errors | Not required |
| Data type validation | Completed |

> No errors were found, so the dataset was left unchanged.

---

## 🔁 Task 6 — Identify Duplicate Rows

### Duplicate Check

| Check | Result |
|---|---|
| Column(s) used to identify duplicates | OrderID |
| Duplicate rows found? | No |
| Rows removed | 0 |
| Reason | No confirmed duplicate records were identified |

### 📌 Observation

> A repeated OrderID was not treated as a duplicate automatically because an order may legitimately contain multiple records.

### ✅ Result

No unwanted duplicate records were identified, so no rows were removed.


---

## 🗑️ Task 7 — Remove Unwanted Duplicates

### Result

No duplicate records were found.

Therefore, no rows were removed.

| Check | Result |
|---|---|
| Duplicate records found | No |
| Rows removed | 0 |
| Remove Duplicates applied | No |
| Valid records preserved | Yes |

> No duplicate records found, so no duplicate-removal transformation was applied.


---

# ✅ Task 8 — Final Data Validation

## Validation Results

| Validation | Result |
|---|---|
| Nulls checked | No null values found |
| Errors checked | No errors found |
| Duplicates checked | No unwanted duplicates found |
| Rows before cleaning | 1,500 |
| Rows after cleaning | 1,500 |
| Data types valid | Yes |
| Final status | Validated |

## 🔍 Data Integrity Check

The following important columns were reviewed:

- `OrderID`
- `OrderDate`
- `CustomerID`
- `Quantity`
- `UnitPrice`
- `NetSales`

### 📌 Final Observation

> The dataset contained no null values, no errors, and no confirmed unwanted duplicate records. Therefore, no rows were removed or modified during the cleaning process.

---

# 🧠 Task 9 — Knowledge Check

### Q1. What is `null` in Power Query?

A `null` represents a missing or empty value.

### Q2. Why should we not replace every null with `0`?

Because a null value does not necessarily mean zero. The correct replacement depends on the meaning of the column.

### Q3. What is the difference between a null and an error?

A null means a value is missing, while an error means Power Query encountered a problem processing the value.

### Q4. Why should you investigate an error before removing it?

Because the error may have a valid cause. We should understand the problem before deciding whether to replace or remove the value.

### Q5. Does a repeated `OrderID` always mean the row is a duplicate?

No. An order may legitimately contain multiple records.

### Q6. What should you check before removing duplicates?

First determine what column or combination of columns defines a true duplicate.

### Q7. Why is validation important after data cleaning?

Validation confirms that the cleaning process worked correctly and that valid data was not accidentally removed or damaged.
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
