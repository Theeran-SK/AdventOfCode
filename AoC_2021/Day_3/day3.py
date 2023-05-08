file = open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_3/input3.txt", "r")
inputdata = file.readlines()

# -------------------- Part 1 -------------------- #

# bitlist = []
# indexofline = 0
# finallist = []
# counter = 0

# def most_common(lst):
#     return max(set(lst), key=lst.count)

# for x in range (12):

#     for line in inputdata:
#         bitlist.append(line[indexofline])
#         counter += 1

#         if counter == 1000:
#             finallist.append(most_common(bitlist))
#             bitlist = []
#             counter = 0
#             indexofline += 1

#         if indexofline == 12:
#             break

# final = "".join(finallist)
# print(final)

# -------------------- Part 2 -------------------- #

totallist = []
bitlist = []

indexofline = 0
counter = 0

oxygenlist = []
carbonlist = []
templist = []

for line in inputdata:
    totallist.append(line)

oxygen = totallist
carbon = totallist


def most_common(lst):
    return max(set(lst), key=lst.count)


while len(oxygen) > 1:

    for line in oxygen:
        bitlist.append(line[indexofline])

    index = 0

    zero = 0
    one = 0

    for i in bitlist:
        if i == '0':
            zero += 1
        if i == '1':
            one += 1

    if zero > one:
        first = 0
    else:
        first = 1

    oxygenlist.append(first)

    for item in oxygen:
        if item[indexofline] == str(first):
            templist.append(oxygen[index])
        index += 1

    oxygen = templist
    templist = []

    indexofline += 1
    bitlist = []


indexofline = 0

while len(carbon) > 1:

    for line in carbon:
        bitlist.append(line[indexofline])

    index = 0

    zero = 0
    one = 0

    for i in bitlist:
        if i == '1':
            zero += 1
        if i == '0':
            one += 1

    if zero >= one:
        first = 0
    else:
        first = 1

    carbonlist.append(first)

    for item in carbon:
        if item[indexofline] == str(first):
            templist.append(carbon[index])
        index += 1

    carbon = templist
    templist = []

    indexofline += 1
    bitlist = []

oxygenstring = [str(int) for int in oxygen]
carbonstring = [str(int) for int in carbon]

finaloxygen = "".join(oxygenstring)
finalcarbon = "".join(carbonstring)

oxygenfinal = int(finaloxygen, 2)
carbonfinal = int(finalcarbon, 2)

print(oxygenfinal * carbonfinal)
