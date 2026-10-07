# ------NESTED IF STATEMENT
#
# 1,Given x = 10 and y = 5, write a Python program to determine if x is greater than y.
# If x is greater than y, check if it's also greater than 15 and print appropriate messages accordingly.
#
# x=10
# y=5
# if x>y:
#     print("x is greater than y")
#     if x>15:
#         print("Its  greater than 15")
#     else:
#         print("Its  less than 15")
# else:
#     print("x is less than y")


# 2,Write a Python program that takes a grade as input and prints the corresponding letter grade.
# If the grade is less than 70, also print "You failed."
#
# n = int(input())
# if n >= 90:
#     print("A")
# elif n >= 80:
#     print("B")
# elif n >= 70:
#     print("C")
# elif n >= 60:
#     print("D")
# else:
#     print("F")
#
# if n < 70:
#     print("You failed.")

# 3,Write a Python program to check if a person is eligible for a credit card based on their age and income.
# If the person is underage, print "You are underage." If they are of age but have an income below $30,000,
# print "Your income is too low for a credit card."
#
# age=int(input())
# income=int(input())
# if age<18:
#     print("you are underage")
# elif income<30000:
#     print("your income is too low")
# else:
#     print("you are eligible")


# 4,Write a Python program to determine if a given number num is even or odd.
# If it's even, check if it's greater than 10 and print appropriate messages.
#
# n=int(input())
# if n%2==0:
#     print('even')
#     if  n>10:
#         print("Greater than 10")


# 5,Write a Python program that calculates the ticket price for a theme park based on age and height.
# If a person is under 12 years old and under 4 feet tall, the ticket price is $10.
# If they are under 12 but 4 feet tall or taller, the ticket price is $15.
# If a person is 12 or older and under 4 feet tall, the ticket price is $15.
# If they are 12 or older and 4 feet tall or taller, the ticket price is $20.

#
# age=int(input())
# height=int(input())
# if age<12 and height<4:
#     print("ticket price is 10")
# elif age<12 and height>=4:
#     print("ticket price is 15")
# elif age>=12 and height<4:
#     print("ticket price is 15")
# elif age>=12 and height>=4:
#     print("ticket price is 20")


# 6,Write a Python program for user authentication. Ask the user to enter their username and password.
# If both the username and password are correct, print "Access granted."
# If the username is correct but the password is incorrect, print "Incorrect password."
# If the username is incorrect, print "Invalid username."

#
# user = input("")
# password = input("")
# if user == "tharun":
#     if password == "12345":
#         print("Access granted")
#     else:
#         print("Incorrect password")
# else:
#     print("Invalid Username")


#
# 7.Write a Python program for ordering food. Ask the user to select a type of food (e.g., "Burger" or "Pizza").
# If they choose "Burger," ask if they want fries. If they choose "Pizza," ask if they want extra cheese.
# Print their order with the additional items if chosen.
#
# food = input("Enter food (Burger/Pizza): ")
# if food == "Burger":
#     fries = input("Do you want fries? (yes/no): ")
#     if fries == "yes":
#         print("You ordered Burger with Fries")
#     else:
#         print("You ordered Burger")
# elif food == "Pizza":
#     cheese = input("Do you want extra cheese? (yes/no): ")
#     if cheese == "yes":
#         print("You ordered Pizza with Extra Cheese")
#     else:
#         print("You ordered Pizza")
# else:
#     print("Invalid choice")

# 8.Write a Python program that takes an integer as input
# and checks if it('s positive, negative, or zero. ''If it')s positive, check if
# it('s even or odd.Print the appropriate messages.)

# n=int(input())
# if n>0:
#     print("it is a positive integer")
#     if n%2==0:
#         print("it is an even integer")
#     else:
#         print("it is an odd integer")
# elif n==0:
#     print("it is a zero integer")
# else:
#     print("it is a negative integer")




# 9.Write a Python program that asks for a user's age and checks if they have a driver's license.
# If the user is 18 or older and has a driver's license, print "You are eligible to drive." Otherwise, print "You are not eligible to drive."
#
#
# age = int(input("Enter your age: "))
# license = input("Do you have a driver's license? (yes/no): ").lower()
#
# if age >= 18 and license == "yes":
#     print("You are eligible to drive.")
# else:
#     print("You are not eligible to drive.")




# 10.Write a Python program that checks if a person is eligible to vote.
# Ask for the person('s age and citizenship. If the person is at least 18 years old and a citizen,'
#  print "You are eligible to vote." Otherwise, print "You are not eligible to vote.")
#
# age=int(input("Enter your age:"))
# citizenship=input()
# if age>=18 and citizenship=="India":
#     print("You are eligible")
# else:
#     print("You are not eligible")


#
# 11.Write a Python program that takes three numbers as input and prints them in ascending order.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a <= b and a <= c:
#     if b <= c:
#         print(a, b, c)
#     else:
#         print(a, c, b)
# elif b <= a and b <= c:
#     if a <= c:
#         print(b, a, c)
#     else:
#         print(b, c, a)
# else:
#     if a <= b:
#         print(c, a, b)
#     else:
#         print(c, b, a)



# 13.Write a Python program that classifies a character as a vowel, consonant, or neither.
# Ask the user to enter a single character. If it's a vowel (a, e, i, o, u), print "Vowel." If it's a consonant, print "Consonant."
# If it's neither (e.g., a digit or special character), print "Neither."
#
# n=input()
# if n in "aeiou":
#     print("vowel")
# elif 'a'<=n<='z':
#     print("consonant")
# else:
#     print("neither")





