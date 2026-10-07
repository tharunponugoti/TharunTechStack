#self

# What is self?
# self is a reference to the current object.

#self tells Python which object we are currently working with.

# It is mainly used inside instance methods to access:
#
# Instance variables
# Instance methods
# The current object's data

# self is a reference variable which is always pointing to current object within the
# python class, to access current object we will use self
#
# the first parameter of constructor is self
#
#
# the first parameter of instance method is self
#
# we are not require to provide value for self variable pvm itself will provide value
#
#
# we can use self within the python class only, inside the constructor we can use self to declare
# object related variables(Instance Variables)
#
# Inside the instance method we will use self to access the values of instance variables
#
# self is not a keyword, we can use delf,kelf instead self but it is recommended to use self
#
# --why are using self variables always
#
# to get current object variable value


# class tharun:
#     def __init__(self):
#         self.name = "ponu"
#     def display(self):
#         print(id(self))
# p=tharun()
# print(id(p))
# p.display()


-----Constructor

A constructor is a special method in a class that is automatically executed when an object is created.

constructor is a special method in python

the name of the constructor is __init__()

the first parameter of constructor is self

we are reqiured call the constructor explicitly

it will execute automatically when we create the object

for object or each object constructor will be executed only once

the main purpose of constructor is declare the instance variables and initialize instance variables
to object


__init__ means initialization


Constructor should take at least one arguemnt

with in the python class constructor is optional

if we are not providing constructor default constructor will be provided by pvm

class Test:
    def m1(self):
        print("m1")
t=test()


but with out writing constructor we cannot pass arguement then it is meaning
it is better to use consrtuctor


class Test:
    def m1(self):
        print("Im Constructor")
t=Test()       ------object creation only once
t.__init__()
t.__init__()


