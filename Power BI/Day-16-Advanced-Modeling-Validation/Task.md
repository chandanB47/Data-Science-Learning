# 📝 Power BI — Day 16 TASK: Advanced Modeling, Filter Context & Model Validation

**Level:** Intermediate  
**Estimated time:** 75–120 minutes

## 🎯 Goal
Perform a final quality review of your Power BI model and understand how relationship settings control filter propagation.

---

# Part A — Start from Day 15

## Task 1: Open and save
1. Open your completed `Day15_Date_Table_Time_Intelligence.pbix`.
2. Save a copy as:

```text
Day16_Advanced_Modeling_Validation.pbix
```

3. Open **Model view**.

Your model should contain:

```text
DimCustomer
DimProduct
DimDate
FactSales
```

---

# Part B — Relationship Audit

## Task 2: Check Customer Relationship

Verify:

```text
DimCustomer[CustomerID]
        1
        |
        *
FactSales[CustomerID]
```

Confirm:
- Cardinality = `1:*`
- Cross filter = `Single`
- Active = `Yes`

## Task 3: Check Product Relationship

Verify:

```text
DimProduct[Product]
        1
        |
        *
FactSales[Product]
```

Confirm:
- Cardinality = `1:*`
- Cross filter = `Single`
- Active = `Yes`

## Task 4: Check Date Relationship

Verify:

```text
DimDate[Date]
        1
        |
        *
FactSales[OrderDate]
```

Confirm:
- Cardinality = `1:*`
- Cross filter = `Single`
- Active = `Yes`

---

# Part C — Customer Filter Test

## Task 5: Create a Customer test

Go to Report view.

Create a simple visual showing:
- `DimCustomer[CustomerType]`
- `FactSales[NetSales]`

Add a slicer using:

```text
DimCustomer[CustomerType]
```

Select one customer type.

### Observe:
Does NetSales change?

Expected:

```text
Customer filter
      ↓
DimCustomer
      ↓
Relationship
      ↓
FactSales
      ↓
NetSales
```

If the value does not respond, investigate the relationship before continuing.

---

# Part D — Product Filter Test

## Task 6

Create a visual using:
- `DimProduct[Category]`
- `FactSales[NetSales]`

Add a slicer using:

```text
DimProduct[Category]
```

Select one category.

Confirm that NetSales responds.

---

# Part E — Date Filter Test

## Task 7

Create a visual using:
- `DimDate[Year]`
- `DimDate[Month Name]`
- `FactSales[NetSales]`

Add a slicer using:

```text
DimDate[Year]
```

Select a year.

Confirm that sales respond.

Then verify that Month Name appears chronologically.

---

# Part F — Understand Filter Direction

## Task 8

For each relationship, identify the normal filter flow:

```text
DimCustomer → FactSales
DimProduct  → FactSales
DimDate     → FactSales
```

Write in your own words why the dimension is normally on the filtering side.

### Important
Do not change relationships to **Both** just to make a visual work.

If a relationship requires bidirectional filtering, first understand why.

---

# Part G — Relationship Problem Investigation

## Task 9: Check for duplicate dimension keys

For each dimension:

### DimCustomer
Check whether `CustomerID` is unique.

### DimProduct
Check whether `Product` is unique.

### DimDate
Check whether `Date` is unique.

If a key is duplicated on the supposed `1` side, investigate the source rather than forcing a many-to-many relationship.

---

# Part H — Check for Blank / Unmatched Keys

## Task 10

Look for blank or unmatched foreign keys in FactSales:

- CustomerID
- Product
- OrderDate

Think about why unmatched values can occur.

Possible causes:
- Missing dimension record.
- Incorrect formatting.
- Blank source value.
- Data-quality issue.
- Incorrect relationship key.

Do not delete records automatically.

---

# Part I — Check for Unnecessary Relationships

## Task 11

Inspect the Model view.

Ask:

1. Does every relationship represent a real business relationship?
2. Are there unnecessary direct relationships between dimensions?
3. Are there multiple paths between the same tables?
4. Are any relationships many-to-many without a clear reason?
5. Are any relationships bidirectional without a clear reason?

For this learning model, keep the architecture simple:

```text
DimCustomer ──┐
DimProduct  ──┼── FactSales
DimDate     ──┘
```

---

# Part J — Final Model Layout

## Task 12

Arrange the Model view so that FactSales is central.

Recommended:

```text
                 DimCustomer
                      |
                      |
DimProduct ───── FactSales ───── DimDate
```

Make the model readable.

Avoid unnecessary crossing relationship lines.

---

# Part K — Final Validation Report

## Task 13

Create one final report page containing:

### Visual 1
Sales by Customer Type.

### Visual 2
Sales by Product Category.

### Visual 3
Sales by Year/Month.

### Slicers
- Customer Type
- Category
- Year

Test the slicers.

A filter from each dimension should affect the relevant sales visuals.

---

# Part L — Modeling Quality Checklist

## Task 14

### FactSales
- [x] Transaction-level table.
- [x] Numeric sales fields are correctly typed.
- [x] Foreign keys can repeat.

### DimCustomer
- [x] CustomerID unique.
- [x] Descriptive attributes available.

### DimProduct
- [x] Product key unique.
- [x] Category descriptive.

### DimDate
- [x] Date unique.
- [x] Continuous calendar.
- [x] Covers FactSales date range.
- [x] Month sorting correct.

### Relationships
- [x] Customer = 1:*.
- [x] Product = 1:*.
- [x] Date = 1:*.
- [x] Single direction.
- [x] Active.
- [x] No unnecessary relationships.



---


# ✅ Completion Checklist

- [x] Day 15 PBIX copied.
- [x] Customer relationship audited.
- [x] Product relationship audited.
- [x] Date relationship audited.
- [x] Customer filter tested.
- [x] Product filter tested.
- [x] Date filter tested.
- [x] Dimension key uniqueness checked.
- [x] Blank/unmatched keys investigated.
- [x] Unnecessary relationships checked.
- [x] Model layout cleaned.
- [x] Final validation page created.
- [x] Knowledge check answered.
- [x] Screenshots saved.
- [x] PBIX saved as `Day16_Advanced_Modeling_Validation.pbix`.

# 📦 Final Folder Structure

```text
Power BI/
└── Day-16-Advanced-Modeling-Validation/
    ├── README.md
    ├── TASK.md
    ├── Day16_Advanced_Modeling_Validation.pbix
   

# 🏆 Phase Completion

After completing Day 16, you will have completed:

```text
Days 1–5   → Power BI Fundamentals
Days 6–12  → Power Query & Data Preparation
Days 13–16 → Data Modeling
```

The next phase is:

**Days 17–21 → DAX**
