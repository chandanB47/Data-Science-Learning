# Power BI — Day 13: Introduction to Data Modeling & Relationships

## Overview
Day 13 begins the **Data Modeling** phase. You will learn fact and dimension tables, primary and foreign keys, one-to-many relationships, and basic filter direction.

**Level:** Beginner → Intermediate  
**Estimated time:** 60–90 minutes

## Objectives
- Understand a Power BI data model.
- Identify fact-style and dimension tables.
- Identify primary and foreign keys.
- Create a 1:* relationship.
- Understand Single cross-filter direction.
- Validate a relationship with a report visual.

## Core Concepts

### Fact Table
A transaction-level table containing business events and measurable values.

Typical sales fields:
`OrderID`, `OrderDate`, `CustomerID`, `Quantity`, `NetSales`.

### Dimension Table
A descriptive table used to analyze facts, such as Customer, Product, Date, or Region.

### Keys
**Primary key:** uniquely identifies a row in a dimension table.

**Foreign key:** references the dimension key from a fact table.

Example:
```text
DimCustomer[CustomerID]  1 ───── *  Sales[CustomerID]
```

One customer can have many sales.

### Star Schema
```text
             Customer
                 |
Product ───── Sales ───── Date
                 |
               Region
```

The sales fact sits in the center and dimensions surround it.

## Practical Setup
Use your Day 11 customer lookup if available. You should have a customer table containing `CustomerID`, `CustomerType`, and `City`, plus your detailed sales table containing `CustomerID` and `NetSales`.

If necessary, recreate a clean customer lookup from the detailed sales query by referencing it and removing duplicate `CustomerID` values.

## Deliverables
1. Clean customer dimension.
2. Detailed sales fact-style table.
3. `CustomerID` relationship.
4. Correct 1:* cardinality and Single direction.
5. Model diagram.
6. Validation visual.
7. Screenshots.
8. `Day13_Data_Modeling_Relationships.pbix`.

## GitHub Structure
```text
Power BI/
└── Day-13-Data-Modeling-Relationships/
    ├── README.md
    ├── TASK.md
    ├── Day13_Data_Modeling_Relationships.pbix
    └── Screenshots/
```

## Completion Criteria
- CustomerID is unique in the customer dimension.
- CustomerID can repeat in Sales.
- 1:* relationship is active.
- Cross-filter direction is Single.
- A report visual successfully uses fields from both tables.
- Screenshots and PBIX are saved.

## Next
**Day 14 — Star Schema & Dimension Tables**
