1. Person (Raise ValueError for Invalid Age)
class Person:

    def __init__(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age


try:
    p = Person(25)
    print("Age:", p.age)

    p1 = Person(-5)

except ValueError as e:
    print(e)




    
2. find_length() Without Using len()
def find_length(obj):

    try:
        count = 0

        for i in obj:
            count += 1

        return count

    except TypeError:
        print("TypeError: Integer is not iterable.")


print(find_length("Python"))

print(find_length([1,2,3,4]))

print(find_length(100))




3. Student Marks Validation
class Student:

    def __init__(self):
        self.marks = 0

    def set_marks(self, marks):

        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100")

        self.marks = marks


s = Student()

try:
    s.set_marks(95)
    print("Marks:", s.marks)

    s.set_marks(120)

except ValueError as e:
    print(e)




4. Custom Exception (InvalidAgeError)
class InvalidAgeError(Exception):
    pass


class Voter:

    def check_eligibility(self, age):

        if age < 18:
            raise InvalidAgeError("Not Eligible to Vote")

        print("Eligible to Vote")


v = Voter()

try:
    v.check_eligibility(20)
    v.check_eligibility(15)

except InvalidAgeError as e:
    print(e)




5. BankAccount Withdrawal
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise Exception("Insufficient Balance")

        self.balance -= amount
        print("Remaining Balance:", self.balance)


b = BankAccount(10000)

try:
    b.withdraw(3000)
    b.withdraw(9000)

except Exception as e:
    print(e)




6. Password Validator
class PasswordValidator:

    def validate(self, password):

        if len(password) < 8:
            raise Exception("Password must contain at least 8 characters")

        print("Valid Password")


p = PasswordValidator()

try:
    p.validate("python123")
    p.validate("abc")

except Exception as e:
    print(e)





7. UserInput (ValueError & TypeError)
class UserInput:

    def get_integer(self, value):

        try:
            print(int(value))

        except ValueError:
            print("ValueError: Invalid Integer")

        except TypeError:
            print("TypeError: Invalid Type")


u = UserInput()

u.get_integer("100")

u.get_integer("abc")

u.get_integer(None)





8. Shape (NotImplementedError)
class Shape:

    def area(self):
        raise NotImplementedError("Area method must be implemented")


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


r = Rectangle(10,5)

print("Area:", r.area())




9. Service Class Exception Handling
class Service:

    def error_method(self):
        raise Exception("Something went wrong")

    def process(self):

        try:
            self.error_method()

        except Exception as e:
            print(e)


s = Service()

s.process(





10. Transaction (try-except-finally)
class Transaction:

    def process(self):

        try:
            amount = 1000
            print("Transaction Amount:", amount)

        except Exception as e:
            print(e)

        finally:
            print("Cleanup Completed")


t = Transaction()

t.process()




11. LoginSystem
class LoginSystem:

    def login(self, password):

        if password != "admin123":
            raise Exception("Incorrect Password")

        print("Login Successful")


l = LoginSystem()

try:
    l.login("admin123")

    l.login("python")

except Exception as e:
    print(e)