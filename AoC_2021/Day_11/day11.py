with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_11/input11.txt") as file:
    inputdata = file.read().strip().split("\n")

for index, line in enumerate(inputdata):
    line = [int(char) for char in line]
    inputdata[index] = line

directions = [(1, 0), (1, -1), (1, 1), (-1, 1),
              (-1, 0), (-1, -1), (0, 1), (0, -1)]

flashes = 0


def step(mtrx):
    for x, row in enumerate(mtrx):
        for y, i in enumerate(row):
            mtrx[x][y] = i + 1
    
    return mtrx

lst = []
alloctupusesflash = False
counter = 0

# -------------------- Part 1 -------------------- #

# for v in range(100):
#     step(inputdata)
#     for x, r in enumerate(inputdata):
#         for y, c in enumerate(r):
#             if c >= 10:
#                 inputdata[x][y] = 0
#                 flashes += 1
#                 ok = True
#                 lst.append((x, y))
#     ok = True
#     if lst != []:
#         while ok == True:
#             element = lst[0]
#             xx, yy = element
#             for add_x, add_y in directions:
#                 nx = xx + add_x
#                 ny = yy + add_y
#                 if 0 <= nx <= 4 and 0 <= ny <= 4:
#                     if inputdata[nx][ny] == 0:
#                         continue
#                     if inputdata[nx][ny] == 9:
#                         inputdata[nx][ny] = 0
#                         lst.append((nx, ny))
#                         flashes += 1
#                     else:
#                         inputdata[nx][ny] = inputdata[nx][ny] + 1                                

            
#             lst.remove(element)
#             if lst == []:
#                 ok = False


# print(flashes)

# -------------------- Part 2 -------------------- #

while alloctupusesflash == False:
    alloctupusesflash = True
    step(inputdata)
    for x, r in enumerate(inputdata):
        for y, c in enumerate(r):
            if c >= 10:
                inputdata[x][y] = 0
                ok = True
                lst.append((x, y))
    ok = True
    if lst != []:
        while ok == True:
            element = lst[0]
            xx, yy = element
            for add_x, add_y in directions:
                nx = xx + add_x
                ny = yy + add_y
                if 0 <= nx <= 9 and 0 <= ny <= 9:
                    if inputdata[nx][ny] == 0:
                        continue
                    if inputdata[nx][ny] == 9:
                        inputdata[nx][ny] = 0
                        lst.append((nx, ny))
                    else:
                        inputdata[nx][ny] = inputdata[nx][ny] + 1                                

            
            lst.remove(element)
            if lst == []:
                ok = False

    counter += 1

    for row in inputdata:
        for column in row:
            if column != 0:
                alloctupusesflash = False

print(counter)



