# 1,Use map() with a lambda to add 5 to every element of the following nested list[[1, 2], [3, 4], [5, 6]]
#
#
# a = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: [i + 5 for i in x], a))
# print(result)


#
# 2.Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
# filter() to keep only the keys whose values are greater than 50.
#
#
# d = {"apple": 100, "banana": 40, "cherry": 150}
# result = list(filter(lambda x: d[x] > 50, d))
# print(result)

#
#
# 3. Use functools.reduce() with a lambda to find the largest number from a given
# list Dynamically.
#
# from functools import reduce
# a = list(map(int, input("Enter numbers: ").split()))
# largest = lambda x, y: max(x, y)
# result = reduce(largest, a)
# print("Largest number:", result)



#
# 4.What happens if the lambda passed to reduce() accepts only one parameter or
# three parameters? Explain the output or error.
#
#
# from functools import reduce
# a = [1, 2, 3]
# result = reduce(lambda x: x, a)
# print(result)
#
# o/p
# TypeError
#
#
# Why?
#
# reduce() needs a function that accepts two arguments:
#
# lambda x, y: ...
#
# Because reduce() works like:
#
# 1, 2 → result
# result, 3 → result
#
# So it needs two values at a time.
#
# Therefore:
#
# lambda x: x
#
# ❌ Only accepts 1 argument → TypeError
#
# B) Lambda with three parameters
# from functools import reduce
#
# a = [1, 2, 3]
#
# result = reduce(lambda x, y, z: x + y + z, a)
#
# print(result)
# Output
# TypeError
#
# Because reduce() normally supplies only two arguments to the function:
#
# x, y
#
# But the lambda expects:
#
# x, y, z
#
# So:
#
# ❌ 3 parameters → TypeError
#
# Remember 🧠
# reduce() → function must normally accept 2 parameters


#
# 5. Use map() on a string to convert each character into its ASCII value
# (using ord()). Print the result list.
#
#
# s = "Python"
# result = list(map(ord, s))
# print(result)
#
#
#
#
# 6.Use filter() to remove all vowels from a string and print the final string.
#
#
# s = "Hello Python"
# result = ''.join(filter(lambda x: x.lower() not in "aeiou", s))
# print(result)


# 7.Use reduce() to concatenate a list of characters into a single string.
# Example input: ['P', 'y', 't', 'h', 'o', 'n'].
#
#
# from functools import reduce
# a = ['P', 'y', 't', 'h', 'o', 'n']
# result = reduce(lambda x, y: x + y, a)
# print(result)



# 8.Given a list of integers, use map() with id() to print the memory address
# of each element.
#
#
# a = [10, 350, 10, 350, 20]
#
# result = list(map(id, a))
#
# print(result)



10.Given a list of numbers:
[5, 10, 15, 20, 25, 30]
Perform the following in a single pipeline:
• Use map() to square each number
• Use filter() to keep only numbers divisible by 5
• Use reduce() to calculate the sum of remaining numbers


from functools import reduce

a = [5, 10, 15, 20, 25, 30]

result = reduce(lambda x, y: x + y,filter(lambda x: x % 5 == 0,map(lambda x: x ** 2, a)))

print(result)