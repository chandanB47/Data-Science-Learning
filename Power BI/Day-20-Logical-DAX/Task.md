# Power BI — Day 20 TASK: Logical DAX

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Create business-logic measures using `IF`, `SWITCH`, `AND`, and `OR`.

## Part A — Open and save
1. Open `Day19_CALCULATE_Filter_Context.pbix`.
2. Choose **File → Save As**.
3. Save a new copy as `Day20_Logical_DAX.pbix`.
4. Confirm the existing model and relationships remain intact.
5. Confirm your actual fact table and net sales column names. Examples use `FactSales[NetSales]`.

## Part B — Create a base measure
If it does not already exist, create:

```DAX
Total Net Sales =
    SUM(FactSales[NetSales])
```

Use your actual table name if it differs.

## Part C — Create an IF measure
Create a measure that labels the currently selected sales total as High or Low using 5,000 as the practice threshold:

```DAX
Sales Level =
    IF(
        [Total Net Sales] >= 5000,
        "High",
        "Low"
    )
```

1. Add a Card visual with `[Sales Level]`.
2. Observe the label with no slicers selected.
3. Use a slicer and observe whether the label changes as the total changes.
4. This is a measure-level classification of the current total, not a label stored on every sales row.

## Part D — Create a SWITCH measure
Create a measure that categorizes the current total sales into three practice tiers:

```DAX
Sales Tier =
    SWITCH(
        TRUE(),
        [Total Net Sales] >= 10000, "Platinum",
        [Total Net Sales] >= 5000, "Gold",
        "Standard"
    )
```

1. Add `[Sales Tier]` to a Card.
2. Test it with filters.
3. Conditions are evaluated in order, so check the highest threshold first.

## Part E — Create an AND measure
Create a measure that flags when the current sales total is at least 5,000 and average net sales is at least 500:

```DAX
High Value Condition =
    IF(
        AND(
            [Total Net Sales] >= 5000,
            [Average Net Sales] >= 500
        ),
        "Meets Both",
        "Does Not Meet Both"
    )
```

If `[Average Net Sales]` does not exist, create it:

```DAX
Average Net Sales =
    AVERAGE(FactSales[NetSales])
```

Add `[High Value Condition]` to a Card and test it under different filters.

## Part F — Create an OR measure
Create a measure that flags when either total sales are at least 10,000 or average net sales is at least 1,000:

```DAX
High Value Alert =
    IF(
        OR(
            [Total Net Sales] >= 10000,
            [Average Net Sales] >= 1000
        ),
        "Alert",
        "No Alert"
    )
```

Add `[High Value Alert]` to a Card. These thresholds are practice values, not universal business standards.

## Part G — Test filter context
1. Add a Card for `[Total Net Sales]`.
2. Add Cards for `[Sales Level]`, `[Sales Tier]`, `[High Value Condition]`, and `[High Value Alert]`.
3. Add a slicer using `DimCustomer[CustomerType]`, if available and related.
4. Change the slicer selection and observe whether logical labels change.
5. If a label does not change, check the underlying measure and relationships before changing formulas.

## Part H — Validate
- [x] No DAX errors.
- [x] `Sales Level` uses `IF`.
- [x] `Sales Tier` uses `SWITCH(TRUE(), ...)` and checks thresholds in descending order.
- [x] `High Value Condition` requires both conditions through `AND`.
- [x] `High Value Alert` is true when either condition is met through `OR`.
- [x] Cards respond to relevant filter selections.
- [x] Existing relationships remain unchanged.
- [x] Save the PBIX file.



**GitHub folder:** `Power BI/Day-20-Logical-DAX/`
