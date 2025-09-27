# ======================================
# ## Python User Input
# ======================================

# ======================================
# 4. Python Data Structures
# ======================================

# ------------------------------
# 4.1 Python Lists
# ------------------------------

# 1. A list is an ordered, mutable (changeable) collection of elements.
# 2. Lists can contain different data types.
# 3. Syntax: my_list = [item1, item2, item3]

# Example 1: Creating and printing a list
# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# Example 2: Accessing elements using index
# print(fruits[0])    # apple
# print(fruits[-1])   # cherry

# Example 3: Modifying list elements (mutable)
# fruits[1] = "mango"
# print(fruits)   # ["apple", "mango", "cherry"]

# Example 4: List slicing
# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:3])   # [20, 30]
# print(numbers[:3])    # [10, 20, 30]
# print(numbers[2:])    # [30, 40, 50]

# Working with Two Lists

# Example 1: Concatenating Two Lists
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined = list1 + list2
# print("Concatenated List:", combined)   # [1, 2, 3, 4, 5, 6]

# Example 2: Iterating Over Two Lists Together
# names = ["Alice", "Bob", "Charlie"]
# ages = [21, 25, 30]
# for i in range(len(names)):
#     print(names[i], "is", ages[i], "years old")

# Example 3: Zipping Two Lists
# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "dark red"]
# for fruit, color in zip(fruits, colors):
#     print(fruit, "→", color)

# ------------------------------
# 4.2 Python List Methods
# ------------------------------
# Common Methods with Examples

# append()
# my_list = [1, 2]
# my_list.append(3)
# print(my_list)   # [1, 2, 3]

# insert()
# my_list.insert(1, 10)
# print(my_list)   # [1, 10, 2, 3]

# remove()
# my_list.remove(10)
# print(my_list)   # [1, 2, 3]

# pop()
# print(my_list.pop())   # 3 removed
# print(my_list)         # [1, 2]

# sort()
# nums = [3, 1, 2]
# nums.sort()
# print(nums)   # [1, 2, 3]

# reverse()
# nums.reverse()
# print(nums)   # [3, 2, 1]

# -------------------------------------------------------------------------------------------------------------

# ------------------------------
# 4.3 Python Tuples
# ------------------------------

# 1. Tuples are ordered but immutable (cannot be changed).
# 2. Defined using parentheses ().
# 3. Useful for fixed collections of items.

# Syntax: my_tuple = (item1, item2, item3)

# Example 1: Creating tuple
# colors = ("red", "green", "blue")
# print(colors)

# Example 2: Accessing elements
# print(colors[0])    # red
# print(colors[-1])   # blue

# Example 3: Attempting modification (will error)
# colors[0] = "yellow"   # TypeError

# Working with Two Tuples

# Example 1: Concatenating Tuples
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# result = t1 + t2
# print("Concatenated:", result)   # (1, 2, 3, 4, 5, 6)

# Example 2: Repeating Tuples
# t = (7, 8)
# print("Repeated:", t * 3)        # (7, 8, 7, 8, 7, 8)

# Example 3: Iterating with Index
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = ("red", "yellow", "dark red")
# for i in range(len(tuple1)):
#     print(tuple1[i], "→", tuple2[i])

# Example 4: Using Zip with Tuples
# colors = ("blue", "green", "orange")
# fruits = ("berry", "melon", "mango")
# for c, f in zip(colors, fruits):
#     print(c, "matches with", f)

# Example 5: Nesting Tuples
# tup1 = (1, 2)
# tup2 = (3, 4)
# nested = (tup1, tup2)
# print("Nested Tuple:", nested)   # ((1, 2), (3, 4))

# ------------------------------
# 4.4 Python Tuple Methods
# ------------------------------
# count()
# nums = (1, 2, 2, 3)
# print(nums.count(2))   # 2

# index()
# print(nums.index(3))   # 3

# -------------------------------------------------------------------------------------------------------------

# ------------------------------
# 4.5 Difference between List and Tuple
# ------------------------------
# 1. List → mutable, Tuple → immutable
# 2. List uses [], Tuple uses ()
# 3. Lists are slower than tuples because of mutability

# -------------------------------------------------------------------------------------------------------------

# ------------------------------
# 4.6 Python Sets
# ------------------------------

# 1. A set is an unordered collection of unique items.
# 2. Defined using curly braces {}.
# 3. No duplicate elements allowed.

# Example 1: Creating a set
# my_set = {1, 2, 3, 2}
# print(my_set)   # {1, 2, 3}

# Example 2: Adding element
# my_set.add(4)
# print(my_set)   # {1, 2, 3, 4}

# Example 3: Removing element
# my_set.remove(2)
# print(my_set)   # {1, 3, 4}

# Working with Two Sets

# Example 1: Union (all unique elements from both sets)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print("Union:", set1 | set2)        # {1, 2, 3, 4, 5}
# print("Union (method):", set1.union(set2))

# Example 2: Intersection (common elements)
# print("Intersection:", set1 & set2)   # {3}
# print("Intersection (method):", set1.intersection(set2))

# Example 3: Difference (elements in set1 but not in set2)
# print("Difference:", set1 - set2)     # {1, 2}
# print("Difference (method):", set1.difference(set2))

# Example 4: Symmetric Difference (elements in either but not both)
# print("Symmetric Difference:", set1 ^ set2)  # {1, 2, 4, 5}
# print("Symmetric Difference (method):", set1.symmetric_difference(set2))

# Example 5: Iterating Two Sets Together
# names = {"Alice", "Bob", "Charlie"}
# roles = {"Admin", "User", "Editor"}
# for n, r in zip(names, roles):
#     print(n, "→", r)

# Example 6: Subset and Superset
# a = {1, 2}
# b = {1, 2, 3, 4}
# print("a is subset of b:", a.issubset(b))    # True
# print("b is superset of a:", b.issuperset(a)) # True

# -------------------------------------------------------------------------------------------------------------

# ------------------------------
# 4.7 Python Set Methods
# ------------------------------
# a = {1, 2, 3}
# b = {3, 4, 5}

# union()
# print(a.union(b))     # {1, 2, 3, 4, 5}

# intersection()
# print(a.intersection(b))   # {3}

# difference()
# print(a.difference(b))     # {1, 2}

# -------------------------------------------------------------------------------------------------------------

# ------------------------------
# 4.8 Python Dictionary
# ------------------------------

# 1. A dictionary is an unordered collection of key-value pairs.
# 2. Defined using curly braces {} with keys and values.
# 3. Keys must be unique and immutable; values can be anything.

# Example 1: Creating dictionary
# student = {"name": "Alice", "age": 21}
# print(student)

# Example 2: Accessing values
# print(student["name"])   # Alice

# Example 3: Updating values
# student["age"] = 22
# print(student)

# Example 4: Adding new key-value
# student["course"] = "Python"
# print(student)

# Working with Two Dictionaries

# Example 1: Merging Two Dictionaries (Python 3.9+)
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = dict1 | dict2
# print("Merged:", merged)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 2: Merging with Update (modifies dict1)
# dict1.update(dict2)
# print("After update:", dict1)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 3: Iterating Two Dicts Together
# names = {"id1": "Alice", "id2": "Bob", "id3": "Charlie"}
# roles = {"id1": "Admin", "id2": "User", "id3": "Editor"}
# for key in names:
#     print(names[key], "→", roles[key])

# Example 4: Dictionary Comprehension with Two Dicts
# prices1 = {"apple": 50, "banana": 30}
# prices2 = {"banana": 40, "cherry": 60}
# take higher price for common fruits
# combined = {k: max(prices1.get(k, 0), prices2.get(k, 0)) for k in set(prices1) | set(prices2)}
# print("Combined Prices:", combined)  
# {'apple': 50, 'banana': 40, 'cherry': 60}

# Example 5: Zipping Two Dicts
# keys = {"k1": 1, "k2": 2}
# values = {"v1": "A", "v2": "B"}
# zipped_dict = dict(zip(keys, values))
# print("Zipped Dict:", zipped_dict)   # {'k1': 'v1', 'k2': 'v2'}

# -------------------------------------------------------------------------------------------------------------

# ------------------------------
# 4.9 Python Dictionary Methods
# ------------------------------
# person = {"name": "Bob", "age": 25}

# keys()
# print(person.keys())    # dict_keys(['name', 'age'])

# values()
# print(person.values())  # dict_values(['Bob', 25])

# items()
# print(person.items())   # dict_items([('name', 'Bob'), ('age', 25)])

# get()
# print(person.get("name"))   # Bob

# pop()
# person.pop("age")
# print(person)    # {"name": "Bob"}

# -------------------------------------------------------------------------------------------------------------

# ------------------------------
# 4.10 Difference between List and Dictionary
# ------------------------------
# 1. List stores items in order by index, Dictionary stores data as key-value pairs.
# 2. List accessed by index, Dictionary accessed by key.
# 3. Lists allow duplicate items, Dictionary keys must be unique.


# ------------------------------
# 4.11 Difference between List, Set, Tuple, and Dictionary
# ------------------------------
# List → Ordered, mutable, duplicates allowed.
# Tuple → Ordered, immutable, duplicates allowed.
# Set → Unordered, mutable, unique elements only.
# Dictionary → Unordered, key-value pairs, keys unique.


# ------------------------------
# 4.12 Difference between Set and Dictionary
# ------------------------------
# 1. Set contains only values, Dictionary contains key-value pairs.
# 2. Syntax: Set → {1,2,3}, Dictionary → {"a":1, "b":2}.
# 3. Set used for membership testing and unique storage.
# 4. Dictionary used for mapping relationships between keys and values.

# ----------------------------------------------------------------------------------------------