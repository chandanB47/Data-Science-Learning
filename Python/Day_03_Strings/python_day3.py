# ==========================================================
# DAY 03 - PYTHON STRINGS
# ==========================================================


# ----------------------------------------------------------
# 1. Creating Strings
# ----------------------------------------------------------

name = "Chandan B"
city = 'Bengaluru'
course = "Data Science"

print("Name:", name)
print("City:", city)
print("Course:", course)
print("Type:", type(name))


# Multiline String

message = """Python
SQL
Power BI
Machine Learning"""

print("\nMultiline String:")
print(message)


# ----------------------------------------------------------
# 2. String Length
# ----------------------------------------------------------

language = "Python"

print("\nLength:", len(language))


# ----------------------------------------------------------
# 3. String Indexing
# ----------------------------------------------------------

print("\n--- Indexing ---")

print("First character:", language[0])
print("Second character:", language[1])
print("Last character:", language[-1])
print("Second last:", language[-2])


# ----------------------------------------------------------
# 4. String Slicing
# ----------------------------------------------------------

print("\n--- Slicing ---")

print(language[0:3])
print(language[:4])
print(language[2:])
print(language[-3:])


# ----------------------------------------------------------
# 5. Step / Reverse
# ----------------------------------------------------------

print("\n--- Step ---")

print(language[::2])

print("Reverse:", language[::-1])


# ----------------------------------------------------------
# 6. Concatenation
# ----------------------------------------------------------

first_name = "Chandan"
last_name = "B"

full_name = first_name + " " + last_name

print("\nFull Name:", full_name)


# ----------------------------------------------------------
# 7. String Repetition
# ----------------------------------------------------------

word = "Python "

print(word * 3)


# ----------------------------------------------------------
# 8. Case Methods
# ----------------------------------------------------------

text = "python data science"

print("\n--- Case Methods ---")

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())


# ----------------------------------------------------------
# 9. Removing Spaces
# ----------------------------------------------------------

username = "   Chandan B   "

print("\n--- Strip ---")

print("Original:", username)
print("strip():", username.strip())
print("lstrip():", username.lstrip())
print("rstrip():", username.rstrip())


# ----------------------------------------------------------
# 10. Replace
# ----------------------------------------------------------

sentence = "I am learning Python"

new_sentence = sentence.replace("Python", "Data Science")

print("\nOriginal:", sentence)
print("Replaced:", new_sentence)


# ----------------------------------------------------------
# 11. Find
# ----------------------------------------------------------

text = "Python is useful for Data Science"

print("\nPython position:", text.find("Python"))
print("Data position:", text.find("Data"))
print("Java position:", text.find("Java"))


# ----------------------------------------------------------
# 12. Count
# ----------------------------------------------------------

word = "banana"

print("\nNumber of a:", word.count("a"))
print("Number of n:", word.count("n"))


# ----------------------------------------------------------
# 13. Membership
# ----------------------------------------------------------

course = "Data Science with Python"

print("\n--- Membership ---")

print("Python" in course)
print("Java" in course)
print("SQL" not in course)


# ----------------------------------------------------------
# 14. startswith() / endswith()
# ----------------------------------------------------------

filename = "sales_data.csv"

print("\nStarts with sales:", filename.startswith("sales"))
print("CSV file:", filename.endswith(".csv"))


# ----------------------------------------------------------
# 15. split()
# ----------------------------------------------------------

skills = "Python,SQL,Power BI,Excel"

skills_list = skills.split(",")

print("\nSkills:", skills_list)


# ----------------------------------------------------------
# 16. join()
# ----------------------------------------------------------

joined_skills = " | ".join(skills_list)

print("Joined:", joined_skills)


# ----------------------------------------------------------
# 17. String Checking Methods
# ----------------------------------------------------------

print("\n--- Checking Methods ---")

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("Python 123".isalnum())


# ----------------------------------------------------------
# 18. f-Strings
# ----------------------------------------------------------

name = "Chandan"
course = "Data Science"
age = 26

print(
    f"\nMy name is {name}, I am {age} years old "
    f"and I am learning {course}."
)


price = 1500
quantity = 3

print(f"Price: ₹{price}")
print(f"Quantity: {quantity}")
print(f"Total: ₹{price * quantity}")


