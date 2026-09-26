# 📊 Power BI — Day 05 Tasks: Basic Report Workflow

**Level:** Beginner  
**Day:** 5 of 30  
**Dataset:** Power BI Master Sales Dataset — 1,500 rows

---

# 🎯 Task Goal

Today the focus is on the basic Power BI report-building workflow:

```text
Data
  ↓
Select Visual
  ↓
Add Fields
  ↓
Choose Aggregation
  ↓
Format Visual
  ↓
Arrange Report
  ↓
Apply Filter
  ↓
Test Interaction
```

Do not start advanced dashboard design today.

---

# 📦 Practice Dataset

Use:

```text
PowerBI_Master_Sales_Dataset_1500.csv
```

Important fields:

- `City`
- `Product`
- `Category`
- `Quantity`
- `GrossSales`
- `NetSales`
- `PaymentMode`

---

# 🧭 Task 1 — Create the Day 5 Report Page

Open your existing Power BI report.

Create a new report page.

Rename it:

```text
Day 5 — Basic Report Workflow
```

This page will contain all today's visuals.

---

# 📊 Task 2 — Create Basic Visuals

Create the following four visuals.

## Visual 1 — Total Net Sales Card

1. Select the **Card** visual.
2. Add:

```text
NetSales
```

3. Set aggregation to:

```text
Sum
```

4. Read the value displayed by Power BI.

Record:

```text
Total Net Sales:
```

Do not guess the value.

---

## Visual 2 — Sales Detail Table

Create a **Table** visual.

Add:

```text
Product
Category
Quantity
GrossSales
NetSales
```

Check that the table displays the expected fields.

---

## Visual 3 — Net Sales by City

Create a **Clustered Column Chart**.

Use:

**X-axis / Category**

```text
City
```

**Y-axis / Values**

```text
NetSales
```

Aggregation:

```text
Sum
```

The chart should compare Net Sales across cities.

---

## Visual 4 — Net Sales by Category

Create a **Clustered Bar Chart**.

Use:

**Y-axis / Category**

```text
Category
```

**X-axis / Values**

```text
NetSales
```

Aggregation:

```text
Sum
```

The chart should compare Net Sales across product categories.

---

## ✅ Task 2 Check

Confirm that you have:

- [x] Total Net Sales Card
- [x] Sales Detail Table
- [x] Net Sales by City column chart
- [x] Net Sales by Category bar chart

---

# 🧩 Task 3 — Practice Adding and Removing Fields

This task helps you understand how fields control a visual.

## Exercise A — Change the City Chart

Select the **Net Sales by City** chart.

Change:

```text
NetSales
```

to:

```text
GrossSales
```

Observe the chart.

Then change it back to:

```text
NetSales
```

---

## Exercise B — Add a Field to the Table

Select the Sales Detail Table.

Add:

```text
PaymentMode
```

Observe the result.

Then remove:

```text
PaymentMode
```

---

## Questions

Write your answers:

```text
1. What happens when a field is added to a visual?
- The field is added to the visual and Power BI uses it to display or analyze the data.

2. What happens when a field is removed?
- The field is removed from the visual, so it is no longer used in that visual.

3. What happens when a numeric field is added to Values?
- Power BI usually aggregates the numeric field, such as using Sum, Average, Count, Minimum, or Maximum.

4. What does Sum mean when used as an aggregation?
- Sum adds all the numeric values together.

Example:
Sales = 100, 200, 300
Sum of Sales = 600

```

---

# 📄 Task 4 — Build the Simple Report Page

Arrange all four visuals on one report page.

Use this basic structure:

```text
+------------------------------------------------------+
|          DAY 5 — BASIC REPORT WORKFLOW              |
|                                                      |
|               [ Total Net Sales ]                    |
|                                                      |
|    [ Net Sales by City ] [ Net Sales by Category ]  |
|                                                      |
|    [              Sales Detail Table              ] |
|                                                      |
+------------------------------------------------------+
```

## Top

Place the **Total Net Sales Card**.

## Middle

Place:

- Net Sales by City
- Net Sales by Category

## Bottom

Place the Sales Detail Table.

---

## Basic Formatting

Do only basic formatting:

- Resize visuals.
- Align visuals.
- Avoid overlapping visuals.
- Give the page a clear title.
- Make visual titles understandable.
- Keep enough space between visuals.

Do not spend time on advanced dashboard design.

---

# 🔎 Task 5 — Understand Basic Filters

Open the **Filters** pane.

Select the **Net Sales by City** chart.

Practice a **visual-level filter**.

Steps:

1. Select the City chart.
2. Open the Filters pane.
3. Add/use `City` as a visual-level filter.
4. Select one city.
5. Observe the chart.
6. Clear the filter.
7. Confirm the chart returns to the previous state.

Record:

```text
Selected City: Bengaluru

What changed in the visual?
- The chart was filtered to Bengaluru and displayed the Net Sales for Bengaluru.
```

---

# 🧪 Task 6 — Test Visual Interactions

Select a city data point in the **Net Sales by City** chart.

Observe whether the other visuals respond.

Check:

- Total Net Sales Card
- Net Sales by Category
- Sales Detail Table

Then clear the selection.

Record:

```text
Selected City:

Card changed: Yes
Yes / No

Category chart changed: Yes
Yes / No

Sales table changed: Yes
Yes / No
```

---

# 🧠 Task 7 — Understand the Basic Report Workflow

Without looking at the previous tasks, explain the workflow:

```text
1. Select a visual
2. Add fields
3. Choose aggregation
4. Format the visual
5. Arrange the visual
6. Test filters
7. Test interactions
8. Save the report
```

Write the process in your own words:

```text

My Power BI Report Workflow:

1. Select a visual and add the required fields.
2. Choose the appropriate aggregation for the data.
3. Format and arrange the visual clearly.
4. Apply filters and test how the visuals interact.
5. Save the completed report.
```


# 🗂️ GitHub Structure

Your Day 5 folder should be:

```text
Day-05-Basic-Report-Workflow/
│
├── README.md
├── TASK.md
├── Day05_Basic_Report_Workflow.pbix
│
└── Screenshots/
    ├── 01-basic-card.png
    ├── 02-sales-table.png
    ├── 03-sales-by-city.png
    ├── 04-sales-by-category.png
    ├── 05-simple-report-page.png
    ├── 06-filter-example.png
    └── 07-visual-interaction.png
```

---

# ✅ Day 5 Completion Checklist

- [ ] Task 1 — Report page created
- [ ] Task 2 — Basic visuals created
- [ ] Task 3 — Fields added/removed
- [ ] Task 4 — Simple report page built
- [ ] Task 5 — Basic filter tested
- [ ] Task 6 — Visual interactions tested
- [ ] Task 7 — Workflow explained
- [ ] Task 8 — Knowledge check completed
- [ ] Screenshots captured
- [ ] PBIX saved
- [ ] Mistakes recorded
- [ ] Key concepts recorded
- [ ] GitHub folder organized
- [ ] Changes committed

---

# 🚀 Day 5 Finish

Once all tasks are completed:

1. Save the PBIX.
2. Capture the screenshots.
3. Answer the knowledge questions.
4. Send the screenshots here.
5. I will review your Day 5 work.
6. After review, move to **Day 6 — Data Types & Column Profiling**.
