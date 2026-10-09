# -----Decorator
#
# A Decorator is a function that takes another function to it, and returns a new function
#
#
# Original Function
#        ↓
#    Decorator
#        ↓
# New/Modified Function
#
#
# We add functionality without modifying the original function's code.
#
#
#
#
# Function
#    ↓
# passed to decorator
#    ↓
# decorator creates wrapper
#    ↓
# wrapper returned
#    ↓
# wrapper executes original function
#
#
#
# Complete Basic Decorator
#
# def decorator(func):
#
#     def wrapper():
#         print("Before")
#
#         func()
#
#         print("After")
#
#     return wrapper
#
#
# @decorator
# def hello():
#     print("Hello")
#
#
# hello()
#
#
#
# What is wrapper()?
# wrapper() is simply another function.
# Its job is to control the original function.
#
#
# the flow
#
# hello()
#    ↓
# wrapper()
#    ↓
# print("Before")
#    ↓
# func()
#    ↓
# original hello()
#    ↓
# print("Hello")
#    ↓
# print("After")


