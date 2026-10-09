# Power BI — Day 17 TASK: Measures vs. Calculated Columns

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Create and compare one calculated column and basic measures, then test how a measure responds to report filters.

## Part A — Open and check your model
1. Open `Day16_Advanced_Modeling_Validation.pbix`.
2. Use **File → Save As** and save a new copy as `Day17_Measures_vs_Calculated_Columns.pbix`.
3. Open **Model view** and confirm the existing customer, product, and date relationships are active.
4. Confirm `FactSales` contains `Quantity`, `UnitPrice`, and `NetSales`. If your fact table has a different name, use that actual table name in the formulas below.
5. If your model uses different names, adapt the table/column references carefully; do not create duplicate tables just to match the example.

## Part B — Understand the difference
Write a short note in your own words in your notes:

- **Calculated column:** produces a value for each row and stores it in the model after calculation/refresh.
- **Measure:** calculates a result when needed by a visual, based on the current filter context.
- **Use a column** when you need a row-level value or a field to group/filter by.
- **Use a measure** for totals, averages, counts, and other dynamic summaries.

## Part C — Create a calculated column
1. Select the `FactSales` table in Data view or Model view.
2. Choose **New column**.
3. Enter this DAX formula:

```DAX
Calculated Sales = FactSales[Quantity] * FactSales[UnitPrice]
```

4. Press Enter.
5. Confirm that the new column contains a row-level value for each sales record.
6. Set its data type to Decimal number or Fixed decimal number, as appropriate.
7. Keep the name `Calculated Sales` for this task.

**Note:** This column is a practice example of a row-level calculation. It does not automatically replace your existing `NetSales` business definition, which may account for discounts or other rules.

## Part D — Create your first measures
1. Select the `FactSales` table.
2. Choose **New measure**.
3. Create these measures one at a time:

```DAX
Total Net Sales = SUM(FactSales[NetSales])
```

```DAX
Average Net Sales = AVERAGE(FactSales[NetSales])
```

```DAX
Total Quantity = SUM(FactSales[Quantity])
```

4. If your Power BI installation uses semicolons or different locale conventions, follow the syntax accepted by your installation.
5. Format `Total Net Sales` as currency or a suitable number format for your dataset.
6. Format `Average Net Sales` consistently.
7. Confirm the calculator icon appears beside measures in the Fields/Data pane, and the calculated column has a column icon.

## Part E — Compare column and measure behavior
1. Go to Report view and add a **Table** visual.
2. Add `FactSales[OrderID]`, `FactSales[NetSales]`, `FactSales[Calculated Sales]`, and the `[Total Net Sales]` measure.
3. Observe the row-level values and how the measure is evaluated in the visual context.
4. Add a **Card** visual and place `[Total Net Sales]` on it.
5. Add another Card with `[Total Quantity]`.
6. Add a **bar chart** with `DimProduct[Category]` on the axis and `[Total Net Sales]` as the value. If your model uses a different category table/field, use the related dimension field.

## Part F — Test evaluation/filter context
1. Add a slicer using `DimCustomer[CustomerType]`.
2. Select one customer type and observe the `[Total Net Sales]` Card and category bar chart.
3. Change the slicer selection. Check whether the measure result changes.
4. Clear the slicer selection and confirm the total returns to the unfiltered result.
5. If the measure does not respond, inspect the relationship between `DimCustomer` and `FactSales`; do not fix it by creating an arbitrary many-to-many relationship.

## Part G — Validate
- [x] No DAX formula errors.
- [x] `Calculated Sales` is a column, not a measure.
- [x] `Total Net Sales`, `Average Net Sales`, and `Total Quantity` are measures.
- [x] The Card total agrees with the expected total when no slicers are applied.
- [x] Customer Type slicer changes the measure when applicable.
- [x] Existing relationships remain active and unchanged.
- [x] Save the PBIX file.

## Screenshot checklist
Save screenshots in the `Screenshots/` folder:

- [x] `01-model-relationships.png` — Model view showing the existing relationships.
- [x] `02-calculated-column.png` — `Calculated Sales` formula and column result.
- [x] `03-basic-measures.png` — measures visible in the Fields/Data pane or formula bar.
- [x] `04-report-measure-card.png` — Card with Total Net Sales and Total Quantity.
- [x] `05-measure-by-category.png` — category chart using Total Net Sales.
- [x] `06-filter-context-test.png` — Customer Type slicer selected and changed measure result.


## Knowledge check
Answer these in your own words:

1. What is the main difference between a measure and a calculated column?
2. Why is `Total Net Sales` usually better as a measure than as a calculated column?
3. What does filter context mean in the example you tested?
4. Why should `Calculated Sales` not automatically be treated as the official net-sales value?

## Completion checklist
- [x] Saved `Day17_Measures_vs_Calculated_Columns.pbix`.
- [x] Completed all tasks.
- [x] Captured the screenshots.
- [x] Answered the knowledge-check questions.


**GitHub folder:** `Power BI/Day-17-Measures-vs-Calculated-Columns/`
