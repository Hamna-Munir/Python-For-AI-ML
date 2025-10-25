# ============================================================
#  01_Built_in_Modules_In_Python.py
# ============================================================
# 🔹 Topic: Built-in Modules in Python
# 🔹 Author: Hamna Munir
# 🔹 Description:
#   This file covers the concept of built-in modules in Python,
#   their usage, and examples of some commonly used modules.
# ============================================================


# ============================================================
# 🔸 1. Introduction
# ============================================================
"""
✅ What are Built-in Modules?

- Built-in modules are modules that come pre-installed with Python.
- You don’t need to install them separately using pip.
- They provide ready-made functions and classes for performing
  common programming tasks like math operations, random numbers,
  date/time handling, etc.

To use a built-in module:
    import module_name
"""

# Example:
import math
import random
import datetime
import os
import sys


# ============================================================
# 🔸 2. math Module
# ============================================================
"""
The math module provides mathematical functions like square root,
power, trigonometric operations, etc.
"""

print("📘 math Module Examples:")
print("Square root of 16:", math.sqrt(16))
print("Power (2^5):", math.pow(2, 5))
print("Ceiling of 3.2:", math.ceil(3.2))
print("Floor of 3.8:", math.floor(3.8))
print("Pi value:", math.pi)
print("-" * 50)


# ============================================================
# 🔸 3. random Module
# ============================================================
"""
The random module is used to generate random numbers or select random items.
"""

print("🎲 random Module Examples:")
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))
print("Shuffling a list:")
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print("Shuffled list:", items)
print("-" * 50)


# ============================================================
# 🔸 4. datetime Module
# ============================================================
"""
The datetime module deals with dates and times.
"""

print("⏰ datetime Module Examples:")
current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)
print("Current Year:", current_time.year)
print("Current Month:", current_time.month)
print("Today's Date:", datetime.date.today())
print("-" * 50)


# ============================================================
# 🔸 5. os Module
# ============================================================
"""
The os module allows interaction with the operating system,
like creating folders, listing files, and accessing environment variables.
"""

print("💻 os Module Examples:")
print("Current Working Directory:", os.getcwd())
print("List of files in current directory:", os.listdir())
print("-" * 50)


# ============================================================
# 🔸 6. sys Module
# ============================================================
"""
The sys module provides functions and variables used to manipulate
different parts of the Python runtime environment.
"""

print("🧠 sys Module Examples:")
print("Python version:", sys.version)
print("System platform:", sys.platform)
print("Command-line arguments:", sys.argv)
print("-" * 50)


# ============================================================
# 🔸 7. Summary
# ============================================================
"""
📘 Summary of Common Built-in Modules:

| Module   | Purpose                                   |
|-----------|-------------------------------------------|
| math      | Mathematical operations                   |
| random    | Random number generation                  |
| datetime  | Date and time handling                    |
| os        | Interacting with the operating system      |
| sys       | Accessing system-specific parameters       |

✅ Tip:
You can see all available built-in modules by typing:
    help('modules')
in your Python shell.
"""

# ============================================================
# 🔹 END OF FILE
# ============================================================
