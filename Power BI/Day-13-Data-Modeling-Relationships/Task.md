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
- [x] CustomerID unique in DimCustomer.
- [x] CustomerID may repeat in Sales.
- [x] No unexplained blank key.
- [x] NetSales numeric.
- [x] Quantity numeric.
- [x] Relationship uses CustomerID.
- [x] Cardinality 1:*.
- [x] Cross filter Single.
- [x] Relationship Active.



## 🧠 Day 13 — Knowledge Check Answers

What is a Power BI data model?
A Power BI data model is the structure that organizes tables and defines relationships between them so the data can be analyzed correctly.

What is a fact table?
A fact table contains transaction or business-event data, usually including numeric values that can be analyzed. In this project, Sales_Appended is the fact-style sales table.

What is a dimension table?
A dimension table contains descriptive information used to filter, categorize, and analyze data. In this project, DimCustomer contains CustomerID, CustomerType, and City.

What is a primary key?
A primary key is a column that uniquely identifies each record in a table. Here, DimCustomer[CustomerID] is the primary key.

What is a foreign key?
A foreign key is a column that references a key in another table and is used to establish a relationship. Here, Sales_Appended[CustomerID] is the foreign key.

Why is CustomerID unique in the customer table but repeated in Sales?
DimCustomer stores each customer only once, so CustomerID must be unique. Sales_Appended contains transactions, so one customer can have multiple transactions and therefore the same CustomerID can appear multiple times.

Why is the relationship 1:*?
The relationship is one-to-many because one customer exists once in DimCustomer, while that customer can have many sales transactions in Sales_Appended.

What does Single cross-filter direction mean?
Single cross-filter direction means filters flow from the one-side dimension table to the many-side sales table.

Why should unnecessary bidirectional relationships be avoided?
Bidirectional relationships can make the model more complicated and may create ambiguous or unexpected filtering behavior. Single direction is preferred when it is sufficient.

What happens when a dimension filter reaches a fact table?
The filter travels through the relationship and restricts the related rows in the fact table. For example, selecting a CustomerType in DimCustomer filters the corresponding sales in Sales_Appended.

Why is a clean model better than putting everything into one table?
A clean model separates transaction data from descriptive dimension data and connects them through relationships. This improves organization, reduces redundancy, makes filtering easier, and provides a better foundation for a star schema.

## 📸 Screenshot Checklist
- [x] `01-model-tables.png` — Model view with tables.
- [x] `02-create-relationship.png` — Relationship dialog.
- [x] `03-model-view.png` — Final relationship diagram.
- [x] `04-relationship-properties.png` — Cardinality/direction/active status.
- [x] `05-validation-visual.png` — Visual using both tables.

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
