# Power BI — Day 17: Measures vs. Calculated Columns

## Overview
**Level:** Beginner to Intermediate  
**Phase:** Level 4 — DAX  
**Estimated time:** 75–120 minutes

## Goal
Understand the difference between a DAX measure and a calculated column, know when to use each, create basic measures, and observe how report filters affect measure results.

## Prerequisites
- Complete Day 16: Advanced Modeling, Filter Context & Model Validation.
- Open your Day 16 PBIX file.
- Confirm the model contains `FactSales`, `DimCustomer`, `DimProduct`, and `DimDate` (or the equivalent tables you established).
- Confirm the relationships are active and working.

## Topics
- What is a measure?
- What is a calculated column?
- When to use each
- Create basic measures
- Understand evaluation context

## Deliverables
- Updated PBIX file: `Day17_Measures_vs_Calculated_Columns.pbix`
- Basic measures created and named clearly
- A small report page demonstrating a measure responding to filters
- Screenshots listed in `TASK.md`

## Folder structure
```text
Power BI/
└── Day-17-Measures-vs-Calculated-Columns/
    ├── README.md
    ├── TASK.md
    ├── Day17_Measures_vs_Calculated_Columns.pbix
    └── Screenshots/
```

## Key idea
- **Calculated column:** calculated for each row when the model is refreshed; the resulting values are stored in the model.
- **Measure:** evaluated when a visual requests a result, using the current filter context. Its result can change when slicers, filters, or visual groupings change.

## Important
Keep your existing model and relationships. Do not rebuild the model or start time-intelligence calculations today. Complete the tasks in order and share screenshots for review before moving to Day 18.
