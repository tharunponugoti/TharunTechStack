# Break and Continue statements

# 2.Create a Python program to calculate the sum of all numbers from 1 to 100.
# However, if the number is divisible by both 3 and 5, skip it using the continue statement.


# n=int(input())
# s=0
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         continue
#     s=s+i
# print(s)


#
# 5.Create a Python program that simulates a basic login system.
# Ask the user to enter a username and password. If the entered password is incorrect, give the user three attempts.
# Use the break statement to exit the loop if the password is correct or the user exceeds the maximum attempts.
#
# correct_username = "admin"
# correct_password = "1234"
#
# for i in range(3):
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#
#     if username == correct_username and password == correct_password:
#         print("Login successful")
#         break
#
#     print("Incorrect username and password")
#
# if i == 2 and not (username == correct_username and password == correct_password):
#     print("Maximum attempts exceeded")


#
# 6.Write a Python program that finds the first 10 even numbers.
# If a number is divisible by 3, skip it using the continue statement.
#
# n=int(input())
# for i in range(1,n+1):
#     if i%3==0:
#         continue
#     print(i)




# 13.Write a Python program that asks the user to input a password.
# If the password is not at least 8 characters long, keep asking for a valid password using a loop.
# Use the continue statement to skip further processing until a valid password is provided.
#
# password = input("Enter password: ")
#
# while len(password) < 8:
#     print("Invalid password")
#     password = input("Enter password: ")
#     continue
#
# print("Valid password")




# 14.Write a Python program to find the sum of all even numbers from 1 to 100.
# However, if a multiple of 7 is encountered, skip it using the continue statement.
#
# n=int(input())
# s=0
# for i in range(1,n+1):
#     if i%2==0:
#         if i%7==0:
#             continue
#         s=s+i
# print(s)
