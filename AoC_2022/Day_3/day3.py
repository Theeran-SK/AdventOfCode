import string

with open("Advent_Of_Code/AoC_2022/Day_3/input3.txt") as file:
    inputdata = file.read().strip().split("\n")

sum = 0
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)


for each in inputdata:
    c1, c2 = each[:len(each)//2], each[len(each)//2:]
    common = set(c1) & set(c2)
    for e in common:
        if e.isupper() == True:
            sum += uppercase.index(e)
            sum += 27
        else:
            sum += lowercase.index(e)
            sum += 1

print(sum)
        

