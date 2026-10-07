class Person:
    def __init__(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.age = age


try:
    p = Person(-5)
except ValueError as e:
    print(e)






def find_length(obj):
    try:
        count = 0
        for i in obj:
            count += 1
        return count
    except TypeError:
        print("Error: Integer is not iterable, so its length cannot be calculated.")


print(find_length("Python"))
print(find_length([1, 2, 3, 4]))
print(find_length(100))





class Student:
    def __init__(self):
        self.marks = 0

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100.")
        self.marks = marks


try:
    s = Student()
    s.set_marks(120)
except ValueError as e:
    print(e)




class InvalidAgeError(Exception):
    pass


class Voter:
    def check_eligibility(self, age):
        if age < 18:
            raise InvalidAgeError("Age must be 18 or above to vote.")
        print("Eligible to vote.")


try:
    v = Voter()
    v.check_eligibility(16)
except InvalidAgeError as e:
    print(e)






class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient Balance.")
        self.balance -= amount
        print("Remaining Balance:", self.balance)


try:
    b = BankAccount(5000)
    b.withdraw(7000)
except Exception as e:
    print(e)







class PasswordValidator:
    def validate(self, password):
        if len(password) < 8:
            raise Exception("Password must contain at least 8 characters.")
        print("Password is valid.")


try:
    p = PasswordValidator()
    p.validate("abc123")
except Exception as e:
    print(e)






class UserInput:
    def get_integer(self, value):
        try:
            result = int(value)
            print("Integer:", result)
        except ValueError:
            print("ValueError: Invalid value.")
        except TypeError:
            print("TypeError: None or invalid type provided.")


u = UserInput()
u.get_integer("123")
u.get_integer("abc")
u.get_integer(None)







class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area().")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle(10, 5)
print("Area:", r.area())






class Service:
    def task(self):
        raise Exception("Something went wrong.")

    def execute(self):
        try:
            self.task()
        except Exception as e:
            print("Handled Exception:", e)


s = Service()
s.execute()









class Transaction:
    def process(self):
        try:
            amount = int(input("Enter amount: "))
            print("Transaction Successful:", amount)
        except ValueError:
            print("Invalid amount.")
        finally:
            print("Cleanup completed.")


t = Transaction()
t.process()









class LoginSystem:
    def login(self, password):
        if password != "admin123":
            raise Exception("Incorrect Password.")
        print("Login Successful.")


l = LoginSystem()

try:
    l.login("hello123")
except Exception as e:
    print(e)

    