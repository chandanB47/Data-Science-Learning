# Power BI --- Day 01: Introduction & First Report

**Level:** Beginner\
**Estimated time:** 45--75 minutes\


## Learning objectives

By the end of this lesson, I can: - Explain what Power BI is used for. -
Identify the main areas of Power BI Desktop. - Import a CSV dataset. -
Create a simple visual and save a `.pbix` report.

## Key concepts

-   **Power BI Desktop:** Windows authoring application for connecting
    to data, transforming it, modeling it, and building reports.
-   **Power Query:** Tool used to clean and transform data before
    loading it.
-   **Report:** One or more interactive pages containing visuals built
    from a data model.
-   **Visual:** A chart, table, card, or other representation of data.

## Materials

Download `PowerBI_Day01_Sales_Practice.csv` from the accompanying file.
It contains sample order dates, cities, products, quantities, unit
prices, and sales values. It is fictional practice data.

## Step-by-step tasks

### Task 1 --- Explore Power BI Desktop

1.  Open **Power BI Desktop**.
2.  Identify the main report canvas and the panes for
    building/formatting visuals and viewing data fields. Pane names may
    vary by version.
3.  Find the **Home** ribbon and locate **Get data**.

### Task 2 --- Import the dataset

1.  Select **Home → Get data → Text/CSV**.
2.  Select `PowerBI_Day01_Sales_Practice.csv`.
3.  Preview the data. Check that dates, text, and numeric columns look
    sensible.
4.  Select **Load**. (If you choose **Transform Data**, inspect the
    preview, then select **Close & Apply**.)

### Task 3 --- Create your first visual

1.  In the report canvas, add a **Clustered column chart**.
2.  Put `City` on the X-axis.
3.  Put `Sales` on the Y-axis and ensure it is summarized as **Sum**.
4.  Add a **Table** visual containing `Product`, `Quantity`, and
    `Sales`.
5.  Save the report as `Day01_First_Report.pbix` inside your Day-01
    folder.

### Task 4 --- Check the result

-   The column chart should show total sales by city.
-   The table should show product, quantity, and sales values.
-   Click a city column and observe whether the table
    cross-filters/highlights. Clear the selection by clicking the
    canvas.

## Screenshot checklist

Save screenshots in `Day-01-Introduction/Screenshots/`: - \[ \]
`01-powerbi-desktop.png` --- Desktop open, showing the report canvas and
panes. - \[ \] `02-data-loaded.png` --- Fields/data visible after
importing the CSV. - \[ \] `03-first-chart.png` --- Column chart showing
Sales by City. - \[ \] `04-table-and-interaction.png` --- Table visual
and (if available) a selected city interaction.

## GitHub deliverables

-   [ ] This `README.md`
-   [ ] `Day01_First_Report.pbix`
-   [ ] The practice CSV (or link/reference to it)
-   [ ] Screenshots listed above

## Reflection

Answer briefly: 1. What is Power BI used for? 2. What is the difference
between Power BI Desktop and Power Query? 3. Which city has the highest
total sales in your chart? 4. What happened when you selected a city
column?


