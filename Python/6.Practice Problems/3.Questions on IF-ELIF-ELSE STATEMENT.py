# -----IF-ELIF-ELSE STATEMENT

# 1,Write a Python program that converts a temperature in Celsius to Fahrenheit
# or vice versa based on user input.

# c=float(input("Enter a number: "))
# f=(c*9/5)+32
# print(f"{f}")

#
# 2,Write a simple calculator program that performs basic arithmetic operations
# (addition, subtraction, multiplication, division) based on user input.
#
# num1 = int(input("Enter first number: "))
# operator = input("Enter operation (+, -, *, /): ")
# num2 = int(input("Enter second number: "))
#
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Cannot divide by zero."
# else:
#     result = "Invalid operator."
#
# print("Result:", result)


#
# 3,Write a Python program for a simple "Guess the Number" game.
# Generate a random number, and let the user guess it.

#
# import random
# secret_number = random.randint(1, 10)
# guess = int(input("Guess a number between 1 and 10: "))
# if guess == secret_number:
#     print("Correct! You guessed the number.")
# else:
#     print("Wrong guess. The number was:", secret_number)


#
# 4,Write a Python program that checks
# the strength of a user's password based on certain criteria.

# password = input("Enter a password: ")
# if len(password) < 8:
#     print("Weak password: Use at least 8 characters.")
# elif password.isalpha():
#     print("Weak password: Add numbers or special characters.")
# elif password.isdigit():
#     print("Weak password: Add letters or special characters.")
# else:
#     print("Strong password.")

#
# 5,Write a Python program that calculates the final price of an item after applying
# a discount based on the purchase amount.


# price = float(input("Enter price: "))
# percent = float(input("Enter discount percentage: "))
# final_price = price * percent / 100
# print("Final price:", final_price)


#
# n=int(input())
# if n>0:
#     print("check balance and withdraw")
# else:
#     print("Insuffient money")

#
# Write a Python program that greets the user differently based on the time of day.

# n=int(input())
# if 7<n<10:
#     print("Good Morning")
# elif 11<n<14:
#     print("Good Afternoon")
# elif 15<n<22:
#     print("Good Evening")
# else:
#     print("Good Night")


#
# 8,Write a Python program that calculates the final price
# of an item after applying a discount coupon code.

# price = float(input("Enter item price: "))
# coupon = input("Enter coupon code: ")
# if coupon == "SAVE10":
#     price = price - (price * 0.10)
# elif coupon == "SAVE20":
#     price = price - (price * 0.20)
# else:
#     print("Invalid coupon code")
# print("Final price:", price)

#
# 9,Write a Python program that calculates and prints the grade based on a given score,
# but also validates the input score.
#
# score = int(input("Enter your score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# elif score >= 50:
#     print("Grade: E")
# else:
#     print("Grade: Fail")




# 10,Write a Python program that acts as a simple calculator and allows the user to choose the operation
# (addition, subtraction, multiplication, division).
#
# a=int(input())
# sign=input("Enter operator (+,-,*,/): ")
# b=int(input())
# if sign=="+":
#     print(a+b)
# elif sign=="-":
#     print(a-b)
# elif sign=="*":
#     print(a*b)
# elif sign=="/":
#     print(a/b)
# elif sign=="//":
#     print(a//b)
# else:
#     print("Invalid sign")


# 11.Write a Python program that determines the
# number of days in a given month.
#
# n = int(input())
# if n == 2:
#     print("28 or 29 days")
# elif n in [4, 6, 9, 11]:
#     print("30 days")
# elif n in [1, 3, 5, 7, 8, 10, 12]:
#     print("31 days")
# else:
#     print("Invalid month")


# 12,Write a Python program that calculates a person Body Mass Index (BMI) and categorizes it into
# different categories (underweight, normal weight, overweight, obese)

# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))
# bmi = weight / (height * height)
# print("BMI:", bmi)
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")


#
# 13,Write a Python program that converts letter grades
# (A, B, C, D, F) to their equivalent GPA values.

# grade = input("")
# if grade == "A":
#     print("GPA: 4.0")
# elif grade == "B":
#     print("GPA: 3.0")
# elif grade == "C":
#     print("GPA: 2.0")
# elif grade == "D":
#     print("GPA: 1.0")
# elif grade == "F":
#     print("GPA: 0.0")
# else:
#     print("Invalid grade")