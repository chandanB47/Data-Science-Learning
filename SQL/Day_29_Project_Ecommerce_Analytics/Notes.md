```markdown
# Day 29: E-Commerce Analytics & RFM Segmentation

## 🎯 Key Concepts

* Schema design patterns for high-throughput transactional e-commerce platforms.
* Understanding core business metrics: Gross Merchandise Value (GMV), Net Revenue, Average Order Value (AOV), and Return Rate.
* Theoretical and practical construction of an RFM Segmentation model using SQL window functions.

---

## 1. What is RFM Segmentation?

**RFM (Recency, Frequency, Monetary)** is a behavioral segmentation technique used by data teams to group customers based on historical transaction patterns:

1. **Recency ($R$)**: How recently did the customer make a purchase?
   * *Formula*: $\text{Snapshot Date} - \text{Latest Order Date}$ (Smaller number = better score).
2. **Frequency ($F$)**: How often does the customer make purchases?
   * *Formula*: $\text{COUNT(DISTINCT order\_id)}$ (Higher number = better score).
3. **Monetary ($M$)**: How much total money has the customer spent?
   * *Formula*: $\text{SUM(net\_order\_amount)}$ (Higher number = better score).

---

## 2. Implementing RFM in SQL

The standard workflow uses statistical quartiles (`NTILE(4)`) or quintiles (`NTILE(5)`):

```text
Raw Transactions ──> CTE 1: Compute R, F, M values per customer
                 ──> CTE 2: Apply NTILE(4) to assign scores (1 to 4)
                 ──> CTE 3: Concatenate scores (e.g., '444', '144', '111')
                 ──> Final Output: CASE WHEN classification into Customer Personas
```
Common Persona Definitions:

* Champions (R=4, F=4, M=4): Bought recently, buy often, and spend the most.
* Loyal Customers (R >= 3, F >= 3): Regular buyers responsive to promotions.
* At Risk / Can't Lose Them (R <= 2, F >= 3, M >= 3): High spenders who haven't bought recently.
* Lost / Inactive (R=1, F=1, M=1): Lowest spend and longest inactivity.


## 3. Essential E-Commerce Metrics Formulas

  $$\text{AOV (Average Order Value)} = \frac{\text{Total Net Sales}}{\text{Total Distinct Orders}}$$

  $$\text{Product Return Rate} = \left(\frac{\text{Cancelled or Returned Orders}}{\text{Total Orders Placed}}\right) \times 100$$
