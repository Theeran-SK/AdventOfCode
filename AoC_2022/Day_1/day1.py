with open("Advent_Of_Code/AoC_2022/Day_1/input1.txt") as file:
    inputdata = file.read().replace("\n", " ").split("  ")

sums = []

for each in inputdata:
    strnums = each.split(" ")
    strnums = sum([int(item) for item in strnums])
    sums.append(strnums)

bigsum = max(sums)

print(bigsum)

sums.sort()

print(sums[-1]+sums[-2]+sums[-3])
    