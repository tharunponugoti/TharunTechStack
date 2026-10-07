import importlib

module_name = input("Enter module name: ")

try:
    module = importlib.import_module(module_name)
    print("Module imported successfully.")
except ModuleNotFoundError:
    print("Module does not exist")







class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student:
    def __init__(self, roll):
        self.roll = roll

    def show_roll(self):
        print("Roll No:", self.roll)



from mypackage.person import Person
from mypackage.student import Student

class CollegeStudent(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display_course(self):
        print("Course:", self.course)

p = Person("Rahul")
p.display()

s = Student(101)
s.show_roll()

c = CollegeStudent("Kiran", "Python")
c.display()
c.display_course()




import module2

def fun1():
    print("Function from Module1")

import module1

def fun2():
    print("Function from Module2")


import module1
import module2

module1.fun1()
module2.fun2()




from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


from .shape import Shape

class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


from shapes.rectangle import Rectangle, Square

objects = [
    Rectangle(10, 5),
    Square(4)
]

for obj in objects:
    print("Area =", obj.area())






class Animal:

    def speak(self):
        print("Animal speaks")
class Walkable:

    def speak(self):
        print("Walkable object")

from animal import Animal
from walkable import Walkable

class Dog(Animal, Walkable):

    def speak(self):
        print("Dog barks")
from dog import Dog

d = Dog()

d.speak()

print(Dog.__mro__)






class Employee:

    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Invalid Salary")
from employee import Employee

emp = Employee(30000)

print(emp.salary)

emp.salary = 50000
print(emp.salary)

emp.salary = -2000

print(emp.salary)

# Direct access
# print(emp.__salary)    # Error







class Engine:

    def start(self):
        print("Engine Started")


class CarComposition:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is Moving")


class Vehicle:

    def move(self):
        print("Vehicle Moving")


class CarInheritance(Vehicle):

    def drive(self):
        self.move()
        print("Car is Driving")


from vehicle import CarComposition, CarInheritance

print("Composition")

c1 = CarComposition()
c1.drive()

print()

print("Inheritance")

c2 = CarInheritance()
c2.drive()


