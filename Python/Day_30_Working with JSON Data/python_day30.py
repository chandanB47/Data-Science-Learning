# ==========================================
# Day 30 — Python JSON Data
# Script: json_data.py
# ==========================================

import json
from datetime import datetime
from pathlib import Path
import os

print("=== 1. JSON LOADS & DUMPS (IN-MEMORY) ===")
# Python dictionary to JSON string
experiment_config = {
    "experiment_id": "EXP-2026-09",
    "model_type": "RandomForest",
    "hyperparameters": {
        "n_estimators": 100,
        "max_depth": 12,
        "criterion": "gini"
    },
    "features": ["age", "income", "credit_history"],
    "is_production_ready": False,
    "baseline_score": None
}

json_str = json.dumps(experiment_config, indent=2, sort_keys=True)
print("Serialized JSON String:\n", json_str)

# JSON string back to Python Dictionary
decoded_dict = json.loads(json_str)
print("\nDecoded Type:", type(decoded_dict))
print("Hyperparameters max_depth:", decoded_dict["hyperparameters"]["max_depth"])


print("\n=== 2. JSON FILE OPERATIONS (DUMP & LOAD) ===")
json_file_path = Path("day30_config.json")

# Writing directly to a file
with open(json_file_path, "w", encoding="utf-8") as f:
    json.dump(experiment_config, f, indent=4)

print(f"JSON file persisted at: {json_file_path.resolve()}")

# Reading directly from a file
with open(json_file_path, "r", encoding="utf-8") as f:
    loaded_from_disk = json.load(f)

print("Loaded Model Type from Disk:", loaded_from_disk["model_type"])


print("\n=== 3. HANDLING NON-SERIALIZABLE OBJECTS ===")
complex_state = {
    "checkpoint": "epoch_50",
    "timestamp": datetime(2026, 9, 11, 10, 30, 0),
    "classes": {"benign", "malignant"}  # Python set
}

def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(obj, set):
        return sorted(list(obj))
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

serialized_custom = json.dumps(complex_state, default=custom_serializer, indent=2)
print("Custom Encoded JSON:\n", serialized_custom)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — String to Dict
raw_json = '{"model": "XGBoost", "accuracy": 0.94, "trained": true}'
parsed_q1 = json.loads(raw_json)
print(f"Q1 Model: {parsed_q1['model']} | Accuracy: {parsed_q1['accuracy']}")


# Q2 — Pretty Printing JSON
payload_q2 = {"z_metric": 10, "a_metric": 50, "nested": {"y": 2, "x": 1}}
pretty_json = json.dumps(payload_q2, indent=4, sort_keys=True)
print("Q2 Sorted & Formatted JSON:\n", pretty_json)


# Q3 — File Persist and Reload
users_list = [
    {"user_id": 1, "username": "alpha_dev"},
    {"user_id": 2, "username": "beta_analyst"}
]
with open("q3_users.json", "w", encoding="utf-8") as f:
    json.dump(users_list, f, indent=2)

with open("q3_users.json", "r", encoding="utf-8") as f:
    reloaded_users = json.load(f)
print("Q3 Reloaded Users Count:", len(reloaded_users))


# Q4 — Set Serializer Handler
def serialize_sets(obj):
    if isinstance(obj, (set, frozenset)):
        return sorted(list(obj))
    raise TypeError(f"Type {type(obj)} not serializable")

set_data = {"unique_tags": {"python", "pandas", "data_science"}}
print("Q4 Serialized Set:", json.dumps(set_data, default=serialize_sets))


# Q5 — ISO Datetime Handler
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

time_payload = {"created_at": datetime(2026, 9, 11, 11, 40, 0)}
print("Q5 ISO Timestamp JSON:", json.dumps(time_payload, default=serialize_datetime))


# Q6 — JSON Key Integrity Check
int_key_dict = {100: "Status OK", 404: "Not Found"}
roundtrip_dict = json.loads(json.dumps(int_key_dict))
print("Q6 Original Keys:", list(int_key_dict.keys()), "-> Types:", [type(k) for k in int_key_dict.keys()])
print("   Roundtrip Keys:", list(roundtrip_dict.keys()), "-> Types:", [type(k) for k in roundtrip_dict.keys()])


# Q7 — Safe JSON Parser
def safe_load_json(filepath, fallback=None):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as err:
        print(f"   [WARN] Failed to load '{filepath}': {err}")
        return fallback

print("Q7 Missing file fallback:", safe_load_json("missing_file.json", fallback={"status": "DEFAULT"}))

with open("q7_corrupt.json", "w", encoding="utf-8") as f:
    f.write("{invalid_json_missing_quotes: 123,}")
print("Q7 Corrupt file fallback:", safe_load_json("q7_corrupt.json", fallback={}))


# Q8 — Nested Key Extraction
nested_api_response = {
    "status": 200,
    "auth": {
        "session": {
            "token": "BEARER_XYZ_987123"
        }
    }
}
token = nested_api_response.get("auth", {}).get("session", {}).get("token", "NO_TOKEN")
missing_flag = nested_api_response.get("auth", {}).get("refresh", {}).get("token", "NO_TOKEN")
print(f"Q8 Extracted Token: {token} | Missing Path Result: {missing_flag}")


# Q9 — Updating Persistent JSON
config_to_update = {"app": "DataApp", "debug": True, "version": 1.0}
config_path = "q9_config.json"

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config_to_update, f, indent=2)

# In-place update pattern:
with open(config_path, "r", encoding="utf-8") as f:
    curr_data = json.load(f)

curr_data["debug"] = False
curr_data["version"] = 1.1

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(curr_data, f, indent=2)

with open(config_path, "r", encoding="utf-8") as f:
    print("Q9 Updated In-Place JSON Config:", json.load(f))


# Q10 — Challenge 🔥 (Hierarchical API Normalizer & Flattener)
raw_api_payload = """
{
    "run_id": "RUN_4091",
    "metadata": {
        "author": "Dr. Rao",
        "dataset": "credit_default_v2"
    },
    "configuration": {
        "algorithm": "GradientBoosting",
        "parameters": {
            "n_estimators": 200,
            "learning_rate": 0.05
        }
    },
    "evaluation": {
        "splits": 5,
        "fold_scores": [0.89, 0.92, 0.94, 0.91, 0.93],
        "metric": "roc_auc"
    }
}
"""

def normalize_experiment_run(json_str, output_filepath):
    data = json.loads(json_str)
    
    # Compute summary aggregates
    scores = data["evaluation"]["fold_scores"]
    best_score = max(scores)
    mean_score = round(sum(scores) / len(scores), 4)
    
    # Flatten hierarchical attributes into single-level record
    flattened_summary = {
        "run_id": data["run_id"],
        "author": data["metadata"]["author"],
        "dataset": data["metadata"]["dataset"],
        "algorithm": data["configuration"]["algorithm"],
        "learning_rate": data["configuration"]["parameters"]["learning_rate"],
        "metric_evaluated": data["evaluation"]["metric"],
        "best_score": best_score,
        "mean_score": mean_score
    }
    
    with open(output_filepath, "w", encoding="utf-8") as out:
        json.dump(flattened_summary, out, indent=4)
        
    return flattened_summary

summary_path = "experiment_summary.json"
summary_res = normalize_experiment_run(raw_api_payload, summary_path)

print("\nQ10 Flattened Experiment Summary:")
for k, v in summary_res.items():
    print(f"   {k}: {v}")

# Cleanup generated practice JSON files
practice_files = [
    json_file_path, "q3_users.json", "q7_corrupt.json",
    config_path, summary_path
]
for f_path in practice_files:
    if os.path.exists(f_path):
        os.remove(f_path)
print("\nTemporary practice JSON files cleaned up.")


