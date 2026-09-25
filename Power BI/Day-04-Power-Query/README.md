  # 📊 Power BI --- Day 04: Power Query Editor Overview

**Level:** Beginner  
**Day:** 4 of 30  
**Dataset:** Power BI Master Sales Dataset --- 1,500 rows

------------------------------------------------------------------------

## 🎯 Learning Objectives

By the end of Day 4, I should be able to:

- Open Power Query Editor from Power BI Desktop.
- Understand the Power Query Editor interface.
- Identify the Queries pane.
- Understand the Data Preview area.
- Understand Query Settings.
- Understand Applied Steps.
- Distinguish Power Query from the Power BI data model.
- Make a simple transformation and observe the Applied Steps.
- Apply and close Power Query.
- Understand why data preparation happens before report modeling.

------------------------------------------------------------------------

# 📦 Practice Dataset

Use:

**PowerBI_Master_Sales_Dataset_1500.csv**

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

Use the same dataset from Day 2/Day 3 so that the learning path remains consistent.

------------------------------------------------------------------------

# 🧭 Task 1 --- Open Power Query Editor

Open your Day 3 `.pbix` file.

Go to:

**Home → Transform data → Transform data**

Power BI should open the **Power Query Editor**.

Do not make major changes yet.

------------------------------------------------------------------------

# 🖥️ Task 2 --- Explore the Power Query Editor Interface

Identify the following areas.

### 1. Ribbon

Explore the main Power Query tabs such as:

- Home
- Transform
- Add Column
- View

The exact available commands can vary by Power BI version.

### 2. Queries Pane

Located on the left side.

It contains the queries/tables available for transformation.

Identify your sales query.

### 3. Data Preview

The central area displays a preview of the selected query.

Use it to inspect:

- Column names
- Rows
- Values
- Data quality
- Data types

### 4. Query Settings

Located on the right side.

Identify:

- Properties
- Applied Steps

### 5. Applied Steps

Applied Steps records transformations performed on the query.

This is one of the most important concepts in Power Query.

------------------------------------------------------------------------

# 🧪 Task 3 --- Identify Applied Steps

Select your sales query.

Look at:

**Query Settings → Applied Steps**

You should see steps created when the data was imported.

Depending on your import method and Power BI version, you may see steps such as:

```text
Source
Promoted Headers
Changed Type
```

Your exact steps may differ.

### Important

Do not delete steps simply to make your list match the example.

Power Query records the actual operations performed on your query.

Write down your actual Applied Steps:

```text
Step 1:
Step 2:
Step 3:
...
```

------------------------------------------------------------------------

# 🔍 Task 4 --- Understand the Query Settings Pane

In the Query Settings pane, inspect:

### Properties

Identify the query name.

### Applied Steps

Understand that every transformation creates a step.

Think of the process as:

```text
Source
   ↓
Transformation 1
   ↓
Transformation 2
   ↓
Transformation 3
   ↓
Final Query
```

Power Query records the transformation process so that the query can be refreshed and reproduced.

------------------------------------------------------------------------

# 📝 Task 5 --- Rename the Query

In the Queries pane:

1. Right-click your sales query.
2. Select **Rename**.
3. Give it a clear name:

```text
Sales_Data
```

If your query already has this name, leave it unchanged.

### Why?

Good query names become important when a model contains many tables.

Avoid unclear names such as:

```text
Query1
Query2
Table1
```

Use meaningful names that describe the data.

------------------------------------------------------------------------

# 🛠️ Task 6 --- Make One Simple Transformation

Select the `Product` column.

Go to:

**Transform → Format → UPPERCASE**

The product values should now appear in uppercase.

For example:

```text
Laptop
```

may become:

```text
LAPTOP
```

### Observe

Look at:

**Query Settings → Applied Steps**

A new step should appear.

The important learning point is:

```text
Action performed
      ↓
Applied Step created
      ↓
Preview updated
```

------------------------------------------------------------------------

# ↩️ Task 7 --- Undo the Transformation

Now remove the uppercase transformation.

In **Applied Steps**, locate the step created by the transformation.

Click the **X** beside that step.

Observe what happens to the `Product` values.

They should return to their previous state.

### Important concept

Applied Steps define the sequence of transformations that Power Query applies to the source data.

------------------------------------------------------------------------

# 🧪 Task 8 --- Try a Safe Second Transformation

Select the `City` column.

Use:

**Transform → Format → Capitalize Each Word**

Observe the result.

Then check **Applied Steps** again.

Do not continue adding random transformations.

The objective is to understand the workflow:

```text
Select column
     ↓
Choose transformation
     ↓
Preview changes
     ↓
Applied Step appears
```

------------------------------------------------------------------------

# 🔎 Task 9 --- Understand Power Query vs Data View

Compare these two areas.

### Power Query Editor

Used primarily for:

- Data preparation
- Cleaning
- Transformation
- Reshaping
- Combining data

### Data/Table View

Used primarily for:

- Inspecting loaded data
- Checking rows and columns
- Reviewing model data after loading

Write:

```text
Power Query is used for:

Data/Table View is used for:
```

------------------------------------------------------------------------

# 💾 Task 10 --- Apply Changes

When you finish:

Select:

**Home → Close & Apply**

Power BI will apply the query steps and return to Power BI Desktop.

Wait for the data refresh to finish.

Then check the Data/Table View.

------------------------------------------------------------------------

# 🧠 Task 11 --- Understand the Workflow

Write the complete workflow from source to report:

```text
Data Source
    ↓
Power Query
    ↓
Transformations
    ↓
Close & Apply
    ↓
Data Model
    ↓
Report
    ↓
Visualizations
```

Explain in your own words what happens at each stage.

------------------------------------------------------------------------

# ❓ Knowledge Check

Answer these without copying the instructions.

### Q1

What is Power Query?

### Q2

Where can you find Applied Steps?

### Q3

Why are Applied Steps important?

### Q4

What happens when you remove an Applied Step?

### Q5

What is the purpose of Query Settings?

### Q6

What is the difference between Power Query Editor and Data/Table View?

### Q7

Why is it useful to give queries meaningful names?

### Q8

What happens when you select **Close & Apply**?

------------------------------------------------------------------------

# 📸 Screenshot Checklist

Create:

```text
Day-04-Power-Query/
└── Screenshots/
```

Capture:

### Screenshot 01

`01-power-query-editor.png`

Show the complete Power Query Editor interface.

### Screenshot 02

`02-queries-pane.png`

Show the Queries pane and your `Sales_Data` query.

### Screenshot 03

`03-query-settings.png`

Show Query Settings and Applied Steps.

### Screenshot 04

`04-transformation-step.png`

Show the Product transformation and the new Applied Step.

### Screenshot 05

`05-undo-step.png`

Show the result after removing the transformation step.

### Screenshot 06

`06-close-and-apply.png`

Show Power BI Desktop after applying the query changes.

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
│
├── Day-04-Power-Query/
│   ├── README.md
│   ├── Day04_Power_Query.pbix
│   └── Screenshots/
│       ├── 01-power-query-editor.png
│       ├── 02-queries-pane.png
│       ├── 03-query-settings.png
│       ├── 04-transformation-step.png
│       ├── 05-undo-step.png
│       └── 06-close-and-apply.png
│
└── ...
```

------------------------------------------------------------------------

# ⚠️ Common Mistakes

Avoid these mistakes:

- Confusing Power Query with the Data Model.
- Making many random transformations without understanding them.
- Deleting Applied Steps without knowing what they do.
- Assuming every Power Query step will have the same name.
- Changing the source data manually instead of using Power Query.
- Forgetting to check Applied Steps after a transformation.
- Forgetting to use **Close & Apply**.
- Keeping unclear query names such as `Query1`.

------------------------------------------------------------------------

# ✅ Day 4 Completion Checklist

- [ ] Power Query Editor opened
- [ ] Ribbon explored
- [ ] Queries pane explored
- [ ] Data Preview explored
- [ ] Query Settings explored
- [ ] Applied Steps identified
- [ ] Query renamed to `Sales_Data`
- [ ] One transformation created
- [ ] Applied Step observed
- [ ] Transformation removed
- [ ] Second safe transformation tested
- [ ] Close & Apply completed
- [ ] Power Query vs Data View understood
- [ ] Knowledge check completed
- [ ] PBIX saved
- [ ] Screenshots captured
- [ ] GitHub folder organized
- [ ] Work reviewed before moving to Day 5

------------------------------------------------------------------------

# 🚀 Next

**Day 5 — Basic Data Cleaning and Transformation**

Day 5 will move from understanding the Power Query interface to performing practical data-cleaning operations such as reviewing data types, identifying issues, and applying controlled transformations.
