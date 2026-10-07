Q1. Student Encapsulation
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks


s = Student("Tharun", 85)

print("Name:", s.name)
print("Marks:", s.get_marks())

s.set_marks(95)
print("Updated Marks:", s.get_marks())

s.set_marks(120)





Q2. Bank Account Encapsulation
class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


b = BankAccount("Tharun", 10000)

b.deposit(2000)
b.withdraw(3000)

print("Balance:", b.get_balance())




Q3. Employee Encapsulation
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_salary(self, salary):
        if salary >= 10000:
            self.__salary = salary
        else:
            print("Invalid Salary")

    def get_salary(self):
        return self.__salary


e = Employee("Rahul", 30000)

print(e.get_salary())

e.set_salary(40000)
print(e.get_salary())

e.set_salary(5000)





Q4. Rectangle Encapsulation
class Rectangle:

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def set_length(self, length):
        if length > 0:
            self.__length = length

    def set_breadth(self, breadth):
        if breadth > 0:
            self.__breadth = breadth


r = Rectangle(10, 5)

print("Area:", r.area())

r.set_length(20)
r.set_breadth(8)

print("Updated Area:", r.area())






Q5. Car Encapsulation
class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed

    def accelerate(self, value):
        self.__speed += value

    def brake(self, value):
        if value <= self.__speed:
            self.__speed -= value

    def show_speed(self):
        print("Speed:", self.__speed)


c = Car("BMW", 80)

c.show_speed()

c.accelerate(20)
c.show_speed()

c.brake(30)
c.show_speed()



Q6. Create a class Student with private marks and percentage
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks

    def percentage(self):
        return self.__marks


s = Student("Tharun", 85)

print("Name:", s.name)
print("Marks:", s.get_marks())
print("Percentage:", s.percentage(), "%")

s.set_marks(95)

print("\nAfter Updating")
print("Marks:", s.get_marks())
print("Percentage:", s.percentage(), "%")




Q7. Create a class Mobile with private price
class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid Price")

    def get_price(self):
        return self.__price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.__price)


m = Mobile("Samsung", 25000)

m.display()

m.set_price(30000)

print("\nAfter Updating")
m.display()




Q8. Create a class Circle with private radius
class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Invalid Radius")

    def get_radius(self):
        return self.__radius

    def area(self):
        return 3.14 * self.__radius * self.__radius


c = Circle(5)

print("Radius:", c.get_radius())
print("Area:", c.area())

c.set_radius(10)

print("\nAfter Updating")
print("Radius:", c.get_radius())
print("Area:", c.area())





Q9. Create a class Employee with private salary and bonus
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")

    def get_salary(self):
        return self.__salary

    def total_salary(self):
        bonus = self.__salary * 0.10
        return self.__salary + bonus


e = Employee("Rahul", 40000)

print("Salary:", e.get_salary())
print("Total Salary:", e.total_salary())

e.set_salary(50000)

print("\nAfter Updating")
print("Salary:", e.get_salary())
print("Total Salary:", e.total_salary())




Q10. Create a class Laptop with private RAM
class Laptop:

    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram

    def upgrade_ram(self, extra):
        self.__ram += extra

    def get_ram(self):
        return self.__ram

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.__ram, "GB")


l = Laptop("HP", 8)

l.display()

l.upgrade_ram(8)

print("\nAfter RAM Upgrade")
l.display()