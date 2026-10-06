# Power BI — Day 13 TASK: Introduction to Data Modeling & Relationships

**Level:** Beginner → Intermediate  
**Estimated time:** 60–90 minutes

## Goal
Build your first proper Power BI relationship between a customer dimension and a sales fact-style table.

## Part A — Open and Identify

### Task 1
1. Open your completed Day 12 PBIX.
2. Save a copy as `Day13_Data_Modeling_Relationships.pbix`.
3. Open **Model view**.
4. Identify your detailed/appended sales table.
5. Identify your customer lookup table from Day 11.

## Part B — Prepare Customer Dimension

### Task 2
Your customer table should contain fields such as:
- `CustomerID`
- `CustomerType`
- `City`

If you need to recreate it:
1. Open **Home → Transform data**.
2. Reference the detailed sales query.
3. Keep `CustomerID`, `CustomerType`, and `City`.
4. Select `CustomerID`.
5. Choose **Remove Rows → Remove Duplicates**.
6. Rename the query/table `DimCustomer`.

**Checkpoint:** Each CustomerID should appear only once.

## Part C — Identify Keys

### Task 3
In `DimCustomer`:
```text
CustomerID = Primary Key
```

In Sales:
```text
CustomerID = Foreign Key
```

Why? A customer should occur once in the dimension but can occur many times in transaction-level sales.

Example:
```text
DimCustomer        Sales
C001               C001
C002               C001
C003               C002
                   C003
                   C003
```

## Part D — Create Relationship

### Task 4
In Model view:
1. Locate `DimCustomer[CustomerID]`.
2. Locate the sales table's `CustomerID`.
3. Drag `DimCustomer[CustomerID]` onto Sales `CustomerID`.
4. Set:
   - **Cardinality:** One to many (1:*)
   - **Cross filter direction:** Single
   - **Active:** Yes
5. Select **OK**.

Expected:
```text
DimCustomer[CustomerID]  1 ───── *  Sales[CustomerID]
```

## Part E — Verify Properties

### Task 5
Double-click the relationship line and confirm:
- Correct tables
- Correct columns
- Cardinality = 1:*
- Cross filter = Single
- Active relationship

Do not switch to Both simply because it is available.

## Part F — Validate in a Report

### Task 6
Create a Table visual in Report view.

Add:
From `DimCustomer`:
- `CustomerID`
- `CustomerType`
- `City`

From Sales:
- `NetSales`

Confirm fields from both tables work together.

### Task 7 — Filter Test
Add a slicer/filter using:
`DimCustomer[CustomerType]`

Select one customer type and observe whether Sales `NetSales` changes.

Expected flow:
```text
Dimension filter
      ↓
Relationship
      ↓
Sales table
      ↓
NetSales
```

## Part G — Model Quality Checks

### Task 8
Check:
- [ ] CustomerID unique in DimCustomer.
- [ ] CustomerID may repeat in Sales.
- [ ] No unexplained blank key.
- [ ] NetSales numeric.
- [ ] Quantity numeric.
- [ ] Relationship uses CustomerID.
- [ ] Cardinality 1:*.
- [ ] Cross filter Single.
- [ ] Relationship Active.

## 🧠 Knowledge Check
Answer in your own words:
1. What is a Power BI data model?
2. What is a fact table?
3. What is a dimension table?
4. What is a primary key?
5. What is a foreign key?
6. Why is CustomerID unique in the customer table but repeated in Sales?
7. Why is the relationship 1:*?
8. What does Single cross-filter direction mean?
9. Why should unnecessary bidirectional relationships be avoided?
10. What happens when a dimension filter reaches a fact table?
11. Why is a clean model better than putting everything into one table?

## 📸 Screenshot Checklist
- [ ] `01-model-tables.png` — Model view with tables.
- [ ] `02-create-relationship.png` — Relationship dialog.
- [ ] `03-model-view.png` — Final relationship diagram.
- [ ] `04-relationship-properties.png` — Cardinality/direction/active status.
- [ ] `05-validation-visual.png` — Visual using both tables.

## ✅ Completion Checklist

- [x] Sales table identified.
- [x] DimCustomer prepared.
- [x] CustomerID uniqueness checked.
- [x] Primary/foreign keys identified.
- [x] 1:* relationship created.
- [x] Single direction selected.
- [x] Relationship active.
- [x] Validation visual created.
- [x] Filter test completed.
- [x] Knowledge check answered.
- [x] Five screenshots saved.
- [x] PBIX saved as `Day13_Data_Modeling_Relationships.pbix`.

## 📦 Folder
```text
Power BI/
└── Day-13-Data-Modeling-Relationships/
    ├── README.md
    ├── TASK.md
    ├── Day13_Data_Modeling_Relationships.pbix
    └── Screenshots/
```

## Next
After completion, share your screenshots and answers for review.

**Day 14 → Star Schema & Dimension Tables**
