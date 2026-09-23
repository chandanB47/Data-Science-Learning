# Power BI --- Day 02: Power BI Desktop Interface & Report Workflow

**Level:** Beginner\
**Day:** 2 of 45\
**Estimated time:** 60--90 minutes\


## 🎯 Learning Objectives

By the end of Day 2, I should be able to: 
- Identify the major areas of Power BI Desktop.
- Understand Report, Data, and Model views.
- Understand the Ribbon, Report Canvas, Data/Fields pane, Visualizations/Build Visual pane, and Filters pane.
- Create and rename report pages.
- Build a simple second report page.
- Save and organize a
Power BI `.pbix` file.

## 1. Explore Power BI Desktop

Identify these areas:

### Ribbon

The top section containing commands such as Home, Insert, Modeling,
View, and Help. Available tabs can vary by version.

### Report Canvas

The central area where charts, tables, cards, slicers, and other visuals
are placed.

### Report / Data / Model Views

**Report View** - Build interactive reports. - Add and arrange visuals.

**Data View** - Inspect rows and columns loaded into the model.

**Model View** - View and manage relationships between tables.

### Data / Fields Pane

Shows tables and columns available in the report.

### Visualizations / Build Visual Pane

Used to choose and configure visuals.

### Filters Pane

Used to apply visual-, page-, or report-level filters.

# 2. Day 2 Practical Exercise

Continue using your **Day 1 Sales Practice dataset**. Do not create a
new dataset.

## Task 1 --- Open and save a copy

Open `Day01_First_Report.pbix`.

Use **Save As** and save a copy as:

`Day02_Interface_Practice.pbix`

This protects your Day 1 work.

## Task 2 --- Explore the three views

Click: 1. Report View 2. Data View 3. Model View

Observe what changes.

Write one sentence in your notes for each: - Report View: - Data View: -
Model View:

## Task 3 --- Create a new report page

Click the `+` button at the bottom.

Rename the new page:

`Interface Practice`

## Task 4 --- Create a Total Sales Card

On `Interface Practice`: 1. Select the **Card** visual. 2. Drag `Sales`
into the card. 3. Confirm it is summarized as **Sum**.

Expected value:

**₹444,250**

## Task 5 --- Add a City Slicer

Add a **Slicer** visual.

Drag `City` into it.

Test: - Bengaluru - Chennai - Hyderabad - Pune

Select **Chennai**, observe the other visual(s), then clear the
selection.

## Task 6 --- Add a Product Table

Create a Table visual containing: - Product - Quantity - Sales

Test the table using the City slicer.

Select Chennai, observe the table, then clear the selection. Test
another city.

## Task 7 --- Organize the page

Arrange the page roughly as:

``` text
┌──────────────────────────────────────────────┐
│             INTERFACE PRACTICE               │
│                                              │
│  ┌───────────────┐   ┌───────────────────┐  │
│  │ Total Sales   │   │   City Slicer     │  │
│  │   ₹444,250    │   │ Bengaluru         │  │
│  └───────────────┘   │ Chennai           │  │
│                      │ Hyderabad         │  │
│                      │ Pune              │  │
│                      └───────────────────┘  │
│                                              │
│  ┌────────────────────────────────────────┐  │
│  │ Product       Quantity       Sales      │  │
│  │ Laptop            6         331000      │  │
│  │ Monitor           7          84600      │  │
│  │ Keyboard         12          18550      │  │
│  │ Mouse            14          10100      │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

Do not spend time on advanced formatting today. The goal is
understanding the interface and interaction.

# 3. Screenshot Checklist

Save screenshots in:

`Day-02-Desktop-Interface/Screenshots/`

-   `01-report-view.png` --- Power BI Desktop showing Report View.
-   `02-data-view.png` --- Data View showing the imported sales table.
-   `03-model-view.png` --- Model View showing the current model/table.
-   `04-interface-practice.png` --- Interface Practice page with Card,
    Slicer, and Table.
-   `05-chennai-filter.png` --- Chennai selected in the slicer and the
    table responding.

# 4. GitHub Folder

``` text
PowerBI/
└── Day-02-Desktop-Interface/
    ├── README.md
    ├── Day02_Interface_Practice.pbix
    └── Screenshots/
        ├── 01-report-view.png
        ├── 02-data-view.png
        ├── 03-model-view.png
        ├── 04-interface-practice.png
        └── 05-chennai-filter.png
```

No new dataset is required for Day 2.

# 5. Knowledge Check

Answer after completing the practical work:

1.  What is the purpose of Report View?
2.  What is the purpose of Data View?
3.  What is the purpose of Model View?
4.  What is the purpose of the Filters pane?
5.  What total sales value is shown in the Card?
6.  What happened to the table when you selected Chennai in the slicer?

# ✅ Day 2 Completion Criteria

-   [ ] Report View explored
-   [ ] Data View explored
-   [ ] Model View explored
-   [ ] Interface Practice page created
-   [ ] Total Sales card created
-   [ ] City slicer created
-   [ ] Product table created
-   [ ] Chennai filter tested
-   [ ] PBIX saved
-   [ ] Screenshots captured
-   [ ] Knowledge check answered
-   [ ] Work reviewed before Day 3
