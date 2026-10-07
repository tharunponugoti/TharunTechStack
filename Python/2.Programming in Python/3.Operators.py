from django.template.smartif import OPERATORS

------Operators

In Python Operators is a Symbols that is used to Perform Operations on data.

----Types of Operators

1,Arthematic Operator
2,Comparsion Operators
3,Assignment Operators
4,Logical Operators
5,Bitwise Operators
6,Membership Operators
7,Identify Operators



------Arthematic Operator

These Opertors used to perform mathematical Operations like +,-,*,/,//,%,**


a=10
b=3
print(a+b)
13


print(a-b)
7

print(a*b)
30


print(a/b)
3.33333


print(a//b)
3

print(a%b)
1         (reminder)


print(a**b)
1000



------Comparsion Operators

1,These operators are used to compare the two values
2,The return type of comparsion operator is "bolean"

==    ----Equal to
!=    ----Not Equal to
<     ----Less than
>     ----Greater than
<=    ----Less than or equal to
>=    ----Greater than or equal to


a>b, a<b, a==b are called as conditions



-----Assignment Operator
It is used to Assign a value to Variable
Ex: = ----Assignment Operator

Age=24
name="THARUN"



-----Logical Operators
These Operators are used to combine the multiple conditions the output of logical
operator is boolean
Here we have three operator
1,and
2,or
3,not

---And
It returns True if both conditions are True

---Or
It returns True if any one of the conditions is True

----Not
It inverts the Output,That means if the condition is True then it returns False and vice versa


Ex:
a=30
b=20
c=10
print(a>b and a<c)
o/p:
False


print(a>c and a>b)
o/p:
True



Ex:
a=30
b=25
c=15
print(not(a>b) or a>c and a<b)
o/p:
False


---Priority Order

not
 |
and   --(multi)
 |
or



-----Bitwise Operators
These operators are used to perform the Opearation at bit level

bits---->0's and 1's
1 byte---> 8 bits
4 byte---> 32 bits

Truth Table

a  b  a&b  a|b  a^b
1  1   1    1    0
1  0   0    1    1
0  1   0    1    1
0  0   0    0    0


-----Identity Operators
These operators are used to check the memory locations of two objects
if it is same then it returns True other wise False
Here we have two Identity operators
1,is
2,is not

Ex:
a=25
b=20
print(a is b)
o/p
False

print(a is not b)
o/p
True


Difference between Identity operator and == operator

1,Identity Operator are used to check memory locations of two objects not Values
2,==(equal to) Operator is used to compare the two values not address


-----Membership Operators
These operators are used to check a Particular value is present in object or not
Here we have two Membership operators
1,in
2,not in

Ex:
a="THARUN"
print("A" in "THARUN")
o/p
True

print("P" in "THARUN")
o/p
False