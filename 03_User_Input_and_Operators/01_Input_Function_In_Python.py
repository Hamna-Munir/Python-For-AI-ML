# Topic: Input Function in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What is the input() Function in Python?

# ➤ The input() function allows users to enter data during program execution.
# ➤ It always takes input as a STRING by default.
# ➤ It temporarily pauses the program and waits for the user to type something.
# ➤ After the user presses ENTER, the input is stored in a variable.

# ----------------------------------------------------------
#   Basic Example
# ----------------------------------------------------------
name = input("Enter your name: ")
print("Hello,", name)
# Example Input: Hamna
# Output: Hello, Hamna


# ----------------------------------------------------------
#   How input() Works Internally
# ----------------------------------------------------------
# 1. The message inside input() appears as a prompt.
# 2. Python waits for the user to type and press ENTER.
# 3. The entered value is stored as a STRING.
# 4. You can process or convert it to other types (int, float, etc.).


# ----------------------------------------------------------
#   Example: Input as String
# ----------------------------------------------------------
city = input("Enter your city name: ")
print("You live in", city)
# Example Input: Faisalabad
# Output: You live in Faisalabad


# ----------------------------------------------------------
#   Example: Input as Number (Type Casting)
# ----------------------------------------------------------
# By default, input() returns data as string.
# We must convert it manually using int(), float(), etc.

age = int(input("Enter your age: "))
print("You are", age, "years old.")
# Example Input: 20
# Output: You are 20 years old.

height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")
# Example Input: 1.65
# Output: Your height is 1.65 meters.


# ----------------------------------------------------------
#   Multiple Inputs in a Single Line
# ----------------------------------------------------------
# We can take multiple inputs separated by space using the split() method.

x, y = input("Enter two numbers separated by space: ").split()
print("First Number:", x)
print("Second Number:", y)
# Example Input: 10 20
# Output:
# First Number: 10
# Second Number: 20


# ----------------------------------------------------------
#   Taking Multiple Numeric Inputs
# ----------------------------------------------------------
a, b, c = map(int, input("Enter three numbers separated by space: ").split())
print("Sum =", a + b + c)
# Example Input: 5 10 15
# Output: Sum = 30


# ----------------------------------------------------------
#   Using input() with Expressions
# ----------------------------------------------------------
# You can use input values directly in expressions after converting them.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The product is:", num1 * num2)
# Example Input:
# 5
# 3
# Output: The product is: 15


# ----------------------------------------------------------
#   Example: User Interaction Program
# ----------------------------------------------------------
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

print("\n--- User Profile ---")
print("Name:", name)
print("Age:", age)
print("Country:", country)
# Example Input:
# Hamna Munir
# 20
# Pakistan
# Output:
# --- User Profile ---
# Name: Hamna Munir
# Age: 20
# Country: Pakistan


# ----------------------------------------------------------
#   Important Notes
# ----------------------------------------------------------
# ✔ input() always returns data as string.
# ✔ Use int() or float() for numeric operations.
# ✔ You can use split() to take multiple values at once.
# ✔ You can display formatted messages using f-strings or commas.


# ----------------------------------------------------------
#   Example: Formatted Input/Output
# ----------------------------------------------------------
user = input("Enter your username: ")
score = int(input("Enter your score: "))
print(f"Player {user} scored {score} points!")
# Example Input:
# Hamna
# 95
# Output: Player Hamna scored 95 points!


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - input() is used to take user input during program execution.
# - It always returns data as string.
# - Use type casting (int(), float()) for numeric data.
# - split() can handle multiple inputs.
# - Use f-strings for clean and formatted output.
# ----------------------------------------------------------
