# ==========================================================
# DAY 08 - PYTHON DICTIONARIES
# Data Science Learning Journey
# ==========================================================

print("========== DAY 08 - PYTHON DICTIONARIES ==========\n")


# ----------------------------------------------------------
# 1. Creating a Dictionary
# ----------------------------------------------------------

print("1. Creating Dictionary")

student = {
    "name": "Chandan",
    "age": 26,
    "city": "Bengaluru",
    "course": "Data Science"
}

print(student)


# ----------------------------------------------------------
# 2. Accessing Values
# ----------------------------------------------------------

print("\n2. Accessing Values")

print(student["name"])
print(student["age"])
print(student["course"])


# ----------------------------------------------------------
# 3. get()
# ----------------------------------------------------------

print("\n3. get()")

print(student.get("name"))
print(student.get("email"))

# get() returns None if the key doesn't exist.


# ----------------------------------------------------------
# 4. Adding New Items
# ----------------------------------------------------------

print("\n4. Adding Items")

student["email"] = "chandan@example.com"

print(student)


# ----------------------------------------------------------
# 5. Updating Values
# ----------------------------------------------------------

print("\n5. Updating Values")

student["age"] = 27

student["city"] = "Bengaluru"

print(student)


# ----------------------------------------------------------
# 6. update()
# ----------------------------------------------------------

print("\n6. update()")

student.update({
    "course": "Data Science - GEN AI",
    "experience": "Beginner"
})

print(student)


# ----------------------------------------------------------
# 7. keys()
# ----------------------------------------------------------

print("\n7. keys()")

print(student.keys())


# ----------------------------------------------------------
# 8. values()
# ----------------------------------------------------------

print("\n8. values()")

print(student.values())


# ----------------------------------------------------------
# 9. items()
# ----------------------------------------------------------

print("\n9. items()")

print(student.items())


# ----------------------------------------------------------
# 10. Membership
# ----------------------------------------------------------

print("\n10. Membership")

print("name" in student)
print("salary" in student)


# ----------------------------------------------------------
# 11. Loop Through Keys
# ----------------------------------------------------------

print("\n11. Loop Through Keys")

for key in student:
    print(key)


# ----------------------------------------------------------
# 12. Loop Through Values
# ----------------------------------------------------------

print("\n12. Loop Through Values")

for value in student.values():
    print(value)


# ----------------------------------------------------------
# 13. Loop Through Key-Value Pairs
# ----------------------------------------------------------

print("\n13. Loop Through Items")

for key, value in student.items():
    print(key, ":", value)


# ----------------------------------------------------------
# 14. pop()
# ----------------------------------------------------------

print("\n14. pop()")

removed_value = student.pop("experience")

print("Removed:", removed_value)
print(student)


# ----------------------------------------------------------
# 15. popitem()
# ----------------------------------------------------------

print("\n15. popitem()")

removed_item = student.popitem()

print("Removed:", removed_item)
print(student)


# ----------------------------------------------------------
# 16. copy()
# ----------------------------------------------------------

print("\n16. copy()")

student_copy = student.copy()

print("Original:", student)
print("Copy:", student_copy)


# ----------------------------------------------------------
# 17. clear()
# ----------------------------------------------------------

print("\n17. clear()")

temporary_data = {
    "name": "Rahul",
    "age": 25
}

print("Before:", temporary_data)

temporary_data.clear()

print("After:", temporary_data)


# ----------------------------------------------------------
# 18. Dictionary with Different Data Types
# ----------------------------------------------------------

print("\n18. Different Data Types")

data = {
    "name": "Chandan",
    "age": 26,
    "salary": 50000.50,
    "skills": ["Python", "SQL"],
    "active": True
}

print(data)


# ----------------------------------------------------------
# 19. Nested Dictionary
# ----------------------------------------------------------

print("\n19. Nested Dictionary")

students = {
    "student1": {
        "name": "Chandan",
        "age": 26,
        "course": "Data Science"
    },

    "student2": {
        "name": "Rahul",
        "age": 24,
        "course": "Python"
    },

    "student3": {
        "name": "Kiran",
        "age": 25,
        "course": "SQL"
    }
}

print(students)


# Access nested value

print(students["student1"]["name"])
print(students["student2"]["course"])


# ----------------------------------------------------------
# 20. Student Marks
# ----------------------------------------------------------

print("\n20. Student Marks")

marks = {
    "Python": 85,
    "SQL": 90,
    "Statistics": 78,
    "Machine Learning": 88
}

print("Python:", marks["Python"])
print("SQL:", marks["SQL"])

print("Highest:", max(marks.values()))
print("Lowest:", min(marks.values()))

average = sum(marks.values()) / len(marks)

print("Average:", average)


# ----------------------------------------------------------
# 21. Practical Data Record
# ----------------------------------------------------------

print("\n21. Practical Data Record")

employee = {
    "employee_id": 101,
    "name": "Chandan",
    "department": "Data Science",
    "salary": 50000,
    "skills": ["Python", "SQL", "Power BI"],
    "active": True
}

for key, value in employee.items():
    print(f"{key}: {value}")


# ----------------------------------------------------------
# 22. Dictionary from Two Lists
# ----------------------------------------------------------

print("\n22. Two Lists to Dictionary")

keys = ["name", "age", "city"]

values = ["Chandan", 26, "Bengaluru"]

student_data = dict(zip(keys, values))

print(student_data)


# ==========================================================
# DAY 08 COMPLETED
# ==========================================================

print("\n========== DAY 08 COMPLETED ==========")









