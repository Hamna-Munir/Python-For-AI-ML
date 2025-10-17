# Topic: Control Statement in Python
# ----------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------
# Description:
# This script demonstrates Python Control Statements.
# Control Statements allow the program to make decisions and execute code conditionally.

# ----------------------------------
# 1. IF STATEMENT
# ----------------------------------
# The 'if' statement executes a block of code only if a specified condition is True.

age = 20
if age >= 18:
    print("You are eligible to vote.")
# Output: You are eligible to vote.

# ----------------------------------
# 2. IF-ELSE STATEMENT
# ----------------------------------
# The 'else' block executes when the 'if' condition is False.

marks = 40
if marks >= 50:
    print("You passed the exam.")
else:
    print("You failed the exam.")
# Output: You failed the exam.

# ----------------------------------
# 3. IF-ELIF-ELSE STATEMENT
# ----------------------------------
# The 'elif' keyword allows multiple conditions to be checked sequentially.

temperature = 25

if temperature > 30:
    print("It's a hot day.")
elif temperature >= 20:
    print("It's a pleasant day.")
else:
    print("It's a cold day.")
# Output: It's a pleasant day.

# ----------------------------------
# 4. NESTED IF STATEMENT
# ----------------------------------
# An 'if' statement inside another 'if' statement is called nested if.

number = 12
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is negative.")
# Output: The number is positive and even.

# ----------------------------------
# 5. SHORT-HAND IF STATEMENT
# ----------------------------------
# Used when you want to write an 'if' statement in a single line.

x = 10
if x > 5: print("x is greater than 5")
# Output: x is greater than 5

# ----------------------------------
# 6. SHORT-HAND IF-ELSE STATEMENT
# ----------------------------------
# Also known as Ternary Operator.
# Syntax: [value_if_true] if [condition] else [value_if_false]

a = 15
b = 20
result = "a is greater" if a > b else "b is greater"
print(result)
# Output: b is greater

# ----------------------------------
# End of Script
# ----------------------------------
