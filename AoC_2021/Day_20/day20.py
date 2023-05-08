with open("Advent_Of_Code/AoC_2021/Day_20/input20.txt") as file:
    inputdata = file.read().strip().split("\n")


def printimage(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            print(matrix[x][y], end="")
        print()


def base10(binnum):
    return int(binnum, 2)


iea = inputdata[0]
image = inputdata[2:]

for i, each in enumerate(image):
    each = [char for char in each]
    image[i] = each

li = 0

for i in range(2):

    l = len(image)+4
    l2 = len(image[0])+4

    matrix = []

    for x in range(l):
        row = []
        for y in range(l2):
            row.append(".")
        matrix.append(row)

    for x, r in enumerate(image):
        for y, c in enumerate(r):
            matrix[x+2][y+2] = c

    image = []

    for x in range(l-2):
        row = []
        for y in range(l2-2):
            row.append(".")
        image.append(row)

    d = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    for x in range(l-2):
        for y in range(l2-2):

            newd = []
            lst = []

            for dir in d:
                xx = x + dir[0]
                yy = y + dir[1]
                newd.append((xx, yy))

            for each in newd:
                r, c = each
                lst.append(matrix[r][c])

            string = ""

            for each in lst:
                if each == "#":
                    each = "1"
                if each == ".":
                    each = "0"
                string += each

            mid = newd[len(newd)//2]
            ind = base10(string)

            if iea[ind] == ".":
                xr, yc = mid
                image[xr-1][yc-1] = "."  

            if iea[ind] == "#":
                xr, yc = mid
                image[xr-1][yc-1] = "#"   
                if i == 1:
                    li += 1       




printimage(image)

lights = 0

for x in image:
    for y in x:
        if y == "#":
            lights += 1

print(li)