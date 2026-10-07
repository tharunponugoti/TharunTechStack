# -----Functions in Python
#
# Function is a block of code which only runs when it is called()
#
#   Types of Functions
#
#   1,user defined function
#   2,predefined function
#
#   -----USER DEFINED FUNCTION
#
#   1,A FUNCTION which is defined by user to perform some task is known as USER DEFINED FUNCTION
#   2,In Python a Function is defined with "def" Keyword,(write once use anywhere)
#   3,The Main Usage of  Function concept is Reusability
#   4,Its Helps to avoid the repetition of code by using FUNCTION
#
# -----How to Create the Function
# We can Create the Function using def Keyword which is followed by
# Function name
# ():
# indented and then block of code
#
#     def functionname(parameters):
#         Block of Code
#
#     The above one is called as Function Definition or Called Function
#
# -----How to Call Function
# We can call Funciton by using function Name
#       Syntax
#      'functionname(Arguments)'
#     The above one is called as Calling Function
#
# Ex:
#    def Message():
#        print("Hello World")
#    Message()
#
# 1,A Function name can starts with Lower Case or Upper Case
# 2,A Function name can also starts with _
# 3,A Function name can not start with digits
#
#      We can Call the Functions in Differents ways
#
#      1,Calling function with Arguments and return type
#      2,Calling funtion with Arguments without return type
#      3,Calling function without Arguments with return type
#      4,Calling function without Arguments and return type
#
# Function calling stores in stack memory
#
#     Static input --- a=20
#     Dynamic input --- a=int(input())
#
# 1,Calling function with Arguments and return type
# def sum(a,b):
#     c=a+b
#     return c
# r=sum(10,20)
# print(r)
#
# 2,Calling funtion with Arguments without return type
#   def Sum(a,b):
#     c=a+b
#     print(c)
#   Sum(10,20)
#
# 3,Calling function without Arguments with return type
#   def Message():
#     return "Hello World"
#   r=Message()
#   print(r)
#
# 4,Calling function without Arguments and return type
#   def Message():
#       print("Hello World")
#   Message()
#
#   Important Example
#
# def Message():
#     return "Hello World"
#     print("end")----------------print Statement will not be executed(Not reachable code)
# r=Message()
# print(r)
# print("HI")
#
#
#
# ----- Default Parameter Value
#     We will assign default value to parameter and it will be used by function, when we call the function
#     without any arguments
# Ex:
# def Message(country="India"):
#     print("my country name is:",country)
# Message("usa")
#
#  ----o/p
#  my country name is:usa
#
# def Message(country="India"):
#     print("my country name is:",country)
# Message()
#
# -----o/p
# my country name is:India
#
#
# -----pass statement
# pass nothing but place holder
# If we dont know what to write in the code inside the function defination
# in that case we will use pass statement
#
# when we want to create the function place holder with any code then we will use pass statement
#
# Ex:
# def Message():
#     pass
#
#
# -----Positional Arguments
# def Info(fname,lname):
#     print("my first name is:",fname)
#     print("my last name is:",lname)
# Info("tharun","p")
#
# If we change the order of the Arguments the outputs will be changed thats why
# we Positional Arguements
#
#
#
# -----Keyword Arguements
# Here, we pass Keyword Arguements in the form of key value
#
# def Info(fname,lname):
#     print("my first name is:",fname)
#     print("my last name is:",lname)
# Info(fname="tharun",lname="p")
# Info(lname="p",fname="tharun")
#
# -----o/p
# my first name is:tharun
# my last name is:p
#
# my first name is:tharun
# my last name is:p
#
#
#
# -----Arbitrary Arguments/Variable length Arguments
#  If we dont know  to pass in the Function then you can add * before Parameters in Function definition
# then that function will accepts any numbers of arguments in the form of tuple
# And it can be Accessed by Index
#
#     ~Python will not Support Method Overloading Concept to achieve that concept we
#        use Arbitrary Arguments.
#
# Ex:
# def Sum(*a):
#     print(Sum(a))
# Sum(10,20)
# Sum(10,20,30)
# Sum(1,2,3,4,5,6)
#
# -----o/p
# 30
# 60
# 21
#
# RealLife Example: Calculator
#
#
# -----Arbitrary Keyword Arguments
#  If we dont know how many Keyword Arguments passed to the function then add **
# before parameters in function definition, then that function will accept any number of
# keyword Arguments and it will be stored in Dictionary
#
# def info(**d):
#     print(d)
# Info(fname="tharun")
# Info(lname="p",fname="tharun")
# Info(age=24,color="white",height="6 feet")
#
# Example : Registration Form
#
#
# How to pass Positional Arguments and Keyword Arguments at a time in function
#
# def Info(collegename,fname,lname):
#     print("my college name is:",collegename)
#     print("my first name is:",fname)
#     print("my last name is:",lname)
#
# Info(collegename:"Raghu",fname="tharun",lname="p")
#
# -----o/p
# my college name is: Raghu
# my first name is: tharun
# my last name is: p
#
#
# How to pass Arbitory Arguments and Keyword Arbitory Arguments at a time in function
#
# def Data(a,*l):
#     print(a)
#     print(l)
# Data (a:10,*l:1,2,3,4,5)
#
# ------o/p
# 10
# (1,2,3,4,5)
#
#
# How to pass list as Argument into function
#
# def Data(l):
#     sum=0
#     for i in l:
#         sum=sum+i
#     print(sum)
# list=[1,2,3,4,5]
# Data(list)
#
# -----o/p
# 15
#
#
# Scope of Variables
#  It defines where the variables can we access in the code
#  1.Local Scope/Local variables
#  2.Global Scope/Global variables
#
# -----Local Variables
# We can create Local Variables inside the function and it can be accessed inside the function only,
# we cant access outside the function
#
# def Display():
#     x=10
#     print(x)
# Dispaly()
#
# ----o/p
# x=10
#
#
# -----Global Variables
# It is created top of all functions and it can be access anywhere in the program
#
#
# x=30
# def Dispaly():
#     x=10:
#     print(x)
# Display()
# print(x)
#
# -----o/p
# 10
# 30
#
# * First preference goes to Local variable
#
# Ex:
# x=30
# def Dispaly():
#     x=40
#     print(x)
# Dispaly()
# print(x)
#
# -----o/p
# 40
# 30
#
#
# -----pass by value/call by value
#
# 1,We can Call the function by passing the value, If we do any changes inside the function
# that wont effected outside the function that is simply called as pass by value
# (we cant change the Original one).
#
# 2,It works with immutable data type (int,float,tuple,string)
#
# def change(x):
#     x=x+1
#     print("x value inside function:",x)
# x=10
# print("x value Before calling function:",x)
# change(x)
# print("x value After calling function:",x)
#
# ---o/p
# x value Before calling function: 10
# x value inside function: 11
# x value After calling function: 10
#
# Real Life Example:
#  OTP & Aadhar Card xerox copy
#
#
#
# -----pass by reference(Address)/call by reference
# 1,Here we can call the function by passing the reference if we do changes inside the function
# that will be affected outside the function
#
# 2,It works with mutable data type (List,Dictionary)
#
# def change(l):
#     l.append('car')
# cart=['Apple','mobile','bike']
# print(cart)
# change(cart) ---passing address
# print(cart)
#
#
# -----BuiltIn Functions/Pre defined Functions
#
# These are pre-functions available in Python that performs common operations
#
# print()
# len()
# abs()
# max()
# sorted()
#
#
#
#
#
# ------Anonymous Function(lambda functions)
#
# 1,A Lambda function is a small Anonymous function that is used to perform short task
# without defining function by using def keyword
#
# 2,Lambda function is a function without its name , its accepts multiple Arguments
# and it has only one expression
#
# 3,Lambda function is defined with lambda keyword
#
# -----syntax
#
# lambda arguments:expression
#
# lambda: lambda function is defined with lambda
# argument: input values
# expression: It is a single line of code that returns o/p
#
#  Ex:
#  square=lambda n:n*n
#  print(square(7))
#
#  ---write a program sum of two numbers by using lambda function
# sum=lambda a,b:a+b
# print(sum(10,20))
#
# -----uses of lambda functions
# 1, It helps you to write concise and short code( No need to use def or return keyword)
#  these functions are used with Map,filter,sorted Functions
# 2,One time use it is good or quick operations
#
#
---How to use lambda function with if else condition
#
largestno=lambda a,b: f"{a} is largest no"if a>b else f"{b} is largest no"
print(largestno(10,20))




