# Day 30: Financial Fraud & Anomaly Detection

## 🎯 Key Concepts
- Transaction velocity heuristics and time-window analysis.
- Threshold avoidance patterns (structuring / smurfing).
- Statistical outlier screening with rolling averages and standard deviations.
- Geographic spatio-temporal anomaly screening.
- Graph-like cycle detection with SQL joins.

## 1. Structuring (Smurfing)

Structuring is the deliberate division of transactions to avoid applicable reporting or monitoring requirements. Rules and thresholds depend on jurisdiction, transaction type, and institution; the ₹50,000 value in this exercise is illustrative, not a statement of a universal legal reporting threshold.

A simple screening heuristic selects transactions in a band such as 85% to less than 100% of a configured threshold, then groups them by source account and a defined time window. Repeated near-threshold activity is a signal for review, not a finding of intent.

## 2. Velocity Anomalies

A compromised account may produce several transfers in a short period. This project screens for clustered activity using timestamp ordering and window logic. The SQL example uses adjacent-transaction intervals; a true sliding-window count should count all transactions in each rolling interval, not merely compare each row with its immediate predecessor.

## 3. Geographic Impossible Travel

For card-present transactions, compare consecutive physical-use events for the same card or account. A production model needs geocoded locations and a distance calculation, then computes:

`required_speed_kmh = distance_km / elapsed_hours`

A speed threshold is a heuristic only. City names alone cannot establish precise distance, and the example's time-gap rule is a simplified proxy. Use card identifiers rather than account identifiers where available.

## 4. Circular Transfer Patterns

Funds may pass through intermediary accounts and return to an origin:

`A → B → C → A`

A chronological multi-hop self-join can identify candidate cycles:

```sql
t1.dest_acc = t2.source_acc
AND t2.dest_acc = t3.source_acc
AND t3.dest_acc = t1.source_acc
AND t1.tx_timestamp < t2.tx_timestamp
AND t2.tx_timestamp < t3.tx_timestamp
```

Cycle detection can produce false positives. Real investigations also examine amounts, timing, beneficial ownership, transaction purpose, and supporting evidence.

## 5. Statistical Outliers

A common standardized score is:

`z = (amount - rolling_mean) / rolling_standard_deviation`

A high absolute Z-score can flag unusual activity relative to an account's own history. Sparse histories, zero variance, seasonality, and changing customer behavior require careful treatment.

## 6. Responsible Use

This capstone is educational and uses synthetic records. Do not treat a SQL flag as proof of wrongdoing or automatically block/report a customer based solely on these heuristics. Production AML decisions require jurisdiction-specific compliance controls, validation, auditability, privacy safeguards, and trained human review.
