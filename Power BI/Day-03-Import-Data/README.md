# 📊 Power BI --- Day 03: Import Data from Excel & CSV

**Level:** Beginner  
**Day:** 3 of 30  
**Dataset:** Power BI Master Sales Dataset --- Excel & CSV

------------------------------------------------------------------------

## 🎯 Learning Objectives

By the end of Day 3, I should be able to:

- Import data from an Excel workbook.
- Import data from a CSV file.
- Understand the Navigator window.
- Understand the difference between **Load** and **Transform Data**.
- Inspect imported tables and columns.
- Check basic column data types.
- Create a simple visual from imported data.
- Save and organize a Power BI `.pbix` file.
- Understand the basic data-import workflow in Power BI.

------------------------------------------------------------------------

# 📦 Practice Dataset

Use the same business-style sales dataset used in the Power BI learning journey.

### Files

```text
PowerBI_Master_Sales_Dataset_1500.xlsx
PowerBI_Master_Sales_Dataset_1500.csv
```

### Dataset details

| Item | Details |
|---|---|
| Rows | 1,500 |
| Columns | 19 |
| Date range | 2025-01-01 to 2026-09-22 |
| Cities | 10 |
| Products | 12 |
| Data type | Fictional sales/business data |

### Main columns

- `OrderID`
- `OrderDate`
- `CustomerID`
- `City`
- `State`
- `Region`
- `Product`
- `Category`
- `Quantity`
- `UnitPrice`
- `DiscountPct`
- `GrossSales`
- `DiscountAmount`
- `NetSales`
- `PaymentMode`
- `Salesperson`
- `Channel`
- `CustomerType`
- `OrderStatus`

This dataset will also be used in later Power BI topics such as Power Query, DAX, filtering, time analysis, KPIs, and dashboard projects.

------------------------------------------------------------------------

# 🧭 Task 1 --- Import Data from Excel

Open **Power BI Desktop**.

If you are starting Day 3 with a new report:

1. Open **Power BI Desktop**.
2. Select **Home → Get Data → Excel Workbook**.
3. Select `PowerBI_Master_Sales_Dataset_1500.xlsx`.
4. Wait for the **Navigator** window.
5. Select the available sales sheet/table.
6. Preview the data.
7. Select **Load**.

### Important

Do not manually clean or transform the data today unless instructed.

Power Query transformations will be covered systematically in later days.

------------------------------------------------------------------------

# 📋 Task 2 --- Explore the Navigator

When the Excel file opens in the Navigator window, identify:

### 1. Available Sheets / Tables

Identify the worksheet or table containing the sales data.

### 2. Data Preview

Look at:

- Column names
- Sample rows
- Number/date/text fields

### 3. Load

Understand that **Load** sends the selected data into the Power BI data model.

### 4. Transform Data

Understand that **Transform Data** opens Power Query so that data can be prepared before loading.

Write one sentence:

```text
Load:
Transform Data:
```

------------------------------------------------------------------------

# 📥 Task 3 --- Import Data from CSV

Now test the CSV format.

1. Open **Home → Get Data → Text/CSV**.
2. Select `PowerBI_Master_Sales_Dataset_1500.csv`.
3. Preview the data.
4. Check the delimiter and detected data types.
5. Select **Load**.

### Important

The purpose of this task is to understand that Power BI can connect to different file formats.

If you already have the same dataset loaded from Excel, do not keep unnecessary duplicate tables in your final report. The CSV import is primarily a learning exercise.

------------------------------------------------------------------------

# 🔍 Task 4 --- Inspect the Imported Data

Go to **Data/Table View**.

Check the following columns:

| Column | Expected Type |
|---|---|
| `OrderID` | Whole number / numeric |
| `OrderDate` | Date |
| `CustomerID` | Text or numeric identifier |
| `City` | Text |
| `State` | Text |
| `Region` | Text |
| `Product` | Text |
| `Category` | Text |
| `Quantity` | Whole number |
| `UnitPrice` | Decimal number |
| `DiscountPct` | Decimal/percentage |
| `GrossSales` | Decimal/number |
| `DiscountAmount` | Decimal/number |
| `NetSales` | Decimal/number |

Do not change the data types unless a problem is clearly visible.

Record any unusual data type you notice:

```text
Column:
Current Type:
Expected Type:
```

------------------------------------------------------------------------

# 📊 Task 5 --- Create a Basic Sales Visual

Go to **Report View**.

Create a **Clustered Column Chart**.

Use:

### X-axis / Category

`City`

### Y-axis / Values

`NetSales`

### Aggregation

**Sum**

This creates a basic **Sales by City** comparison.

------------------------------------------------------------------------

# 🧮 Task 6 --- Create a Total Sales Card

Create a **Card** visual.

Add:

```text
NetSales
```

Set aggregation to:

**Sum**

Record the result:

```text
Total Net Sales:
```

The exact value should be read from your Power BI report rather than guessed.

------------------------------------------------------------------------

# 🧪 Task 7 --- Compare Excel and CSV

Think about the two import methods.

Answer:

### Question 1

Which option did you use to import the Excel file?

```text
Answer:
```

### Question 2

Which option did you use to import the CSV file?

```text
Answer:
```

### Question 3

What is the main difference between **Load** and **Transform Data**?

```text
Answer:
```

### Question 4

Why is it useful to preview data before loading it?

```text
Answer:
```

### Question 5

Why should you avoid keeping duplicate copies of the same dataset in a Power BI model?

```text
Answer:
```

------------------------------------------------------------------------

# 📈 Task 8 --- Basic Data Inspection

Before moving to the next day, inspect:

- Number of rows
- Number of columns
- Column names
- Data types
- Date column
- Numeric columns
- Text columns

Record:

```text
Rows:
Columns:
Date Column:
Main Numeric Columns:
Main Text Columns:
```

------------------------------------------------------------------------

# 📸 Screenshot Checklist

Create:

```text
Day-03-Import-Data/
└── Screenshots/
```

Capture:

### Screenshot 01

`01-excel-get-data.png`

Show the Excel Get Data/import process.

### Screenshot 02

`02-excel-navigator.png`

Show the Excel Navigator window and data preview.

### Screenshot 03

`03-excel-loaded-data.png`

Show the imported dataset in Data/Table View.

### Screenshot 04

`04-csv-preview.png`

Show the CSV preview window.

### Screenshot 05

`05-sales-by-city.png`

Show the Sales-by-City clustered column chart.

### Screenshot 06

`06-total-sales-card.png`

Show the Total Net Sales Card.

### Screenshot 07

`07-final-report.png`

Show the completed Day 3 report page.

------------------------------------------------------------------------

# 🗂️ GitHub Folder Structure

Your Power BI repository should now look like:

```text
Power BI/
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
│
├── Day-03-Import-Data/
│   ├── README.md
│   ├── PowerBI_Master_Sales_Dataset_1500.xlsx
│   ├── PowerBI_Master_Sales_Dataset_1500.csv
│   ├── Day03_Import_Data.pbix
│   └── Screenshots/
│       ├── 01-excel-get-data.png
│       ├── 02-excel-navigator.png
│       ├── 03-excel-loaded-data.png
│       ├── 04-csv-preview.png
│       ├── 05-sales-by-city.png
│       ├── 06-total-sales-card.png
│       └── 07-final-report.png
│
└── ...
```

------------------------------------------------------------------------



# ⚠️ Common Mistakes

Avoid these mistakes:

- Loading the same dataset multiple times unnecessarily.
- Ignoring the Navigator preview.
- Building visuals without checking the imported columns.
- Assuming every numeric-looking column should be a number.
- Changing data unnecessarily before learning Power Query.
- Saving the `.pbix` file without organizing the Day 3 folder.
- Forgetting to capture screenshots of the completed work.

------------------------------------------------------------------------

# ✅ Day 3 Completion Checklist

- [ ] Excel dataset imported
- [ ] Excel Navigator explored
- [ ] Load vs Transform Data understood
- [ ] CSV dataset imported
- [ ] Imported data inspected
- [ ] Column types reviewed
- [ ] Sales-by-City chart created
- [ ] Total Net Sales Card created
- [ ] Excel vs CSV questions answered
- [ ] Knowledge check completed
- [ ] PBIX saved
- [ ] Screenshots captured
- [ ] GitHub folder organized
- [ ] Work reviewed before moving to Day 4

------------------------------------------------------------------------

# 🚀 Next

**Day 4 — Power Query Editor Overview**

Day 4 will move from simply importing data to understanding how Power BI can **inspect, transform, and prepare data before it enters the model**.
