# ----What is an Object
# An object is a real entity created in Python that contains:
#
# Data → values/information
# Behavior → actions/functions it can perform
#
#
# Simple definition
#
# An object is an instance of a class.
#
#
#
# ----Syntax
# object_name = ClassName()
#
# Ex:
# class Student:
#     pass
# s1 = Student()
#
# Here:
#
# Student → Class
# s1 → Object
# Student() → creates the object
#
#
#
# ---Instance Variables are belongs objects

# An instance variable is a variable that belongs to a particular object (instance) of a class.
#
# Instance variable = Data that is separately stored for each object.

# ---The value of variables are varied from object to object then such a kind of variables are called Instance variables
# ---For each object a separate copy of instance variables will be shared
# ---we can declare instance variables inside the methods with the help of self variable
# ---We can access instance variables inside the class using self variable and outside the class
# by using reference variables
#
# One - line definition for interviews
#
# An instance variable is a variable that belongs to a specific object and stores data
# independently for each object, usually created using self inside __init__().
#
# When we Create Object __init__() runs automatically
#
# Real - Time Example Bank Account
#
# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
# account1 = BankAccount("Rahul", 5000)
# account2 = BankAccount("Ravi", 10000)
# print(account1.name,account1.balance)
# print(account2.name,account2.balance)

#
# Easy Way to Identify an Instance Variable
#
# self.something
#
# self.name
# self.age
# self.salary
# self.address
# self.marks

# Ex:
#
# class Student:
#     def __init__(self):
#         self.name = "tharun"
#         self.age = 24
#         self.marks = 90
# s1=Student()
# print(s1.name)
# print(s1.age)
# print(s1.marks)
#
#
#
#
# -----Class Variable/Static variable
# It belongs to class
# We can declare class Variables inside the class outside all methods
# If the values of variables not varied from object to object then the variables are calls as class variables
# for each object class variables are commonly shared or class variables are shared by objects in class
# We can access class variables inside the class by using cls variable and outside the class by using class name or
# Reference Variable
#
#
# Real-Time Examples
#
# class Student:
#
#     college = "ABC College"
#
#
# Interview Definition
#
# If an interviewer asks:
#
# What is a class variable in Python?
#
# You can answer:
#
# A class variable is a variable defined inside a class but outside methods.
# It belongs to the class and is shared by all objects of that class.
# We can access it using the class name or through an object.


# Ex:
#
# class Student:
#     collegename="Raghu College"
#     def __init__(self):
#         self.name = "tharun"
#         self.age = 24
#         self.marks = 90
# s1=Student()
# print(s1.collegename)
# print(s1.name)
# print(s1.age)
# print(s1.marks)
#
#
# ----Local variables
# to meet the temporary requirement of the programmer we will define local variables inside the method
# we can access inside the method only
#
#
# ----self always related to object
#
# Ex:

class Test:
    def m1(self):
        x=10
        print(x)
t=Test()
t.m1()

