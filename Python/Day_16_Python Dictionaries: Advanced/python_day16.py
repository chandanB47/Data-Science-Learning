
# ==========================================
# Day 16 — Python Dictionaries: Advanced
# Script: dictionaries_advanced.py
# ==========================================

print("=== 1. SAFE RETRIEVAL & DEFAULT VALUES ===")
user_profile = {"id": 101, "username": "alex99", "role": "Analyst"}

# Using .get() to prevent KeyError
salary = user_profile.get("salary", "Not Disclosed")
print("Salary:", salary)

# Using .setdefault() to ensure keys exist without overwriting
user_profile.setdefault("status", "Active")
user_profile.setdefault("role", "Admin")  # Retains "Analyst"
print("Updated Profile:", user_profile)


print("\n=== 2. DICTIONARY MERGING ===")
defaults = {"theme": "light", "notifications": True, "timeout": 30}
user_settings = {"theme": "dark", "timeout": 60}

# Modern merge using union operator |
merged_config = defaults | user_settings
print("Merged Config:", merged_config)


print("\n=== 3. DICTIONARY COMPREHENSION ===")
temperatures_c = {"Berlin": 18, "Tokyo": 25, "New York": 22, "London": 15}
temperatures_f = {
    city: round((temp * 9 / 5) + 32, 1)
    for city, temp in temperatures_c.items()
    if ((temp * 9 / 5) + 32) > 65
}
print("Filtered Temperatures (>65°F):", temperatures_f)


print("\n=== 4. NESTED DICTIONARIES ===")
company = {
    "emp_01": {"name": "Sara", "skills": ["Python", "SQL"], "exp": 4},
    "emp_02": {"name": "David", "skills": ["R", "Tableau"], "exp": 2},
}

# Modifying nested data
company["emp_01"]["skills"].append("Pandas")
print("Sara's Skills:", company["emp_01"]["skills"])


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Character Frequency Counter
text_sample = "data engineering"
char_freq = {}
for ch in text_sample.replace(" ", ""):
    char_freq[ch] = char_freq.get(ch, 0) + 1
print("Q1 Char Frequency:", char_freq)


# Q2 — Dictionary Inversion
id_to_user = {101: "Alice", 102: "Bob", 103: "Charlie"}
user_to_id = {v: k for k, v in id_to_user.items()}
print("Q2 Inverted Dict:", user_to_id)


# Q3 — Threshold Filtering
sales = {"Store_A": 45000, "Store_B": 12000, "Store_C": 67000, "Store_D": 29000}
high_performing = {k: v for k, v in sales.items() if v >= 30000}
print("Q3 High-Performing Stores:", high_performing)


# Q4 — Nested Field Extraction
students = {
    "s1": {"name": "Aman", "gpa": 3.8},
    "s2": {"name": "Priya", "gpa": 3.2},
    "s3": {"name": "Rohan", "gpa": 3.9},
}
gpas = {info["name"]: info["gpa"] for info in students.values()}
print("Q4 Extracted GPAs:", gpas)


# Q5 — Expense Aggregator
dept_a_expenses = {"travel": 1200, "hardware": 3500, "software": 800}
dept_b_expenses = {"travel": 800, "marketing": 2400, "software": 600}

combined_expenses = dept_a_expenses.copy()
for category, amount in dept_b_expenses.items():
    combined_expenses[category] = combined_expenses.get(category, 0) + amount
print("Q5 Aggregated Expenses:", combined_expenses)


# Q6 — Grouping by Key
names_list = ["Anna", "Bob", "Alice", "Brian", "Charlie", "David"]
grouped_names = {}
for name in names_list:
    first_letter = name[0]
    grouped_names.setdefault(first_letter, []).append(name)
print("Q6 Grouped by Initial:", grouped_names)


# Q7 — In-Stock Inventory Filter
inventory = {"apples": 50, "bananas": 0, "oranges": 12, "grapes": 0}
in_stock = {k: v for k, v in inventory.items() if v > 0}
print("Q7 In-Stock Items:", in_stock)


# Q8 — Top Performer Lookup
player_scores = {"Player1": 88, "Player2": 95, "Player3": 72, "Player4": 91}
top_player = max(player_scores, key=player_scores.get)
print(f"Q8 Top Player: {top_player} ({player_scores[top_player]} pts)")


# Q9 — Deep Config Update
config_base = {
    "server": {"host": "localhost", "port": 8080},
    "debug": False
}
config_base["server"]["port"] = 9000
print("Q9 Updated Port:", config_base["server"]["port"])


# Q10 — Challenge 🔥 (Nested Dict Flattening)
nested_payload = {
    "user": "jdoe",
    "meta": {
        "device": "mobile",
        "ip": "10.0.0.1"
    },
    "active": True
}

flattened_payload = {}
for key, value in nested_payload.items():
    if isinstance(value, dict):
        for sub_key, sub_val in value.items():
            flattened_payload[f"{key}_{sub_key}"] = sub_val
    else:
        flattened_payload[key] = value

print("Q10 Flattened Payload:\n", flattened_payload)
