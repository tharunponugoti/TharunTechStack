Q1. Animal Sounds (Runtime Polymorphism)
class Animal:

    def make_sound(self):
        print("Animal Sound")


class Dog(Animal):

    def make_sound(self):
        print("Dog Barks")


class Cat(Animal):

    def make_sound(self):
        print("Cat Meows")


class Cow(Animal):

    def make_sound(self):
        print("Cow Moos")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.make_sound()



Q2. Duck Typing (Behavior-Based Polymorphism)
class Car:

    def start(self):
        print("Car Starts")


class Computer:

    def start(self):
        print("Computer Starts")


class WashingMachine:

    def start(self):
        print("Washing Machine Starts")


def operate(device):
    device.start()


c = Car()
co = Computer()
w = WashingMachine()

operate(c)
operate(co)
operate(w)

Output

Car Starts
Computer Starts
Washing Machine Starts

This works because Python follows duck typing—if an object has a start() method, it can be passed to operate(), regardless of inheritance.

Q3. Vector Class (Operator Overloading)
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = Vector(2, 3)

result = v1 + v2

print("Vector Addition =", result)

print("v1 == v2 :", v1 == v2)

print("v1 == v3 :", v1 == v3)



Q4. Transport (Method Overriding with super())
class Transport:

    def move(self):
        print("Transport is Moving")


class Bus(Transport):

    def move(self):
        super().move()
        print("Bus is Moving on Road")


class Bike(Transport):

    def move(self):
        super().move()
        print("Bike is Moving Fast")


b1 = Bus()
b2 = Bike()

b1.move()
print()

b2.move()



Q5. Abstract Class (Notification)
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):

    def send(self):
        print("Email Notification Sent")


class SMSNotification(Notification):

    def send(self):
        print("SMS Notification Sent")


class PushNotification(Notification):

    def send(self):
        print("Push Notification Sent")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    n.send()



Q6. Payment Method (Different Method Signature)
class Payment:

    def process(self, amount):
        print("Payment Amount:", amount)


class CreditCardPayment(Payment):

    def process(self, amount, card_type):
        print("Payment:", amount)
        print("Card Type:", card_type)


p = Payment()
p.process(5000)

c = CreditCardPayment()
c.process(5000, "Visa")

Note:

If you write:

c.process(5000)

Python raises a TypeError because card_type is missing.


class Payment:

    def process(self, amount):
        print("Payment Amount:", amount)


class CreditCardPayment(Payment):

    def process(self, amount, card_type=None):
        if card_type is None:
            print("Payment Amount:", amount)
        else:
            print("Payment Amount:", amount)
            print("Card Type:", card_type)


p = Payment()
p.process(5000)

c = CreditCardPayment()
c.process(5000)
c.process(5000, "Visa")



Q7. Strategy Pattern (Polymorphism Without Inheritance)
class BS:

    def logic(self):
        print("Bubble Sort")


class MS:

    def logic(self):
        print("Merge Sort")


class QS:

    def logic(self):
        print("Quick Sort")


class Sorter:

    def change(self, strategy):
        self.strategy = strategy

    def sort(self):
        self.strategy.logic()


s = Sorter()

s.change(BS())
s.sort()

s.change(MS())
s.sort()

s.change(QS())
s.sort()


Q8. Multi-Level Polymorphism (Account → SavingsAccount → PremiumSavingsAccount)
class Account:

    def withdraw(self):
        print("Withdraw from Account")


class SavingsAccount(Account):

    def withdraw(self):
        print("Withdraw from Savings Account")


class PremiumSavingsAccount(SavingsAccount):

    def withdraw(self):
        super().withdraw()
        print("Extra Benefits for Premium Savings Account")


a = Account()
s = SavingsAccount()
p = PremiumSavingsAccount()

print("Account:")
a.withdraw()

print("\nSavings Account:")
s.withdraw()

print("\nPremium Savings Account:")
p.withdraw()
Output
Account:
Withdraw from Account

Savings Account:
Withdraw from Savings Account

Premium Savings Account:
Withdraw from Savings Account
Extra Benefits for Premium Savings Account



Q9. Duck Typing (draw() Function)
class Circle:

    def draw(self):
        print("Drawing Circle")


class Square:

    def draw(self):
        print("Drawing Square")


class Rectangle:

    def draw(self):
        print("Drawing Rectangle")


class Car:

    def draw(self):
        print("Drawing Car")


def draw(shape):
    shape.draw()


c = Circle()
s = Square()
r = Rectangle()
car = Car()

draw(c)
draw(s)
draw(r)
draw(car)
Output
Drawing Circle
Drawing Square
Drawing Rectangle
Drawing Car
Explanation

Python uses Duck Typing.

The draw() function does not care about the object's type. It only checks whether the object has a draw() method.

Since Car also has a draw() method, it works even though it is not related to the other classes.

Q10. Payment System (Polymorphism)
Method 1: Polymorphism (Recommended)
class UPI:

    def pay(self):
        print("Payment through UPI")


class Card:

    def pay(self):
        print("Payment through Card")


class Cash:

    def pay(self):
        print("Payment through Cash")


payments = [UPI(), Card(), Cash()]

for p in payments:
    p.pay()
Output
Payment through UPI
Payment through Card
Payment through Cash




Method 2: Using isinstance()
class UPI:

    def pay(self):
        print("Payment through UPI")


class Card:

    def pay(self):
        print("Payment through Card")


class Cash:

    def pay(self):
        print("Payment through Cash")


def make_payment(obj):

    if isinstance(obj, UPI):
        obj.pay()

    elif isinstance(obj, Card):
        obj.pay()

    elif isinstance(obj, Cash):
        obj.pay()

    else:
        print("Invalid Payment")


make_payment(UPI())
make_payment(Card())
make_payment(Cash())
Output
Payment through UPI
Payment through Card
Payment through Cash