#           0   1   2   3   4   5   6   7   8
numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

#                            5     10    2
# range(5, 10, 2) -> range(start, end, step)

print(numbers[2:7:2])
#               2     7     2
# [2:7:2] -> [start, end, step]
# [33, 55, 77]

print(numbers[2:7])
#             2     7
# [2:7] -> [start, end]
# [33, 44, 55, 66, 77]

print(numbers[0:9])
#             0     9
# [0:9] -> [start, end]
# [11, 22, 33, 44, 55, 66, 77, 88, 99]

print(numbers[0:9:3])
#               0     9     3
# [0:9:3] -> [start, end, step]
# [11, 44, 77]