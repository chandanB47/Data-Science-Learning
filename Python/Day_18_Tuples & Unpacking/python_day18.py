# ==========================================
# Day 18 — Python Tuples & Unpacking
# Script: tuples_and_unpacking.py
# ==========================================

from collections import namedtuple

print("=== 1. TUPLE CREATION & TRAILING COMMA ===")
not_a_tuple = ("DataScience")
real_tuple = ("DataScience",)

print(f"not_a_tuple type: {type(not_a_tuple)}")
print(f"real_tuple type:  {type(real_tuple)}")


print("\n=== 2. TUPLE IMMUTABILITY & DICT KEYS ===")
# Tuples as hashable dictionary keys
geo_locations = {
    (37.7749, -122.4194): "San Francisco",
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
san_francisco = geo_locations[(37.7749, -122.4194)]
print("Lookup by coordinate tuple:", san_francisco)


print("\n=== 3. STAR UNPACKING (*REST) ===")
daily_metrics = [1200, 1450, 1100, 1800, 1350, 2100]
first_day, *mid_days, last_day = daily_metrics

print("First Day:", first_day)
print("Middle Days:", mid_days)
print("Last Day:", last_day)


print("\n=== 4. NESTED UNPACKING ===")
dataset_meta = ("Iris_Dataset", (150, 4), ("setosa", "versicolor", "virginica"))
name, (rows, cols), classes = dataset_meta

print(f"Dataset: {name} | Dimensions: {rows}x{cols} | Classes Count: {len(classes)}")


print("\n=== 5. NAMEDTUPLES ===")
Observation = namedtuple("Observation", ["timestamp", "sensor_id", "reading"])
obs1 = Observation("2026-08-23 12:00:00", "SENSOR_A", 24.8)

print("NamedTuple record:", obs1)
print(f"Reading from {obs1.sensor_id}: {obs1.reading}°C")


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Coordinate Swap
x, y = 10, 20
x, y = y, x
print(f"Q1 Swapped: x = {x}, y = {y}")


# Q2 — Boundary Value Extraction
temps = (68, 72, 75, 80, 82, 79, 70)
sorted_temps = sorted(temps)
min_temp, *normal_temps, max_temp = sorted_temps
print(f"Q2 Min: {min_temp}, Max: {max_temp}, Normal Range: {normal_temps}")


# Q3 — Function Multi-Return
def get_stats(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    mean_val = round(sum(numbers) / len(numbers), 2)
    return min_val, max_val, mean_val

data_points = [15, 22, 8, 45, 31, 19]
min_v, max_v, avg_v = get_stats(data_points)
print(f"Q3 Stats -> Min: {min_v}, Max: {max_v}, Average: {avg_v}")


# Q4 — Trailing Comma Check
single_element_tuple = ("DataScience",)
print(f"Q4 Single element is tuple?: {isinstance(single_element_tuple, tuple)}")


# Q5 — Tuple Immutability Proof
immutable_sample = (1, 2, 3)
try:
    immutable_sample[0] = 99
except TypeError as error:
    print("Q5 Caught Expected Exception:", error)


# Q6 — Nested Hierarchy Unpacking
employee_record = ("Emp_101", ("Sales", "North America"), (85000, 12000))
emp_id, (department, region), (base_salary, bonus) = employee_record
print(f"Q6 Unpacked: {emp_id} | Dept: {department} ({region}) | Total Comp: ${base_salary + bonus:,}")


# Q7 — Ignoring Elements with Underscore (_)
log_entry = ("2026-08-23", "ERROR", "DB_CONN_TIMEOUT", "192.168.1.1")
date, _, err_msg, _ = log_entry
print(f"Q7 Extracted Log: Date = {date}, Error = {err_msg}")


# Q8 — Frequency and Indexing
data = (10, 20, 30, 20, 40, 20, 50)
count_20 = data.count(20)
index_40 = data.index(40)
print(f"Q8 Count of 20: {count_20}, First Index of 40: {index_40}")


# Q9 — Dictionary Keys via Tuples
academic_records = {
    (101, "Fall_2026"): 3.85,
    (105, "Fall_2026"): 3.92,
    (105, "Spring_2026"): 3.78,
}
query_gpa = academic_records.get((105, "Fall_2026"), "Not Found")
print(f"Q9 Student 105 Fall 2026 GPA: {query_gpa}")


# Q10 — Challenge 🔥 (Batch Record Processing)
users = [
    ("Alice", 25, "NY"),
    ("Bob", 30, "CA"),
    ("Charlie", 22, "NY"),
    ("Diana", 28, "NY"),
    ("Evan", 21, "TX")
]

ny_qualifying_users = [
    name
    for name, age, city in users
    if city == "NY" and age > 23
]
print("Q10 Qualifying NY Users (>23):", ny_qualifying_users)