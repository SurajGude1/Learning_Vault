# ======================================
# 2. Python Variables & Data Types  
# ======================================

# ======================================
# 2.1 Python Variables  
# ======================================

# What are Variables?
# Variables are like containers that store data values.
# In Python, you don’t need to declare the type of a variable.
# The type is automatically assigned when a value is given.

# Python Variable Naming Rules

# Must start with letter/underscore
# name = "Suraj"    # valid
# _name = 25        # valid

# Cannot start with number or use symbols
# 1name = "Test"    # invalid
# first-name = "Hi" # invalid

# Case-sensitive & no keywords
# Age = 20   # valid (different from 'age')
# class = 5  # invalid (keyword)

# ----------------------------------------------------------------------------------------

# Example 1: Assigning values to variables
# name = "John"        # String variable
# age = 25              # Integer variable
# pi = 3.1415           # Float variable
# is_active = True      # Boolean variable

# print(name)   # Output: Suraj
# print(age)    # Output: 25
# print(pi)     # Output: 3.1415
# print(is_active)  # Output: True


# Example 2: Reassigning variables (Dynamic typing)
# x = 10        # Initially integer
# print(x)      # Output: 10

# x = "Python"  # Now becomes string
# print(x)      # Output: Python


# Example 3: Multiple assignments
# a, b, c = 1, 2, 3
# print(a, b, c)  # Output: 1 2 3

# Example 4: Same value to multiple variables
# p = q = r = "Learning"
# print(p, q, r)  # Output: Learning Learning Learning


# ----------------------------------------------------------------------------------------------------------------------------


# ======================================
# 2.2 Python Data Types
# ======================================

# In Python, every value has a data type.
# Data types define the kind of value stored in a variable
# and what operations can be performed on it.

# --------------------------------------
# 1. Integer (int)
# --------------------------------------
# Whole numbers, positive or negative, without decimals.
# Range: Unlimited (depends on memory, unlike C/Java fixed range).

# x = 10
# y = -250
# print(x, type(x))   # Output: 10 <class 'int'>
# print(y, type(y))   # Output: -250 <class 'int'>


# --------------------------------------
# 2. Floating Point (float)
# --------------------------------------
# Numbers with decimals, or scientific notation.

# pi = 3.1415
# e = 2.5e3   # 2500.0
# print(pi, type(pi))   # Output: 3.1415 <class 'float'>
# print(e, type(e))     # Output: 2500.0 <class 'float'>


# --------------------------------------
# 3. Complex Numbers (complex)
# --------------------------------------
# Numbers with real + imaginary part (a + bj).

# z1 = 2 + 3j
# z2 = -5j
# print(z1, type(z1))   # Output: (2+3j) <class 'complex'>
# print(z2, type(z2))   # Output: -5j <class 'complex'>


# --------------------------------------
# 4. String (str)
# --------------------------------------
# Sequence of characters inside quotes.
# Can be single, double, or triple quotes.

# s1 = "Hello Python"
# s2 = '''Multiline
# String Example'''
# print(s1, type(s1))   # Output: Hello Python <class 'str'>
# print(s2, type(s2))   # Output: Multiline String Example <class 'str'>


# --------------------------------------
# 5. Boolean (bool)
# --------------------------------------
# Logical values: True or False.

# is_active = True
# is_admin = False
# print(is_active, type(is_active))  # Output: True <class 'bool'>
# print(is_admin, type(is_admin))    # Output: False <class 'bool'>


# --------------------------------------
# 6. None Type
# --------------------------------------
# Represents absence of a value (null in other languages).

# a = None
# b = None
# print(a, type(a))   # Output: None <class 'NoneType'>
# print(b is None)    # Output: True


# ----------------------------------------------------------------------------------------------------------------------------


# ======================================
# 2.3 Python Numbers
# ======================================

# Python has three main numeric types:
# 1. int (Integer)
# 2. float (Floating point)
# 3. complex (Complex numbers)

# --------------------------------------
# 1. Integers (int)
# --------------------------------------
# Whole numbers, positive or negative, no decimals.
# Range: Unlimited (depends on system memory).

# a = 100
# b = -42
# print(a, type(a))   # Output: 100 <class 'int'>
# print(b, type(b))   # Output: -42 <class 'int'>


# --------------------------------------
# 2. Floating Point Numbers (float)
# --------------------------------------
# Numbers with decimals or scientific notation.

# pi = 3.14159
# exp = 1.2e4   # 12000.0
# print(pi, type(pi))   # Output: 3.14159 <class 'float'>
# print(exp, type(exp)) # Output: 12000.0 <class 'float'>


# --------------------------------------
# 3. Complex Numbers (complex)
# --------------------------------------
# Written as (a + bj), where a = real part, b = imaginary part.

# z1 = 2 + 5j
# z2 = -7j
# print(z1, type(z1))   # Output: (2+5j) <class 'complex'>
# print(z2, type(z2))   # Output: -7j <class 'complex'>


# ----------------------------------------------------------------------------------------------------------------------------

 
# ======================================
# 2.4 Type Casting in Python
# ======================================

# Type Casting = Converting one data type to another.
# Two types:
# 1. Implicit Casting (done automatically by Python)
# 2. Explicit Casting (done using built-in functions)

# --------------------------------------
# 1. Implicit Type Casting
# --------------------------------------
# Python converts smaller data type to larger automatically.

# x = 10      # int
# y = 2.5     # float
# z = x + y   # int + float → float
# print(z, type(z))   # Output: 12.5 <class 'float'>


# --------------------------------------
# 2. Explicit Type Casting
# --------------------------------------
# Manual conversion using int(), float(), str(), complex(), etc.

# int → float
# a = 5
# b = float(a)
# print(b, type(b))   # Output: 5.0 <class 'float'>

# float → int
# pi = 3.99
# num = int(pi)
# print(num, type(num))   # Output: 3 <class 'int'>

# int → string
# n = 100
# s = str(n)
# print(s, type(s))   # Output: "100" <class 'str'>

# string → int
# st = "25"
# val = int(st)
# print(val + 5)      # Output: 30

# int → complex
# c = complex(7)
# print(c, type(c))   # Output: (7+0j) <class 'complex'>


# ----------------------------------------------------------------------------------------------------------------------------

 
# ======================================
# 2.5 Python Strings
# ======================================

# A string is a sequence of characters enclosed
# in single quotes (' '), double quotes (" "), 
# or triple quotes (''' ''' / """ """).

# --------------------------------------
# Creating Strings
# --------------------------------------
# s1 = 'Hello'
# s2 = "Python"
# s3 = '''This is
# a multi-line string.'''
# print(s1)   # Output: Hello
# print(s2)   # Output: Python
# print(s3)   # Output: multi-line text


# --------------------------------------
# String Indexing & Slicing
# --------------------------------------
# text = "Learning"
# print(text[0])      # Output: L   (first character)
# print(text[-1])     # Output: g   (last character)
# print(text[0:4])    # Output: Lear (slice from index 0 to 3)
# print(text[2:])     # Output: arning


# --------------------------------------
# String Operations
# --------------------------------------
# a = "Python"
# b = "Rocks"
# print(a + " " + b)   # Concatenation → "Python Rocks"
# print(a * 3)         # Repetition → "PythonPythonPython"

# --------------------------------------
# Useful String Methods
# --------------------------------------
# msg = " hello world "
# print(msg.upper())      # HELLO WORLD
# print(msg.lower())      # hello world
# print(msg.strip())      # removes spaces → "hello world"
# print(msg.replace("world", "Python"))   # hello Python
# print(msg.split())      # ['hello', 'world']


# ----------------------------------------------------------------------------------------------------------------------------

 
# ======================================
# 2.6 Python String Methods
# ======================================

# Commonly used String Methods:
# .upper()       → Converts to uppercase
# .lower()       → Converts to lowercase
# .title()       → First letter of each word capitalized
# .capitalize()  → First letter capitalized, rest lowercase
# .strip()       → Removes spaces (leading & trailing)
# .lstrip()      → Removes spaces from left
# .rstrip()      → Removes spaces from right
# .replace()     → Replace substring with another
# .split()       → Split string into list
# .join()        → Join list into string
# .find()        → Return index of first occurrence
# .count()       → Count occurrences of substring
# .startswith()  → Check if string starts with substring
# .endswith()    → Check if string ends with substring

# --------------------------------------
# Examples
# --------------------------------------
# text = "   hello python world   "

# print(text.upper())       # HELLO PYTHON WORLD
# print(text.lower())       # hello python world
# print(text.title())       # Hello Python World
# print(text.capitalize())  # Hello python world
# print(text.strip())       # "hello python world"
# print(text.lstrip())      # "hello python world   "
# print(text.rstrip())      # "   hello python world"
# print(text.replace("python", "Java"))   # "   hello Java world   "
# print(text.split())       # ['hello', 'python', 'world']

# words = ["Python", "is", "fun"]
# print(" ".join(words))    # "Python is fun"

# print(text.find("python"))  # 9
# print(text.count("o"))      # 2
# print(text.startswith("   h"))  # True
# print(text.endswith("ld   "))   # True


# ----------------------------------------------------------------------------------------------------------------------------

 
# ======================================
# 2.7 Python Boolean
# ======================================

# Booleans represent one of two values: True or False.
# Used in conditions, comparisons, and logical operations.

# --------------------------------------
# Boolean Values
# --------------------------------------
# x = True
# y = False
# print(x, type(x))   # Output: True <class 'bool'>
# print(y, type(y))   # Output: False <class 'bool'>


# --------------------------------------
# Comparisons return Boolean
# --------------------------------------
# a = 10
# b = 20
# print(a > b)   # False
# print(a < b)   # True
# print(a == b)  # False
# print(a != b)  # True


# --------------------------------------
# Boolean with Numbers
# --------------------------------------
# In Python, 0 → False, non-zero → True

# print(bool(0))     # False
# print(bool(5))     # True
# print(bool(-10))   # True


# --------------------------------------
# Boolean with Strings
# --------------------------------------
# Empty string → False, non-empty → True

# print(bool(""))       # False
# print(bool("Python")) # True


# --------------------------------------
# Logical Operators with Booleans
# --------------------------------------
# print(True and False)   # False
# print(True or False)    # True
# print(not True)         # False
  

# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------