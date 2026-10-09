# Q1. Bank Account Operations

# class BankAccount:
#
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Balance")
#
#     def __str__(self):
#         return f"Account Holder : {self.account_holder}\nBalance : {self.balance}"
#
#     def __add__(self, other):
#         return self.balance + other.balance
#
#     def __sub__(self, other):
#         return self.balance - other.balance
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __lt__(self, other):
#         return self.balance < other.balance
#
#     def __getattribute__(self, name):
#         print("Accessing:", name)
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, value):
#         if name == "balance" and value < 0:
#             print("Negative balance not allowed")
#         else:
#             object.__setattr__(self, name, value)
#
#
# a1 = BankAccount("Tharun", 5000)
# a2 = BankAccount("Rahul", 3000)
#
# a1.deposit(1000)
# a2.withdraw(500)
#
# print(a1)
# print(a2)
#
# print("Addition =", a1 + a2)
# print("Subtraction =", a1 - a2)
# print("Equal =", a1 == a2)
# print("Less Than =", a1 < a2)
#
# print(a1.balance)
#
# a1.balance = -100


# Q2. Product Price Comparison
#
# class Product:
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total_price(self):
#         return self.price * self.quantity
#
#     def __str__(self):
#         return f"{self.name} {self.price} {self.quantity}"
#
#     def __add__(self, other):
#         return self.total_price() + other.total_price()
#
#     def __mul__(self, number):
#         return self.price * number
#
#     def __gt__(self, other):
#         return self.total_price() > other.total_price()
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#     def __getattr__(self, name):
#         return "Attribute not found"
#
#     def __setattr__(self, name, value):
#         if name == "price" and value < 0:
#             print("Price cannot be negative")
#         else:
#             object.__setattr__(self, name, value)
#
#
# p1 = Product("Laptop", 50000, 2)
# p2 = Product("Mobile", 25000, 3)
#
# print(p1)
# print(p2)
#
# print("Total Price Addition =", p1 + p2)
# print("Multiply Price =", p1 * 2)
# print("Greater =", p1 > p2)
# print("Equal Price =", p1 == p2)
#
# print(p1.color)
#
# p1.price = -500
#
#
#
# Q3. Student Marks
#
# class Student:
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 75:
#             return "B"
#         elif self.marks >= 60:
#             return "C"
#         elif self.marks >= 40:
#             return "D"
#         else:
#             return "F"
#
#     def __str__(self):
#         return f"{self.name} {self.marks}"
#
#     def __add__(self, other):
#         return self.marks + other.marks
#
#     def __truediv__(self, number):
#         return self.marks / number
#
#     def __ge__(self, other):
#         return self.marks >= other.marks
#
#     def __lt__(self, other):
#         return self.marks < other.marks
#
#     def __getattribute__(self, name):
#         print("Accessing:", name)
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, value):
#         if name == "marks" and (value < 0 or value > 100):
#             print("Marks should be between 0 and 100")
#         else:
#             object.__setattr__(self, name, value)
#
#
# s1 = Student("Tharun", 85)
# s2 = Student("Rahul", 70)
#
# print(s1)
# print(s2)
#
# print("Grade:", s1.grade())
#
# print("Total Marks =", s1 + s2)
# print("Average =", s1 / 2)
#
# print("Greater or Equal =", s1 >= s2)
# print("Less Than =", s1 < s2)
#
# print(s1.name)
#
# s1.marks = 150
#
#
#
# Q4. Rectangle Area Comparison
# class Rectangle:
#
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def area(self):
#         return self.length * self.breadth
#
#     def __str__(self):
#         return f"Length={self.length}, Breadth={self.breadth}"
#
#     def __add__(self, other):
#         return self.area() + other.area()
#
#     def __sub__(self, other):
#         return self.area() - other.area()
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __gt__(self, other):
#         return self.area() > other.area()
#
#     def __getattr__(self, name):
#         return "Attribute not found"
#
#     def __setattr__(self, name, value):
#         if (name == "length" or name == "breadth") and value <= 0:
#             print("Length and Breadth must be positive")
#         else:
#             object.__setattr__(self, name, value)
#
#
# r1 = Rectangle(10, 5)
# r2 = Rectangle(8, 6)
#
# print(r1)
# print(r2)
#
# print("Area1 =", r1.area())
# print("Area2 =", r2.area())
#
# print("Addition =", r1 + r2)
# print("Subtraction =", r1 - r2)
#
# print("Equal =", r1 == r2)
# print("Greater =", r1 > r2)
#
# print(r1.color)
#
# r1.length = -2
#
#
#
# Q5. Employee Salary System
# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def annual_salary(self):
#         return self.salary * 12
#
#     def __str__(self):
#         return f"{self.name} {self.salary}"
#
#     def __add__(self, other):
#         return self.salary + other.salary
#
#     def __mul__(self, months):
#         return self.salary * months
#
#     def __ne__(self, other):
#         return self.salary != other.salary
#
#     def __le__(self, other):
#         return self.salary <= other.salary
#
#     def __getattribute__(self, name):
#         print("Accessing:", name)
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, value):
#         if name == "salary" and value < 10000:
#             print("Salary cannot be below 10000")
#         else:
#             object.__setattr__(self, name, value)
#
#
# e1 = Employee("Tharun", 50000)
# e2 = Employee("Rahul", 60000)
#
# print(e1)
# print(e2)
#
# print("Annual Salary =", e1.annual_salary())
#
# print("Salary Addition =", e1 + e2)
#
# print("Salary for 6 Months =", e1 * 6)
#
# print("Not Equal =", e1 != e2)
#
# print("Less Than or Equal =", e1 <= e2)
#
# print(e1.name)
#
# e1.salary = 5000
#
#
# Q6. Book Object Comparison
# class Book:
#
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def reading_time(self):
#         return self.pages * 2
#
#     def __str__(self):
#         return f"{self.title} {self.author} {self.pages}"
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
#     def __floordiv__(self, days):
#         return self.pages // days
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#     def __eq__(self, other):
#         return self.title == other.title
#
#     def __getattr__(self, name):
#         return "Attribute not found"
#
#     def __setattr__(self, name, value):
#         if name == "title" and value == "":
#             print("Title cannot be empty")
#         elif name == "pages" and value <= 0:
#             print("Pages must be positive")
#         else:
#             object.__setattr__(self, name, value)
#
#
# b1 = Book("Python", "Guido", 300)
# b2 = Book("Java", "James", 250)
#
# print(b1)
# print(b2)
#
# print("Reading Time =", b1.reading_time())
#
# print("Total Pages =", b1 + b2)
#
# print("Pages Per Day =", b1 // 5)
#
# print("Greater =", b1 > b2)
#
# print("Equal =", b1 == b2)
#
# print(b1.publisher)
#
# b1.pages = -50
#
#
#
# Q7. Shopping Cart
# class CartItem:
#
#     def __init__(self, item_name, price, quantity):
#         self.item_name = item_name
#         self.price = price
#         self.quantity = quantity
#
#     def final_amount(self):
#         return self.price * self.quantity
#
#     def __str__(self):
#         return f"{self.item_name} {self.price} {self.quantity}"
#
#     def __add__(self, other):
#         return self.final_amount() + other.final_amount()
#
#     def __mod__(self, discount):
#         return self.final_amount() % discount
#
#     def __lt__(self, other):
#         return self.final_amount() < other.final_amount()
#
#     def __ge__(self, other):
#         return self.quantity >= other.quantity
#
#     def __getattribute__(self, name):
#         print("Accessing:", name)
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, value):
#         if name == "quantity" and value < 1:
#             print("Quantity cannot be less than 1")
#         else:
#             object.__setattr__(self, name, value)
#
#
# c1 = CartItem("Laptop", 50000, 2)
# c2 = CartItem("Mouse", 1000, 5)
#
# print(c1)
# print(c2)
#
# print("Final Amount =", c1.final_amount())
#
# print("Addition =", c1 + c2)
#
# print("Discount Remainder =", c1 % 1000)
#
# print("Less Than =", c1 < c2)
#
# print("Greater or Equal Quantity =", c1 >= c2)
#
# print(c1.price)
#
# c1.quantity = 0
#
#
# Q8. Time Duration
# class TimeDuration:
#
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
#
#     def total_minutes(self):
#         return self.hours * 60 + self.minutes
#
#     def __str__(self):
#         return f"{self.hours} Hours {self.minutes} Minutes"
#
#     def __add__(self, other):
#         return self.total_minutes() + other.total_minutes()
#
#     def __sub__(self, other):
#         return self.total_minutes() - other.total_minutes()
#
#     def __eq__(self, other):
#         return self.total_minutes() == other.total_minutes()
#
#     def __gt__(self, other):
#         return self.total_minutes() > other.total_minutes()
#
#     def __getattr__(self, name):
#         return "Attribute not found"
#
#     def __setattr__(self, name, value):
#         if name == "minutes" and (value < 0 or value > 59):
#             print("Minutes must be between 0 and 59")
#         else:
#             object.__setattr__(self, name, value)
#
#
# t1 = TimeDuration(2, 30)
# t2 = TimeDuration(1, 45)
#
# print(t1)
# print(t2)
#
# print("Total Minutes =", t1.total_minutes())
#
# print("Addition =", t1 + t2)
#
# print("Subtraction =", t1 - t2)
#
# print("Equal =", t1 == t2)
#
# print("Greater =", t1 > t2)
#
# print(t1.seconds)
#
# t1.minutes = 70
#
#
#
#
# Q9. Laptop Specification
# class Laptop:
#
#     def __init__(self, brand, ram, price):
#         self.brand = brand
#         self.ram = ram
#         self.price = price
#
#     def upgrade_ram(self, extra_ram):
#         self.ram += extra_ram
#
#     def __str__(self):
#         return f"{self.brand} {self.ram}GB ₹{self.price}"
#
#     def __add__(self, other):
#         return self.price + other.price
#
#     def __mul__(self, number):
#         return self.price * number
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __eq__(self, other):
#         return self.ram == other.ram
#
#     def __getattribute__(self, name):
#         print("Accessing:", name)
#         return object.__getattribute__(self, name)
#
#     def __setattr__(self, name, value):
#         if (name == "ram" or name == "price") and value <= 0:
#             print("RAM and Price must be positive")
#         else:
#             object.__setattr__(self, name, value)
#
#
# l1 = Laptop("HP", 8, 50000)
# l2 = Laptop("Dell", 16, 65000)
#
# print(l1)
# print(l2)
#
# l1.upgrade_ram(8)
#
# print("After Upgrade")
# print(l1)
#
# print("Price Addition =", l1 + l2)
#
# print("Bulk Price =", l1 * 3)
#
# print("Less Than =", l1 < l2)
#
# print("RAM Equal =", l1 == l2)
#
# print(l1.brand)
#
# l1.ram = -4
#
#
#
#
# Q10. Game Player
# class Player:
#
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power
#
#     def attack(self, enemy):
#         enemy.health -= self.attack_power
#
#     def __str__(self):
#         return f"{self.name} Health={self.health} Attack={self.attack_power}"
#
#     def __add__(self, other):
#         return self.attack_power + other.attack_power
#
#     def __sub__(self, other):
#         return self.health - other.attack_power
#
#     def __gt__(self, other):
#         return self.health > other.health
#
#     def __eq__(self, other):
#         return self.attack_power == other.attack_power
#
#     def __getattr__(self, name):
#         return "Player stat not found"
#
#     def __setattr__(self, name, value):
#         if name == "health" and value < 0:
#             value = 0
#         object.__setattr__(self, name, value)
#
#
# p1 = Player("Warrior", 100, 20)
# p2 = Player("Knight", 120, 15)
#
# print(p1)
# print(p2)
#

print("hello")
# p1.attack(p2)
#
# print("After Attack")
# print(p2)
#
# print("Combined Attack =", p1 + p2)
#
# print("Health Difference =", p1 - p2)
#
# print("Greater Health =", p1 > p2)
#
# print("Attack Equal =", p1 == p2)
#
# print(p1.speed)
#
# p1.health = -50
#
# print(p1)