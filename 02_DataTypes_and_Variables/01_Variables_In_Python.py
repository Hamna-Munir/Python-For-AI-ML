# Topic: Variables in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What is a Variable in Python?

# ➤ A variable is a name that stores a value in the computer’s memory.
# ➤ It acts as a container to hold data that can be used or changed later.
# ➤ In Python, you don’t need to declare the type of a variable — it’s
#   automatically determined when you assign a value.
# ➤ Variables make code reusable, readable, and flexible.

# Example:
x = 10
print(x)
# Output: 10


# ----------------------------------------------------------
#   Rules for Naming Variables
# ----------------------------------------------------------
# 1. Variable names can contain letters (A–Z, a–z), digits (0–9), and underscores (_).
# 2. They must start with a letter or underscore, not a number.
# 3. They are case-sensitive (Age and age are different variables).
# 4. No special symbols allowed (!, @, #, $, %, etc.).
# 5. Avoid using Python keywords (like "for", "if", "class", etc.) as variable names.

# Valid variable names
student_name = "Hamna"
_age = 20
user1 = "AI Learner"

# Invalid examples (will cause errors)
# 1name = "Hamna"
# user-name = "AI"
# class = "Python"


# ----------------------------------------------------------
#   Variable Assignment in Python
# ----------------------------------------------------------
# You can assign values to variables using the equals sign (=).

a = 5
b = 10
c = a + b
print(c)
# Output: 15


# Multiple assignments in one line
x, y, z = 1, 2, 3
print(x, y, z)
# Output: 1 2 3

# Assigning the same value to multiple variables
p = q = r = 100
print(p, q, r)
# Output: 100 100 100


# ----------------------------------------------------------
#   Changing Variable Values
# ----------------------------------------------------------
# Variables can be reassigned at any time.

language = "Python"
print(language)
# Output: Python

language = "Java"
print(language)
# Output: Java


# ----------------------------------------------------------
#   Dynamic Typing in Python
# ----------------------------------------------------------
# ➤ Python is dynamically typed, meaning you can change the type of a variable.
# ➤ The same variable can store different data types at different times.

x = 10        # integer
print(x)
# Output: 10

x = "Hamna"   # string
print(x)
# Output: Hamna


# ----------------------------------------------------------
#   Memory Reference (How Variables Work Internally)
# ----------------------------------------------------------
# Each variable is a name pointing to an object stored in memory.
# Use the id() function to see the memory address (unique identifier).

a = 5
b = 5
print(id(a))
print(id(b))
# Output: (same ID for both because Python optimizes small integers)


# ----------------------------------------------------------
#   Constants in Python
# ----------------------------------------------------------
# Python doesn’t have true constants, but by convention,
# we use uppercase letters for values that should not change.

PI = 3.14159
GRAVITY = 9.8
print(PI, GRAVITY)
# Output: 3.14159 9.8


# ----------------------------------------------------------
#   Best Practices for Variables
# ----------------------------------------------------------
# ✔ Use meaningful names (e.g., age, total_score, user_name)
# ✔ Follow snake_case convention for multi-word names.
# ✔ Keep names short but descriptive.
# ✔ Use uppercase for constants.
# ✔ Avoid single-letter names (except for short loops or math).

# Example of clear and meaningful variables:
student_name = "Hamna Munir"
student_age = 20
course_enrolled = "AI/ML Fundamentals"

print("Name:", student_name)
print("Age:", student_age)
print("Course:", course_enrolled)
# Output:
# Name: Hamna Munir
# Age: 20
# Course: AI/ML Fundamentals


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Variables store data for use and modification.
# - No need to declare type; Python detects it automatically.
# - Variable names must follow rules (start with letter/underscore, etc.).
# - You can reassign variables or change their type.
# - Use meaningful names and uppercase for constants.
# ----------------------------------------------------------
