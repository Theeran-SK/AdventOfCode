with open('/Users/theeran-new/VSCode/Advent_Of_Code/AoC_2020/Day_5/input5.txt') as file:
    inputdata = file.read().strip().split('\n')

rownums = []
colnums = []

for number in range(128):
    rownums.append(number)

for number in range(8):
    colnums.append(number)


def findrow(specification):
    global rownums
    rn = rownums
    rowdetails = specification[:7]
    for detail in rowdetails:
        if detail == 'F':
            rn = rn[:int(len(rn)/2)]
        if detail == 'B':
            rn = rn[int(len(rn)/2):]

    return rn


def findcol(specification):
    global colnums
    cn = colnums
    coldetails = specification[7:]
    for detail in coldetails:
        if detail == 'L':
            cn = cn[:int(len(cn)/2)]
        if detail == 'R':
            cn = cn[int(len(cn)/2):]

    return cn


def id(row, col):
    return row[0]*8+col[0]

# -------------------- Part 1 -------------------- #

# highestid = 0

# for s in inputdata:
#     if id(findrow(s), findcol(s)) > highestid:
#         highestid = id(findrow(s), findcol(s))

# print(highestid)

# -------------------- Part 2 -------------------- #

nums = []
for x in range(980):
    nums.append(x)
    
lst = []

for s in inputdata:
    lst.append(id(findrow(s), findcol(s)))

for each in nums:
    if each not in lst:
        if each > 40:
            print(each)
    

