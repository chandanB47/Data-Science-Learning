# Power BI — Day 19 TASK: CALCULATE & Filter Context

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Create measures using `CALCULATE`, understand filter context, and observe how the same base measure returns different results under different filters.

## Part A — Open and save
1. Open `Day18_Basic_DAX_Functions.pbix`.
2. Choose **File → Save As**.
3. Save as `Day19_CALCULATE_Filter_Context.pbix`.
4. Confirm the existing model and relationships remain present.
5. Check your actual fact table and category field names. Examples use `FactSales[NetSales]` and `DimProduct[Category]`.

## Part B — Confirm the base measure
Create this only if it does not already exist:

```DAX
Total Net Sales =
    SUM(FactSales[NetSales])
```

Add it to a Card and record the value with no slicers selected.

## Part C — Create a CALCULATE measure for one category
1. Find a category value that actually exists in your data.
2. Create the following measure, replacing `Technology` with an exact category value if necessary:

```DAX
Technology Sales =
    CALCULATE(
        [Total Net Sales],
        DimProduct[Category] = "Technology"
    )
```

3. Add the measure to a Card.
4. If the measure is blank or unexpected, verify the category spelling and the relationship from `DimProduct` to `FactSales`.

## Part D — Create a second filtered measure
Choose a second category that exists in your data and replace the example value:

```DAX
Second Category Sales =
    CALCULATE(
        [Total Net Sales],
        DimProduct[Category] = "Office Supplies"
    )
```

Add this measure to a Card. Do not leave `Office Supplies` in the formula if it is not an actual category in your dataset.

## Part E — Observe filter context in a visual
1. Add a clustered bar chart.
2. Put `DimProduct[Category]` on the axis and `[Total Net Sales]` in Values.
3. Compare sales across categories. Each category bar provides a different filter context.
4. Add a slicer using `DimCustomer[CustomerType]`.
5. Select a customer type and observe how the total and category values change.
6. Clear the slicer and check that the visuals return to their unfiltered state.

## Part F — Compare results
1. Add Cards for `[Total Net Sales]`, `[Technology Sales]`, and `[Second Category Sales]`.
2. Compare category-specific sales with the overall total.
3. The category measures explicitly apply a category filter inside `CALCULATE`; the base measure responds to the current visual and slicer filters.
4. Note unexpected interactions. A filter applied by `CALCULATE` to a column can replace an existing filter on that same column unless the expression is designed to preserve it.

## Part G — Validate
- [ ] No DAX errors.
- [ ] `[Total Net Sales]` works without filters.
- [ ] Both category measures use values that exist in the data.
- [ ] The category chart displays values by category.
- [ ] Customer Type slicer affects results where relationships allow it.
- [ ] Existing relationships remain active and unchanged.
- [ ] Save the PBIX file.

## Screenshot checklist
Save screenshots in `Screenshots/`:

- [ ] `01-base-total-sales.png` — Card showing Total Net Sales.
- [ ] `02-calculate-category-measure.png` — Formula bar for the first `CALCULATE` measure.
- [ ] `03-category-measures-cards.png` — Cards comparing overall and category-specific sales.
- [ ] `04-sales-by-category.png` — Bar chart of Total Net Sales by category.
- [ ] `05-filter-context-slicer.png` — Customer Type slicer selected and updated visual values.

## Knowledge check
Answer in your own words:
1. What does `CALCULATE` do?
2. What is filter context?
3. Why can `[Total Net Sales]` show different values for different category bars?
4. How is a category-specific `CALCULATE` measure different from the base sales measure?
5. What should you check if a filtered measure returns blank?

## Completion checklist
- [ ] Saved `Day19_CALCULATE_Filter_Context.pbix`.
- [ ] Created and tested the measures.
- [ ] Captured the screenshots.
- [ ] Answered the knowledge-check questions.
- [ ] Shared screenshots here for review before starting Day 20.

**GitHub folder:** `Power BI/Day-19-CALCULATE-Filter-Context/`
