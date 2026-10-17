# Power BI — Day 28 TASK: Final Project — Data & Model

**Estimated time:** 90–120 minutes

## Objective
Prepare and validate the data model for your final **Sales Performance Analysis** report.

## Part A — Create your project copy
- [ ] Open your latest Day 27 PBIX.
- [ ] Use **File → Save As**.
- [ ] Save as `Day28_Final_Project_Data_Model.pbix`.
- [ ] Keep the Day 27 file unchanged.

## Part B — Define the business problem
Write a short answer in your notes or a text box:
- [ ] Who will use the report?
- [ ] What business problem will it help solve?
- [ ] List at least four questions the report should answer.

Suggested questions:
1. What is total net sales?
2. Which regions and categories contribute most?
3. What is the monthly sales trend?
4. Which channels perform best?
5. How many unique customers are represented?

## Part C — Validate the data
Open **Home → Transform data**.
- [ ] Confirm `OrderDate` is Date.
- [ ] Confirm `Quantity` is Whole Number.
- [ ] Confirm `NetSales`, `GrossSales`, `DiscountAmount`, and `UnitPrice` are numeric.
- [ ] Confirm `Region`, `Category`, `Product`, and `Channel` are Text.
- [ ] Check for errors and blank key fields.
- [ ] Inspect duplicate `OrderID` values; determine whether they are valid order line items.
- [ ] Select **Close & Apply** if you changed anything.

## Part D — Check the model
In **Model view**:
- [ ] Identify the sales table and any dimension tables.
- [ ] Check the date-table relationship if you created `DimDate`.
- [ ] Confirm the date relationship is active and uses the correct date fields.
- [ ] Avoid adding unnecessary tables or duplicate relationships.
- [ ] Capture a screenshot of Model view.

## Part E — Create or verify measures
Replace `'YourSalesTable'` with your actual table name. Reuse existing measures rather than making duplicates.

```DAX
Total Net Sales = SUM('YourSalesTable'[NetSales])

Total Orders = DISTINCTCOUNT('YourSalesTable'[OrderID])

Unique Customers = DISTINCTCOUNT('YourSalesTable'[CustomerID])

Total Quantity = SUM('YourSalesTable'[Quantity])

Average Net Sales = AVERAGE('YourSalesTable'[NetSales])
```

- [ ] Create or verify all five measures.
- [ ] Format sales measures as currency.
- [ ] Format counts and quantity as whole numbers.
- [ ] Add Card visuals for Total Net Sales, Total Orders, Unique Customers, and Total Quantity.
- [ ] Filter by one Region or Category and confirm the cards respond.
- [ ] Clear the filter and confirm the original totals return.

## Part F — Validate and save
- [ ] Compare Total Net Sales with the source dataset total.
- [ ] Investigate any mismatch before moving on.
- [ ] Save the PBIX.
- [ ] Record the data-quality checks and model decisions.

## Screenshot checklist
- [ ] Model view and relationships
- [ ] Data types or data validation
- [ ] KPI cards
- [ ] Final project scope/business questions

## Completion checklist
- [ ] PBIX saved as `Day28_Final_Project_Data_Model.pbix`
- [ ] Core measures validated
- [ ] No unresolved critical data/model issue
- [ ] README and TASK saved in `Power BI/Day-28-Final-Project-Data-Model/`

## Questions to answer
1. What is the grain of your sales table (what does one row represent)?
2. Why might `OrderID` repeat in a sales dataset?
3. What relationship connects your date table to the sales table?
4. Which check helped you trust the Total Net Sales measure?

**Stop here when complete.** Day 29 will use this validated model to build the final dashboard and communicate insights.
