1. Method Overriding (Animal → Dog)
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


d = Dog()
d.sound()




2. Method Overriding with super()
class A:

    def show(self):
        print("Class A")


class B(A):

    def show(self):
        super().show()
        print("Class B")


obj = B()
obj.show()





3. Multi-Level Inheritance
class A:

    def display(self):
        print("Class A")


class B(A):

    def display(self):
        print("Class B")


class C(B):

    def display(self):
        print("Class C")


obj = C()
obj.display()





4. Hierarchical Inheritance
class Vehicle:

    def vehicle(self):
        print("Vehicle Class")


class Car(Vehicle):

    def wheels(self):
        print("Car has 4 wheels")


class Bike(Vehicle):

    def wheels(self):
        print("Bike has 2 wheels")


c = Car()
b = Bike()

c.vehicle()
c.wheels()

b.vehicle()
b.wheels()



5. Employee → Manager (Method Overriding)
class Employee:

    def salary(self):
        print("Salary = 30000")


class Manager(Employee):

    def salary(self):
        super().salary()
        print("Salary with Incentive = 40000")


m = Manager()
m.salary()




6. University → College (Class Variable & Class Method)
class University:

    university_name = "JNTU"

    @classmethod
    def show_university(cls):
        print("University:", cls.university_name)


class College(University):
    pass


print(College.university_name)
College.show_university()



7. Static Method Inheritance
class MathOps:

    @staticmethod
    def add(a, b):
        return a + b


class AdvancedOps(MathOps):
    pass


print(AdvancedOps.add(10, 20))




8. Multiple Inheritance (MRO)
class Father:

    def skills(self):
        print("Father Skills")


class Mother:

    def skills(self):
        print("Mother Skills")


class Child(Father, Mother):
    pass


c = Child()

c.skills()

print(Child.mro())



9. Abstract Class
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area =", self.length * self.breadth)


r = Rectangle(10, 5)
r.area()


10. Constructor Inheritance using super()
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print("Name =", self.name)
        print("Roll =", self.roll)


s = Student("Tharun", 101)

s.display()