# Power BI — Day 14: Star Schema & Dimension Tables

## Overview
Day 14 develops the Day 13 data model into a basic **star schema**. You will identify a central sales fact table and create supporting Customer, Product, and Date dimensions.

**Level:** Beginner → Intermediate  
**Estimated time:** 75–120 minutes

## Objectives
- Explain a star schema.
- Identify fact and dimension tables.
- Prepare Customer and Product dimensions.
- Create a basic Date dimension.
- Create 1:* dimension-to-fact relationships.
- Use Single cross-filter direction.
- Validate the model with a report visual.

## Core Concept
A star schema places the fact table in the center:

```text
                 DimCustomer
                      |
                      |
DimProduct ───── FactSales ───── DimDate
```

The fact table contains transaction-level business events and numeric values. Dimensions contain descriptive attributes used for filtering and grouping.

### FactSales
Typical fields:
`OrderID`, `OrderDate`, `CustomerID`, `Product`, `Quantity`, `NetSales`.

### Dimensions
- `DimCustomer` — customer attributes.
- `DimProduct` — product/category attributes.
- `DimDate` — dates and calendar attributes.

### Modeling Rules
- Dimension keys should be unique.
- Fact foreign keys can repeat.
- Prefer `Dimension 1 → * Fact` for this model.
- Keep cross-filter direction **Single**.
- Avoid unnecessary bidirectional relationships.
- Do not create relationships merely because column names happen to match.

## Deliverables
1. FactSales identified.
2. DimCustomer verified.
3. DimProduct created/verified.
4. DimDate created.
5. Three correct 1:* relationships.
6. Clean star-shaped Model view.
7. Validation report page.
8. Five screenshots.
9. `Day14_Star_Schema_Dimensions.pbix`.

## GitHub Structure
```text
Power BI/
└── Day-14-Star-Schema-Dimensions/
    ├── README.md
    ├── TASK.md
    ├── Day14_Star_Schema_Dimensions.pbix
    └── Screenshots/
```

## Completion Criteria
Fact and dimension roles are understood; dimension keys are unique; relationships are 1:* from dimensions to FactSales; cross-filter direction is Single; the model resembles a star; and the validation report works.

## Next
**Day 15 — Date Table & Time Intelligence Foundation**
