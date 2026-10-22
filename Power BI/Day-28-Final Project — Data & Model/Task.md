# Power BI — Day 28 TASK: Final Project — Data & Model

**Estimated time:** 90–120 minutes

## Objective
Prepare and validate the data model for your final **Sales Performance Analysis** report.

## Part A — Create your project copy
- [x] Open your latest Day 27 PBIX.
- [x] Use **File → Save As**.
- [x] Save as `Day28_Final_Project_Data_Model.pbix`.
- [x] Keep the Day 27 file unchanged.

## Part B — Define the business problem

Write a short answer in your notes or a text box:
- [x] Who will use the report?
- [x] What business problem will it help solve?
- [x] List at least four questions the report should answer.

Suggested questions:
1. What is total net sales?
2. Which regions and categories contribute most?
3. What is the monthly sales trend?
4. Which channels perform best?
5. How many unique customers are represented?

## Part C — Validate the data
Open **Home → Transform data**.
- [x] Confirm `OrderDate` is Date.
- [x] Confirm `Quantity` is Whole Number.
- [x] Confirm `NetSales`, `GrossSales`, `DiscountAmount`, and `UnitPrice` are numeric.
- [x] Confirm `Region`, `Category`, `Product`, and `Channel` are Text.
- [x] Check for errors and blank key fields.
- [x] Inspect duplicate `OrderID` values; determine whether they are valid order line items.
- [x] Select **Close & Apply** if you changed anything.

## Part D — Check the model
In **Model view**:
- [x] Identify the sales table and any dimension tables.
- [x] Check the date-table relationship if you created `DimDate`.
- [x] Confirm the date relationship is active and uses the correct date fields.
- [x] Avoid adding unnecessary tables or duplicate relationships.
- [x] Capture a screenshot of Model view.

## Part E — Create or verify measures
Replace `'YourSalesTable'` with your actual table name. Reuse existing measures rather than making duplicates.

```DAX
Total Net Sales = SUM('YourSalesTable'[NetSales])

Total Orders = DISTINCTCOUNT('YourSalesTable'[OrderID])

Unique Customers = DISTINCTCOUNT('YourSalesTable'[CustomerID])

Total Quantity = SUM('YourSalesTable'[Quantity])

Average Net Sales = AVERAGE('YourSalesTable'[NetSales])
```

- [x] Create or verify all five measures.
- [x] Format sales measures as currency.
- [x] Format counts and quantity as whole numbers.
- [x] Add Card visuals for Total Net Sales, Total Orders, Unique Customers, and Total Quantity.
- [x] Filter by one Region or Category and confirm the cards respond.
- [x] Clear the filter and confirm the original totals return.

## Part F — Validate and save
- [x] Compare Total Net Sales with the source dataset total.
- [x] Investigate any mismatch before moving on.
- [x] Save the PBIX.
- [x] Record the data-quality checks and model decisions.

      
## Screenshot checklist
- [x] Model view and relationships
- [x] Data types or data validation
- [x] KPI cards
- [x] Final project scope/business questions

## Completion checklist
- [x] PBIX saved as `Day28_Final_Project_Data_Model.pbix`
- [x] Core measures validated
- [x] No unresolved critical data/model issue
- [x] README and TASK saved in `Power BI/Day-28-Final-Project-Data-Model/`


## Questions to answer

### 1. What is the grain of your sales table?

The grain of Fact_Sales is one row per sales record. In our dataset, no repeated OrderID values were found, so each row appears to represent one unique order.

### 2. Why might OrderID repeat in a sales dataset?

An OrderID may repeat when a single order contains multiple products or line items. Each row represents a different item within the same order, so several rows can share the same order ID.

### 3. What relationship connects your date table to the sales table?

The relationship is:

DimDate[Date] → Fact_Sales[OrderDate]
- Cardinality: One-to-many (1:*)
- Relationship status: Active
- Filter direction: Single direction, from DimDate to Fact_Sales
This relationship enables date-based analysis, such as monthly sales and year-to-date calculations.


### 4. Which check helped you trust the Total Net Sales measure?

The most important check was comparing the Power BI Total Net Sales result with the sum of the NetSales column in the original CSV file. Both totals matched.

Additional checks strengthened confidence in the result:
- Verified the NetSales column's data type.
- Checked for missing values and Power Query errors.
- Confirmed the data model relationships.
- Tested that KPI cards responded to the Region slicer.

**Stop here when complete.** Day 29 will use this validated model to build the final dashboard and communicate insights.
