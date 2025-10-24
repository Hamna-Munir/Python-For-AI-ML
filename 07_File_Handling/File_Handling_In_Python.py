# -----------------------------------------
# 📂 File Handling in Python
# -----------------------------------------
# File handling allows us to store, read, and modify data permanently in files.
# Python provides built-in functions to create, read, write, and delete files.

# -----------------------------------------
# Opening and Closing Files
# -----------------------------------------
# Syntax: open(filename, mode)
# Common Modes:
# 'r' - Read (default): Error if file doesn’t exist.
# 'w' - Write: Creates new file or overwrites existing.
# 'a' - Append: Adds data at the end of the file.
# 'x' - Create: Creates file but gives error if it exists.
# 't' - Text mode (default)
# 'b' - Binary mode (for images, etc.)

# Example: Opening a file in write mode
file = open("example.txt", "w")
file.write("Hello, this is my first file in Python!\n")
file.write("Python makes file handling simple.\n")
file.close()

# Output: A file named 'example.txt' is created with above text written inside.


# -----------------------------------------
# Reading From a File
# -----------------------------------------
# 'r' mode is used for reading. If the file doesn’t exist, it raises an error.
file = open("example.txt", "r")
content = file.read()
print("Reading the entire file:\n", content)
file.close()

# Output:
# Reading the entire file:
# Hello, this is my first file in Python!
# Python makes file handling simple.


# -----------------------------------------
# Reading Line by Line
# -----------------------------------------
file = open("example.txt", "r")
print("Reading line by line:")
for line in file:
    print(line.strip())  # strip() removes extra newline characters
file.close()

# Output:
# Reading line by line:
# Hello, this is my first file in Python!
# Python makes file handling simple.


# -----------------------------------------
# Appending to a File
# -----------------------------------------
file = open("example.txt", "a")
file.write("This line is added using append mode.\n")
file.close()

# Output: The new line will be added at the end of example.txt.


# -----------------------------------------
# Using 'with open()' — Best Practice
# -----------------------------------------
# Automatically closes the file after block execution.
with open("example.txt", "r") as file:
    print("\nReading file using 'with open()':")
    print(file.read())

# Output:
# Reading file using 'with open()':
# Hello, this is my first file in Python!
# Python makes file handling simple.
# This line is added using append mode.


# -----------------------------------------
# Writing and Reading Binary Files (Example)
# -----------------------------------------
# For image or binary data, use 'rb' or 'wb' mode.
# Example (conceptual, not executed):
# with open("image.png", "rb") as img_file:
#     data = img_file.read()
# with open("copy_image.png", "wb") as copy_file:
#     copy_file.write(data)


# -----------------------------------------
# Checking if File Exists
# -----------------------------------------
import os

if os.path.exists("example.txt"):
    print("\n✅ File 'example.txt' exists.")
else:
    print("\n❌ File does not exist.")

# Output:
# ✅ File 'example.txt' exists.


# -----------------------------------------
# Deleting a File
# -----------------------------------------
# Uncomment below lines to delete file
# os.remove("example.txt")
# print("File deleted successfully.")
