# Power BI — Day 28: Final Project — Data & Model

**Level:** Beginner to Intermediate  
**Estimated time:** 90–120 minutes  
**Phase:** Final Project (Day 28 of 30)

## Goal
Start a portfolio-ready **Sales Performance Analysis** project by preparing the dataset, validating the data model, and creating the core measures. Reuse the sales dataset from your earlier lessons so you can focus on building a reliable model.

## Project business problem
A retail business wants to understand sales performance across time, regions, product categories, sales channels, and customers.

### Questions this report should answer
1. What is total net sales?
2. How do net sales change month by month?
3. Which regions and categories contribute most to net sales?
4. Which sales channels perform best?
5. How many unique customers placed orders?
6. How do results change when a user filters by date, region, category, or channel?

## Files and starting point
- Main dataset: `PowerBI_Master_Sales_Dataset_1500.csv` (1,500 rows).
- Starting PBIX: your latest working report from Day 27.
- Save the new project as: `Day28_Final_Project_Data_Model.pbix`.

> Use the actual table name in your Power BI model. If your table is not named `FactSales`, do not rename it just to match this guide.

## Step-by-step workflow

### 1. Create a separate final-project copy
1. Open your latest Day 27 PBIX.
2. Select **File → Save As**.
3. Save it as `Day28_Final_Project_Data_Model.pbix`.
4. Keep your Day 27 file unchanged.

### 2. Confirm the business goal and report scope
Create a report page named `Final Project — Sales Overview` (you will build the final dashboard on Day 29). Add a text box with the business problem and the six questions above, or record them in your project notes.

### 3. Inspect and validate the data
Open **Home → Transform data** and verify:
- `OrderDate` has the Date data type.
- `Quantity` is a whole number.
- `UnitPrice`, `GrossSales`, `DiscountAmount`, and `NetSales` are numeric/currency fields as appropriate.
- `DiscountPct` uses a consistent numeric format.
- Text fields such as `Region`, `Category`, `Product`, `Channel`, and `CustomerType` are text.
- Check for errors, blank key fields, and duplicate order identifiers. Do not delete rows without understanding what they represent.
- Check whether `OrderID` is unique per row. If one order can have multiple line items, repeated order IDs may be valid.

Select **Close & Apply** after any required corrections.

### 4. Review the model
Open **Model view** and check the tables and relationships.
- Confirm that the sales table is connected to the date table if you already created one.
- If a separate date table exists, confirm the relationship is `DimDate[Date]` (one) to your sales table's `OrderDate` (many), using the actual column names in your model.
- Ensure the relationship is active and the date table covers the sales dates.
- Avoid creating duplicate relationships or unnecessary tables.
- If your project currently uses one clean sales table, document that as the current model rather than adding tables without a clear purpose.

### 5. Create or verify core measures
Create these measures in your sales table or a dedicated measures table. Replace `[YourSalesTable]` with the actual table name.

```DAX
Total Net Sales = SUM('YourSalesTable'[NetSales])

Total Orders = DISTINCTCOUNT('YourSalesTable'[OrderID])

Unique Customers = DISTINCTCOUNT('YourSalesTable'[CustomerID])

Total Quantity = SUM('YourSalesTable'[Quantity])

Average Net Sales = AVERAGE('YourSalesTable'[NetSales])
```

If you already created measures with these meanings, reuse them instead of creating duplicates. Format `Total Net Sales` and `Average Net Sales` as currency (₹ if that matches your report), and `Total Orders`, `Unique Customers`, and `Total Quantity` as whole numbers.

**Important:** `Average Net Sales` above is the average row-level `NetSales`. If you want average sales per order, create a separate measure and label it clearly.

### 6. Validate the measures
Add temporary Card visuals for `Total Net Sales`, `Total Orders`, `Unique Customers`, and `Total Quantity`.
- Compare `Total Net Sales` with the sum of `NetSales` in your source data.
- Apply a Region or Category filter and verify that the cards update.
- Clear the filters and confirm that the original totals return.
- If totals do not match, inspect data types, duplicate rows, filters, and the meaning of each row before continuing.

### 7. Save and document
Save the PBIX. Record the table names, relationships, measures, data-quality checks, and any issues you could not resolve.

## Day 28 deliverables
- `Day28_Final_Project_Data_Model.pbix`
- Validated sales data and model
- Core measures created or checked
- Screenshot evidence of Model view, data validation, and KPI cards
- A short note describing the business problem and data model

## Screenshot checklist
- [ ] Model view showing tables and relationships
- [ ] Power Query/data view showing checked data types or validation
- [ ] KPI cards showing the core measures
- [ ] Full report page with the business questions or project scope

## GitHub folder
Create `Power BI/Day-28-Final-Project-Data-Model/` and place:
- `README.md`
- `TASK.md`
- `Screenshots/` (screenshots only; do not commit sensitive data)
- PBIX file if its size is acceptable for your repository

## Completion criteria
Day 28 is complete when the data types and model are checked, the core measures are validated, and the PBIX is saved separately from your earlier daily files.

**Next:** Day 29 — Final Project: Dashboard & Insights.
