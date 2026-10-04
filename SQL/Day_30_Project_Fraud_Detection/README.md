# 🛡️ Day 30: Project 2 - Fraud Detection & Financial Anomaly Analytics

## 📌 Overview
Day 30 is the final capstone project of the 30-day curriculum. You will construct an end-to-end fraud monitoring and risk engine over transactional banking ledgers. Using advanced window functions, self joins, CTEs, and statistical standard deviation thresholds, you will investigate high-velocity transfers, possible structuring, geographic anomalies, and circular transfer patterns.

> **Training-data notice:** This is a synthetic learning exercise, not a production AML system. Reporting thresholds and rules vary by jurisdiction and institution. Alerts are investigative leads, not proof of fraud.

## 🎯 Key Project Deliverables
- [x] Banking ledger schema with account-to-account transaction records.
- [x] Rapid velocity screening for clustered transfers.
- [x] Structuring screening for repeated transfers just below a configurable illustrative threshold.
- [x] Outlier spend screening using rolling statistics and Z-score approximation.
- [x] Geographic anomaly screening for consecutive physical transactions in different cities.
- [x] Circular transfer tracking for three-account cycles.
- [x] Illustrative suspicious-activity review output for AML investigation.

## 📂 Folder Structure

| File | Purpose |
| :--- | :--- |
| **`README.md`** | Project overview and execution instructions. |
| **`Notes.md`** | Theory, assumptions, limitations, and detection heuristics. |
| **`queries.sql`** | MySQL 8.0+ schema, synthetic data, and audit queries. |



The script drops and recreates `bank_fraud_analytics`; do not run it against a database containing data you need to keep.

## ⚠️ Interpretation
The sample rules are intentionally simplified. A production implementation needs calibrated thresholds, reliable device/card identifiers, geocoded locations, currency handling, transaction reversals, account ownership relationships, explainable alert logic, and human review.
