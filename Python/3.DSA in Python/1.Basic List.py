#Sum of all elements in a 2D list

#
# l= [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# s=0
# for i in l:
#     for value in row:
#         total = total + value
# print("Sum of all elements:", total)



numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in numbers:
    for value in row:
        total = total + value

print("Sum of all elements:", total)


second largest 