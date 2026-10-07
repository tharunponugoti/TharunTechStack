-----Variables

A Variable in Python is Name that refers to value stored in a memory

------syntax to create
variable:

Variablename = Value

Ex:
Age = 20

a = 10
print(a) - ----10
print(id(a)) - ----101

a = 20
print(a) - ----20
print(id(a)) - ----102

Variables stored in the Stack Memory
Values stored in the Heap Memory



----what is mutable objects
These are the objects whose content can be changed once it is created
Ex:
List,Set,Dictionary


------what is Immutable objects
These objects whose content can not be changed once it is created
Ex:
Integer, float ,String, Boolean, Tuple, Froozen Set, None



----How to Assign Multiple Values to Multiple Variables

 Variablename1,Variablename2=Value1,Value2
 Ex:
 a,b=10,20

-----How to Assign Single Values to Multiple Variables


 Variablename1=Variablename2=Value
 Ex:
 a=b=10


----How to Reassign Variable

Ex:
age=10
print(id(age())
o/p: 101


age=20
print(id(age))
o/p: 102




-----Rules for Naming the Variables
Python variable-naming rules:
- Start with a letter or underscore: name, _count
- After that, use letters, digits, or underscores: student_1
- Do not start with a digit: 1student ❌
- Do not use spaces or symbols such as -, @, or #: student-name ❌
- Do not use Python keywords: class, if, for, True ❌
- Variable names are case-sensitive: age, Age, and AGE are different.
Python style convention: use lowercase snake_case.




student_name = "THARUN"
total_marks = 95
is_present = True



Use clear, meaningful names:
price = 100          # Good
total_price = 100    # Better
x = 100              # Avoid when its meaning is unclear
