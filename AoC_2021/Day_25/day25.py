from copy import deepcopy

with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_25/input25.txt") as file:
    inputdata = file.read().strip().split("\n")

for index, line in enumerate(inputdata):
    line = [char for char in line]
    inputdata[index] = line

east = []
south = []

for x, r in enumerate(inputdata):
    for y, c in enumerate(r):
        if c == ".":
            continue
        else:
            if c == ">":
                east.append((x, y))
            if c == "v":
                south.append((x, y))

havestopped = False
step = 0


while havestopped == False:
    old = deepcopy(east)
    old1 = deepcopy(south)
    e = east.copy()
    s = south.copy()

    for i, coord in enumerate(east):
        a, b = coord

        if b == 138:
            newb = 0
        else:
            newb = b + 1

        if ((a, newb) not in s) and ((a, newb) not in e):
            east[i] = (a, newb)
        else:
            continue

    for i, coord in enumerate(south):
        a, b = coord

        if a == 136:
            newa = 0
        else:
            newa = a + 1

        if ((newa, b) not in s) and ((newa, b) not in east):
            south[i] = (newa, b)
        else:
            continue
    
    new = deepcopy(east)
    new1 = deepcopy(south)

    if (old == new) and (old1 == new1):
        break

    step += 1
    print(step)

print(step+1)



