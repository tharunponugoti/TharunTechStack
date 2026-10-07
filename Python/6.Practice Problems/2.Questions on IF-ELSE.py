# If-Else Statement

# 1,Write a Python program that checks if a given year is a leap year.
#
# n = int(input("Enter the year: "))
# if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
#     print(f"{n} is a leap year")
# else:
#     print(f"{n} is not a leap year")

# 2,Write a Python program that checks if a given character is a vowel or a consonant.

# n = input("Enter a character: ").lower()
# if n in "aeiou":
#     print(f"{n} is a vowel")
# else:
#     print(f"{n} is a consonant")


# 3,Write a Python program that checks if a given year is a century year (ending in '00').
#
# n=int(input("Enter a number: "))
# if n%100==0:
#     print(n,"is ending in 100")
# else:
#     print(n,"is not ending in 100")

# 4,Write a Python program that checks if a given number is prime

# num = int(input("Enter a number: "))
# c = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         c = c + 1
# if c == 2:
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# 5,Write a Python program that checks if a person is eligible to vote based on their age.
#
# n=int(input())
# if n<=18:
#     print("person is not eligible for vote")
# else:
#     print("person is eligible for vote")
#
# 6,Write a Python program that checks if a number is positive or non-positive (including zero).
#
# n=int(input())
# if n<0 :
#     print("number is negative")
# if n>0:
#     print("number is positive")
# if n==0:
#     print("number is zero")


# 7,Write a Python program that compares two numbers and prints the larger one.
#
# a=int(input())
# b=int(input())
# if a>b:
#     print(a)
# else:
#     print(b)


# 8,Write a Python program that checks if a given character is a letter or not.

# ch = input("Enter a character: ")
# if ch.isalpha():
#     print(f"{ch} is a letter")
# else:
#     print(f"{ch} is not a letter")


# 9,Write a Python program that finds and prints the smallest of three numbers without using inbuilt methods.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a <= b and a <= c:
#     print(a)
# elif b <= a and b <= c:
#     print(b)
# else:
#     print(c)


# 10,Write a Python program to check if a given string is a palindrome.

# text = input("Enter a string: ")
# if text == text[::-1]:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")

#
# 11,Write a Python program that finds and prints the largest of four numbers.
#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# if a>= b and a>= c and a>=d:
#     print(a)
# elif b >= a and b >= c and b>=d:
#     print(b)
# elif c >= a and c >= b and c>=d:
#     print(c)
# else:
#     print(d)

#
# 12,Write a Python program that takes two numbers as input and determines the sign of their difference.
#
# a=int(input())
# b=int(input())
# sign=a+b
# if sign<0:
#     print("difference is minus")
# elif sign>0:
#     print("difference is plus")
# else:
#     print("difference is zero")

#
# 13,Write a Python program that checks if a given year is a leap year using an alternative method.
#
#
# year = int(input("Enter a year: "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# 14,Write a Python program that checks if a number is a multiple of 7 or not.
#
# n=int(input())
# if n%7==0:
#     print("It is a multiple of 7")
# else:
#     print("It is not a multiple of 7")



# 15,Write a Python program that calculates and prints the absolute value of a given number.
#
#
# n = int(input("Enter a number: "))
# print("Absolute value:", abs(n))