# ------DATA TYPES
#
# Data types in Python are a way to classify data items.
# They represent the kind of value which determines what operations can be performed on that data.
# Since everything is an object in Python programming,
# Python data types are classes and variables are instances (objects) of these classes.
#
# The following are standard or built-in data types in Python:
#
# Numeric: int, float, complex
# Sequence Type: string, list, tuple
# Mapping Type: dict
# Boolean: bool
# Set Type: set, frozenset
# Binary Types: bytes, bytearray, memoryview
#
#
# 1.Numeric Data Types
# Python numbers represent data that has a numeric value. A numeric value can be an integer, a floating
# number or even a complex number. These values are defined as int, float and complex classes.
#
# Integers: value is represented by int class.
# It contains positive or negative whole numbers (without fractions or decimals).
# There is no limit to how long an integer value can be.
#
# Float: value is represented by float class.
# It is a real number with a floating-point representation.
# It is specified by a decimal point.
# Optionally, character e or E followed by a positive or negative integer may be appended to specify scientific notation.
#
#
# Complex Numbers: It is represented by a complex class. It is specified as (real part) + (imaginary part)j. For example - 2+3j
#
#
# a = 5
# print(type(a))
#
# b = 5.0
# print(type(b))
#
# c = 2 + 4j
# print(type(c))
#
# 2,Boolean Data Type
# Python Boolean Data type is one of the two built-in values, True or False.
# Boolean objects that are equal to True are truthy (true) and those equal to False are falsy (false).
# However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false.
# It is denoted by class bool.
#
#
#
#
# print(type(True))
# print(type(False))
# print(type(true))
#
# 3,Sequence Data Types
# A sequence is an ordered collection of items, which can be of similar or different data types.
# Sequences allow storing of multiple values in an organized and efficient fashion.
#
#
# There are several sequence data types of Python:
#
# String Data Type
# Python Strings are arrays of bytes representing Unicode characters.
# In Python, there is no character data type, a character is a string of length one.
# It is represented by str class.
#
# Strings in Python can be created using single quotes, double quotes or even triple quotes.
# We can access individual characters of a String using index.
#
#
#
#
# s = 'THARUN'
# print(s)
#
# # check data type
# print(type(s))
#
# # access string with index
# print(s[1])
# print(s[2])
# print(s[-1]) # -1 refers to the last character, -2 is second last, and so on
#
# Output
# THARUN
# <class 'str'>
# H
# A
# N
#
#
#
# ----List Data Type
# Lists are similar to arrays found in other languages. They are an ordered and mutable collection of items.
# It is very flexible as items in a list do not need to be of the same type.
#
# Creating a List in Python: Lists can be created by just placing sequence inside the square brackets[].
#
#
#
#
# # Empty list
# a = []
#
# # list with int values
# a = [1, 2, 3]
# print(a)
# # list with mixed values int and String
# b = ["PYTHON", "For", "SQL", 4, 5]
# print(b)
#
# Output
# [1, 2, 3]
# ['PYTHON', 'For', 'SQL', 4, 5]
#
#
# Tuple Data Type
# Tuple is an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable.
# Tuples cannot be modified after it is created.
#
# Creating a Tuple in Python: tuples are created by placing a sequence of values separated by a ‘comma’ with or without the use of parentheses for grouping data sequence.
# Tuples can contain any number of elements and of any datatype (like strings, integers, lists, etc.).
#
# Note: Tuples can also be created with a single element, but it is a bit tricky.
# Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.
#
#
#
#
# # initiate empty tuple
# tup1 = ()
# tup2 = ('THARUN', 'For')
# print("\nTuple with the use of String: ", tup2)
#
# Output
# Tuple with the use of String:  ('THARUN', 'For')
#
# Note: The creation of a Python tuple without the use of parentheses is known as Tuple Packing.
#
# Access Tuple Items: In order to access tuple items refer to the index number. Use the index operator [] to access an item in a tuple.
#
#
#
#
# tup1 = (1, 2, 3, 4, 5)
#
# # access tuple items
# print(tup1[0])
# print(tup1[-1])
# print(tup1[-3])
#
# Output
# 1
# 5
# 3
#
#
#
# 3. Boolean Data Type
# Python Boolean Data type is one of the two built-in values, True or False.
# Boolean objects that are equal to True are truthy (true) and those equal to False are falsy (false).
# However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false. It is denoted by class bool.
#
#
# print(type(True))
# print(type(False))
# print(type(true))
#
# Built-in Data Types
# In programming, data type is an important concept.
#
# Variables can store data of different types, and different types can do different things.
#
# Python has the following data types built-in by default, in these categories:
#
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
#
#
# Getting the Data Type
# You can get the data type of any object by using the type() function:
#
#
# Example	Data Type	Try it
# x = "Hello World"	str
# x = 20	int
# x = 20.5	float
# x = 1j	complex
# x = ["apple", "banana", "cherry"]	list
# x = ("apple", "banana", "cherry")	tuple
# x = range(6)	range
# x = {"name" : "John", "age" : 36}	dict
# x = {"apple", "banana", "cherry"}	set
# x = frozenset({"apple", "banana", "cherry"})	frozenset
# x = True	bool
# x = b"Hello"	bytes
# x = bytearray(5)	bytearray
# x = memoryview(bytes(5))	memoryview
# x = None	NoneType
#
#
#
# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
#
# Example	Data Type
# x = str("Hello World")	str
# x = int(20)	int
# x = float(20.5)	float
# x = complex(1j)	complex
# x = list(("apple", "banana", "cherry"))	list
# x = tuple(("apple", "banana", "cherry"))	tuple
# x = range(6)	range
# x = dict(name="John", age=36)	dict
# x = set(("apple", "banana", "cherry"))	set
# x = frozenset(("apple", "banana", "cherry"))	frozenset
x = bool(5)	bool
x = bytes(5)	bytes
x = bytearray(5)	bytearray
x = memoryview(bytes(5))	memoryview











