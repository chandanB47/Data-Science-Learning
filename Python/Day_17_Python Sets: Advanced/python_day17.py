# ==========================================
# Day 17 — Python Sets: Advanced
# Script: sets_advanced.py
# ==========================================

print("=== 1. ELEMENT MANAGEMENT & SAFE DELETION ===")
skills = {"Python", "SQL", "Pandas"}

# Safe removal using discard
skills.discard("Java")  # No error raised

# Batch update
skills.update(["NumPy", "Git", "SQL"])
print("Updated Skills:", skills)


print("\n=== 2. MATHEMATICAL SET OPERATIONS ===")
group_a = {"Python", "SQL", "Tableau", "Excel"}
group_b = {"Python", "R", "Tableau", "PowerBI"}

print("Union (All):", group_a | group_b)
print("Intersection (Common):", group_a & group_b)
print("Difference (A only):", group_a - group_b)
print("Symmetric Difference (Non-overlapping):", group_a ^ group_b)


print("\n=== 3. SET RELATIONSHIPS ===")
core_reqs = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "Docker", "AWS"}

print("Is subset?:", core_reqs.issubset(candidate_skills))
print("Is superset?:", candidate_skills.issuperset(core_reqs))

banned_ips = {"10.0.0.1", "192.168.1.1"}
active_ips = {"172.16.0.5", "192.168.1.50"}
print("Is disjoint (No overlaps)?:", banned_ips.isdisjoint(active_ips))


print("\n=== 4. SET COMPREHENSIONS & FROZENSET ===")
words = ["data", "science", "python", "ai", "data", "ml"]
unique_lengths = {len(w) for w in words}
print("Unique Word Lengths:", unique_lengths)

immutable_ids = frozenset(["USR_01", "USR_02", "USR_03"])
print("Frozenset:", immutable_ids)


# ==========================================
# PRACTICE QUESTIONS SOLUTIONS (Q1 - Q10)
# ==========================================

print("\n" + "=" * 40)
print("PRACTICE SOLUTIONS (Q1 - Q10)")
print("=" * 40)

# Q1 — Deduplication with Preserved Uniqueness
raw_ids = [101, 102, 103, 101, 104, 102, 105]
unique_ids = set(raw_ids)
print("Q1 Unique IDs:", unique_ids)


# Q2 — Safe Element Removal
tags = {"data", "python", "ml"}
tags.discard("deep_learning")
tags.discard("ml")
print("Q2 Tags after discard:", tags)


# Q3 — Common Customers (Intersection)
cohort_jan = {"c1", "c2", "c3", "c4"}
cohort_feb = {"c3", "c4", "c5", "c6"}
retained_customers = cohort_jan & cohort_feb
print("Q3 Retained Customers (Jan & Feb):", retained_customers)


# Q4 — Churn Analysis (Difference)
churned_customers = cohort_jan - cohort_feb
print("Q4 Churned Customers (Jan only):", churned_customers)


# Q5 — Unique Platform Users (Symmetric Difference)
mobile_users = {"u1", "u2", "u3"}
web_users = {"u2", "u3", "u4"}
single_platform_users = mobile_users ^ web_users
print("Q5 Single Platform Users:", single_platform_users)


# Q6 — Subset Verification
mandatory_modules = {"Mod1", "Mod2"}
completed_modules = {"Mod1", "Mod2", "Mod3", "Mod4"}
requirements_met = mandatory_modules.issubset(completed_modules)
print("Q6 Mandatory Requirements Met?:", requirements_met)


# Q7 — Set Comprehension (Even Squares)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x ** 2 for x in nums if x % 2 == 0}
print("Q7 Even Squares Set:", even_squares)


# Q8 — Unique Vocabulary Extraction
sentence_sample = "data science is great and data analytics is powerful"
unique_vocab = set(sentence_sample.lower().split())
print("Q8 Unique Vocabulary:", unique_vocab)


# Q9 — Disjoint Check
banned = {"192.168.1.1", "10.0.0.1"}
session_ips = {"172.16.0.5", "192.168.1.50"}
is_secure = banned.isdisjoint(session_ips)
print("Q9 Zero Banned IPs Active?:", is_secure)


# Q10 — Challenge 🔥 (Jaccard Similarity Coefficient)
sentence_a = "machine learning and data science"
sentence_b = "data science and deep learning"

words_a = set(sentence_a.lower().split())
words_b = set(sentence_b.lower().split())

intersection = len(words_a & words_b)
union = len(words_a | words_b)
jaccard_score = intersection / union

print(f"Q10 Words A: {words_a}")
print(f"Q10 Words B: {words_b}")
print(f"Q10 Jaccard Similarity: {jaccard_score:.4f} ({jaccard_score:.2%})")






