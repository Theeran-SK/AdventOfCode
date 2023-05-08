from copy import deepcopy

with open('Advent_Of_Code/AoC_2020/Day_11/input11.txt') as file:
    inputdata = file.read().strip().split('\n')

for i, e in enumerate(inputdata):
    inputdata[i] = [char for char in e]

adj = [(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1)]

havestopped = False

# -------------------- Part 1 -------------------- #

# while havestopped == False:
#     cpy = deepcopy(inputdata)
#     for x, row in enumerate(inputdata):
#         for y, col in enumerate(row):
#             if col == '.':
#                 continue
#             elif col == 'L':
#                 ok = False
#                 for a in adj:
#                     if (0 <= x+a[0] < len(inputdata)) and (0 <= y+a[1] < len(inputdata[0])):
#                         if cpy[x+a[0]][y+a[1]] == '#':
#                             ok = True
#                 if ok == False:
#                     inputdata[x][y] = '#'
#             elif col == '#':
#                 cnt = 0
#                 for a in adj:
#                     if (0 <= x+a[0] < len(inputdata)) and (0 <= y+a[1] < len(inputdata[0])):
#                         if cpy[x+a[0]][y+a[1]] == '#':
#                             cnt += 1
#                 if cnt >= 4:
#                     inputdata[x][y] = 'L'
#     if cpy == inputdata:
#         havestopped = True

# occ = 0

# for r in inputdata:
#     for c in r:
#         if c == '#':
#             occ += 1

# print(occ)

# -------------------- Part 2 -------------------- #


def addone(coord):
    if coord[0] == 0:
        if coord[1] < 0:
            return (coord[0], coord[1]-1)

        elif coord[1] > 0:
            return (coord[0], coord[1]+1)

    elif coord[1] == 0:
        if coord[0] < 0:
            return (coord[0]-1, coord[1])

        elif coord[0] > 0:
            return (coord[0]+1, coord[1])

    else:
        if (coord[0] < 0) and (coord[1] < 0):
            return (coord[0]-1, coord[1]-1)

        elif (coord[0] > 0) and (coord[1] > 0):
            return (coord[0]+1, coord[1]+1)

        elif (coord[0] < 0) and (coord[1] > 0):
            return (coord[0]-1, coord[1]+1)

        elif (coord[0] > 0) and (coord[1] < 0):
            return (coord[0]+1, coord[1]-1)


def firstone(x, y, dir, data):
    while (0 <= x+dir[0] < len(data)) and (0 <= y+dir[1] < len(data[0])):
        if data[x+dir[0]][y+dir[1]] == '#':
            return '#'
        elif data[x+dir[0]][y+dir[1]] == 'L':
            return 'L'
        dir = addone(dir)
    return 'L'


while havestopped == False:
    cpy = deepcopy(inputdata)
    for x, row in enumerate(inputdata):
        for y, col in enumerate(row):
            if col == 'L':
                ok = False
                for a in adj:
                    if firstone(x, y, a, cpy) == '#':
                        ok = True

                if ok == False:
                    inputdata[x][y] = '#'

            elif col == '#':
                cnt = 0
                for a in adj:
                    if firstone(x, y, a, cpy) == '#':
                        cnt += 1

                if cnt >= 5:
                    inputdata[x][y] = 'L'

    if cpy == inputdata:
        havestopped = True

    for r in inputdata:
        for c in r:
            print(c, end="")
        print()
    print()

occ = 0

for r in inputdata:
    for c in r:
        if c == '#':
            occ += 1

for r in inputdata:
    for c in r:
        print(c, end="")
    print()

print(occ)
