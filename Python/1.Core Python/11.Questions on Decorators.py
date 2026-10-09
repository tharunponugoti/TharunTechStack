# 1,Add Before & After Messages
# Create a decorator that prints "Start" before the function execution and "End" after it finishes.
# • Expected Output:
# o Start
# o Hello
# o End
#
#
# def my_decorator(func):
#
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#
#     return wrapper
#
#
# @my_decorator
# def hello():
#     print("Hello")
#
#
# hello()
#
#
# 2,Decorator With Input (Parameters)
# Create a decorator that works for a function taking a name as input. It should print "Starting..."
# before greeting the user.
# • Function: def greet(name): print("Hello", name)
# • Expected Output:
# o Starting...
# o Hello Ravi
# o Done


#
# def my_decorator(func):
#
#     def wrapper(name):
#         print("Starting...")
#         func(name)
#         print("Done")
#
#     return wrapper
#
#
# @my_decorator
# def greet(name):
#     print("Hello", name)
#
#
# greet("Ravi")
#
#
#
# greet("Ravi")
#        ↓
# wrapper("Ravi")
#        ↓
# Starting...
#        ↓
# func("Ravi")
#        ↓
# Hello Ravi
#        ↓
# Done
#
#
#
# 3.Result Doubler
# Create a decorator that captures the value returned by a function and multiplies it by 2 before
# returning it.
# • Example: If the function returns 25, the final output should be 50.
#
#
# def double_result(func):
#
#     def wrapper():
#         result = func()
#         return result * 2
#
#     return wrapper
#
#
# @double_result
# def get_number():
#     return 25
#
#
# print(get_number())


# 4,Admin Access Check
# Create a decorator that checks a user_role variable. If the role is not "admin", it should print
# "Access Denied" and prevent the function from running.
# • Expected Output: Access Denied (if user is a 'student').
#
#
# def admin_only(func):
#
#     def wrapper(user_role):
#         if user_role != "admin":
#             print("Access Denied")
#             return
#
#         func(user_role)
#
#     return wrapper
#
#
# @admin_only
# def dashboard(user_role):
#     print("Welcome to Admin Dashboard")
#
#
# dashboard("student")


#
# 5.Uppercase Output
# Create a decorator that takes a string returned by a function and converts the entire string to
# uppercase.
# • Function: def get_msg(): return "hello world"
# • Expected Output: HELLO WORLD
#
#
# ```python
# def uppercase(func):
#
#     def wrapper():
#         result = func()
#         return result.upper()
#
#     return wrapper
#
#
# @uppercase
# def get_msg():
#     return "hello world"
#
#
# print(get_msg())

