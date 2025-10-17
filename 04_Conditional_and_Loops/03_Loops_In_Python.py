# Topic: Loops in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What are Loops in Python?

# ➤ Loops are control structures that allow us to execute a block of code repeatedly
#   as long as a specified condition is True.
# ➤ They help in automating repetitive tasks and reducing code duplication.
# ➤ Python provides two main types of loops: for loop and while loop.

# ----------------------------------------------------------
#   1. For Loop
# ----------------------------------------------------------
# ➤ A for loop is used to iterate over a sequence (like a list, tuple, string, or range).
# ➤ It automatically goes through each item in the sequence.

# Example: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# Example: Using range() with for loop
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4


# Example: Using range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9


# ----------------------------------------------------------
#   2. While Loop
# ----------------------------------------------------------
# ➤ A while loop runs as long as a condition remains True.
# ➤ Be careful — if the condition never becomes False, it can cause an infinite loop.

# Example:
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
# Output:
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4
# Count is: 5


# Example: Infinite loop (be cautious)
# while True:
#     print("This will run forever!")


# ----------------------------------------------------------
#   3. Loop Control Statements
# ----------------------------------------------------------
# ➤ These statements control the flow of loops:
#     - break: exits the loop completely
#     - continue: skips the current iteration
#     - pass: does nothing (placeholder)

# Example: break statement
for i in range(10):
    if i == 5:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4


# Example: continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output:
# 0
# 1
# 3
# 4


# Example: pass statement
for i in range(3):
    pass  # Placeholder for future code


# ----------------------------------------------------------
#   4. Nested Loops
# ----------------------------------------------------------
# ➤ A loop inside another loop is called a nested loop.
# ➤ Commonly used for working with matrices or patterns.

# Example:
for i in range(3):        # Outer loop
    for j in range(2):    # Inner loop
        print(i, j)
# Output:
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1


# ----------------------------------------------------------
#   5. else Clause with Loops
# ----------------------------------------------------------
# ➤ Python allows an optional else block with loops.
# ➤ The else block runs only if the loop completes normally (without a break).

# Example with for loop
for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")
# Output:
# 0
# 1
# 2
# Loop finished successfully!


# Example with while loop
x = 0
while x < 3:
    print("x =", x)
    x += 1
else:
    print("While loop completed!")
# Output:
# x = 0
# x = 1
# x = 2
# While loop completed!


# ----------------------------------------------------------
#   6. Common Use Cases of Loops
# ----------------------------------------------------------
# ➤ Iterating through lists, dictionaries, or strings
# ➤ Performing repetitive calculations
# ➤ Automating data collection or transformation
# ➤ Implementing algorithms like search, sorting, etc.

# Example: Iterating over a string
for letter in "AI/ML":
    print(letter)
# Output:
# A
# I
# /
# M
# L


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Loops repeat a block of code multiple times.
# - Python has two main loops: for and while.
# - Loop control statements (break, continue, pass) modify loop behavior.
# - Loops can have else clauses and can be nested.
# - Useful for automating repetitive tasks and data processing.
# ----------------------------------------------------------
