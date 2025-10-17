# Topic: Operators in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What are Operators in Python?

# ➤ Operators are special symbols or keywords used to perform operations
#   on values and variables (operands).
# ➤ Example: +, -, *, /, ==, >, and, or, etc.
# ➤ Python supports several types of operators for different tasks.

# ----------------------------------------------------------
#   Types of Operators in Python
# ----------------------------------------------------------
# 1. Arithmetic Operators
# 2. Comparison (Relational) Operators
# 3. Assignment Operators
# 4. Logical Operators
# 5. Bitwise Operators
# 6. Membership Operators
# 7. Identity Operators
# ----------------------------------------------------------


# ----------------------------------------------------------
#   1. Arithmetic Operators
# ----------------------------------------------------------
# ➤ Used to perform mathematical calculations.

a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3 (removes decimal part)
print("Modulus:", a % b)         # 1 (remainder)
print("Exponentiation:", a ** b) # 1000 (10³)
# ----------------------------------------------------------


# ----------------------------------------------------------
#   2. Comparison (Relational) Operators
# ----------------------------------------------------------
# ➤ Used to compare two values.
# ➤ The result is always Boolean (True or False).

x = 5
y = 8

print("Equal:", x == y)           # False
print("Not Equal:", x != y)       # True
print("Greater than:", x > y)     # False
print("Less than:", x < y)        # True
print("Greater or Equal:", x >= y)# False
print("Less or Equal:", x <= y)   # True
# ----------------------------------------------------------


# ----------------------------------------------------------
#   3. Assignment Operators
# ----------------------------------------------------------
# ➤ Used to assign and update values in variables.

num = 10
num += 5   # num = num + 5
print("After += :", num)  # 15

num -= 3   # num = num - 3
print("After -= :", num)  # 12

num *= 2   # num = num * 2
print("After *= :", num)  # 24

num /= 4   # num = num / 4
print("After /= :", num)  # 6.0

num //= 2  # num = num // 2
print("After //= :", num) # 3.0

num **= 3  # num = num ** 3
print("After **= :", num) # 27.0

num %= 5   # num = num % 5
print("After %= :", num)  # 2.0
# ----------------------------------------------------------


# ----------------------------------------------------------
#   4. Logical Operators
# ----------------------------------------------------------
# ➤ Used to combine multiple conditions.
# ➤ Returns True or False.

a = 10
b = 5
c = 0

print("and Operator:", a > b and b > c)  # True
print("or Operator:", a > b or b < c)    # True
print("not Operator:", not(a < b))       # True
# ----------------------------------------------------------


# ----------------------------------------------------------
#   5. Bitwise Operators
# ----------------------------------------------------------
# ➤ Used to perform operations on binary numbers (bit-level).

x = 5   # 0101
y = 3   # 0011

print("Bitwise AND:", x & y)   # 1 (0001)
print("Bitwise OR:", x | y)    # 7 (0111)
print("Bitwise XOR:", x ^ y)   # 6 (0110)
print("Bitwise NOT:", ~x)      # -6 (inverts bits)
print("Left Shift:", x << 1)   # 10 (1010)
print("Right Shift:", x >> 1)  # 2 (0010)
# ----------------------------------------------------------


# ----------------------------------------------------------
#   6. Membership Operators
# ----------------------------------------------------------
# ➤ Used to check if a value exists in a sequence (string, list, etc.).

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      # True
print(6 not in my_list)  # True

text = "Python"
print('P' in text)       # True
print('z' not in text)   # True
# ----------------------------------------------------------


# ----------------------------------------------------------
#   7. Identity Operators
# ----------------------------------------------------------
# ➤ Used to compare memory locations (object identity).
# ➤ Returns True if both variables point to the same object.

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)       # False (different objects)
print(a is c)       # True  (same object)
print(a is not b)   # True
# ----------------------------------------------------------


# ----------------------------------------------------------
#   Operator Precedence
# ----------------------------------------------------------
# ➤ Defines the order in which operators are evaluated.
# ➤ Example of precedence order:
#   1. ** (Exponent)
#   2. *, /, //, %
#   3. +, -
#   4. Comparison (>, <, ==, etc.)
#   5. Logical (and, or, not)

result = 2 + 3 * 4 ** 2
print(result)
# Output: 50 (because 4**2 = 16 → 3*16=48 → 48+2=50)
# ----------------------------------------------------------


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Operators perform various actions on data.
# - Python has Arithmetic, Comparison, Assignment, Logical, Bitwise,
#   Membership, and Identity operators.
# - Operator precedence defines the execution order.
# - Use parentheses () to make complex expressions clear.
# ----------------------------------------------------------
