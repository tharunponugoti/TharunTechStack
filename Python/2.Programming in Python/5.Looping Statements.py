# ------range()
# It is use to generate the sequence of numbers or it returns sequence of numbers


# for i in range(10,0,-2):
#     print(i)

r=range(1,11,1)
print(r) # returns range object
i=iter(r) #converts range object into iter object
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))   # stop iteration


-----Looping statements

1,These statements are used to repeat the block of code into multiple statements
2,Loops are used to execute block of code repeatedly until the condition True
3,There are two types in Python

1,for loop
2,while loop



-----for loop

when we know the number of iterations then we use for loop
for loop is used to iterating over the sequence of numbers

syntax for loop

    for  variable in range(start,end,step):
        Block of code

Ex:
1,Write a program to print 1 to 10

  range(1,11,1)

  for i in range(1,11,1):
      print(i)

O/p
1
2
3
4
5
6
7
8
9
10

for i in range(1,11,2):
    print(i)

o/p
1
3
5
7
9

for i in range(10,1,-1):
    print(i)

o/p
10
9
8
7
6
5
4
3
2


for i in range(10,0,-1):
    print(i)

o/p
10
9
8
7
6
5
4
3
2
1

for i in range(1,10):
    print(i)

o/p
1
2
3
4
5
6
7
8
9




for i in range(1,10):
    print(i,end=" ")

o/p
1 2 3 4 5 6 7 8 9


for i in range(10,0,-1):
    print(i)
print("end")

o/p
10
9
8
7
6
5
4
3
2
1
end


for i in range(1,11):
    print(i)
print("end")

o/p
1
2
3
4
5
6
7
8
9
10
end

for i in range(1):
    print(i)
print("end")

o/p
0
end


for i in range(0):
    print(i)
print("end")

o/p
end



l=[1,2,3,4,5,6]
for i in l:
    print(i)
print("end of for loop")
print("hey")

o/p
1
2
3
4
5
6
end of for loop
hey



l=[1,2,3,4,5,6]
for i in l:
    print(i,end=" ")
print("end of for loop")
print("hey")

o/p
1 2 3 4 5 6 end of for loop
hey


l=[10,20,30,40,50]
for i in range(len(l)):
    print(i,l[i])


o/p
0 10
1 20
3 30
4 40




-----while loop
when we dont know numbers of iteration then we will use while loop

use cases of while loop
reading or counting on documents
binary search implementation



-----while loop syntax

    initialization
while condition:
    statement
    Incre/decrement


to print 1 to 10 numbers
i=1
e=10
while i<=e:
    print(i)
    i=i+1





