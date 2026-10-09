# Q1. Student Class

# class Student:
#     total_students = 0
#     passing_marks = 40
#     students = []
#
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         Student.total_students += 1
#         Student.students.append(self)
#
#     def result(self):
#         if self.marks >= Student.passing_marks:
#             return "Passed"
#         else:
#             return "Failed"
#
#     @classmethod
#     def curve_marks(cls, percentage):
#         for student in cls.students:
#             student.marks = student.marks + (student.marks * percentage / 100)
#             if student.marks > 100:
#                 student.marks = 100
#
#     @staticmethod
#     def grade(marks):
#         if marks >= 90:
#             return "A"
#         elif marks >= 75:
#             return "B"
#         elif marks >= 60:
#             return "C"
#         elif marks >= 40:
#             return "D"
#         else:
#             return "F"
#
#
# s1 = Student("Tharun", 72)
# s2 = Student("Rahul", 35)
# s3 = Student("Sai", 88)
#
# print("Total Students:", Student.total_students)
#
# print("\nBefore Curve")
# for s in Student.students:
#     print(s.name, s.marks, Student.grade(s.marks), s.result())
#
# Student.curve_marks(10)
#
# print("\nAfter Curve")
# for s in Student.students:
#     print(s.name, s.marks, Student.grade(s.marks), s.result())




# Q2. Product Class
#
# class Product:
#     tax_rate = 18
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def final_price(self):
#         return self.price + (self.price * Product.tax_rate / 100)
#
#     @classmethod
#     def change_tax_rate(cls, new_rate):
#         cls.tax_rate = new_rate
#
#     @staticmethod
#     def valid_price(price):
#         return price >= 0 and price <= 100000
#
#
# p1 = Product("Laptop", 50000)
# p2 = Product("Mobile", 20000)
#
# print("Before Tax Change")
# print(p1.name, p1.final_price())
# print(p2.name, p2.final_price())
#
# Product.change_tax_rate(12)
#
# print("\nAfter Tax Change")
# print(p1.name, p1.final_price())
# print(p2.name, p2.final_price())
#
# print("\nPrice Validation")
# print(Product.valid_price(500))
# print(Product.valid_price(-50))
# print(Product.valid_price(200000))



#
# Q3. Employee Class
#
# class Employee:
#     min_experience = 5
#     valid_departments = ["HR", "Tech", "Admin"]
#
#     def __init__(self, name, experience, department):
#         self.name = name
#         self.experience = experience
#         self.department = department
#
#     def promotion(self):
#         if self.experience >= Employee.min_experience:
#             return "Eligible"
#         else:
#             return "Not Eligible"
#
#     @classmethod
#     def update_promotion_criteria(cls, years):
#         cls.min_experience = years
#
#     @staticmethod
#     def check_department(dept):
#         if dept in Employee.valid_departments:
#             return True
#         else:
#             return False
#
#
# e1 = Employee("Tharun", 6, "Tech")
# e2 = Employee("Rahul", 3, "HR")
# e3 = Employee("Sai", 8, "Sales")
#
# print("Before Updating Criteria")
# print(e1.name, e1.promotion())
# print(e2.name, e2.promotion())
# print(e3.name, e3.promotion())
#
# Employee.update_promotion_criteria(7)
#
# print("\nAfter Updating Criteria")
# print(e1.name, e1.promotion())
# print(e2.name, e2.promotion())
# print(e3.name, e3.promotion())
#
# print("\nDepartment Validation")
# print("Tech:", Employee.check_department("Tech"))
# print("HR:", Employee.check_department("HR"))
# print("Sales:", Employee.check_department("Sales"))


# Q4. Loan Class
# class Loan:
#     interest_rate = 10
#
#     def __init__(self, borrower, principal):
#         self.borrower = borrower
#         self.principal = principal
#
#     def total_payable(self):
#         return self.principal + (self.principal * Loan.interest_rate / 100)
#
#     @classmethod
#     def update_interest_rate(cls, rate):
#         cls.interest_rate = rate
#
#     @staticmethod
#     def check_eligibility(salary):
#         return salary > 30000
#
#
# l1 = Loan("Tharun", 100000)
# l2 = Loan("Rahul", 50000)
#
# print("Before Interest Update")
# print(l1.borrower, l1.total_payable())
# print(l2.borrower, l2.total_payable())
#
# Loan.update_interest_rate(12)
#
# print("\nAfter Interest Update")
# print(l1.borrower, l1.total_payable())
# print(l2.borrower, l2.total_payable())
#
# print("\nLoan Eligibility")
# print(Loan.check_eligibility(40000))
# print(Loan.check_eligibility(25000))
#
#
#
# Q5. Course Class
# class Course:
#     total_courses = 0
#     min_duration = 30
#
#     def __init__(self, title, duration):
#         self.title = title
#         self.duration = duration
#         self.enrolled_students = 0
#         Course.total_courses += 1
#
#     def enroll(self):
#         self.enrolled_students += 1
#
#     @classmethod
#     def update_min_duration(cls, days):
#         cls.min_duration = days
#
#     @staticmethod
#     def check_duration(duration):
#         return duration >= 0 and duration <= 365
#
#
# c1 = Course("Python", 45)
# c2 = Course("Java", 60)
#
# c1.enroll()
# c1.enroll()
# c2.enroll()
#
# print("Total Courses:", Course.total_courses)
#
# print(c1.title, c1.enrolled_students)
# print(c2.title, c2.enrolled_students)
#
# Course.update_min_duration(40)
#
# print("Minimum Duration:", Course.min_duration)
#
# print(Course.check_duration(50))
# print(Course.check_duration(-10))
# print(Course.check_duration(500))
#
#
#
#
# Q6. Vehicle Class

# class Vehicle:
#     service_rate = 2
#
#     def __init__(self, model, kilometers_run, year):
#         self.model = model
#         self.kilometers_run = kilometers_run
#         self.year = year
#         self.service_history = []
#
#     def service_charge(self):
#         return self.kilometers_run * Vehicle.service_rate
#
#     @classmethod
#     def update_service_rate(cls, rate):
#         cls.service_rate = rate
#
#     @staticmethod
#     def eligible_for_service(current_year, model_year):
#         return (current_year - model_year) <= 15
#
#
# v1 = Vehicle("Swift", 20000, 2018)
# v2 = Vehicle("Alto", 50000, 2008)
#
# print("Before Rate Update")
# print(v1.model, v1.service_charge())
# print(v2.model, v2.service_charge())
#
# Vehicle.update_service_rate(3)
#
# print("\nAfter Rate Update")
# print(v1.model, v1.service_charge())
# print(v2.model, v2.service_charge())
#
# print("\nEligibility")
# print(Vehicle.eligible_for_service(2026, v1.year))
# print(Vehicle.eligible_for_service(2026, v2.year))
#
#
#
# Q7. Inventory Class

# class Inventory:
#     total_items = 0
#     min_stock = 5
#
#     def __init__(self):
#         self.stock = {}
#
#     def add_stock(self, item, quantity):
#         if item in self.stock:
#             self.stock[item] += quantity
#         else:
#             self.stock[item] = quantity
#         Inventory.total_items += quantity
#
#     def remove_stock(self, item, quantity):
#         if item in self.stock and self.stock[item] >= quantity:
#             self.stock[item] -= quantity
#             Inventory.total_items -= quantity
#
#             if Inventory.below_threshold(self.stock[item], Inventory.min_stock):
#                 print(item, "is below minimum stock.")
#         else:
#             print("Not enough stock.")
#
#     @classmethod
#     def update_threshold(cls, value):
#         cls.min_stock = value
#
#     @staticmethod
#     def below_threshold(stock, threshold):
#         return stock < threshold
#
#
# i1 = Inventory()
# i2 = Inventory()
#
# i1.add_stock("Pen", 20)
# i1.add_stock("Book", 10)
#
# i2.add_stock("Pencil", 8)
#
# print("Total Items:", Inventory.total_items)
#
# i1.remove_stock("Pen", 17)
#
# Inventory.update_threshold(10)
#
# i2.remove_stock("Pencil", 2)
#
# print(i1.stock)
# print(i2.stock)
# print("Total Items:", Inventory.total_items)
#
#
#
# Q8. HotelRoom Class
# class HotelRoom:
#     base_price = 2000
#
#     def __init__(self, room_number, nights_booked, guest_name):
#         self.room_number = room_number
#         self.nights_booked = nights_booked
#         self.guest_name = guest_name
#
#     def total_bill(self):
#         return self.nights_booked * HotelRoom.base_price
#
#     @classmethod
#     def update_base_price(cls, price):
#         cls.base_price = price
#
#     @staticmethod
#     def valid_nights(nights):
#         return isinstance(nights, int) and nights > 0
#
#
# r1 = HotelRoom(101, 3, "Tharun")
# r2 = HotelRoom(102, 5, "Rahul")
#
# print("Before Price Update")
# print(r1.guest_name, r1.total_bill())
# print(r2.guest_name, r2.total_bill())
#
# HotelRoom.update_base_price(2500)
#
# print("\nAfter Price Update")
# print(r1.guest_name, r1.total_bill())
# print(r2.guest_name, r2.total_bill())
#
# print("\nNight Validation")
# print(HotelRoom.valid_nights(4))
# print(HotelRoom.valid_nights(-2))
#
#
#
#
# Q9. LibraryMember Class
# class LibraryMember:
#     total_members = 0
#     borrow_limit = 3
#
#     def __init__(self, name):
#         self.name = name
#         self.books_borrowed = 0
#         LibraryMember.total_members += 1 
#
#     def borrow_book(self, title):
#         if not LibraryMember.valid_title(title):
#             print("Invalid Book Title")
#         elif self.books_borrowed < LibraryMember.borrow_limit:
#             self.books_borrowed += 1
#             print(self.name, "borrowed", title)
#         else:
#             print(self.name, "Borrow Limit Reached")
#
#     @classmethod
#     def update_limit(cls, limit):
#         cls.borrow_limit = limit
#
#     @staticmethod
#     def valid_title(title):
#         return isinstance(title, str) and len(title.strip()) >= 2 and len(title) <= 50
#
#
# m1 = LibraryMember("Tharun")
# m2 = LibraryMember("Rahul")
#
# m1.borrow_book("Python")
# m1.borrow_book("Java")
# m1.borrow_book("SQL")
# m1.borrow_book("HTML")
#
# LibraryMember.update_limit(5)
#
# m1.borrow_book("CSS")
# m2.borrow_book("AI")
#
# print("\nTotal Members:", LibraryMember.total_members)
#
# print(LibraryMember.valid_title("C"))
# print(LibraryMember.valid_title(""))
# print(LibraryMember.valid_title("Machine Learning"))
#
#
#
#
# Q10. Member Class
# class Member:
#     bmi_limit = 25
#
#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     def calculate_bmi(self):
#         return self.weight / (self.height ** 2)
#
#     def fit_status(self):
#         bmi = self.calculate_bmi()
#         if bmi <= Member.bmi_limit:
#             return "Fit"
#         else:
#             return "Not Fit"
#
#     @classmethod
#     def update_bmi_limit(cls, limit):
#         cls.bmi_limit = limit
#
#     @staticmethod
#     def valid_input(height, weight):
#         return height > 0 and weight > 0
#
#
# m1 = Member("Tharun", 1.75, 68)
# m2 = Member("Rahul", 1.70, 85)
#
# print("Before BMI Limit Update")
# print(m1.name, round(m1.calculate_bmi(), 2), m1.fit_status())
# print(m2.name, round(m2.calculate_bmi(), 2), m2.fit_status())
#
# Member.update_bmi_limit(23)
#
# print("\nAfter BMI Limit Update")
# print(m1.name, round(m1.calculate_bmi(), 2), m1.fit_status())
# print(m2.name, round(m2.calculate_bmi(), 2), m2.fit_status())
#
# print("\nInput Validation")
# print(Member.valid_input(1.75, 68))
# print(Member.valid_input(-1.75, 68))
# print(Member.valid_input(1.80, -50))