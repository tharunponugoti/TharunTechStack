# ----Instance method
#
#-----It is used to work with instance variables
#-----We can declare the instance methods inside the class, the first parameter of
# instace method is self
#-----If you are accesing Instance Variables inside the Methods then such of method called as Instance Method

# Ex:
#
# class Student:
#     def __init__(self,name,marks,age):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.marks)
# s1=Student(name="tharun",age=30,marks=50)
# s1.display()








# ---class Method
#
# ----It is used to work with class variables
# ----We can declare class method inside the class, the first parameter of class method is cls
# to make the method as class method we use @classmethod decorator
#
# Ex:
#
# class Student:
#      collagename="Raghu"
#      @classmethod
#      def GetStudentInfo(cls):
#          print(cls.collagename)
# print(Student.collagename)
# Student.GetStudentInfo()



#
# ----Static Method
# It has no relation with class and method
# It is utility method or helper inside the class
# the first parameter of static method is neither self nor cls
# we cant use self , cls inside static method
# to make the method as static method, we need to declare method
# as @staticmethod decorator

#
# class Test:
#     @staticmethod
#     def Add():
#         print("Im Static Method")
# t=Test()
# t.Add()



# class Test:
#     @staticmethod
#     def Mul(a,b):
#         print(a*b)
# t=Test()
# t.Mul(10,20)

#
#
# How to access Instance Variables?
# Inside the class
#
# Use
#
# self.
#
# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name)
#         print(self.age)
#
#
# Outside the class
#
#  Use the object name
#
#  s1 = Student("Tharun", 24)
#
#  print(s1.name)
#  print(s1.age)
#
#
#
#  Inside class → self.variable
#
#  Outside class → object.variable
#
#
#  class Variable
#
# class Student:
#     college = "ABC College"
#
#     def display(self):
#         print(Student.college)
#
#
# Outside the class
#
# print(Student.college)
#
#
#
#
# Local Variables
#
# class Student:
#     def display(self):
#         x = 10
#         print(x)
#
#
# But you cannot normally do:
#
# s = Student()
# print(s.x)
#
# because x is not an instance variable.
#
# Important Difference
#
# self.x = 10
#
# means:
#
# Instance variable
#
# Whereas:
#
# x = 10
#
# means: Local variable
#
#
#
# Instance Method
#
# Instance Method accessing Instance Variable
#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#     def display(self):
#         print(self.name)
#
# Create object
#
# s1 = Student("Tharun")
#
#
# Call
#
# s1.display()
#
# The instance method accesses the instance variable through self.
#
#
# classMethod
#
# @classmethod
#
# And it takes cls as its first parameter
#
#
# class Student:
#
#     college = "ABC College"
#
#     @classmethod
#     def display_college(cls):
#         print(cls.college)
#
# call it
#
# Student.display_college()
#
#
# cls.college
#
# Access the class variable belonging to the current class.
#
#
# Can
# we
# call
# a
#
#
# class method using an object?
#
#
# Yes.
#
# s1 = Student()
#
# s1.display_college()
#
#
#
# Static Method
#
# A static method is a method that does not need self or cls.
#
# @staticmethod
#
# class Student:
#
#     @staticmethod
#     def add(a, b):
#         return a + b



# Example:
class Student:

    college = "ABC College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        x = 100
        print(x)
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)
        print("Local:", x)

    @classmethod
    def college_info(cls):
        print("College:", cls.college)

    @staticmethod
    def add(a, b):
        print("Sum:", a + b)

s1 = Student("Tharun", 24)
print(s1.name)
print(s1.age)
print(Student.college)
s1.display()
Student.college_info()
Student.add(10, 20)


#
# | Member            | Inside Class                      | Outside Class     | Uses              |
# | ----------------- | --------------------------------- | ----------------- | ----------------- |
# | Instance Variable | `self.name`                       | `s1.name`         | Object            |
# | Class Variable    | `Student.college` / `cls.college` | `Student.college` | Class             |
# | Local Variable    | `x`                               | ❌ Not directly    | Method            |
# | Instance Method   | `self.display()`                  | `s1.display()`    | Object            |
# | Class Method      | `cls.info()` / `Student.info()`   | `Student.info()`  | Class             |
# | Static Method     | `Student.add()`                   | `Student.add()`   | Independent logic |
