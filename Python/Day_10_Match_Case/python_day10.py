# ==========================================================
# DAY 10 - PYTHON MATCH CASE
# Data Science Learning Journey
# ==========================================================

print("========== DAY 10 - MATCH CASE ==========\n")


# ----------------------------------------------------------
# 1. Basic Match
# ----------------------------------------------------------

print("1. Basic Match")

number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Unknown number")


# ----------------------------------------------------------
# 2. Default Case
# ----------------------------------------------------------

print("\n2. Default Case")

choice = 5

match choice:
    case 1:
        print("Option 1")
    case 2:
        print("Option 2")
    case 3:
        print("Option 3")
    case _:
        print("Invalid option")


# ----------------------------------------------------------
# 3. String Matching
# ----------------------------------------------------------

print("\n3. String Matching")

order = "Tea"

match order:
    case "Tea":
        print("Here is your Tea")

    case "Coffee":
        print("Here is your Coffee")

    case "GreenTea":
        print("Here is your Green Tea")

    case _:
        print("We don't have that here")


# ----------------------------------------------------------
# 4. Multiple Patterns
# ----------------------------------------------------------

print("\n4. Multiple Patterns")

day = "Sunday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")

    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")

    case _:
        print("Invalid day")


# ----------------------------------------------------------
# 5. User Input
# ----------------------------------------------------------

print("\n5. User Input")

choice = input("Enter choice (1/2/3): ")

match choice:
    case "1":
        print("Add Record")

    case "2":
        print("View Records")

    case "3":
        print("Exit")

    case _:
        print("Invalid choice")


# ----------------------------------------------------------
# 6. Numeric User Input
# ----------------------------------------------------------

print("\n6. Numeric User Input")

number = int(input("Enter a number from 1 to 3: "))

match number:
    case 1:
        print("You selected One")

    case 2:
        print("You selected Two")

    case 3:
        print("You selected Three")

    case _:
        print("Invalid number")


# ----------------------------------------------------------
# 7. Calculator Menu
# ----------------------------------------------------------

print("\n7. Calculator")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:

    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid operator")


# ----------------------------------------------------------
# 8. Food Menu
# ----------------------------------------------------------

print("\n8. Food Menu")

food = input("Enter food: ")

match food:

    case "Pizza":
        print("Pizza selected")

    case "Burger":
        print("Burger selected")

    case "Biryani":
        print("Biryani selected")

    case "Dosa":
        print("Dosa selected")

    case _:
        print("Food not available")


# ----------------------------------------------------------
# 9. Traffic Signal
# ----------------------------------------------------------

print("\n9. Traffic Signal")

signal = input("Enter signal: ")

match signal:

    case "Red":
        print("Stop")

    case "Yellow":
        print("Ready")

    case "Green":
        print("Go")

    case _:
        print("Invalid signal")


# ----------------------------------------------------------
# 10. Simple ATM Menu
# ----------------------------------------------------------

print("\n10. ATM Menu")

print("1. Check Balance")
print("2. Withdraw")
print("3. Deposit")
print("4. Exit")

atm_choice = int(input("Enter choice: "))

match atm_choice:

    case 1:
        print("Check Balance selected")

    case 2:
        print("Withdraw selected")

    case 3:
        print("Deposit selected")

    case 4:
        print("Thank you")

    case _:
        print("Invalid choice")


# ----------------------------------------------------------
# 11. Match with Condition (Guard)
# ----------------------------------------------------------

print("\n11. Match with Condition")

age = 25

match age:

    case age if age < 18:
        print("Minor")

    case age if age >= 18 and age < 60:
        print("Adult")

    case age if age >= 60:
        print("Senior Citizen")


# ----------------------------------------------------------
# 12. Comparison with IF / ELIF
# ----------------------------------------------------------

print("\n12. Match vs If")

choice = 2

# match is useful for fixed choices

match choice:

    case 1:
        print("Add")

    case 2:
        print("View")

    case 3:
        print("Delete")

    case _:
        print("Invalid")


# ==========================================================
# DAY 10 COMPLETED
# ==========================================================

print("\n========== DAY 10 COMPLETED ==========")



