# --- Q1: Variables + f-string ---
name = "Chandan B"
age = 26
city = "Bengaluru"
course = "Data Science"

print(f"I am {name}, My age is {age} years old, I live in {city} and I am Learning {course}.")


# --- Q2: Data Types (Without shadowing built-in names) ---
# Renamed variables to avoid overwriting int, float, str, and bool
integer_val = 100
float_val = 0.45
string_val = "Hello"
boolean_val = True

print(integer_val, type(integer_val))
print(float_val, type(float_val))
print(string_val, type(string_val))
print(boolean_val, type(boolean_val))


# --- Q3: User Input & Arithmetic ---
# Using num1 and num2 directly for the calculations instead of hardcoded numbers
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# --- Q4: Type Casting ---

number_str = "500"

# Convert string "500" into integer 500
number_int = int(number_str)

# Add 250 after conversion
result = number_int + 250

print("Original value:", number_str, "| Type:", type(number_str))
print("Converted value:", number_int, "| Type:", type(number_int))
print("Result after adding 250:", result)


# --- Q5: Birth Year / Age Challenge ---
user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

calculated_age = 2026 - birth_year
print(f"Hello {user_name}, you are approximately {calculated_age} years old in 2026.")




