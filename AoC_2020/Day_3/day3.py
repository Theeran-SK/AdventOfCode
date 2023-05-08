with open('Advent_Of_Code/AoC_2020/Day_3/input3.txt') as file:
    inputdata = file.read().strip().split()

x = 1
y = 3
max_x = len(inputdata)
max_y = len(inputdata[0])

trees = 0

# -------------------- Part 1 -------------------- #

# while max_x != x:
#     if y >= max_y:
#         y -= max_y
#     if inputdata[x][y] == '#':
#         trees += 1
    
#     x += 1
#     y += 3

# print(trees) 

# -------------------- Part 1 -------------------- #

final = 1

while max_x != x:
    if y >= max_y:
        y -= max_y
    if inputdata[x][y] == '#':
        trees += 1
    
    x += 1
    y += 3
final *= trees

trees = 0
x = 1
y = 1
while max_x != x:
    if y >= max_y:
        y -= max_y
    if inputdata[x][y] == '#':
        trees += 1
    
    x += 1
    y += 1
final *= trees

trees = 0
x = 1
y = 5
while max_x != x:
    if y >= max_y:
        y -= max_y
    if inputdata[x][y] == '#':
        trees += 1
    
    x += 1
    y += 5
final *= trees

trees = 0
x = 1
y = 7
while max_x != x:
    if y >= max_y:
        y -= max_y
    if inputdata[x][y] == '#':
        trees += 1
    
    x += 1
    y += 7
final *= trees

trees = 0
x = 2
y = 1
while max_x > x:
    if y >= max_y:
        y -= max_y
    if inputdata[x][y] == '#':
        trees += 1
    
    x += 2
    y += 1
final *= trees

print(final)
