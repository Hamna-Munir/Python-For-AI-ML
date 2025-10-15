# Topic: Escape Sequences in Python
# ----------------------------------------------------------
# Author: Hamna Munir
# Repository: Python-For-AI-ML
# ----------------------------------------------------------

#    What are Escape Sequences in Python?

# ➤ An escape sequence is a special combination of characters used inside strings.
# ➤ It starts with a backslash (\) followed by a character.
# ➤ Escape sequences are used to represent characters that are difficult or
#   impossible to type directly, such as newline, tab, or quotes.
# ➤ They “tell” Python to treat the next character differently.


# ----------------------------------------------------------
#   Why Are Escape Sequences Needed?
# ----------------------------------------------------------
# When we write text inside quotes, sometimes we need special formatting.
# For example:
# - Printing quotes inside a string
# - Moving to a new line
# - Adding a tab space
# - Showing special characters like backslash (\) itself


# Example without escape sequence (this causes an error):
# print("Hamna said "Python is amazing"")  ❌  # Invalid syntax

# Correct example using escape sequence:
print("Hamna said \"Python is amazing\"")
# Output: Hamna said "Python is amazing"


# ----------------------------------------------------------
#   Common Escape Sequences in Python
# ----------------------------------------------------------

# \n  → New line
print("Hello\nWorld")
# Output:
# Hello
# World

# \t  → Tab space
print("Hello\tWorld")
# Output: Hello    World

# \\  → Backslash
print("This is a backslash: \\")
# Output: This is a backslash: \

# \'  → Single quote
print('It\'s a beautiful day!')
# Output: It's a beautiful day!

# \"  → Double quote
print("She said, \"Keep learning Python!\"")
# Output: She said, "Keep learning Python!"

# \b  → Backspace
print("Hello\b!")
# Output: Hell!    (removes the 'o' before '!')

# \r  → Carriage return
print("Python\rCode")
# Output: Codeon    ('Code' overwrites the beginning of 'Python')

# \f  → Form feed (new page – rarely used today)
print("Hello\fWorld")
# Output: Hello
#         World    (behaves like a page break in some systems)

# \a  → Bell sound (system alert)
# May not produce sound on all systems
print("Beep\a")
# Output: Beep (plus an alert sound if supported)

# \u or \U → Unicode character
# Used to display symbols or characters by Unicode code points
print("\u03A9")   # Greek Omega symbol
# Output: Ω
print("\u2764")   # Heart symbol
# Output: ❤


# ----------------------------------------------------------
#   Raw Strings and Escape Sequences
# ----------------------------------------------------------
# Sometimes we don’t want Python to interpret escape sequences.
# To prevent that, use an ‘r’ before the string — called a raw string.

print(r"Hello\nWorld")
# Output: Hello\nWorld  (no new line)
print(r"C:\Users\Hamna")
# Output: C:\Users\Hamna


# ----------------------------------------------------------
#   Multi-line Strings and Escape Sequences
# ----------------------------------------------------------
# Escape sequences can also be used inside multi-line strings.

message = """This is a message with a new line:\nSee you soon!"""
print(message)
# Output:
# This is a message with a new line:
# See you soon!


# ----------------------------------------------------------
#   Best Practices for Escape Sequences
# ----------------------------------------------------------
# ✔ Use escape sequences for formatting output properly.
# ✔ Use raw strings (r" ") when working with file paths or regex patterns.
# ✔ Avoid unnecessary use of backslashes — it can make strings confusing.
# ✔ Always test how your escape sequence behaves before using it in production.


# ----------------------------------------------------------
#   Summary:
# ----------------------------------------------------------
# - Escape sequences begin with a backslash (\).
# - They allow you to include special characters in strings.
# - Common ones: \n (new line), \t (tab), \\ (backslash), \" (quote).
# - Use raw strings (r" ") to ignore escape sequences.
# - They make string formatting flexible and powerful in Python.
# ----------------------------------------------------------
