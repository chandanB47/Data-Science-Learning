# 📋 Power BI — Day 09 TASK: Conditional & Custom Columns

**Level:** Beginner  
**Day:** 9 of 30  
**Phase:** Level 2 — Power Query & Data Preparation  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`

# 🎯 Objective

Today you will learn:
1. Conditional Columns
2. Custom Columns
3. Basic `if ... then ... else` logic
4. Simple calculations
5. Validation

---

# 🛠️ Task 1 — Open Power Query

1. Open your completed Day 8 `.pbix`.
2. Save a new copy as:

```text
Day09_Conditional_Custom_Columns.pbix
```

3. Go to **Home → Transform data**.
4. Open the main dataset query.

---

# 🟢 Task 2 — Create a Conditional Column

Create:

```text
Sales Level
```

Use `NetSales`:

```text
If NetSales >= 5000 → "High"
Else → "Low"
```

### Steps

1. Select the dataset.
2. Go to **Add Column → Conditional Column**.
3. New column name: `Sales Level`
4. Column: `NetSales`
5. Condition: `is greater than or equal to`
6. Value: `5000`
7. Output: `High`
8. Else: `Low`
9. Click **OK**.


---

# 🔍 Task 3 — Check Conditional Results

Inspect several rows.

For every row:

```text
NetSales >= 5000
```

should produce:

```text
High
```

Otherwise:

```text
Low
```

Check:
- Column appears correctly
- Values are logical
- No unexpected results
- Data type is Text


---

# 🧮 Task 4 — Create a Custom Column

Create:

```text
Calculated Sales
```

Use:

```text
[Quantity] * [UnitPrice]
```

### Steps

1. Go to **Add Column → Custom Column**.
2. New column name: `Calculated Sales`
3. Enter:

```text
[Quantity] * [UnitPrice]
```

4. Click **OK**.

Example:

```text

Quantity = 5
UnitPrice = 100
Calculated Sales = 500
```
---

## 🧮 Task 5 — Check Custom Column Results

Three sample rows were manually calculated and compared with the `Calculated Sales` column.

| Row | Quantity | UnitPrice | Expected | Actual | Correct? |
|---|---:|---:|---:|---:|---|
| 1 | 1 | 22000 | 22000 | 22000 | ✅ |
| 2 | 3 | 22000 | 66000 | 66000 | ✅ |
| 3 | 7 | 1600 | 11200 | 11200 | ✅ |

### Result

All 3 sample calculations matched the `Calculated Sales` values.

> The custom column formula `[Quantity] * [UnitPrice]` was verified successfully.


---

# 🧠 Task 6 — Understand Basic M Logic

Understand the concept:

```text
if condition then result else result
```

Meaning:

```text
IF something is true
    THEN return one value
ELSE
    return another value
```

You do not need advanced M language today.

---

## 🔎 Task 7 — Review Applied Steps

### Transformations Reviewed

| Transformation | Result |
|---|---|
| Conditional Column | `Sales Level` created using `NetSales >= 5000` |
| Custom Column | `Calculated Sales` created using `[Quantity] * [UnitPrice]` |

### 📌 Observation

> The Conditional Column and Custom Column transformations were recorded in the Applied Steps pane. Each step can be selected to review how the table changes.

### Applied Steps Reviewed

- Conditional Column — `Sales Level`
- Custom Column — `Calculated Sales`

---

# ✅ Task 8 — Final Validation

| Validation | Result |
|---|---|
| Conditional Column checked | Yes |
| Custom Column checked | Yes |
| Formula verified | Yes |
| Data types verified | Yes |
| Errors checked | No errors found |
| Row count verified | No unexpected change |
| Final status | Validated |

## 🔍 Validation Details

### Sales Level

- `NetSales >= 5000` → `High`
- `NetSales < 5000` → `Low`
- Data type: Text

### Calculated Sales

- Formula: `[Quantity] * [UnitPrice]`
- Manual sample calculations matched the results.
- Data type: Numeric
- No errors found.

### 📌 Final Observation

> The Conditional Column and Custom Column were validated successfully. The formulas produced the expected results, data types were appropriate, no errors were introduced, and the row count remained unchanged.



---

# 🧠 Task 9 — Knowledge Check

### Q1. What is a Conditional Column?

A Conditional Column uses a condition to return different values, such as High or Low.

### Q2. When would you use a Conditional Column?

A Conditional Column can be used to classify or categorize data based on conditions, such as creating High and Low sales levels.

### Q3. What is a Custom Column?

A Custom Column creates a new column using a formula or expression.

### Q4. What does this calculate?

```text
[Quantity] * [UnitPrice]

It calculates the sales amount by multiplying Quantity by UnitPrice.

Example:

2 × 100 = 200
```
### Q5. What does if ... then ... else mean?

It means that if a condition is true, return one result; otherwise, return another result.

### Q6. Why should you validate a newly created column?

To check that the new column contains the expected results and does not contain errors or unexpected values.

### Q7. What data type should a calculated numeric column normally have?

A calculated numeric column should normally have a numeric data type, such as Decimal Number or Whole Number depending on the calculation.


---

# 💾 Save Your Work

```text
Power BI/
└── Day-09-Conditional-Custom-Columns/
    ├── README.md
    ├── TASK.md
    ├── Day09_Conditional_Custom_Columns.pbix
    └── Screenshots/
```

---

# ✅ Day 9 Completion Checklist

- [x] Created a Conditional Column
- [x] Checked the Conditional Column results
- [x] Created a Custom Column
- [x] Verified the formula with sample calculations
- [x] Reviewed Applied Steps
- [x] Checked data types
- [x] Checked for errors
- [x] Validated the final table
- [x] Saved the PBIX file
- [x] Captured all required screenshots
- [ ] Ready for Day 10

---

# 🚀 Next

**Day 10 — Group By & Aggregation**

Do not start Day 10 until Day 9 has been completed and reviewed.
