# Power BI — Day 18 TASK: Basic DAX Functions

**Level:** Beginner to Intermediate  
**Estimated time:** 75–120 minutes

## Goal
Create and test measures using `SUM`, `AVERAGE`, `COUNT`, `COUNTA`, and `DISTINCTCOUNT`.

## Part A — Open and save your file
1. Open `Day17_Measures_vs_Calculated_Columns.pbix`.
2. Choose **File → Save As**.
3. Save a new copy as `Day18_Basic_DAX_Functions.pbix`.
4. Confirm the existing model and relationships remain present.
5. Identify your actual fact table and the columns equivalent to `NetSales`, `Quantity`, `OrderID`, and `CustomerID`.
6. The examples use `FactSales`; replace it with your actual table name if needed.

## Part B — Create a SUM measure
1. Select your fact table and choose **New measure**.
2. Enter:

```DAX
Total Net Sales = SUM(FactSales[NetSales])
```

3. Press Enter and set a suitable currency or numeric format.
4. Add a **Card** visual with `[Total Net Sales]`.
5. Record the value with no slicers selected.

## Part C — Create an AVERAGE measure
Create this measure:

```DAX
Average Net Sales = AVERAGE(FactSales[NetSales])
```

Add a second Card with `[Average Net Sales]`. Compare the average with the total.

## Part D — Create a COUNT measure
Create:

```DAX
Order ID Count = COUNT(FactSales[OrderID])
```

`COUNT` is suitable for supported numeric/date-style columns, not text IDs. If `OrderID` is stored as text, use a numeric/date column for this COUNT demonstration or record the data-type limitation and proceed to COUNTA.

## Part E — Create a COUNTA measure
Create:

```DAX
Nonblank Order IDs = COUNTA(FactSales[OrderID])
```

Add a Card. `COUNTA` counts nonblank values, including text. If `OrderID` is text, this is more suitable than `COUNT` for counting populated IDs.

## Part F — Create a DISTINCTCOUNT measure
Create:

```DAX
Unique Customers = DISTINCTCOUNT(FactSales[CustomerID])
```

Add a Card. This counts distinct customer IDs in the current filter context; it is not the same as counting sales rows.

## Part G — Build a visual and test slicers
1. Add a **clustered bar chart**.
2. Use `DimProduct[Category]` for the axis and `[Total Net Sales]` for values. If your model uses a different related category field, use that instead.
3. Add a slicer using `DimCustomer[CustomerType]`.
4. Select one customer type and observe the Cards and category chart.
5. Change or clear the slicer and confirm results update as expected.
6. If results do not change, inspect the existing relationship between the dimension and fact table. Do not create an arbitrary many-to-many relationship.

## Part H — Validate
- [x] `Total Net Sales` uses `SUM`.
- [x] `Average Net Sales` uses `AVERAGE`.
- [x] `Order ID Count` uses `COUNT` only if the column's data type supports it.
- [x] `Nonblank Order IDs` uses `COUNTA`.
- [x] `Unique Customers` uses `DISTINCTCOUNT`.
- [x] No formula errors.
- [x] Cards display values with no filters selected.
- [x] The Customer Type slicer changes results when the model relationship supports that filter path.
- [x] Existing relationships remain unchanged.
- [x] Save the PBIX file.

## Screenshot checklist
Save screenshots in the `Screenshots/` folder:

- [x] `01-total-and-average-measures.png` — Total Net Sales and Average Net Sales Cards.
- [x] `02-count-and-counta.png` — COUNT and COUNTA measures/results, with any data-type limitation noted.
- [x] `03-distinctcount-customers.png` — Unique Customers measure and Card.
- [x] `04-sales-by-category.png` — Category chart using Total Net Sales.
- [x] `05-slicer-filter-test.png` — Customer Type slicer selected and updated results.
- [x] `06-measures-list.png` — All Day 18 measures visible in the Fields/Data pane.

## Knowledge check
Answer in your own words:
1. What does `SUM` return?
2. How is `AVERAGE` different from `SUM`?
3. What is the difference between `COUNT` and `COUNTA`?
4. Why use `DISTINCTCOUNT` for CustomerID instead of counting every row?
5. Why can a measure return a different result after selecting a slicer?

## Completion checklist
- [x] Saved `Day18_Basic_DAX_Functions.pbix`.
- [x] Created and tested the measures.
- [x] Captured the screenshots.
- [x] Answered the knowledge-check questions.


**GitHub folder:** `Power BI/Day-18-Basic-DAX-Functions/`
