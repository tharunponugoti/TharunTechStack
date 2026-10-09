# What is an Iterator?
#
# An iterator is an object that allows us to access elements one at a time.
#
# numbers = [10, 20, 30, 40]
#
# o/p
#
# 10
# 20
# 30
# 40
#
#
# Iterator = An object that gives values one by one using __next__()
#
#
# Iterable vs Iterator
#
# This is the most important concept.
#
# Iterable
#
# An iterable is an object that we can loop through.
#
#
# Ex:

# list
# tuple
# string
# set
# dictionary
#
# numbers = [10, 20, 30]
#
# for x in numbers:
#     print(x)
#
#
#
#
# Iterator
#
# An iterator is an object that actually gives us the next value using:
#
# next()
#
# Example:
#
# numbers = [10, 20, 30]
#
# it = iter(numbers)
#
# print(next(it))
# print(next(it))
# print(next(it))
#
#
# o/p
# 10
# 20
# 30
#
#
# Python provides the built-in function:
#
# iter()
#
# It converts an iterable into an iterator.
#
# Example:
#
# numbers = [10, 20, 30]
#
# it = iter(numbers)
#
# print(it)

# Line by line

# numbers = [10, 20, 30]
#
# Creates a list.
#
# it = iter(numbers)
#
# Converts the list into an iterator.
#
# Now it is an iterator.
#
# next() Function
#
# The next() function gets the next value from an iterator.
#
# numbers = [10, 20, 30]
#
# it = iter(numbers)
#
# print(next(it))
# print(next(it))
# print(next(it))
#
# Output:
#
# 10
# 20
# 30

# num=[1,2,3]
# value=num.__iter__()
#
# item=value.__next__()
# print(item)
#
# item=value.__next__()
# print(item)
#
# item=value.__next__()
# print(item)
#
# item=value.__next__()
# print(item)              ------Stop Iteration Error





# ------Generator

# A generator is a special type of function that produces values one at a time,
# instead of creating and storing all values in memory at once.
#
# The main keyword used with generators is:
#     yield
#
# ----Normal function
#
#
# def numbers():
#     return [1, 2, 3, 4, 5]
# r=numbers()
# print(r)


# This creates the entire list in memory.




# -----Generator function
#
# def numbers():
#         yield 1
#         yield 2
#         yield 3
#         yield 4
#         yield 5
#
# It produces values one by one.
#
# ----return vs yield
#
# def test():
#     return 10
# x=test()
# print(x)
#
#
# o/p
# 10
#
# def test():
#     yield 10
#     yield 20
#     yield 30
#     yield 40
#
# yield does not permanently end the function.
#
# It pauses the function and remembers where it stopped.
#
#
#
# How Generator works
# def numbers():
#     yield 1
#     yield 2
#     yield 3
# g=numbers()
#
# At this point the function does not execute complete
#
#
# g is a generator. object
#
# print(next(g))
#
# o/p
# 1
#
# print(next(g))
# o/p
# 2
#
#
# print(next(g))
# o/p
# 3
#
# next(g)
#    ↓
# yield 1
#    ↓
# pause
#
# next(g)
#    ↓
# yield 2
#    ↓
# pause
#
# next(g)
#    ↓
# yield 3
#    ↓
# pause
#
#
#
# What is next()?
#
# next() is used to get the next value from a generator.
#
# Example:
#
# def numbers():
#     yield 10
#     yield 20
#     yield 30
#
# g = numbers()
#
# print(next(g))
# print(next(g))
# print(next(g))
#
# o/p
# 10
# 20
# 30
#
#
# ------Using for Loop with Generator
#
# Usually, we don't manually call next().
#
# def numbers():
#     yield 1
#     yield 2
#     yield 3
#
# for i in numbers():
#     print(i)
#
#
# o/p
# 1
# 2
# 3
#
#
# The for loop automatically calls next() internally.
#
#
#
# for loop
#    ↓
# next()
#    ↓
# value
#    ↓
# next()
#    ↓
# value
#    ↓
# next()
#    ↓
# value
#    ↓
# StopIteration
#
# -----Simple Generator Example
#

# def count():
#     for i in range(1,6):
#         yield i
# for x in count():
#        print(x)


# o/p
# 1
# 2
# 3
# 4
# 5
#
# Therefore, generators are particularly useful for:
#
# Large datasets
# Large files
# Data processing
# Streaming data
# Infinite sequences
# Memory - sensitive programs
#

#
# def gen():
#     print("tharun")
#     return "Hey"
# g=gen()
# print(g)

#
# def gen():
#     print("Start")
#     yield 1
#     yield 2
# g=gen()
# print(next(g))

#
# def gen():
#     print("Start")
#     yield "first"
#     yield "second"
#     yield "third"
# g=gen()
# print('one')
# print(next(g))
# print("two")
# print(next(g))
# print("three")
# print(next(g))


#
# def Countdown(n):
#     for i in range(1,n+1):
#         yield i
# c=Countdown(10)
# for i in c:
#     print(i)
#     print("hello")
#
# Write a a python function to dispaly squares of 1 to 5

# def Square(n):
#     l=[]
#     for i in range(1,6):
#         l.append(i**2)
#     return l
# result=Square(5)
# print(result)

#
#
# def Squares(n):
#      for i in range(1,n+1):
#          yield i**2
# s=Squares(5)
# for i in s:
#     print(i)
#     print("hey")



# def MusicPlayer(l):
#     for i in l:
#         yield i
# songs=['song1','song2','song3']
# m=MusicPlayer(songs)
# for i in m:
#     print(i)
#     print("break")