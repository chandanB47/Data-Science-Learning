# 📋 Power BI — Day 08 TASK: Rename, Split & Replace Columns

**Level:** Beginner  
**Day:** 8 of 30  
**Phase:** Level 2 — Power Query & Data Preparation  
**Dataset:** `PowerBI_Master_Sales_Dataset_1500.csv`

# 🎯 Objective

Today you will practice:

1. Rename columns
2. Split columns
3. Replace values
4. Review Applied Steps
5. Validate the transformed table

---

# 🛠️ Task 1 — Open Power Query

1. Open your completed Day 7 `.pbix`.
2. Save a new copy as:

```text
Day08_Rename_Split_Replace.pbix
```

3. Go to:

**Home → Transform data**

4. Open the main dataset query.

---

# ✏️ Task 2 — Rename a Column

1. Select a suitable column.
2. Right-click → **Rename**.
3. Give it a clear business-friendly name.
4. Press Enter.
5. Confirm the new name.

### Example

```text
OrderStatus
```

could become:

```text
Order Status
```

Only make a rename if it improves readability.



---

# ✂️ Task 3 — Split a Column

1. Select a suitable text column.
2. Go to **Transform → Split Column**.
3. Choose a suitable split method.
4. If using a delimiter, choose one that actually exists in the data.
5. Apply the split.
6. Check the new columns.

### Example

```text
North-East
```

split using `-` becomes:

```text
North
East
```

If your dataset does not contain a suitable column for a meaningful split, do not damage an important field. Record that observation and practice on a controlled copy if needed.



---

# 🔄 Task 4 — Replace a Value

1. Select a suitable text column.
2. Go to **Transform → Replace Values**.
3. Enter the existing value.
4. Enter the replacement value.
5. Apply the transformation.
6. Check the affected rows.

### Example

```text
Online
```

could be standardized to:

```text
Online Sales
```

### ⚠️ Important

Replace only the value you intend to change.



---

# 🔍 Task 5 — Inspect the Transformed Table

Review the table after the transformations.

Check:

- Renamed column
- Split columns
- Replaced values
- Existing columns
- Data types
- Row count

Make sure no important records were unexpectedly changed.


---

## 🔍 Task 6 — Review Applied Steps

### Transformations Reviewed

| Transformation | Applied Step Reviewed | Result |
|---|---|---|
| Rename Column | Rename step | `OrderStatus` changed to `Order Status` |
| Split Column | Split step | `OrderID` was split into separate columns |
| Replace Value | Replace Values step | `Online` changed to `Online Sales` |

### 📌 Observation

> Power Query records each transformation as an Applied Step. Clicking the steps allows the transformation process to be reviewed step by step.

---

# ✅ Task 7 — Final Validation

Check:

### Column Names
- Is the renamed column correct?
- Is the name clear?

### Split
- Did the split produce the expected columns?
- Are the values correct?

### Replace
- Was the intended value replaced?
- Were unrelated values left unchanged?

### Data Integrity
- Row count
- Data types
- Important business columns
- Overall table structure

Complete:
| Validation | Result |
|---|---|
| Rename checked | `OrderStatus` → `Order Status` |
| Split checked | `OrderID` split successfully |
| Replace checked | `Online` → `Online Sales` |
| Row count verified | No unexpected change |
| Data types verified | Correct |
| Data integrity verified | Yes |
| Final status | Validated |

### 📌 Final Observation

> The renamed column, split columns, and replaced value were reviewed. The table structure, row count, data types, and important business columns were also validated.


---

# 🧠 Task 8 — Knowledge Check

### Q1. Why should column names be clear and meaningful?

Clear and meaningful column names make the data easier to understand, identify, and work with.

### Q2. What is the purpose of splitting a column?

Splitting a column separates one column into multiple columns based on a delimiter or another splitting method.

### Q3. What should you check before choosing a delimiter?

Check which character or pattern actually exists in the data and whether it correctly separates the values.

### Q4. What does Replace Values do?

Replace Values changes a specific existing value in a column to another value.

### Q5. Why should you be careful when replacing values?

Because an incorrect replacement could change values that were not intended to be changed.

### Q6. Where can you see transformations performed in Power Query?

Transformations can be viewed in **Query Settings → Applied Steps**.

### Q7. Why should you validate the table after a transformation?

Validation confirms that the transformation worked correctly and that important data, row counts, data types, and table structure were not unexpectedly changed.


---

# 💾 Save Your Work

```text
Power BI/
└── Day-08-Rename-Split-Replace/
    ├── README.md
    ├── TASK.md
    ├── Day08_Rename_Split_Replace.pbix
    └── Screenshots/
```

---

# ✅ Day 8 Completion Checklist

- [x] I renamed a column.
- [x] I understand why the rename was useful.
- [x] I split a suitable column.
- [x] I understand how the split affected the table.
- [x] I replaced a specific value.
- [x] I checked that unrelated values were not changed.
- [x] I reviewed Applied Steps.
- [x] I validated the final table.
- [x] I saved the PBIX file.
- [x] I captured all required screenshots.
- [x] I am ready for Day 9.

---

# 🚀 Next

**Day 9 — Conditional & Custom Columns**

Do not start Day 9 until Day 8 has been completed and reviewed.
