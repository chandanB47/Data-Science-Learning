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
- [ ] Transaction-level table.
- [ ] Numeric sales fields are correctly typed.
- [ ] Foreign keys can repeat.

### DimCustomer
- [ ] CustomerID unique.
- [ ] Descriptive attributes available.

### DimProduct
- [ ] Product key unique.
- [ ] Category descriptive.

### DimDate
- [ ] Date unique.
- [ ] Continuous calendar.
- [ ] Covers FactSales date range.
- [ ] Month sorting correct.

### Relationships
- [ ] Customer = 1:*.
- [ ] Product = 1:*.
- [ ] Date = 1:*.
- [ ] Single direction.
- [ ] Active.
- [ ] No unnecessary relationships.

---

# 🧠 Knowledge Check

Answer in your own words:

1. What is filter propagation?
2. What is an active relationship?
3. What is an inactive relationship?
4. Why is 1:* the normal pattern for a dimension-to-fact relationship?
5. What is the risk of unnecessary bidirectional relationships?
6. What is an ambiguous relationship path?
7. Why should dimension keys be unique?
8. What can cause unmatched foreign keys?
9. Why should you avoid unnecessary many-to-many relationships?
10. Why is model validation important before writing DAX?
11. What happens when a Customer Type filter reaches FactSales?
12. What happens when a Date filter reaches FactSales?
13. Why is a star schema easier to troubleshoot?

---

# 📸 Screenshot Checklist

Save:

- [ ] `01-final-model.png` — Clean final star-schema Model view.
- [ ] `02-relationship-properties.png` — Relationship properties.
- [ ] `03-customer-filter-test.png` — Customer filter affecting sales.
- [ ] `04-product-date-filter-test.png` — Product/date filters affecting sales.
- [ ] `05-model-validation.png` — Final validation report page.

---

# ✅ Completion Checklist

- [ ] Day 15 PBIX copied.
- [ ] Customer relationship audited.
- [ ] Product relationship audited.
- [ ] Date relationship audited.
- [ ] Customer filter tested.
- [ ] Product filter tested.
- [ ] Date filter tested.
- [ ] Dimension key uniqueness checked.
- [ ] Blank/unmatched keys investigated.
- [ ] Unnecessary relationships checked.
- [ ] Model layout cleaned.
- [ ] Final validation page created.
- [ ] Knowledge check answered.
- [ ] Screenshots saved.
- [ ] PBIX saved as `Day16_Advanced_Modeling_Validation.pbix`.

# 📦 Final Folder Structure

```text
Power BI/
└── Day-16-Advanced-Modeling-Validation/
    ├── README.md
    ├── TASK.md
    ├── Day16_Advanced_Modeling_Validation.pbix
    └── Screenshots/
        ├── 01-final-model.png
        ├── 02-relationship-properties.png
        ├── 03-customer-filter-test.png
        ├── 04-product-date-filter-test.png
        └── 05-model-validation.png
```

# 🏆 Phase Completion

After completing Day 16, you will have completed:

```text
Days 1–5   → Power BI Fundamentals
Days 6–12  → Power Query & Data Preparation
Days 13–16 → Data Modeling
```

The next phase is:

**Days 17–21 → DAX**
