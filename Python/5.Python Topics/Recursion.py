from threading import Condition

from matplotlib.pyplot import step

-----Recursion

1,Recursion function is a function that calls its self to solve small part of Program
(A function calls itself is called Recursion)

2,It has base case and recursive step

3,It reduce length of the code

4,It is used Implement Concepts like Trees,Merge sort,Quick sort, etc...

5,The Recursive limit is 1000

* Stack LIFO
* Queue FIFO

 Syntax

 def functionName():
     if Condition
         return Value #base case
     else:
         return functionName()
