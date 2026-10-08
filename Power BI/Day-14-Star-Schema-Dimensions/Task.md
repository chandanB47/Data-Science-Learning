# Power BI — Day 14 TASK: Star Schema & Dimension Tables

**Level:** Beginner → Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Transform your Day 13 relationship model into a basic **star schema** with a central sales fact-style table and supporting dimensions.

## Part A — Start from Day 13
### Task 1
1. Open `Day13_Data_Modeling_Relationships.pbix`.
2. Save a copy as `Day14_Star_Schema_Dimensions.pbix`.
3. Open **Model view**.
4. Identify the sales and customer tables.
5. Do not delete your Power Query work.

## Part B — Identify FactSales
### Task 2
Identify the detailed sales table containing fields such as:
- `OrderID`
- `OrderDate`
- `CustomerID`
- `Product`
- `Quantity`
- `NetSales`

Treat it as your central fact-style table. If appropriate, rename it clearly to `FactSales`; only rename if it will not disrupt your workflow.

## Part C — Verify DimCustomer
### Task 3
Use your Day 13 customer table. It should contain fields such as `CustomerID`, `CustomerType`, and `City`.

Check that `CustomerID` is unique. If necessary, open **Transform data**, reference the customer query, keep the relevant fields, remove duplicate `CustomerID` values, and rename it `DimCustomer`.

Relationship:
```text
DimCustomer[CustomerID]  1 ───── * FactSales[CustomerID]
```

## Part D — Create DimProduct
### Task 4
If you do not already have a product table:
1. Open **Transform data**.
2. Reference the detailed sales query.
3. Rename the query `DimProduct`.
4. Keep product-related fields such as `Product` and `Category`.
5. Remove duplicate product records.
6. If there is no ProductID, use the existing `Product` field as the learning key.

Check that Product is unique in DimProduct.

### Task 5 — Product relationship
In Model view connect:
```text
DimProduct[Product]  1 ───── * FactSales[Product]
```
Set **Cardinality = One to many (1:*)**, **Cross filter = Single**, **Active = Yes**.

## Part E — Create DimDate
### Task 6
1. Select **Modeling → New table**.
2. Create a date table covering your sales OrderDate range:

```DAX
DimDate =
CALENDAR(
    MIN(FactSales[OrderDate]),
    MAX(FactSales[OrderDate])
)
```

If your fact table has a different name, use that name. Ensure `OrderDate` is a proper Date type.

### Task 7 — Add calendar columns
Create:
```DAX
Year = YEAR(DimDate[Date])
```
```DAX
Month Number = MONTH(DimDate[Date])
```
```DAX
Month Name = FORMAT(DimDate[Date], "MMMM")
```
```DAX
Quarter = "Q" & FORMAT(DimDate[Date], "Q")
```

These will be useful in later DAX lessons.

## Part F — Date Relationship
### Task 8
Connect:
```text
DimDate[Date]  1 ───── * FactSales[OrderDate]
```
Set **1:***, **Single**, **Active**.

Your model should now resemble:
```text
                  DimCustomer
                       |
                       |
DimProduct ─────── FactSales ─────── DimDate
```

## Part G — Clean the Model Layout
### Task 9
In Model view:
1. Place FactSales in the center.
2. Place dimensions around it.
3. Keep relationship lines readable.
4. Avoid unnecessary crossing lines.

## Part H — Validate Relationships
### Task 10
Verify:
- Customer: `DimCustomer 1 → * FactSales`
- Product: `DimProduct 1 → * FactSales`
- Date: `DimDate 1 → * FactSales`

For all three:
- Cardinality = `1:*`
- Cross filter = `Single`
- Active = `Yes`

## Part I — Validation Report
### Task 11
Create a simple Table or Matrix visual using:
- `DimCustomer[CustomerType]`
- `DimProduct[Category]`
- `DimDate[Year]`
- `FactSales[NetSales]`

Confirm fields from multiple dimensions work together.

### Task 12 — Filter tests
Test filters from:
1. `DimCustomer[CustomerType]`
2. `DimProduct[Category]`
3. `DimDate[Year]`

Observe whether `NetSales` responds.

Expected flow:
```text
Dimension filter → Relationship → FactSales → NetSales
```

## Part J — Model Quality Review
### Task 13
Check:
- [x] FactSales has transaction-level rows.
- [x] CustomerID is unique in DimCustomer.
- [x] Product is unique in DimProduct.
- [x] DimDate Date is unique.
- [x] DimDate covers the sales date range.
- [x] All relationships are 1:*.
- [x] Dimensions are on the 1 side.
- [x] FactSales is on the * side.
- [x] Cross-filter direction is Single.
- [x] Relationships are active.




## POWER BI — DAY 14 KNOWLEDGE CHECK

### Star Schema & Dimension Tables

1. What is a star schema?

A star schema is a data model where one central fact table is connected to multiple dimension tables. The structure looks like a star because the dimensions surround the central fact table.


2. Why is FactSales in the center?

FactSales contains the transaction-level sales data such as OrderID, CustomerID, Product, OrderDate, Quantity, and NetSales. The dimension tables connect to FactSales and provide information for filtering and analyzing the transactions.


3. What is the purpose of DimCustomer?

DimCustomer stores customer-related descriptive information such as CustomerID, CustomerType, and City. It allows sales to be analyzed and filtered by customer characteristics.


4. What is the purpose of DimProduct?

DimProduct stores product-related information such as Product and Category. It allows sales to be analyzed by product and category.


5. Why should dimension keys be unique?

Dimension keys should be unique because each key must identify one specific record on the one side of the relationship. This allows Power BI to create a correct 1:* relationship.


6. Why can foreign keys repeat in FactSales?

Foreign keys can repeat because FactSales contains transaction-level records. For example, the same customer can make multiple purchases, so the same CustomerID can appear many times in FactSales.


7. Why is DimDate useful?

DimDate provides a consistent calendar for analyzing sales by Year, Month, Quarter, and Date. It also provides the foundation for future time-intelligence calculations.


8. Why use 1:* relationships here?

A 1:* relationship is used because each dimension contains one unique record for a key, while the fact table can contain many transactions using that same key.

Example:

DimProduct                 FactSales

Product A       1 ---- *   Product A
                            Product A
                            Product A


9. What does Single cross-filter direction accomplish?

Single cross-filter direction allows filters to flow from the dimension table to the fact table.

Example:

DimProduct
    |
    v
Relationship
    |
    v
FactSales
    |
    v
NetSales

Selecting a product category therefore filters the related sales transactions.


10. Why is a star schema easier to work with than one huge flat table?

A star schema separates descriptive information from transaction data.

It provides:
- Better organization
- Less unnecessary duplication
- Easier filtering
- Clear relationships
- Easier maintenance
- More predictable analysis


11. What happens if DimProduct contains duplicate Product values?

Duplicate Product values can prevent DimProduct from being a proper one-side table. This can cause relationship and cardinality problems and may result in incorrect or ambiguous filtering behavior.

Therefore, the Product key should be unique in DimProduct.


12. Why should dimensions generally filter the fact table?

Dimensions describe how we want to analyze the transactions. Therefore, filters should generally flow from the dimension to the fact table.

The normal flow is:

Dimension
    |
    v
Relationship
    |
    v
FactSales
    |
    v
Measures / NetSales


DAY 14 SUMMARY

Model created:

DimCustomer  1 ---- *  FactSales  * ---- 1  DimProduct
                           |
                           |
                           *
                           |
                           1
                        DimDate




### Key concepts learned:

- Star Schema
- Fact Table
- Customer Dimension
- Product Dimension
- Date Dimension
- Primary Key
- Foreign Key
- 1:* Relationships
- Single Cross-Filtering
- Dimension-to-Fact Filtering
- Multi-dimension Analysis



## Screenshot Checklist
- [x] `01-fact-dimension-identification.png`
- [x] `02-dimension-tables.png`
- [x] `03-star-schema-model.png`
- [x] `04-relationship-properties.png`
- [x] `05-validation-report.png`

## Completion Checklist
- [x] FactSales identified.
- [x] DimCustomer verified.
- [x] DimProduct created/verified.
- [x] DimDate created.
- [x] Customer, Product, and Date relationships created.
- [x] All relationships 1:* / Single / Active.
- [x] Model arranged as a star.
- [x] Validation report created.
- [x] Filter tests completed.
- [x] Knowledge check answered.
- [x] Screenshots saved.
- [x] PBIX saved as `Day14_Star_Schema_Dimensions.pbix`.

## Folder Structure
```text
Power BI/
└── Day-14-Star-Schema-Dimensions/
    ├── README.md
    ├── TASK.md
    ├── Day14_Star_Schema_Dimensions.pbix
    └── Screenshots/
```

## Next
After completion, share your screenshots and answers for review.

**Day 15 → Date Table & Time Intelligence Foundation**
