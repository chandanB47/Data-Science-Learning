-- ==========================================================
-- Day 30: Project 2 - Fraud Detection & Financial Anomaly Engine
-- MySQL 8.0+ | Synthetic educational data
-- ==========================================================

DROP DATABASE IF EXISTS bank_fraud_analytics;
CREATE DATABASE bank_fraud_analytics;
USE bank_fraud_analytics;

-- 1. Schema
CREATE TABLE bank_accounts (
    account_id INT PRIMARY KEY,
    account_holder VARCHAR(100) NOT NULL,
    account_type VARCHAR(20) NOT NULL,
    risk_level VARCHAR(10) DEFAULT 'LOW',
    balance DECIMAL(15, 2) NOT NULL
);

CREATE TABLE transactions (
    tx_id INT PRIMARY KEY AUTO_INCREMENT,
    source_acc INT NOT NULL,
    dest_acc INT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    tx_timestamp DATETIME NOT NULL,
    location_city VARCHAR(50) NOT NULL,
    tx_channel VARCHAR(20) NOT NULL,
    CONSTRAINT chk_tx_channel CHECK (tx_channel IN ('ATM', 'POS', 'ONLINE_WIRE', 'UPI')),
    CONSTRAINT chk_positive_amount CHECK (amount > 0),
    CONSTRAINT fk_tx_src FOREIGN KEY (source_acc) REFERENCES bank_accounts(account_id),
    CONSTRAINT fk_tx_dst FOREIGN KEY (dest_acc) REFERENCES bank_accounts(account_id)
);

CREATE INDEX idx_tx_source_time ON transactions(source_acc, tx_timestamp);
CREATE INDEX idx_tx_channel_time ON transactions(tx_channel, tx_timestamp);

-- 2. Synthetic accounts
INSERT INTO bank_accounts (account_id, account_holder, account_type, balance) VALUES
(101, 'Aarav Sharma', 'SAVINGS', 250000.00),
(102, 'Neha Patel', 'SAVINGS', 480000.00),
(103, 'Vikram Singh', 'CURRENT', 950000.00),
(104, 'Rohan Verma', 'SAVINGS', 12000.00),
(105, 'Global Shell A', 'CURRENT', 150000.00),
(106, 'Global Shell B', 'CURRENT', 140000.00),
(107, 'Global Shell C', 'CURRENT', 130000.00);

INSERT INTO transactions
(source_acc, dest_acc, amount, tx_timestamp, location_city, tx_channel) VALUES
(101, 102, 5000.00, '2026-09-01 09:15:00', 'Bengaluru', 'UPI'),
(102, 103, 12000.00, '2026-09-01 10:30:00', 'Bengaluru', 'ONLINE_WIRE'),

-- Pattern A: repeated near-threshold transfers (illustrative threshold: 50,000)
(104, 103, 48500.00, '2026-09-02 11:00:00', 'Mumbai', 'ONLINE_WIRE'),
(104, 103, 49000.00, '2026-09-02 13:45:00', 'Mumbai', 'ONLINE_WIRE'),
(104, 103, 47800.00, '2026-09-02 16:20:00', 'Mumbai', 'ONLINE_WIRE'),

-- Pattern B: clustered transfer activity
(101, 104, 30000.00, '2026-09-03 02:00:10', 'Bengaluru', 'UPI'),
(101, 104, 35000.00, '2026-09-03 02:03:45', 'Bengaluru', 'UPI'),
(101, 104, 40000.00, '2026-09-03 02:08:12', 'Bengaluru', 'UPI'),

-- Pattern C: physical transactions in distant cities close in time
(102, 103, 2500.00, '2026-09-04 14:00:00', 'Bengaluru', 'POS'),
(102, 103, 18000.00, '2026-09-04 14:40:00', 'Delhi', 'POS'),

-- Pattern D: candidate circular transfer (105 -> 106 -> 107 -> 105)
(105, 106, 120000.00, '2026-09-05 10:00:00', 'Hyderabad', 'ONLINE_WIRE'),
(106, 107, 118000.00, '2026-09-05 12:30:00', 'Hyderabad', 'ONLINE_WIRE'),
(107, 105, 115000.00, '2026-09-05 15:00:00', 'Hyderabad', 'ONLINE_WIRE');

-- 3. Audit 1: near-threshold structuring screen
-- Illustrative threshold only; aggregate within a 24-hour window.
WITH near_threshold AS (
    SELECT *
    FROM transactions
    WHERE amount >= 45000.00 AND amount < 50000.00
)
SELECT
    source_acc AS flagging_account,
    COUNT(*) AS near_threshold_transfer_count,
    SUM(amount) AS aggregate_amount,
    MIN(tx_timestamp) AS first_seen,
    MAX(tx_timestamp) AS last_seen
FROM near_threshold
GROUP BY source_acc, DATE(tx_timestamp)
HAVING COUNT(*) >= 2
ORDER BY aggregate_amount DESC;

-- 4. Audit 2: rolling 15-minute transfer count per source account
SELECT
    t1.source_acc,
    t1.tx_id,
    t1.tx_timestamp,
    COUNT(t2.tx_id) AS transfers_in_15_min_window,
    SUM(t2.amount) AS amount_in_15_min_window,
    'VELOCITY REVIEW' AS alert_reason
FROM transactions t1
JOIN transactions t2
  ON t2.source_acc = t1.source_acc
 AND t2.tx_timestamp BETWEEN t1.tx_timestamp - INTERVAL 15 MINUTE
                          AND t1.tx_timestamp
GROUP BY t1.source_acc, t1.tx_id, t1.tx_timestamp
HAVING COUNT(t2.tx_id) >= 3
ORDER BY t1.source_acc, t1.tx_timestamp;

-- 5. Audit 3: physical-use city/time anomaly proxy
-- City-to-city distance is not computed; enrich with geocodes for production use.
WITH physical_swipes AS (
    SELECT
        tx_id, source_acc, location_city, tx_timestamp,
        LAG(location_city) OVER (
            PARTITION BY source_acc ORDER BY tx_timestamp, tx_id
        ) AS prior_city,
        LAG(tx_timestamp) OVER (
            PARTITION BY source_acc ORDER BY tx_timestamp, tx_id
        ) AS prior_timestamp
    FROM transactions
    WHERE tx_channel IN ('POS', 'ATM')
)
SELECT
    source_acc,
    prior_city,
    location_city AS current_city,
    prior_timestamp,
    tx_timestamp AS current_timestamp,
    TIMESTAMPDIFF(MINUTE, prior_timestamp, tx_timestamp) AS elapsed_minutes,
    'GEOGRAPHIC REVIEW - DISTANCE NOT VERIFIED' AS alert_tag
FROM physical_swipes
WHERE prior_city IS NOT NULL
  AND prior_city <> location_city
  AND TIMESTAMPDIFF(MINUTE, prior_timestamp, tx_timestamp) < 120;

-- 6. Audit 4: chronological three-edge circular transfer candidates
SELECT
    t1.source_acc AS originating_account,
    t1.dest_acc AS intermediary_1,
    t2.dest_acc AS intermediary_2,
    t1.amount AS initial_amount,
    t2.amount AS second_amount,
    t3.amount AS returned_amount,
    t1.tx_timestamp AS cycle_start,
    t3.tx_timestamp AS cycle_end,
    'CIRCULAR FLOW REVIEW' AS alert_reason
FROM transactions t1
JOIN transactions t2
  ON t1.dest_acc = t2.source_acc
 AND t1.tx_timestamp < t2.tx_timestamp
JOIN transactions t3
  ON t2.dest_acc = t3.source_acc
 AND t2.tx_timestamp < t3.tx_timestamp
WHERE t3.dest_acc = t1.source_acc
  AND t1.source_acc <> t1.dest_acc;

-- 7. Audit 5: simple account-level amount outlier screen
-- Requires at least 3 prior observations; sample is intentionally small.
WITH account_stats AS (
    SELECT
        source_acc,
        amount,
        tx_timestamp,
        AVG(amount) OVER (
            PARTITION BY source_acc
            ORDER BY tx_timestamp
            ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING
        ) AS prior_avg_amount,
        STDDEV_SAMP(amount) OVER (
            PARTITION BY source_acc
            ORDER BY tx_timestamp
            ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING
        ) AS prior_stddev,
        COUNT(amount) OVER (
            PARTITION BY source_acc
            ORDER BY tx_timestamp
            ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING
        ) AS prior_observations
    FROM transactions
)
SELECT
    source_acc,
    amount,
    tx_timestamp,
    prior_avg_amount,
    prior_stddev,
    CASE
        WHEN prior_stddev > 0
        THEN (amount - prior_avg_amount) / prior_stddev
        ELSE NULL
    END AS approximate_z_score
FROM account_stats
WHERE prior_observations >= 3
  AND prior_stddev > 0
  AND ABS((amount - prior_avg_amount) / prior_stddev) >= 3
ORDER BY source_acc, tx_timestamp;

-- End of educational audit suite.
