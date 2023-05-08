file = open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_7/input7.txt", "r")
inputdata = file.readlines()

# -------------------- Part 1 -------------------- #

# data = inputdata[0].split(',')
# values = []

# for i in data:
#     inti = int(i)
#     values.append(inti)

# maxvalue = max(values)
# minvalue = min(values)

# alltotalsums = []

# for integer in range (minvalue, maxvalue + 1):

#     totalsum = 0

#     for value in values:
#         totalsum = totalsum + abs(integer - value)

#     alltotalsums.append(totalsum)

# minvalue = min(alltotalsums)

# print(minvalue)

# -------------------- Part 2 -------------------- #

data = inputdata[0].split(',')
values = []

def sigma(number):
    ssum = 0
    for i in range(number + 1):
        ssum = ssum + i
    return ssum

for i in data:
    inti = int(i)
    values.append(inti)

maxvalue = max(values)
minvalue = min(values)

alltotalsums = []

for integer in range (minvalue, maxvalue + 1):

    totalsum = 0

    for value in values:
        totalsum = totalsum + sigma(abs(value - integer))

    alltotalsums.append(totalsum)

minvalue = min(alltotalsums)

print(minvalue)








