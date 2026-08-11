# ==========================================================
# DAY 09 - PYTHON IF / ELSE
# Data Science Learning Journey
# ==========================================================


# ----------------------------------------------------------
# 1. Simple IF
# ----------------------------------------------------------

print("1. Simple IF")

age = 25

if age >= 18:
    print("You are an adult")


# ----------------------------------------------------------
# 2. IF / ELSE
# ----------------------------------------------------------

print("\n2. IF / ELSE")

age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# ----------------------------------------------------------
# 3. IF / ELIF / ELSE
# ----------------------------------------------------------

print("\n3. IF / ELIF / ELSE")

marks = 82

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# ----------------------------------------------------------
# 4. Positive / Negative / Zero
# ----------------------------------------------------------

print("\n4. Number Check")

number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ----------------------------------------------------------
# 5. Even / Odd
# ----------------------------------------------------------

print("\n5. Even / Odd")

number = 25

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ----------------------------------------------------------
# 6. AND Operator
# ----------------------------------------------------------

print("\n6. AND")

age = 25
salary = 50000

if age >= 21 and salary >= 30000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# ----------------------------------------------------------
# 7. OR Operator
# ----------------------------------------------------------

print("\n7. OR")

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")


# ----------------------------------------------------------
# 8. NOT Operator
# ----------------------------------------------------------

print("\n8. NOT")

logged_in = False

if not logged_in:
    print("Please login")


# ----------------------------------------------------------
# 9. Nested IF
# ----------------------------------------------------------

print("\n9. Nested IF")

age = 25
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")

else:
    print("Under age")


# ----------------------------------------------------------
# 10. String Condition
# ----------------------------------------------------------

print("\n10. String Condition")

course = "Python"

if course == "Python":
    print("Python course selected")
else:
    print("Different course selected")


# ----------------------------------------------------------
# 11. Membership Condition
# ----------------------------------------------------------

print("\n11. Membership")

skills = ["Python", "SQL", "Power BI"]

skill = "Python"

if skill in skills:
    print("Skill found")
else:
    print("Skill not found")


# ----------------------------------------------------------
# 12. Empty / Non-empty List
# ----------------------------------------------------------

print("\n12. Truthy / Falsy")

items = []

if items:
    print("List contains items")
else:
    print("List is empty")


# ----------------------------------------------------------
# 13. Discount Calculator
# ----------------------------------------------------------

print("\n13. Discount")

amount = 6000

if amount >= 5000:
    discount = amount * 10 / 100
else:
    discount = 0

final_amount = amount - discount

print("Original Amount:", amount)
print("Discount:", discount)
print("Final Amount:", final_amount)


# ----------------------------------------------------------
# 14. User Input
# ----------------------------------------------------------

print("\n14. User Input")

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")


# ----------------------------------------------------------
# 15. Login System
# ----------------------------------------------------------

print("\n15. Login")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


# ----------------------------------------------------------
# 16. Nested Business Example
# ----------------------------------------------------------

print("\n16. Employee Bonus")

salary = float(input("Enter salary: "))
performance = input("Enter performance (good/bad): ")

if salary >= 50000:

    if performance == "good":
        bonus = salary * 10 / 100
        print("Bonus:", bonus)

    else:
        bonus = salary * 5 / 100
        print("Bonus:", bonus)

else:

    if performance == "good":
        bonus = salary * 5 / 100
        print("Bonus:", bonus)

    else:
        bonus = 0
        print("No Bonus")

print("Final Salary:", salary + bonus)


# ----------------------------------------------------------
# 17. Conditional Expression
# ----------------------------------------------------------

print("\n17. Conditional Expression")

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)


# ==========================================================
# DAY 09 COMPLETED
# ==========================================================

print("\n========== DAY 09 COMPLETED ==========")







