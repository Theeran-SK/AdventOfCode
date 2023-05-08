import copy

with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_9/input9.txt") as file:
    inputdata = file.read().strip().split("\n")

for index, line in enumerate(inputdata):
    line = [char for char in line]
    inputdata[index] = line

# -------------------- Part 1 -------------------- #

# totalsum = 0

# for number, row in enumerate(inputdata):
#     for num, x in enumerate(row):

#         flag = False
#         x = int(x)

#         if number != 0:
#             check = int(inputdata[number-1][num])
#             if x >= check:
#                 flag = True

#         if number != 99:
#             check = int(inputdata[number+1][num])
#             if x >= check:
#                 flag = True

#         if num != 0:
#             check = int(inputdata[number][num-1])
#             if x >= check:
#                 flag = True

#         if num != 99:
#             check = int(inputdata[number][num+1])
#             if x >= check:
#                 flag = True

#         if flag == True:
#             continue

#         totalsum += x+1

# print(totalsum)

# -------------------- Part 2 -------------------- #

lst = []
basinsize = []


for number, row in enumerate(inputdata):
    for num, x in enumerate(row):

        flag = False
        x = int(x)

        if x == 9:
            continue

        if number != 0:
            check = int(inputdata[number-1][num])
            if x >= check:
                flag = True

        if number != 99:
            check = int(inputdata[number+1][num])
            if x >= check:
                flag = True

        if num != 0:
            check = int(inputdata[number][num-1])
            if x >= check:
                flag = True

        if num != 99:
            check = int(inputdata[number][num+1])
            if x >= check:
                flag = True

        if flag == True:
            continue

        lst.append((number, num))


directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

boardcopy = copy.deepcopy(inputdata)

for (xlow, ylow) in lst:

    a = True
    newnewlst = []
    newlst = []
    newlst.append((xlow, ylow))
    boardcopy[xlow][ylow] = None

    while a == True:
        for element in newlst:
            (xheight, yheight) = element
            for add_x, add_y in directions:
                nx = xheight + add_x
                ny = yheight + add_y
                if 0 <= nx <= 99 and 0 <= ny <= 99:
                    nval = int(inputdata[nx][ny])
                    neighval = int(str(inputdata[xheight][yheight]))
                    if 0 <= nval <= 8:
                        if nval > neighval:
                            if boardcopy[nx][ny] != None:
                                newlst.append((nx, ny))
                                boardcopy[nx][ny] = None
            newlst.remove((xheight, yheight))
            newnewlst.append((xheight, yheight))
        if newlst == []:
            basinsize.append(len(newnewlst))
            break

basinsize.sort()

print(basinsize[-1] * basinsize[-2] * basinsize[-3])        


