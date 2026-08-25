# ==========================================
# Day 20 — Advanced Loop Practice
# Script: advanced_loops.py
# ==========================================

print("=== 1. BREAK, CONTINUE & PASS ===")
filtered_numbers = []
for num in range(1, 15):
    if num % 3 == 0:
        continue  # Skip multiples of 3
    if num > 10:
        break     # Stop when exceeding 10
    filtered_numbers.append(num)
print("Filtered output:", filtered_numbers)


print("\n=== 2. FOR-ELSE SEARCH PATTERN ===")
def check_prime(number):
    if number < 2:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            print(f"{number} is composite (divisible by {n})")
            break
    else:
        print(f"{number} is PRIME")

check_prime(47)
check_prime(49)


print("\n=== 3. ZIP & ENUMERATE ===")
departments = ["Analytics", "Engineering", "Design"]
headcounts = [12, 45, 8]

# Parallel iteration
for dept, count in zip(departments, headcounts):
    print(f"Dept: {dept:<12} | Headcount: {count}")

# Indexed iteration
print("\nIndexed Menu:")
for idx, dept in enumerate(departments, start=1):
    print(f"{idx}. {dept}")


print("\n=== 4. NESTED MATRIX TRANSPOSE ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = []
for c in range(len(matrix[0])):
    new_row = []
    for r in range(len(matrix)):
        new_row.append(matrix[r][c])
    transposed.append(new_row)

print("Original Matrix:", matrix)
print("Transposed Matrix:", transposed)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Prime Search with for-else
target_q1 = 47
for i in range(2, target_q1):
    if target_q1 % i == 0:
        print(f"Q1 {target_q1} is not prime")
        break
else:
    print(f"Q1 {target_q1} is prime")


# Q2 — Parallel Cohort Pairing
students = ["Aman", "Sara", "Rohan"]
scores = [88, 92, 79]
print("Q2 Paired Cohort:")
for name, score in zip(students, scores):
    print(f"   Student: {name} | Score: {score}")


# Q3 — Skip & Stop
q3_result = []
for x in range(1, 21):
    if x % 3 == 0:
        continue
    if x > 16:
        break
    q3_result.append(x)
print("Q3 Skip & Stop Result:", q3_result)


# Q4 — Indexed Feature Map
cols = ["id", "timestamp", "target", "prediction"]
print("Q4 Schema Map:")
for idx, col_name in enumerate(cols, start=1):
    print(f"   Column {idx}: {col_name}")


# Q5 — Transpose a 3x3 Matrix
mat3x3 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
mat_trans = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        mat_trans[j][i] = mat3x3[i][j]
print("Q5 Transposed 3x3:", mat_trans)


# Q6 — Dictionary of Lists Traversal
dept_skills = {
    "DS": ["Python", "SQL"],
    "DevOps": ["Docker", "K8s"]
}
print("Q6 Department Skills:")
for dept, skills_list in dept_skills.items():
    for sk in skills_list:
        print(f"   [{dept}] -> {sk}")


# Q7 — Star Pyramid Pattern
rows = 5
print("Q7 Centered Pyramid:")
for r in range(rows):
    spaces = " " * (rows - r - 1)
    stars = "*" * (2 * r + 1)
    print(f"   {spaces}{stars}")


# Q8 — Consecutive Duplicate Remover
data_q8 = [1, 2, 2, 3, 4, 4, 4, 5, 1, 1]
deduped = []
for item in data_q8:
    if not deduped or item != deduped[-1]:
        deduped.append(item)
print("Q8 Consecutive Deduplicated:", deduped)


# Q9 — Retry Mechanism Simulation
retries = 3
success = False
print("Q9 Simulating Network Calls:")
while retries > 0:
    print(f"   Attempting connection... ({retries} retries left)")
    # Simulating a failure on first two tries, success on 3rd
    if retries == 1:
        success = True
        print("   Connection established successfully.")
        break
    retries -= 1
else:
    print("   Connection failed: Exhausted all retries.")


# Q10 — Challenge 🔥 (Multi-Level Validation & Early Exit)
txs = [
    {"id": 101, "items": [10, 20, 15]},
    {"id": 102, "items": [5, -2, 30]},
    {"id": 103, "items": [50, 40]}
]

audit_log = {}
for tx in txs:
    tx_id = tx["id"]
    for amount in tx["items"]:
        if amount < 0:
            audit_log[tx_id] = "CORRUPT"
            break  # Break inner loop immediately upon invalid entry
    else:
        audit_log[tx_id] = "VALID"

print("Q10 Transaction Audit Results:", audit_log)