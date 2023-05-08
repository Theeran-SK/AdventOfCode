with open('Advent_Of_Code/AoC_2018/Day_1/input1.txt') as file:
    inputdata = file.read().strip().split('\n')

sum = 0

# -------------------- Part 1 -------------------- #

# for line in inputdata:
#     if line[0] == '+':
#         sum += int(line[1:])
#     elif line[0] == '-':
#         sum -= int(line[1:])

# print(sum)

# -------------------- Part 2 -------------------- #

freqlst = []
ok = False

while ok == False:
    for line in inputdata:
        if line[0] == '+':
            sum += int(line[1:])
        elif line[0] == '-':
            sum -= int(line[1:])

        if sum in freqlst:
            print(sum)
            ok = True
            break
        else:
            freqlst.append(sum)
    