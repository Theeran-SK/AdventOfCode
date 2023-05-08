with open('/Users/theeran-new/VSCode/Advent_Of_Code/AoC_2020/Day_1/input1.txt') as file:
    inputdata = file.read().strip().split('\n')

# -------------------- Part 1 -------------------- #

# def findsum(sum, num1, num2):
#     if num1 + num2 + num3 == sum:
#         return num1*num2
#     return None

# for x in inputdata:
#     for y in inputdata:
#         if findsum(2020, int(x), int(y)) != None:
#             print(int(x)*int(y))

# -------------------- Part 1 -------------------- #

def findsum(sum, num1, num2, num3):
    if num1 + num2 + num3 == sum:
        return True
    return None

for x in inputdata:
    for y in inputdata:
        for z in inputdata:
            if findsum(2020, int(x), int(y), int(z)) != None:
                print(int(x)*int(y)*int(z))

