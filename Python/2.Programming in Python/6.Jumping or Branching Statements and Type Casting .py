-----Jumping or Branching Statements
These statements are used to change normal flow of execution in program
It is used to jump the controller(PVM) from the one part of another instead of
execution in sequential order

These are into 4 types
1,break
2,continue
3,pass
4,return


1,Break
It is used to break the loop whenever specified condition is satisfied

syntax for break

for var in object:
    if condition:
        break


Ex:
for i in range(1,6):
    if i==3:
        break
    print(i)


o/p
1
2


2,continue
It is used to skip the particular iteration where the condition is statisfed
and continue further iterations normally

Ex:
for i in range(1,6):
    if i==3:
        continue
    print(i)



o/p
1
2
4
5
6




---for else
Here else will be executed when the when for loop executes normally

    for var in object:
        block of code
    else:
        block of code

Ex:
for i in range(1,6):
    print(i)
else:
    print("else")

o/p
1
2
3
4
5
else






Ex:
for i in range(1,6):
    if i==3:
        break
    print(i)
else:
    print("else")


o/p
1
2


Ex;

rids=[101,102,103,104,105]
uid=103
for id in rids:
    if id==uid:
        print("user id is found")
        break
else:
    print("user id is not found")

o/p
user id is found


Ex:
rids = [101, 102, 103, 104, 105]
uid = 106
for id in rids:
    if id == uid:
        print("user id is found")
        break
else:
    print("user id is not found")



o/p
user id is not found


Ex

rids=[101,102,103,104,105]
uid =103
for id in range(len(rids)):
    if rids==uid:
        print(f'user id is found at index no is {rids[id]}')
        break
else:
    print("user id is not found")
print("end")



o/p
user id is found at index no is 2
end



Ex:
rids=[101,102,103,104,105]
uid =107
for id in range(len(rids)):
    if rids==uid:
        print(f'user id is found at index no is {rids[id]}')
        break
else:
    print("user id is not found")
print("end")



o/p
user id is not found
end




rids=[101,102,103,104,105]
uid =103
for id in range(len(rids)):
    if rids==uid:
        continue
else:
    print(rids[id])
print("end")



o/p
101
102
104
105
end





---while else

Here else block will execute while loop completes normally

    Syntax


initialization
while condition:
    block of code
else:
    block of code






-----Assert Keyword
It is used to check the condition if the condition is true then program continue
normally otherwise it rise Assertion error

assert keyword:

age =15
assert age>=18,'not eligible for vote'
print("eligible for vote")


o/p
eligible for vote


age = 19
assert age >= 18, 'not eligible for vote'
print("eligible for vote")

o/p
Assertion Error