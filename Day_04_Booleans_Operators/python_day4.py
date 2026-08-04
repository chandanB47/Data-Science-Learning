# ===========================================
# DAY 04 - BOOLEANS & OPERATORS
# ===========================================

# Boolean Values

print("=== Boolean Values ===")

print(True)
print(False)

print(type(True))


# bool()

print("\n=== bool() ===")

print(bool(10))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1]))


# Comparison Operators

print("\n=== Comparison Operators ===")

a = 20
b = 15

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# Arithmetic Operators

print("\n=== Arithmetic Operators ===")

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)


# Assignment Operators

print("\n=== Assignment Operators ===")

number = 10

number += 5
print(number)

number -= 3
print(number)

number *= 2
print(number)


# Logical Operators

print("\n=== Logical Operators ===")

age = 22
salary = 45000

print(age > 18 and salary > 30000)
print(age > 25 or salary > 30000)
print(not(age > 18))


# Membership Operators

print("\n=== Membership Operators ===")

skills = ["Python", "SQL", "Power BI"]

print("Python" in skills)
print("Excel" in skills)
print("Excel" not in skills)


# Identity Operators

print("\n=== Identity Operators ===")

a = [1,2,3]
b = a
c = [1,2,3]

print(a is b)
print(a is c)
print(a == c)


# Operator Precedence

print("\n=== Operator Precedence ===")

result = 10 + 5 * 2

print(result)


# Mini Example

print("\n=== Eligibility ===")

age = int(input("Enter age: "))

print(age >= 18)

print("\n===== Day 04 Completed =====")





