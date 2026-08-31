# ==========================================
# Day 24 — Python Lambda Functions
# Script: lambda_functions.py
# ==========================================

print("=== 1. BASIC & MULTI-ARGUMENT LAMBDAS ===")
add_numbers = lambda a, b: a + b
linear_eqn = lambda m, x, c: (m * x) + c

print("Sum (15 + 27):", add_numbers(15, 27))
print("Linear Equation (m=3, x=5, c=10):", linear_eqn(3, 5, 10))


print("\n=== 2. TERNARY CONDITIONS IN LAMBDAS ===")
anomaly_detector = lambda val, threshold: "ANOMALY" if val > threshold else "NORMAL"

print("Score 85 (thresh 80):", anomaly_detector(85, 80))
print("Score 75 (thresh 80):", anomaly_detector(75, 80))


print("\n=== 3. CUSTOM SORTING WITH LAMBDA KEYS ===")
candidates = [
    {"name": "Sneha", "experience": 5, "score": 92},
    {"name": "Vikram", "experience": 8, "score": 85},
    {"name": "Anil", "experience": 3, "score": 96}
]

# Sort by score descending
by_score = sorted(candidates, key=lambda c: c["score"], reverse=True)
print("Ranked by Score:")
for cand in by_score:
    print(f"  {cand['name']}: {cand['score']} pts")


print("\n=== 4. MULTI-LEVEL SORTING ===")
# Primary: experience ascending; Secondary: score descending (using negative score)
multi_sort = sorted(
    candidates, 
    key=lambda c: (c["experience"], -c["score"])
)
print("Sorted by Experience (asc) then Score (desc):", multi_sort)


print("\n=== 5. LAMBDA FACTORIES (CLOSURES) ===")
def create_power_scaler(exponent):
    return lambda base: base ** exponent

square_scaler = create_power_scaler(2)
cube_scaler = create_power_scaler(3)

print("4 squared:", square_scaler(4))
print("4 cubed:  ", cube_scaler(4))


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Inline Arithmetic
triangle_area = lambda base, height: 0.5 * base * height
print("Q1 Triangle Area (b=10, h=6):", triangle_area(10, 6))


# Q2 — Ternary Normalization
cap_value = lambda x: 100 if x > 100 else x
print("Q2 Capped 125:", cap_value(125))
print("Q2 Capped 85: ", cap_value(85))


# Q3 — Sorting Tuples by Second Element
coordinates = [(1, 9), (5, 2), (0, 7), (4, 4)]
sorted_coords = sorted(coordinates, key=lambda pt: pt[1])
print("Q3 Coordinates sorted by Y:", sorted_coords)


# Q4 — Sorting Dictionaries by Nested Key
products = [
    {"id": "P1", "pricing": {"unit_price": 450, "currency": "USD"}},
    {"id": "P2", "pricing": {"unit_price": 120, "currency": "USD"}},
    {"id": "P3", "pricing": {"unit_price": 890, "currency": "USD"}}
]
sorted_products = sorted(products, key=lambda item: item["pricing"]["unit_price"])
print("Q4 Products sorted by Price:", [p["id"] for p in sorted_products])


# Q5 — Case-Insensitive String Sorting
words = ["banana", "Apple", "cherry", "Date"]
case_insensitive = sorted(words, key=lambda w: w.lower())
print("Q5 Case-Insensitive Words:", case_insensitive)


# Q6 — Lambda Multiplier Factory
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
print("Q6 Multiplier -> Double 14:", double(14), "| Triple 14:", triple(14))


# Q7 — Multi-Key Ranking
students_q7 = [
    ("Aman", 88, 20),
    ("Priya", 94, 22),
    ("Rohan", 88, 19),
    ("Sara", 94, 20)
]
# Grade descending (use -item[1]), age ascending (item[2])
ranked_students = sorted(students_q7, key=lambda s: (-s[1], s[2]))
print("Q7 Ranked Students (Grade desc, Age asc):", ranked_students)


# Q8 — Custom String Length & Alphabetical Tie-Breaker
cities = ["Tokyo", "Berlin", "Paris", "Rome", "London", "Oslo"]
sorted_cities = sorted(cities, key=lambda city: (len(city), city))
print("Q8 Sorted Cities (Length, Alphabetical):", sorted_cities)


# Q9 — Date String Sorter
dates = ["23-08-2026", "15-01-2025", "04-12-2026", "10-08-2026"]
# Split DD-MM-YYYY and sort by (YYYY, MM, DD)
sorted_dates = sorted(
    dates, 
    key=lambda d: (int(d.split("-")[2]), int(d.split("-")[1]), int(d.split("-")[0]))
)
print("Q9 Chronologically Sorted Dates:", sorted_dates)


# Q10 — Challenge 🔥 (Dynamic Metric Sorter & Ranker)
def rank_models(model_records, metric_name, ascending=False):
    sorted_records = sorted(
        model_records, 
        key=lambda m: m["metrics"].get(metric_name, 0), 
        reverse=not ascending
    )
    
    ranked_output = []
    for rank_idx, record in enumerate(sorted_records, start=1):
        ranked_output.append({
            "rank": rank_idx,
            "model": record["name"],
            metric_name: record["metrics"].get(metric_name)
        })
    return ranked_output

model_benchmarks = [
    {"name": "RandomForest", "metrics": {"accuracy": 0.88, "f1": 0.86}},
    {"name": "XGBoost",      "metrics": {"accuracy": 0.94, "f1": 0.93}},
    {"name": "LogisticReg",  "metrics": {"accuracy": 0.81, "f1": 0.80}},
    {"name": "LightGBM",     "metrics": {"accuracy": 0.92, "f1": 0.91}}
]

print("Q10 Ranked Models by F1-Score:")
for entry in rank_models(model_benchmarks, "f1"):
    print(" ", entry)

    