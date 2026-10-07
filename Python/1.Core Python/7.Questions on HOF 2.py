# 1.Explain the difference between map(), filter(), and reduce() in Python.
# What does each function return?
# When should you prefer lambda functions over normal functions?
#
#
# 1. Difference between map(), filter(), and reduce()
#
# These are Higher-Order Functions in Python.
#
# Function	Purpose	What it does	Returns
# map()	Transform	Changes every element	map object
# filter()	Select	Keeps elements that satisfy a condition	filter object
# reduce()	Combine	Combines all elements into one value	Single value
# map()
#
#
# Purpose:
# Use map() when you want to perform an operation on every element.
#
# Example:
#
# nums = [1, 2, 3, 4]
#
# result = list(map(lambda x: x * 2, nums))
#
# print(result)
#
# Output:
#
# [2, 4, 6, 8]
# How it works:
# 1 → 1 × 2 → 2
# 2 → 2 × 2 → 4
# 3 → 3 × 2 → 6
# 4 → 4 × 2 → 8
#
# map() returns a map object, so we commonly use list() to see the results as a list.
#
# filter()
# Purpose:
#
# Use filter() when you want to select only elements that satisfy a condition.
#
# Example:
#
# nums = [1, 2, 3, 4, 5, 6]
#
# result = list(filter(lambda x: x % 2 == 0, nums))
#
# print(result)
#
# Output:
#
# [2, 4, 6]
#
# Here:
#
# x % 2 == 0
#
# checks whether the number is even.
#
# filter() returns a filter object.
#
# reduce()
#
# reduce() is available from the functools module.
#
# from functools import reduce
# Purpose:
#
# Use reduce() when you want to combine multiple values into one value.
#
# Example:
#
# nums = [1, 2, 3, 4]
#
# result = reduce(lambda x, y: x + y, nums)
#
# print(result)
#
# Output:
#
# 10
#
# Working:
#
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
#
# So reduce() returns one final value.
#
# map() vs filter() vs reduce()
#
# Think of them like this:
#
# map()    → CHANGE every element
# filter() → SELECT some elements
# reduce() → COMBINE all elements
#
# Easy memory trick:
#
# MAP = Modify
# FILTER = Select
# REDUCE = Combine
#
# When should you prefer lambda over normal functions?
#
# A lambda is useful when the function is:
#
# very small
# used only once
# simple enough to understand in one line
# Lambda
# square = lambda x: x * x
# print(square(5))
#
# Output:
#
# 25
#
# Instead of:
#
# def square(x):
#     return x * x
#
# Prefer normal functions when:
# the logic is complicated
# you need multiple statements
# you want to reuse the function many times
# you want clearer code
#
# Example:
#
# def calculate_salary(basic, bonus, tax):
#     total = basic + bonus
#     result = total - tax
#     return result
#
# This is better as a normal function than trying to write everything as a lambda.
#
#
# 2. Given two lists:
# a = [1, 2, 3, 4] b = [10, 20, 30, 40]
# Use map() with a lambda to create a new list containing the sum of corresponding
# elements.
# What happens if the lists are of unequal length?
#
#
# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
#
# result = list(map(lambda x, y: x + y, a, b))
#
# print(result)
#
#
# 3. Given a list:
# nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
# 5 but NOT divisible by both.
# Explain how the logical condition works
#
#
# nums = [12, 15, 7, 18, 20, 21, 25]
#
# result = list(filter(lambda x: (x % 3 == 0) != (x % 5 == 0), nums))
#
# print(result)
#
#
# 4. Given a list:
# nums = [1, 2, 3, 4]
# Use reduce() with a lambda to compute the sum, but start with an initial value
# of 10.
# Explain how the initial value affects the reduction process.
#
#

# from functools import reduce
# nums = [1, 2, 3, 4]
# initial=10
# result = reduce(lambda acc,x:acc + x, nums, initial)
# print(result)


#
#
5.nums= [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums))
print("Result:", result) print("Nums:", nums)
Questions
• What will be the output of result?
• What will be the output of nums?
• Why does map() behave this way with list.append()?
• How can you modify the lambda so that nums is not changed?


nums = [[1, 2], [3, 4], [5, 6]]

result = list(map(lambda x: x.append(10), nums))

print("Result:", result)
print("Nums:", nums)