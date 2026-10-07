from django.db.backends.ddl_references import Statement
from django.views.decorators.http import condition

-----Control Statements
Contol Statements are used control the  flow of program execution by allowing you
to make make decisions and repeat the task and jump to different parts of code based on certain condition


Types of Control Statements
1,Conditions Statements/Decision Statements
2,Looping Statements
3,Branching/Jumping Statements


-----Conditions Statements/Decision Statements
   if,if-else,elif,nested-if/,nested if-else



------Looping Statements
  for,while


------Jumping Statements
  break,continue,pass,return



-----Indentation
Indentation is a wide space at begining of the code
It is used to represent or difine block of code



1,Conditions Statements/Decision Statements
These statements allows the program to make decisions
These Statements are used to check the conditions

-----if Statements
It is used to check the condition,if the condition is True then if block will execute
otherwise controller(PVM) moves out of if statement

---if statement syntax:
if condition:
    Block of code

Ex:
a=10
if a>5:
    print('THARUN')

o/p
THARUN

2,
a=15
if a>10:
    print("THARUN")
    print("PONUGOTI")

o/p
THARUN
PONUGOTI


3,
a=15
if a>20:
    print("THARUN")
print("PONUGOTI")

o/p
PONUGOTI


-----if-else Statement
It is also used to check the condition  if the condition is True then if block
will execute otherwise else block will execute

syntax of if-else

if condition:
    Block of code
else:
    else Block of code



Ex
a=10
if a>5:
    print("THARUN")
else:
    print("PONUGOTI")

o/p
THARUN


2,
a=15
if a>10:
    print("THARUN")
else:
    print("PONUGOTI")
print("end")

o/p
THARUN
end



3,
a=5
if a>3:
    print("THARUN")
print("PONUGOTI")
else:
    print("Hey")


o/p
syntax error(This gives a syntax error because else must come immediately after its if block.)


Even or not

n=int(input())
if n%2==0:
    print(f"{n} is even")
else:
    print(f"{n} is not even")

odd or not
n=int(input())
if n%2==1:
    print(f"{n} is odd")
else:
    print(f"{n} is not odd")


Largest number among two numbers
a=20
b=15
if a>b:
    print("a is greater than number")
else:
    print("b is greater than number")




-----elif Statement


It used for check multiple conditions
if the first condition is false then if you want to check further conditions then we go for elif statements

syntax  for  elif Statements

    if condition1:
        Block1 of code
    elif condition2:
        Block2 of code
    elif condition3:
        Block3 of code
          .
          .
          .
    else:
        else Block code

Ex; Write a python program to find largest among three numbers

a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("f{a} is a largest number")
elif b>a and b>c:
    print("f{b} is a largest number")
else:
    print("f{c} is a largest number")


Ex: Take an input number check whether it is three digit number or not

n=int(input())
if 100<=n<=999 or -999<=n<=-100:
    print(f'{n} is a three digit number')
else:
    print(f'{n} is not a three digit number')


Ex: Take a temperatue input and :
-- If above 30: print 'its hot
--if between 15 and 30: print 'pleasant'
--if below 15: print 'cold'


t=int(input())
if t>30:
    print("cold")
elif 15<t<=30:
    print("pleasant")
else:
    print("hot")


Ex: check whether character is lower case or upper case or not alphabet

n=input()
if n.isupper():
    print('given char is uppercase')
elif n.islower():
    print('given char is lowercase')
else:
    print('not alphabet')



-----nested if Statement
Nested if means writing if condition inside another if conditions

syntax of nested if

if condition 1:
    if condition 2:
        Block of code
    if condition 3:
        Block of code



Ex:

age=int(input())
if age>=18:
    print("adult")
    if age>=60:
        print("senior citizen")
    if age<=60:
        print("your not senior citizen")
print("end")


Ex:

age=int(input())
if age>=18:
    print("adult")
    if age>=60:
        print("senior citizen")
    print("end-1")
    if age<=60:
        print("your not senior citizen")
    print("end-2")
print("end")


---Nested if else statement

Nested if else means writing if conditions inside another if conditions,
Here we will else condition/ else block to handle the opposite conditions

syntax for nested if else statement

if condition1:
    if condition2:
        Block 1 code
    else:
        Block 2 code
else:
    Block 3 code


Ex: Cricket Game
age>=15
weight>=30


a=int(input())
b=int(input())
if a>=15:
    if b>=30:
        print("eligible")
    else:
        print("not eligible")
else:
    print("not eligible")

