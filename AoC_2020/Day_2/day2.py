with open('/Users/theeran-new/VSCode/Advent_Of_Code/AoC_2020/Day_2/input2.txt') as file:
    inputdata = file.read().strip().split('\n')

for i, line in enumerate(inputdata):
    line = line.split(': ')
    line[0] = line[0].split(' ')
    inputdata[i] = line

valid = 0

# -------------------- Part 1 -------------------- #

# for line in inputdata:
#     password = line[1]
#     count = password.count(line[0][1])
#     num1 = int(line[0][0].split('-')[0])
#     num2 = int(line[0][0].split('-')[1])
#     if count >= num1 and count <= num2:
#         valid += 1

# print(valid)

# -------------------- Part 1 -------------------- #

for line in inputdata:
    password = line[1]
    letter = line[0][1]
    one = password[int(line[0][0].split('-')[0])-1]
    two = password[int(line[0][0].split('-')[1])-1]
    if (one == letter and two != letter) or (one != letter and two == letter):
        valid += 1

print(valid)
