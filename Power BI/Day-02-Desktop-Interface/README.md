# 📊 Power BI --- Day 02: Desktop Interface & First Interactive Report

**Level:** Beginner\
**Day:** 2 of 45\
**Dataset:** Power BI Master Sales Dataset --- 1,500 rows\


------------------------------------------------------------------------

## 🎯 Learning Objectives

By the end of Day 2, I should be able to:

-   Identify the main areas of Power BI Desktop.
-   Understand Report View, Data/Table View, and Model View.
-   Understand the Data pane, Visualizations/Build visual pane, and
    Filters pane.
-   Import and inspect a larger real-world-style dataset.
-   Create a new report page.
-   Create a Card, Slicer, and Table visual.
-   Test how slicers interact with report visuals.
-   Save and organize a Power BI `.pbix` file.

------------------------------------------------------------------------

# 📦 Practice Dataset

Use:

**PowerBI_Master_Sales_Dataset_1500.csv**

### Dataset details

  Item         Details
  ------------ -------------------------------
  Rows         1,500
  Columns      19
  Date range   2025-01-01 to 2026-09-22
  Cities       10
  Products     12
  Data type    Fictional sales/business data

### Main columns

-   `OrderID`
-   `OrderDate`
-   `CustomerID`
-   `City`
-   `State`
-   `Region`
-   `Product`
-   `Category`
-   `Quantity`
-   `UnitPrice`
-   `DiscountPct`
-   `GrossSales`
-   `DiscountAmount`
-   `NetSales`
-   `PaymentMode`
-   `Salesperson`
-   `Channel`
-   `CustomerType`
-   `OrderStatus`

This dataset will also be useful for later Power BI topics such as Power
Query, DAX, filtering, time analysis, KPIs, and dashboard projects.

------------------------------------------------------------------------

# 🧭 Task 1 --- Explore Power BI Desktop

Open Power BI Desktop and identify:

### 1. Ribbon

Contains commands and tools such as:

-   Home
-   Insert
-   Modeling
-   View
-   Help

The exact tabs can vary by Power BI version.

### 2. Report Canvas

The main area where visuals are created and arranged.

### 3. Data/Table View

Used to inspect the rows and columns loaded into the model.

### 4. Model View

Used to inspect and later manage relationships between tables.

### 5. Data Pane

Shows available tables, columns, and fields.

### 6. Visualizations / Build Visual Pane

Used to select and configure charts, cards, tables, slicers, and other
visuals.

### 7. Filters Pane

Used to apply filters at visual, page, or report level.

------------------------------------------------------------------------

# 📥 Task 2 --- Import the 1,500-row Dataset

If you are starting Day 2 with a new report:

1.  Open **Power BI Desktop**.
2.  Select **Home → Get Data → Text/CSV**.
3.  Select `PowerBI_Master_Sales_Dataset_1500.csv`.
4.  Preview the data.
5.  Check that columns such as `OrderDate`, `Quantity`, `UnitPrice`, and
    `NetSales` have appropriate data types.
6.  Select **Load**.

### Important

Do not manually change or clean the data today unless instructed.

Data cleaning and transformation will be taught systematically in the
Power Query section of the roadmap.

------------------------------------------------------------------------

# 📊 Task 3 --- Explore the Three Views

Open each view and take a screenshot.

### Report View

Used to create interactive reports and dashboards.

### Data/Table View

Used to inspect the loaded rows and columns.

### Model View

Used to understand the structure of tables and relationships.

### Notes

Write one sentence for each:

``` text
Report View:
Data/Table View:
Model View:
```

------------------------------------------------------------------------

# 📄 Task 4 --- Create the Day 2 Report Page

Create a new report page.

Rename it:

**Day 2 --- Sales Overview**

------------------------------------------------------------------------

# 🧮 Task 5 --- Create a Total Sales Card

Create a **Card** visual.

Add:

`NetSales`

Set the aggregation to:

**Sum**

The exact value will depend on the generated dataset and should be read
from your Power BI report rather than guessed.

Record your result:

``` text
Total Net Sales:
```

------------------------------------------------------------------------

# 🎛️ Task 6 --- Create a City Slicer

Add a **Slicer** visual.

Add:

`City`

The slicer should contain cities such as:

-   Bengaluru
-   Chennai
-   Hyderabad
-   Pune
-   Mumbai
-   Delhi
-   Kolkata
-   Ahmedabad
-   Jaipur
-   Kochi

Select one city and observe how the other visuals respond.

------------------------------------------------------------------------

# 📋 Task 7 --- Create a Sales Table

Create a Table visual containing:

-   `Product`
-   `Category`
-   `Quantity`
-   `GrossSales`
-   `NetSales`

Then select a city in the slicer.

Observe how the table changes.

Clear the selection and test another city.

------------------------------------------------------------------------

# 📈 Task 8 --- Create a Sales-by-City Chart

Create a **Clustered Column Chart**.

Use:

**X-axis / Category**

`City`

**Y-axis / Values**

`NetSales`

Aggregation:

**Sum**

This gives you your first larger-dataset comparison.

------------------------------------------------------------------------

# 🧪 Task 9 --- Test Interactions

Test the following:

### Test A

Select **Bengaluru** in the slicer.

Observe:

-   Total Net Sales
-   Sales table
-   Sales-by-city chart

### Test B

Clear Bengaluru.

Select **Chennai**.

Observe the same visuals.

### Test C

Clear the slicer completely.

Compare the report with the unfiltered state.

Write down what changed.

------------------------------------------------------------------------

# 📸 Screenshot Checklist

Create:

``` text
Day-02-Desktop-Interface/
└── Screenshots/
```

Capture:

### Screenshot 01

`01-report-view.png`

Show Power BI Desktop in Report View.

### Screenshot 02

`02-data-view.png`

Show the 1,500-row dataset in Data/Table View.

### Screenshot 03

`03-model-view.png`

Show Model View.

### Screenshot 04

`04-sales-overview.png`

Show:

-   Total Net Sales Card
-   City Slicer
-   Sales Table
-   Sales-by-City chart

### Screenshot 05

`05-city-filter.png`

Select one city and show the resulting interaction.

### Screenshot 06

`06-cleared-filter.png`

Clear the slicer and show the report returning to the unfiltered state.

------------------------------------------------------------------------

# 🗂️ GitHub Folder Structure

Your Power BI repository should now look like:

``` text
PowerBI/
│
├── README.md
├── Day-01-Introduction/
│   ├── README.md
│   ├── Day01_First_Report.pbix
│   └── Screenshots/
│
├── Day-02-Desktop-Interface/
│   ├── README.md
│   ├── PowerBI_Master_Sales_Dataset_1500.csv
│   ├── Day02_Sales_Overview.pbix
│   └── Screenshots/
│       ├── 01-report-view.png
│       ├── 02-data-view.png
│       ├── 03-model-view.png
│       ├── 04-sales-overview.png
│       ├── 05-city-filter.png
│       └── 06-cleared-filter.png
│
└── ...
```

------------------------------------------------------------------------


# ✅ Day 2 Completion Checklist

-   [ ] 1,500-row dataset imported
-   [ ] Report View explored
-   [ ] Data/Table View explored
-   [ ] Model View explored
-   [ ] Day 2 report page created
-   [ ] Total Net Sales Card created
-   [ ] City Slicer created
-   [ ] Sales Table created
-   [ ] Sales-by-City chart created
-   [ ] City filtering tested
-   [ ] Filter cleared and tested
-   [ ] PBIX saved
-   [ ] Screenshots captured
-   [ ] Knowledge questions answered
-   [ ] Work reviewed
-   [ ] GitHub folder organized
-   [ ] GitHub commit created

------------------------------------------------------------------------


## 🚀 Next

Day 3 will move toward **data types and basic data preparation**, which
starts the transition from simply creating visuals to actually preparing
data for analysis.
