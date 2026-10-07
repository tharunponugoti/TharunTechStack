Q1. Abstract Class Shape
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(3, 4, 5)

print(c.area(), c.perimeter())
print(r.area(), r.perimeter())
print(t.area(), t.perimeter())

Note:

The abstract class contains only method declarations (pass).
If a subclass does not implement all abstract methods, Python raises a TypeError when you try to create its object.







Q2. Payment Gateway
from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class UPIPayment(PaymentGateway):

    def authenticate(self):
        print("UPI Authentication")

    def pay(self, amount):
        print("UPI Payment:", amount)

    def refund(self, amount):
        print("UPI Refund:", amount)


class CardPayment(PaymentGateway):

    def authenticate(self):
        print("Card Authentication")

    def pay(self, amount):
        print("Card Payment:", amount)

    def refund(self, amount):
        print("Card Refund:", amount)


class NetBankingPayment(PaymentGateway):

    def authenticate(self):
        print("NetBanking Authentication")

    def pay(self, amount):
        print("NetBanking Payment:", amount)

    def refund(self, amount):
        print("NetBanking Refund:", amount)


payments = [
    UPIPayment(),
    CardPayment(),
    NetBankingPayment()
]

for p in payments:
    p.authenticate()
    p.pay(5000)
    p.refund(1000)
    print()






Q3. Vehicle Control
from abc import ABC, abstractmethod

class VehicleControl(ABC):

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def steer(self):
        pass


class CarControl(VehicleControl):

    def accelerate(self):
        print("Car Accelerating")

    def brake(self):
        print("Car Braking")

    def steer(self):
        print("Car Steering")


class BikeControl(VehicleControl):

    def accelerate(self):
        print("Bike Accelerating")

    def brake(self):
        print("Bike Braking")

    def steer(self):
        print("Bike Steering")


class TruckControl(VehicleControl):

    def accelerate(self):
        print("Truck Accelerating")

    def brake(self):
        print("Truck Braking")

    def steer(self):
        print("Truck Steering")


vehicles = [
    CarControl(),
    BikeControl(),
    TruckControl()
]

for v in vehicles:
    v.accelerate()
    v.brake()
    v.steer()
    print()




Q4. Database Driver
from abc import ABC, abstractmethod

class DatabaseDriver(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def close(self):
        pass


class MySQLDriver(DatabaseDriver):

    def connect(self):
        print("MySQL Connected")

    def execute(self, query):
        print("Executing:", query)

    def close(self):
        print("MySQL Closed")


class PostgresDriver(DatabaseDriver):

    def connect(self):
        print("Postgres Connected")

    def execute(self, query):
        print("Executing:", query)

    def close(self):
        print("Postgres Closed")


class SQLiteDriver(DatabaseDriver):

    def connect(self):
        print("SQLite Connected")

    def execute(self, query):
        print("Executing:", query)

    def close(self):
        print("SQLite Closed")


db = MySQLDriver()

db.connect()
db.execute("SELECT * FROM Student")
db.close()







Q5. Report Generator
from abc import ABC, abstractmethod

class ReportGenerator(ABC):

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def export(self):
        pass


class PDFReport(ReportGenerator):

    def load_data(self):
        print("Loading PDF Data")

    def process(self):
        print("Processing PDF Data")

    def export(self):
        print("Exporting PDF")


class ExcelReport(ReportGenerator):

    def load_data(self):
        print("Loading Excel Data")

    def process(self):
        print("Processing Excel Data")

    def export(self):
        print("Exporting Excel")


reports = [
    PDFReport(),
    ExcelReport()
]

for r in reports:
    r.load_data()
    r.process()
    r.export()
    print()





    Q6.Robot
    Command
    from abc import ABC, abstractmethod


    class RobotCommand(ABC):

        @abstractmethod
        def execute(self):
            pass

        @abstractmethod
        def undo(self):
            pass


    class PickCommand(RobotCommand):

        def execute(self):
            print("Picking Object")

        def undo(self):
            print("Undo Pick")


    class PlaceCommand(RobotCommand):

        def execute(self):
            print("Placing Object")

        def undo(self):
            print("Undo Place")


    class MoveCommand(RobotCommand):

        def execute(self):
            print("Moving Robot")

        def undo(self):
            print("Undo Move")


    commands = [PickCommand(), PlaceCommand(), MoveCommand()]

    for c in commands:
        c.execute()
        c.undo()
        print()







    Q7.Machine
    Learning
    Model
    from abc import ABC, abstractmethod


    class MLModel(ABC):

        @abstractmethod
        def train(self, data):
            pass

        @abstractmethod
        def predict(self, x):
            pass

        @abstractmethod
        def evaluate(self, test_set):
            pass


    class LinearRegressionModel(MLModel):

        def train(self, data):
            print("Training Linear Regression")

        def predict(self, x):
            print("Predicting using Linear Regression")

        def evaluate(self, test_set):
            print("Evaluating Linear Regression")


    class DecisionTreeModel(MLModel):

        def train(self, data):
            print("Training Decision Tree")

        def predict(self, x):
            print("Predicting using Decision Tree")

        def evaluate(self, test_set):
            print("Evaluating Decision Tree")


    models = [LinearRegressionModel(), DecisionTreeModel()]

    for model in models:
        model.train("Training Data")
        model.predict(10)
        model.evaluate("Test Data")
        print()






    Q8.Notifier(Without and With
    Abstraction)
    Without
    Abstraction


    def email_sender():
        print("Email Sent")


    def sms_sender():
        print("SMS Sent")


    def push_sender():
        print("Push Notification Sent")


    choice = "email"

    if choice == "email":
        email_sender()
    elif choice == "sms":
        sms_sender()
    else:
        push_sender()
    With
    Abstraction
    from abc import ABC, abstractmethod


    class Notifier(ABC):

        @abstractmethod
        def send(self):
            pass


    class EmailNotifier(Notifier):

        def send(self):
            print("Email Sent")


    class SMSNotifier(Notifier):

        def send(self):
            print("SMS Sent")


    class PushNotifier(Notifier):

        def send(self):
            print("Push Notification Sent")


    notifications = [
        EmailNotifier(),
        SMSNotifier(),
        PushNotifier()
    ]

    for n in notifications:
        n.send()

    Explanation:

    Without
    abstraction → Uses if - else repeatedly.
    With
    abstraction → Just
    call
    send()
    on
    every
    object(polymorphism).



    Q9.Media
    Player
    from abc import ABC, abstractmethod


    class MediaPlayer(ABC):

        @abstractmethod
        def load(self):
            pass

        @abstractmethod
        def play(self):
            pass

        @abstractmethod
        def stop(self):
            pass


    class MP3Player(MediaPlayer):

        def load(self):
            print("MP3 Loaded")

        def play(self):
            print("MP3 Playing")

        def stop(self):
            print("MP3 Stopped")


    class WAVPlayer(MediaPlayer):

        def load(self):
            print("WAV Loaded")

        def play(self):
            print("WAV Playing")

        def stop(self):
            print("WAV Stopped")


    class AACPlayer(MediaPlayer):

        def load(self):
            print("AAC Loaded")

        def play(self):
            print("AAC Playing")

        def stop(self):
            print("AAC Stopped")


    players = [
        MP3Player(),
        WAVPlayer(),
        AACPlayer()
    ]

    for p in players:
        p.load()
        p.play()
        p.stop()
        print()




    Q10.Sensor(Encapsulation + Abstraction)
    from abc import ABC, abstractmethod


    class Sensor(ABC):

        def __init__(self, raw_value, calibration):
            self.__raw_value = raw_value
            self.__calibration = calibration

        @abstractmethod
        def read_value(self):
            pass

        @abstractmethod
        def calibrate(self):
            pass

        def get_reading(self):
            return self.__raw_value * self.__calibration


    class TemperatureSensor(Sensor):

        def read_value(self):
            print("Reading Temperature")

        def calibrate(self):
            print("Temperature Sensor Calibrated")


    class PressureSensor(Sensor):

        def read_value(self):
            print("Reading Pressure")

        def calibrate(self):
            print("Pressure Sensor Calibrated")


    class HumiditySensor(Sensor):

        def read_value(self):
            print("Reading Humidity")

        def calibrate(self):
            print("Humidity Sensor Calibrated")


    sensors = [
        TemperatureSensor(30, 1.1),
        PressureSensor(50, 1.2),
        HumiditySensor(70, 0.9)
    ]

    for s in sensors:
        s.read_value()
        s.calibrate()
        print("Reading:", s.get_reading())
        print()