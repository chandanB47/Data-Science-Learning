# ==========================================
# Day 19 — Python Nested Data Structures
# Script: nested_data_structures.py
# ==========================================

import copy

print("=== 1. CHAINED INDEXING & TRAVERSAL ===")
students = [
    {"id": 1, "name": "Aman", "scores": {"math": 90, "algo": 85}},
    {"id": 2, "name": "Priya", "scores": {"math": 95, "algo": 92}}
]

priya_algo = students[1]["scores"]["algo"]
print("Priya's Algo Score:", priya_algo)


print("\n=== 2. SHALLOW VS DEEP COPYING ===")
original_record = {"cohort": "DS-2026", "modules": ["Python", "SQL"]}

# Deep copy isolation
independent_clone = copy.deepcopy(original_record)
independent_clone["modules"].append("Pandas")

print("Original Modules:", original_record["modules"])
print("Cloned Modules:  ", independent_clone["modules"])


print("\n=== 3. NESTED COMPREHENSIONS ===")
orders = [
    {"order_id": 101, "items": [{"name": "Laptop", "price": 1200}, {"name": "Mouse", "price": 25}]},
    {"order_id": 102, "items": [{"name": "Monitor", "price": 300}, {"name": "Keyboard", "price": 75}]}
]

all_items = [item["name"] for order in orders for item in order["items"]]
print("All Extracted Products:", all_items)


print("\n=== 4. FLATTENING HIERARCHIES ===")
nested_user = {
    "user_id": "U100",
    "profile": {"first_name": "Rohan", "last_name": "Sharma"},
    "location": {"city": "Bengaluru", "country": "India"}
}

flat_user = {
    "user_id": nested_user["user_id"],
    "name": f"{nested_user['profile']['first_name']} {nested_user['profile']['last_name']}",
    "city": nested_user["location"]["city"],
    "country": nested_user["location"]["country"]
}
print("Flat User Record:", flat_user)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Nested Score Retrieval
school_data = {"class_10": {"students": {"s1": {"marks": 88}, "s2": {"marks": 94}}}}
s2_marks = school_data["class_10"]["students"]["s2"]["marks"]
print("Q1 s2 Marks:", s2_marks)


# Q2 — Safe Deep Mutation
config = {"env": "production", "db": {"host": "10.0.0.1", "port": 5432}}
dev_config = copy.deepcopy(config)
dev_config["db"]["host"] = "localhost"
print(f"Q2 Original DB Host: {config['db']['host']} | Dev DB Host: {dev_config['db']['host']}")


# Q3 — Extracting Nested List Elements
catalog = [
    {"category": "Electronics", "products": ["TV", "Radio"]},
    {"category": "Furniture", "products": ["Chair", "Table", "Bed"]}
]
all_products = [prod for entry in catalog for prod in entry["products"]]
print("Q3 All Products:", all_products)


# Q4 — Aggregating Order Totals
customer_orders = [
    {"customer": "Alice", "purchases": [{"cost": 120}, {"cost": 45}]},
    {"customer": "Bob", "purchases": [{"cost": 300}, {"cost": 150}, {"cost": 25}]},
    {"customer": "Charlie", "purchases": [{"cost": 80}]}
]
customer_totals = {
    entry["customer"]: sum(p["cost"] for p in entry["purchases"])
    for entry in customer_orders
}
print("Q4 Customer Totals:", customer_totals)


# Q5 — Filtering Nested Records
employees = [
    {"name": "Anil", "metrics": {"rating": 4.8, "projects": 5}},
    {"name": "Sneha", "metrics": {"rating": 4.2, "projects": 3}},
    {"name": "Vikram", "metrics": {"rating": 4.9, "projects": 8}}
]
top_performers = [emp["name"] for emp in employees if emp["metrics"]["rating"] > 4.5]
print("Q5 Top Performers (>4.5 Rating):", top_performers)


# Q6 — Inverting Dict of Lists
skills_map = {
    "Python": ["Dev1", "Dev2"],
    "SQL": ["Dev1", "Dev3"],
    "Docker": ["Dev2", "Dev3"]
}
dev_to_skills = {}
for skill, devs in skills_map.items():
    for dev in devs:
        dev_to_skills.setdefault(dev, []).append(skill)
print("Q6 Developer to Skills Mapping:", dev_to_skills)


# Q7 — Nested Key Counter
org_tree = {
    "Engineering": {
        "Frontend": ["Alex", "Blake"],
        "Backend": ["Chloe", "Dave", "Elena"]
    },
    "Marketing": {
        "SEO": ["Farah"],
        "Content": ["George", "Hannah"]
    }
}
total_employees = sum(
    len(staff)
    for dept in org_tree.values()
    for staff in dept.values()
)
print("Q7 Total Employees across departments:", total_employees)


# Q8 — Dynamic Nested Extraction
def safe_nested_get(dictionary, path, default=None):
    current = dictionary
    for step in path:
        if isinstance(current, dict) and step in current:
            current = current[step]
        else:
            return default
    return current

sample_api_data = {"user": {"details": {"address": {"pincode": 560001}}}}
pincode = safe_nested_get(sample_api_data, ["user", "details", "address", "pincode"])
missing_val = safe_nested_get(sample_api_data, ["user", "profile", "age"], default="N/A")
print(f"Q8 Extracted Pincode: {pincode}, Missing Value: {missing_val}")


# Q9 — Normalizing Nested Sensor Logs
telemetry_logs = [
    {"sensor": "S1", "payload": {"temp": 24.5, "humidity": 60}, "ts": 1700001},
    {"sensor": "S2", "payload": {"temp": 26.1, "humidity": 55}, "ts": 1700002}
]
normalized_telemetry = [
    {
        "sensor_id": row["sensor"],
        "timestamp": row["ts"],
        "temperature": row["payload"]["temp"],
        "humidity": row["payload"]["humidity"]
    }
    for row in telemetry_logs
]
print("Q9 Normalized Telemetry:", normalized_telemetry)


# Q10 — Challenge 🔥 (E-Commerce Order Normalizer)
raw_ecommerce_payload = {
    "order_id": "ORD-9821",
    "customer": {"name": "Meera Patel", "tier": "Gold"},
    "status": "Shipped",
    "line_items": [
        {"item": "Wireless Keyboard", "unit_price": 50.0, "qty": 1, "discount_pct": 10},
        {"item": "USB-C Cable", "unit_price": 15.0, "qty": 2, "discount_pct": 0},
        {"item": "Ergonomic Mouse", "unit_price": 80.0, "qty": 1, "discount_pct": 15}
    ]
}

normalized_orders = []
for line in raw_ecommerce_payload["line_items"]:
    undiscounted = line["unit_price"] * line["qty"]
    final_price = round(undiscounted * (1 - line["discount_pct"] / 100), 2)
    normalized_orders.append({
        "order_id": raw_ecommerce_payload["order_id"],
        "customer_name": raw_ecommerce_payload["customer"]["name"],
        "customer_tier": raw_ecommerce_payload["customer"]["tier"],
        "item_name": line["item"],
        "quantity": line["qty"],
        "final_price": final_price,
        "status": raw_ecommerce_payload["status"]
    })

print("Q10 Normalized Order Line Items:")
for record in normalized_orders:
    print(" ", record)


    
