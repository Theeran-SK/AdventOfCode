from collections import Counter

with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_5/input5.txt") as file:
    inputdata = file.read().strip().split("\n")

biglist = []


def numsthrough(n1, n2):
    if n1 > n2:
        t = n1
        n1 = n2
        n2 = t

    num_range = range(n1, n2+1)
    return list(num_range)


def pointsthrough(c1, c2):

    x1, y1 = c1
    x2, y2 = c2

    coordlst = []

    if x1 == x2:
        yvals = numsthrough(y1, y2)
        for yval in yvals:
            coord = (x1, yval)
            coordlst.append(coord)

    if y1 == y2:
        xvals = numsthrough(x1, x2)
        for xval in xvals:
            coord = (xval, y1)
            coordlst.append(coord)

    return coordlst


def diagpoints(c1, c2):

    x1, y1 = c1
    x2, y2 = c2

    coordlst = []

    if x1 > x2 and y1 < y2:
        for i in range(x1-x2):
            coordlst.append((x1, y1))
            x1 -= 1
            y1 += 1
        coordlst.append((x2, y2))


    if x1 < x2 and y1 > y2:
        for i in range(x2-x1):
            coordlst.append((x2, y2))
            x2 -= 1
            y2 += 1
        coordlst.append((x1, y1))

    if x1 > x2 and y1 > y2:
        for i in range(x1-x2):
            coordlst.append((x1, y1))
            x1 -= 1
            y1 -= 1
        coordlst.append((x2, y2))

    if x1 < x2 and y1 < y2:
        for i in range(x2-x1):
            coordlst.append((x2, y2))
            x2 -= 1
            y2 -= 1
        coordlst.append((x1, y1))

    return coordlst


for line in inputdata:
    c1 = line.split(" -> ")[0].split(",")
    c2 = line.split(" -> ")[1].split(",")

    for i, n in enumerate(c1):
        n = int(n)
        c1[i] = n
    for i, n in enumerate(c2):
        n = int(n)
        c2[i] = n

    x1, y1 = c1
    x2, y2 = c2

    if x1 == x2 or y1 == y2:
        biglist.extend(pointsthrough(c1, c2))

    else:
        biglist.extend(diagpoints(c1, c2))

print(biglist)

cnt = Counter(biglist)

final = [k for k, v in cnt.items() if v > 1]
ans = len(final)

print(ans)
