# 📊 Power BI — Day 16: Advanced Modeling, Filter Context & Model Validation

## 📌 Overview
Day 16 is the final day of the Data Modeling phase. You will review how relationships control filter propagation, test the model from multiple dimensions, identify common relationship problems, and perform a final model-quality check before entering the DAX phase.

**Level:** Intermediate  
**Phase:** Data Modeling  
**Estimated time:** 75–120 minutes

## 🎯 Learning Objectives
- Understand filter propagation through relationships.
- Distinguish active and inactive relationships.
- Understand why relationship cardinality matters.
- Recognize common relationship errors.
- Validate dimension-to-fact filtering.
- Check the model for ambiguous or unnecessary relationships.
- Perform a final modeling-quality review.

## 📚 Core Concepts

### 1. Filter Propagation
In a standard star schema:

```text
Dimension
    ↓
Fact
```

For example:

```text
DimCustomer[CustomerType]
          ↓
       FactSales
          ↓
      NetSales
```

A filter placed on a dimension can affect the related fact rows.

### 2. Active Relationship
An active relationship is available for normal filter propagation.

It is normally shown as a solid relationship line in Model view.

### 3. Inactive Relationship
An inactive relationship exists but is not used automatically for normal filtering.

It can be useful when a fact table contains multiple date roles, such as:
- Order Date
- Ship Date
- Delivery Date

Do not create unnecessary inactive relationships today. The goal is to understand the concept.

### 4. Cardinality
Common relationship types include:
- One-to-many (1:*)
- One-to-one (1:1)
- Many-to-many (*:*)

For the current star schema, the preferred pattern is:

```text
Dimension 1 ───── * Fact
```

### 5. Ambiguous Filtering
Ambiguity can occur when multiple relationship paths allow filters to travel between tables in unexpected ways.

This is one reason to avoid unnecessary bidirectional relationships.

## 🧰 Target Model

Your model should resemble:

```text
                  DimCustomer
                       |
                       |
DimProduct ─────── FactSales ─────── DimDate
```

Expected relationships:

```text
DimCustomer 1 → * FactSales
DimProduct  1 → * FactSales
DimDate     1 → * FactSales
```

For today's model:
- Cardinality: **1:***
- Cross filter: **Single**
- Relationships: **Active**

## 🏁 Day 16 Deliverables
1. Relationship properties reviewed.
2. Dimension-to-fact filter tests completed.
3. Model validation performed.
4. Relationship issues investigated.
5. Clean Model view.
6. Validation report page.
7. Screenshots saved.
8. PBIX saved as `Day16_Advanced_Modeling_Validation.pbix`.

## 📁 Recommended GitHub Structure

```text
Power BI/
└── Day-16-Advanced-Modeling-Validation/
    ├── README.md
    ├── TASK.md
    ├── Day16_Advanced_Modeling_Validation.pbix
    └── Screenshots/
        ├── 01-final-model.png
        ├── 02-relationship-properties.png
        ├── 03-customer-filter-test.png
        ├── 04-product-date-filter-test.png
        └── 05-model-validation.png
```

## 🧠 Modeling Rules to Remember

### Rule 1
Dimension keys should be unique on the `1` side.

### Rule 2
Fact foreign keys can repeat on the `*` side.

### Rule 3
Prefer dimension-to-fact filtering.

### Rule 4
Use bidirectional filtering only when there is a clear modeling reason.

### Rule 5
Avoid unnecessary many-to-many relationships.

### Rule 6
A relationship should represent a real business relationship.

### Rule 7
A clean model is more important than simply having many relationships.

## ✅ Completion Criteria
- All major relationships reviewed.
- 1:* cardinality confirmed.
- Single filter direction confirmed.
- Active relationships confirmed.
- Customer, Product, and Date filtering tested.
- No unexplained blanks or relationship errors.
- No unnecessary relationships.
- Model layout is clear.
- Final validation completed.

## 🏆 Phase Completion
After Day 16, you have completed the **Data Modeling** section of the 30-day roadmap.

Next phase:

**Days 17–21 → DAX**
