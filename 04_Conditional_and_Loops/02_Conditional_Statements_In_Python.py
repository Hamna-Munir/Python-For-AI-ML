# Topic: Conditional Statement in Python
# --------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------
# Description:
# This script explains Conditional Statements in Python.
# Conditional statements are used to make decisions in a program
# based on certain conditions (True or False).

# --------------------------------------
# 1. IF STATEMENT
# --------------------------------------
# The 'if' statement runs a block of code only when its condition is True.

age = 20
if age >= 18:
    print("You are eligible to vote.")
# Output: You are eligible to vote.

# --------------------------------------
# 2. IF-ELSE STATEMENT
# --------------------------------------
# The 'else' block runs when the condition in 'if' is False.

marks = 45
if marks >= 50:
    print("You passed the test.")
else:
    print("You failed the test.")
# Output: You failed the test.

# --------------------------------------
# 3. IF-ELIF-ELSE STATEMENT
# --------------------------------------
# Used when multiple conditions need to be checked in sequence.

temperature = 30

if temperature > 35:
    print("It's a very hot day.")
elif temperature > 25:
    print("It's a warm day.")
elif temperature > 15:
    print("It's a pleasant day.")
else:
    print("It's cold outside.")
# Output: It's a warm day.

# --------------------------------------
# 4. NESTED IF STATEMENT
# --------------------------------------
# You can use one 'if' statement inside another to test multiple conditions.

number = 10

if number >= 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")
# Output: The number is positive and even.

# --------------------------------------
# 5. SHORT-HAND IF STATEMENT
# --------------------------------------
# Used to write an 'if' condition in a single line.

x = 7
if x > 5: print("x is greater than 5")
# Output: x is greater than 5

# --------------------------------------
# 6. SHORT-HAND IF-ELSE STATEMENT
# --------------------------------------
# Also known as a Ternary Operator.
# Syntax: [value_if_true] if [condition] else [value_if_false]

a = 12
b = 20
print("a is greater") if a > b else print("b is greater")
# Output: b is greater

# --------------------------------------
# 7. MULTIPLE CONDITIONS WITH 'AND' / 'OR'
# --------------------------------------
# You can combine conditions using logical operators 'and' or 'or'.

score = 85

if score >= 80 and score <= 100:
    print("Grade: A")
elif score >= 60 and score < 80:
    print("Grade: B")
else:
    print("Grade: C or below")
# Output: Grade: A

# --------------------------------------
# End of Script
# --------------------------------------
