A function that accepts another function as an argument or returns a function
is called a higher-order function.




------Map
It is used apply the function on each element in the list

Ex:
marks:[10,20,30,40]
result=list(map(lambda x:x+5,marks))
print(result)

o/p
[15,25,35,45]


-----Filter
It is used to filter the elements based on the condition


Ex:
numbers=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x:x>3,numbers))
print(result)


o/p
[4,5,6,7,8,9]



-----Reduce
It returns single value, if you want use reduce function we should import reduce
from functools




Ex:
from functools import reduce
marks=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,marks)
print(result)


o/p
150



----sorted
sorted() is used to sort elements.

numbers = [5, 2, 8, 1, 3]
result = sorted(numbers)
print(result)


o/p
[1, 2, 3, 5, 8]



numbers = [5, 2, 8, 1, 3]
result = sorted(numbers, reverse=True)
print(result)

o/p
[8, 5, 3, 2, 1]


names = ["Ram", "Alexander", "Joe", "Christopher"]
result = sorted(names, key=len)
print(result)

o/p
['Ram', 'Joe', 'Alexander', 'Christopher']


sorted() with lambda

students = [("Ram", 80),("John", 95),("Sam", 70)]
result = sorted(students, key=lambda x: x[1])
print(result)

o/p
[('Sam', 70), ('Ram', 80), ('John', 95)]

Here:

x[1]

means the second value:

("Ram", 80)
          ↑

So students are sorted according to their marks.


Descending marks
students = [("Ram", 80),("John", 95),("Sam", 70)]
result = sorted(students, key=lambda x: x[1], reverse=True)
print(result)

Output:

[('John', 95), ('Ram', 80), ('Sam', 70)] 