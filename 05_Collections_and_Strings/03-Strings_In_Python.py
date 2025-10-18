#   03_Strings_In_Python.py
# ----------------------------------------------------------

# ➤ What is a String in Python?
# A string is a sequence of characters enclosed in single (' '), double (" "), or triple (''' ''' / """ """) quotes.
# Strings are immutable — once created, they cannot be modified.

# ----------------------------------------------------------
#   Creating Strings
# ----------------------------------------------------------

# Using single quotes
single_quote = 'Hello Python'
print(single_quote)  
# Output: Hello Python

# Using double quotes
double_quote = "Hello World"
print(double_quote)  
# Output: Hello World

# Using triple quotes (for multi-line strings)
multi_line = '''This is
a multi-line
string.'''
print(multi_line)
# Output:
# This is
# a multi-line
# string.

# ----------------------------------------------------------
#   Accessing Characters in a String
# ----------------------------------------------------------

text = "Python"

print(text[0])   # Output: P
print(text[5])   # Output: n

# Negative indexing
print(text[-1])  # Output: n
print(text[-6])  # Output: P

# ----------------------------------------------------------
#   String Slicing
# ----------------------------------------------------------

# Syntax: string[start:end:step]
print(text[0:4])   # Output: Pyth
print(text[2:])    # Output: thon
print(text[:3])    # Output: Pyt
print(text[::2])   # Output: Pto
print(text[::-1])  # Output: nohtyP

# ----------------------------------------------------------
#   String Concatenation and Repetition
# ----------------------------------------------------------

greet = "Hello"
name = "Hamna"

print(greet + " " + name)  
# Output: Hello Hamna

print(greet * 3)  
# Output: HelloHelloHello

# ----------------------------------------------------------
#   String Methods
# ----------------------------------------------------------

sample = "  Python Programming  "

print(sample.lower())          # Output: '  python programming  '
print(sample.upper())          # Output: '  PYTHON PROGRAMMING  '
print(sample.strip())          # Output: 'Python Programming'
print(sample.replace("Python", "AI"))  # Output: '  AI Programming  '
print(sample.split())          # Output: ['Python', 'Programming']
print(sample.title())          # Output: '  Python Programming  '

# ----------------------------------------------------------
#   String Membership
# ----------------------------------------------------------

print("Python" in sample)       # Output: True
print("Java" not in sample)     # Output: True

# ----------------------------------------------------------
#   String Formatting
# ----------------------------------------------------------

language = "Python"
version = 3.10

# Using f-string
print(f"I am learning {language} version {version}.")
# Output: I am learning Python version 3.10.

# Using format() method
print("I am learning {} version {}.".format(language, version))
# Output: I am learning Python version 3.10.

# ----------------------------------------------------------
#   Escape Sequences in Strings
# ----------------------------------------------------------

print("Hello\nWorld")            # Output: Hello
                                 #         World
print("This is a tab:\tPython")  # Output: This is a tab:	Python
print("He said, \"Python is great!\"")  # Output: He said, "Python is great!"

# ----------------------------------------------------------
#   String Immutability
# ----------------------------------------------------------

word = "Python"
# word[0] = "J"  # ❌ Error: Strings are immutable
new_word = "J" + word[1:]
print(new_word)  
# Output: Jython

# ----------------------------------------------------------
#   Summary
# ----------------------------------------------------------
# - Strings are sequences of characters enclosed in quotes.
# - Strings are immutable.
# - You can access characters using indexing and slicing.
# - Common methods: lower(), upper(), strip(), replace(), split(), title()
# - Use f-strings or format() for formatted outputs.
# - Escape sequences (\n, \t, \") allow adding special characters.
