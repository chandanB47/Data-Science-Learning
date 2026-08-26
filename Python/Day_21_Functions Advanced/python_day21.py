# ==========================================
# Day 21 — Python Functions Advanced
# Script: functions_advanced.py
# ==========================================

from datetime import datetime

print("=== 1. POSITIONAL VS KEYWORD ARGUMENTS ===")
def generate_endpoint(protocol, domain, port=80, secure=False):
    return f"{protocol}://{domain}:{port} (Secure: {secure})"

# Positional call
print("Positional:", generate_endpoint("http", "localhost", 8080, False))

# Keyword call (unordered)
print("Keyword:   ", generate_endpoint(domain="api.cloud.io", protocol="https", secure=True, port=443))


print("\n=== 2. MUTABLE DEFAULT ARGUMENT FIX ===")
# Safe accumulator pattern
def add_transaction(item_id, amount, registry=None):
    if registry is None:
        registry = []
    registry.append((item_id, amount))
    return registry

batch_1 = add_transaction("T101", 250.0)
batch_1 = add_transaction("T102", 400.0, batch_1)
batch_2 = add_transaction("T201", 99.0)  # Starts fresh

print("Batch 1 (Accumulated):", batch_1)
print("Batch 2 (Independent):", batch_2)


print("\n=== 3. POSITIONAL-ONLY & KEYWORD-ONLY ENFORCEMENT ===")
def build_model_pipeline(dataset_name, /, iterations=100, *, learning_rate=0.01, verbose=False):
    return {
        "dataset": dataset_name,
        "epochs": iterations,
        "lr": learning_rate,
        "verbose": verbose
    }

pipeline_config = build_model_pipeline("Customer_Churn", 50, learning_rate=0.005, verbose=True)
print("Config:", pipeline_config)


print("\n=== 4. MULTI-VALUE RETURNS & TYPE HINTS ===")
def summarize_scores(scores: list[float]) -> tuple[float, float, float]:
    """Calculates min, max, and average for a list of scores."""
    return min(scores), max(scores), round(sum(scores) / len(scores), 2)

low, high, avg = summarize_scores([88.5, 92.0, 79.5, 95.0, 84.0])
print(f"Low: {low} | High: {high} | Average: {avg}")


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Explicit Argument Mapping
def format_user(first, last, role="User"):
    return f"{first} {last} [{role}]"

print("Q1 Positional:", format_user("John", "Doe"))
print("Q1 Keyword:   ", format_user(last="Smith", first="Jane", role="Admin"))
print("Q1 Mixed:     ", format_user("Alice", "Brown", role="Moderator"))


# Q2 — Safe Default Mutable
def add_log(entry, logs=None):
    if logs is None:
        logs = []
    logs.append(entry)
    return logs

l1 = add_log("First")
l2 = add_log("Second")
print("Q2 Independent logs -> l1:", l1, "| l2:", l2)


# Q3 — Keyword-Only Enforcement
def evaluate_metric(y_true, y_pred, *, metric="accuracy", round_to=2):
    correct = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp)
    score = correct / len(y_true)
    return f"{metric.upper()}: {round(score, round_to)}"

print("Q3 Metric Evaluation:", evaluate_metric([1, 0, 1, 1], [1, 0, 1, 0], metric="accuracy", round_to=3))


# Q4 — Positional-Only Enforcement
def convert_currency(amount, rate, /):
    return round(amount * rate, 2)

print("Q4 Converted Currency:", convert_currency(150.0, 83.25))


# Q5 — Multi-Attribute Return & Unpacking
def vector_bounds(x_coords, y_coords):
    return min(x_coords), max(x_coords), min(y_coords), max(y_coords)

min_x, max_x, min_y, max_y = vector_bounds([1, 4, 8, 2], [10, 3, 15, 6])
print(f"Q5 Bounds: X[{min_x}, {max_x}] | Y[{min_y}, {max_y}]")


# Q6 — Type Annotated Pipeline Function
def normalize_scale(values: list[float], scale: float = 1.0) -> list[float]:
    max_val = max(values)
    return [round((v / max_val) * scale, 3) for v in values]

print("Q6 Normalized Scale:", normalize_scale([10.0, 20.0, 50.0], scale=100.0))


# Q7 — Complex Parameter Signatures
def train_test_split(data, target, /, test_size=0.2, *, shuffle=True, random_state=None):
    return {
        "data_len": len(data),
        "target_len": len(target),
        "test_size": test_size,
        "shuffle": shuffle,
        "seed": random_state
    }

split_out = train_test_split([1, 2, 3, 4], [0, 1, 0, 1], 0.25, shuffle=False, random_state=42)
print("Q7 Split Metadata:", split_out)


# Q8 — Dynamic Default Timestamp
def create_audit_record(action, timestamp=None):
    if timestamp is None:
        timestamp = "2026-08-26 09:56:00"  # deterministic representation
    return {"action": action, "timestamp": timestamp}

print("Q8 Audit Record:", create_audit_record("DELETE_RECORD"))


# Q9 — Discount Calculator with Bounds
def apply_discount(price: float, discount_pct: float = 0.0, /) -> float:
    discount_pct = max(0.0, min(100.0, discount_pct))
    return round(price * (1 - discount_pct / 100), 2)

print("Q9 Discounted Price:", apply_discount(120.0, 15.0))


# Q10 — Challenge 🔥 (Data Sanitization Pipeline Engine)
def clean_dataset(records: list[dict], /, *, drop_na=True, fill_val=0, upper_keys=False) -> tuple[list[dict], dict]:
    cleaned_records = []
    dropped_count = 0
    modified_count = 0

    for row in records:
        row_has_na = any(v is None for v in row.values())
        if drop_na and row_has_na:
            dropped_count += 1
            continue

        new_row = {}
        for k, v in row.items():
            formatted_key = k.upper() if upper_keys else k
            if v is None:
                new_row[formatted_key] = fill_val
                modified_count += 1
            else:
                new_row[formatted_key] = v
        cleaned_records.append(new_row)

    stats = {
        "initial_records": len(records),
        "retained_records": len(cleaned_records),
        "dropped_rows": dropped_count,
        "imputed_values": modified_count
    }
    return cleaned_records, stats

raw_data = [
    {"user": "Alice", "score": 95},
    {"user": "Bob", "score": None},
    {"user": "Charlie", "score": 80}
]

clean_data, pipeline_stats = clean_dataset(raw_data, drop_na=False, fill_val=0, upper_keys=True)
print("Q10 Sanitized Dataset:", clean_data)
print("Q10 Execution Stats:  ", pipeline_stats)



