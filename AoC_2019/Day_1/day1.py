from math import floor

with open('Advent_Of_Code/AoC_2019/Day_1/input1.txt') as file:
    inputdata = file.read().strip().split('\n')

sum = 0

for line in inputdata:
    sum += floor(int(line)/3) - 2

print(sum)