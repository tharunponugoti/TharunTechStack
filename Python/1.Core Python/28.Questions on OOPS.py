from abc import ABC, abstractmethod

class Account(ABC):
    interest_rate = 5

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.validate_amount(amount):
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print("Insufficient Balance")

    @abstractmethod
    def calculate_interest(self):
        pass

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @classmethod
    def update_interest_policy(cls, rate):
        cls.interest_rate = rate


class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class CurrentAccount(Account):
    def calculate_interest(self):
        return self.balance * 2 / 100


class FixedDepositAccount(Account):
    def calculate_interest(self):
        return self.balance * 8 / 100


accounts = [
    SavingsAccount("S101", 10000),
    CurrentAccount("C101", 15000),
    FixedDepositAccount("F101", 20000)
]

Account.update_interest_policy(6)

print("Interest Details")
for acc in accounts:
    print(type(acc).__name__, "Interest =", acc.calculate_interest())

accounts[0].deposit(2000)
accounts[1].withdraw(3000)

print("\nBalance using property:", accounts[0].balance)

try:
    print(accounts[0].__balance)
except AttributeError:
    print("Direct access to private balance is not allowed.")











class Vehicle:
    def calculate_fare(self, distance):
        pass


class Car(Vehicle):
    def calculate_fare(self, distance):
        return distance * 15


class Bike(Vehicle):
    def calculate_fare(self, distance):
        return distance * 8


class Auto(Vehicle):
    def calculate_fare(self, distance):
        return distance * 10


class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle


class Ride:
    def __init__(self, driver, distance):
        self.driver = driver
        self.distance = distance
        self.__fare = self.driver.vehicle.calculate_fare(distance)

    @property
    def fare(self):
        return self.__fare

    def __str__(self):
        return (f"Driver: {self.driver.name}, "
                f"Vehicle: {type(self.driver.vehicle).__name__}, "
                f"Distance: {self.distance} km, "
                f"Fare: ₹{self.__fare}")


drivers = [
    Driver("Rahul", Car()),
    Driver("Anil", Bike()),
    Driver("Kiran", Auto())
]

rides = [
    Ride(drivers[0], 10),
    Ride(drivers[1], 10),
    Ride(drivers[2], 10)
]

print("Ride Details\n")

for ride in rides:
    print(ride)

print("\nProtected Fare Access")
print(rides[0].fare)

try:
    print(rides[0].__fare)
except AttributeError:
    print("Cannot access private fare directly.")











from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @abstractmethod
    def validate(self, amount):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    def __add__(self, other):
        return self.balance + other.balance


class CardPayment(PaymentMethod):

    def validate(self, amount):
        return amount <= self.balance

    def pay(self, amount):
        if self.validate(amount):
            print(f"Card Payment of ₹{amount} Successful")
        else:
            print("Insufficient Card Balance")


class WalletPayment(PaymentMethod):

    def validate(self, amount):
        return amount <= self.balance

    def pay(self, amount):
        if self.validate(amount):
            print(f"Wallet Payment of ₹{amount} Successful")
        else:
            print("Insufficient Wallet Balance")


class UPIPayment(PaymentMethod):

    def validate(self, amount):
        return amount <= self.balance

    def pay(self, amount):
        if self.validate(amount):
            print(f"UPI Payment of ₹{amount} Successful")
        else:
            print("Insufficient UPI Balance")


payments = [
    CardPayment("Visa", 10000),
    WalletPayment("Paytm", 3000),
    UPIPayment("PhonePe", 5000)
]

print("Checkout Process")

for p in payments:
    p.pay(2000)

print("\nAvailable Funds")
for p in payments:
    print(p.name, ":", p.balance)

print("\nSplit Payment =", payments[0] + payments[1])












from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def perform_duty(self):
        pass


class MedicalStaff(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    @property
    def salary(self):
        return "Confidential"

    def perform_duty(self):
        print("Providing Medical Support")


class Doctor(MedicalStaff):

    def __init__(self, name, age, salary, notes):
        super().__init__(name, age, salary)
        self.__patient_notes = notes

    @property
    def patient_notes(self):
        return "Restricted"

    def perform_duty(self):
        print("Diagnosing Patients")


class Surgeon(Doctor):

    def __init__(self, name, age, salary, notes, specialty):
        super().__init__(name, age, salary, notes)
        self.specialty = specialty

    def perform_duty(self):
        print("Performing", self.specialty, "Surgery")


staff = [
    MedicalStaff("Anil", 35, 50000),
    Doctor("Rahul", 42, 120000, "Patient Stable"),
    Surgeon("Priya", 45, 200000, "Critical", "Heart")
]

print("Hospital Staff")

for emp in staff:
    print(type(emp).__name__, "-", emp.name)
    emp.perform_duty()

print("\nHidden Data")

print(staff[1].salary)
print(staff[1].patient_notes)












class User:

    def __init__(self, name):
        self.name = name


class Instructor(User):

    def __init__(self, name):
        super().__init__(name)

    def grade_work(self):
        print(self.name, "is grading assignments")


class Student(User):

    def __init__(self, name):
        super().__init__(name)
        self.__courses = []

    def assign_course(self, course):
        self.__courses.append(course)

    def submit_work(self):
        print(self.name, "submitted assignment")

    @property
    def courses(self):
        return self.__courses


class TeachingAssistant(Student, Instructor):

    def __init__(self, name):
        super().__init__(name)

    def submit_work(self):
        print(self.name, "submitted assignment as Student")

    def grade_work(self):
        print(self.name, "graded assignments as Instructor")


ta = TeachingAssistant("Kiran")

ta.assign_course("Python")

print("Assigned Courses:", ta.courses)

ta.submit_work()

ta.grade_work()

print("\nMethod Resolution Order (MRO)")
for cls in TeachingAssistant.__mro__:
    print(cls.__name__)
















class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    def __str__(self):
        return f"{self.name} (₹{self.price}, Qty:{self.quantity})"


class Warehouse:

    total_warehouses = 0

    def __init__(self):
        self.products = {}
        Warehouse.total_warehouses += 1

    def add_product(self, product):
        self.products[product.name] = product

    def __add__(self, other):
        new = Warehouse()
        new.products = {**self.products, **other.products}
        return new

    def __len__(self):
        return len(self.products)

    def __contains__(self, item):
        return item in self.products

    @classmethod
    def warehouse_count(cls):
        return cls.total_warehouses


w1 = Warehouse()
w1.add_product(Product("Laptop", 50000, 10))
w1.add_product(Product("Mouse", 500, 50))

w2 = Warehouse()
w2.add_product(Product("Keyboard", 1200, 20))

merged = w1 + w2

print("Products:", len(merged))
print("Laptop" in merged)
print("Warehouses:", Warehouse.warehouse_count())













from abc import ABC, abstractmethod

class MediaFile(ABC):

    def __init__(self, path):
        self.__path = path

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class MP3File(MediaFile):

    def play(self):
        print("Playing MP3")

    def stop(self):
        print("Stopping MP3")


class MP4File(MediaFile):

    def play(self):
        print("Playing MP4")

    def stop(self):
        print("Stopping MP4")


class WAVFile(MediaFile):

    def play(self):
        print("Playing WAV")

    def stop(self):
        print("Stopping WAV")


class OnlineStream:

    def play(self):
        print("Streaming Online")


def start_player(media):
    media.play()


files = [
    MP3File("song.mp3"),
    MP4File("movie.mp4"),
    WAVFile("voice.wav")
]

for file in files:
    start_player(file)

stream = OnlineStream()
start_player(stream)














from abc import ABC, abstractmethod

class StatementFormatter(ABC):

    @abstractmethod
    def format(self, data):
        pass

    def __call__(self, data):
        return self.format(data)

    def __repr__(self):
        return self.__class__.__name__


class PDFFormatter(StatementFormatter):

    def format(self, data):
        return f"PDF => {data}"


class JSONFormatter(StatementFormatter):

    def format(self, data):
        return f"JSON => {data}"


class TextFormatter(StatementFormatter):

    def format(self, data):
        return f"TEXT => {data}"


formatters = [
    PDFFormatter(),
    JSONFormatter(),
    TextFormatter()
]

report = "Monthly Sales Report"

for formatter in formatters:
    print(formatter(report))
    print(repr(formatter))















class LightDevice:

    def activate(self):
        print("Light Activated")


class SecurityDevice:

    def activate(self):
        print("Security Monitoring Started")


class SmartCamera(LightDevice, SecurityDevice):

    def __init__(self):
        self.__logs = []

    def activate(self):
        super().activate()
        self.__logs.append("Camera Activated")
        print("Camera Recording Started")

    @property
    def logs(self):
        return self.__logs


camera = SmartCamera()

camera.activate()

print(camera.logs)

print()

print("MRO")

for cls in SmartCamera.__mro__:
    print(cls.__name__)














from abc import ABC, abstractmethod

class MenuItem(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_price(self):
        pass


class Pizza(MenuItem):

    def get_price(self):
        return 300


class Burger(MenuItem):

    def get_price(self):
        return 150


class Drink(MenuItem):

    def get_price(self):
        return 80


class Order:

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    @property
    def items(self):
        return self.__items

    def total(self):
        return sum(item.get_price() for item in self.__items)


order = Order()

order.add_item(Pizza("Veg Pizza"))
order.add_item(Burger("Cheese Burger"))
order.add_item(Drink("Coke"))

print("Items")

for item in order.items:
    print(item.name, "-", item.get_price())

print()

print("Total Bill =", order.total())











class Applicant:

    def __init__(self, name):
        self.name = name
        self.__skills = []

    @property
    def skills(self):
        return self.__skills.copy()

    def __add__(self, skill):
        if skill not in self.__skills:
            self.__skills.append(skill)
        return self

    def __sub__(self, skill):
        if skill in self.__skills:
            self.__skills.remove(skill)
        return self

    def __eq__(self, other):
        return set(self.__skills) == set(other.__skills)

    def __str__(self):
        return f"{self.name} : {self.__skills}"


class ExperiencedApplicant(Applicant):

    def __init__(self, name, years):
        super().__init__(name)
        self.years = years

    def __str__(self):
        return f"{self.name} ({self.years} Years Experience) : {self.skills}"


a1 = ExperiencedApplicant("Rahul", 5)
a2 = ExperiencedApplicant("Kiran", 4)

a1 + "Python" + "SQL" + "Django"
a2 + "SQL" + "Python" + "Django"

print(a1)
print(a2)

print("Same Skills:", a1 == a2)

a1 - "SQL"
print(a1)












class Character:

    stamina_cost = 10

    def __init__(self, name, health):
        self.name = name
        self.health = health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, value)

    def attack(self):
        pass


class Warrior(Character):

    stamina_cost = 15

    def attack(self):
        return 30


class Archer(Character):

    stamina_cost = 12

    def attack(self):
        return 20


class Mage(Character):

    stamina_cost = 18

    def attack(self):
        return 40


players = [
    Warrior("Warrior", 100),
    Archer("Archer", 100),
    Mage("Mage", 100)
]

enemy_hp = 100

for player in players:
    damage = player.attack()
    enemy_hp -= damage
    enemy_hp = max(0, enemy_hp)

    print(player.name, "attacks for", damage)
    print("Enemy HP =", enemy_hp)











from abc import ABC, abstractmethod

class Transport(ABC):

    tax = 5

    def __init__(self):
        self.__fare = 0

    @staticmethod
    def validate_distance(distance):
        return distance > 0

    @classmethod
    def update_tax(cls, tax):
        cls.tax = tax

    @property
    def fare(self):
        return self.__fare

    @fare.setter
    def fare(self, value):
        self.__fare = value

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Taxi(Transport):

    def calculate_fare(self, distance):
        self.fare = distance * 20 + self.tax
        return self.fare


class Bus(Transport):

    def calculate_fare(self, distance):
        self.fare = distance * 5 + self.tax
        return self.fare


class Train(Transport):

    def calculate_fare(self, distance):
        self.fare = distance * 3 + self.tax
        return self.fare


Transport.update_tax(10)

vehicles = [
    Taxi(),
    Bus(),
    Train()
]

distance = 15

for vehicle in vehicles:
    if Transport.validate_distance(distance):
        print(type(vehicle).__name__,
              "Fare =", vehicle.calculate_fare(distance))











from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass


class LinearRegressionModel(Model):

    def train(self, data):
        print("Training Linear Regression Model...")

    def predict(self, data):
        return [x * 2 for x in data]


class DecisionTreeModel(Model):

    def train(self, data):
        print("Training Decision Tree Model...")

    def predict(self, data):
        return ["Yes" if x > 5 else "No" for x in data]


class Pipeline:

    def __init__(self, model):
        self.model = model
        self.__steps = []

    def add_step(self, step):
        self.__steps.append(step)

    def train(self, data):
        for step in self.__steps:
            print("Applying:", step)
        self.model.train(data)

    def __call__(self, data):
        return self.model.predict(data)


pipeline1 = Pipeline(LinearRegressionModel())
pipeline1.add_step("Remove Missing Values")
pipeline1.add_step("Normalize Data")

pipeline1.train([1, 2, 3, 4])

print("Prediction:", pipeline1([10, 20, 30]))

print()

pipeline2 = Pipeline(DecisionTreeModel())
pipeline2.add_step("Feature Selection")

pipeline2.train([2, 6, 8])

print("Prediction:", pipeline2([2, 6, 8]))












from abc import ABC, abstractmethod


class RewardsMixin:

    def reward_points(self):
        print("Reward Points Added")


class User(ABC):

    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        User.total_users += 1

    @property
    def password(self):
        return "********"

    @classmethod
    def user_count(cls):
        return cls.total_users

    @abstractmethod
    def get_role(self):
        pass


class Product:

    def __init__(self, pid, name, price):
        if self.validate_product_id(pid):
            self.pid = pid

        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            self.__price = 1

    @staticmethod
    def validate_product_id(pid):
        return isinstance(pid, int)

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


class Seller(User):

    def get_role(self):
        return "Seller"


class Cart:

    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def __add__(self, product):
        self.__items.append(product)
        return self

    def __sub__(self, product):
        if product in self.__items:
            self.__items.remove(product)
        return self

    def total(self):
        return sum(product.price for product in self.__items)

    def __str__(self):
        if not self.__items:
            return "Cart is Empty"

        result = ""

        for product in self.__items:
            result += str(product) + "\n"

        result += f"Total = ₹{self.total()}"

        return result


class Buyer(RewardsMixin, User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self.cart = Cart()

    def get_role(self):
        return "Buyer"

    def checkout(self):
        print("Checkout Successful")
        print(self.cart)
        self.reward_points()


class Order:

    def __init__(self, buyer):
        self.buyer = buyer

    def place_order(self):
        print("Order Placed Successfully")
        print("Customer:", self.buyer.username)
        print("Amount:", self.buyer.cart.total())


# Products
p1 = Product(101, "Laptop", 55000)
p2 = Product(102, "Mouse", 700)
p3 = Product(103, "Keyboard", 1200)

# Users
seller = Seller("TechStore", "seller123")
buyer = Buyer("Rahul", "buyer123")

print("Seller Role:", seller.get_role())
print("Buyer Role:", buyer.get_role())

# Cart Operations
buyer.cart + p1
buyer.cart + p2
buyer.cart + p3

print()
print("Cart Details")
print(buyer.cart)

buyer.cart - p2

print()
print("After Removing Mouse")
print(buyer.cart)

print()

buyer.checkout()

print()

order = Order(buyer)
order.place_order()

print()

print("Total Users:", User.user_count())

print()

print("Buyer MRO")

for cls in Buyer.__mro__:
    print(cls.__name__)












