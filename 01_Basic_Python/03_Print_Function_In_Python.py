# Topic: The print() Function in Python
# ---------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ---------------------------------------------------------
# Description:
# The print() function is one of the most commonly used functions in Python.
# It is used to display output on the screen. You can print text, numbers,
# variables, or even multiple items at once.
# ---------------------------------------------------------


# -------------------------------
# Example 1: Printing a simple message
# -------------------------------
print("Hello, Python!")  # Output: Hello, Python!


# -------------------------------
# Example 2: Printing multiple items
# -------------------------------
name = "Hamna"
age = 20
print("My name is", name, "and I am", age, "years old.")
# Output: My name is Hamna and I am 20 years old.


# -------------------------------
# Example 3: Using f-strings (formatted strings)
# -------------------------------
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Hamna and I am 20 years old.
# f-strings make it easier to include variables inside strings.


# -------------------------------
# Example 4: Using the 'sep' parameter
# -------------------------------
# The 'sep' parameter defines the separator between multiple items.
print("Python", "For", "AI", "and", "ML", sep="-")
# Output: Python-For-AI-and-ML


# -------------------------------
# Example 5: Using the 'end' parameter
# -------------------------------
# The 'end' parameter changes what is printed at the end of each print statement.
print("Learning", end="... ")
print("Complete!")
# Output: Learning... Complete!


# -------------------------------
# Example 6: Printing multi-line text using triple quotes
# -------------------------------
print("""
Python is fun to learn.
It is powerful for AI and Machine Learning.
Keep practicing!
""")

# -------------------------------
# Example 7: Printing special characters
# -------------------------------
print("Hello\tWorld")   # \t adds a tab space
print("Hello\nWorld")   # \n adds a new line


# -------------------------------
# Example 8: Printing using string concatenation
# -------------------------------
print("Welcome " + name + " to Python Programming!")
# Output: Welcome Hamna to Python Programming!

# ---------------------------------------------------------
# Summary:
# - print() displays output.
# - Use 'sep' and 'end' to control formatting.
# - f-strings are preferred for readable, formatted output.
# ---------------------------------------------------------
