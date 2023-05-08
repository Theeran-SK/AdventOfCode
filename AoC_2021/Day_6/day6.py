from collections import defaultdict

file = open("Advent_Of_Code/AoC_2021/Day_6/input6.txt", "r")
inputdata = file.read().strip().split(",")

print(inputdata)
# values = defaultdict(int)
# for i in inputdata:
#     values[int(i)] += 1

# for i in range(256):

#     templist = defaultdict(int)

#     for value in values:
#         if value == 0:
#             templist[6] += values[value]
#             templist[8] = values[value]
#         else:
#             templist[value - 1] += values[value]
    
#     values = templist

# final = 0
# for value in values:
#     final += values[value]

# print(final)


        