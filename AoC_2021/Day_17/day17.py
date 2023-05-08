# -------------------- Part 1 -------------------- #

# import re

# xmin, xmax, ymin, ymax = map(int, re.findall(r"-?\d+", "target area: x=70..125, y=-159..-121"))
# print((ymin + 1) * ymin // 2)

# -------------------- Part 1 -------------------- #

with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_17/input17.txt") as file:
    inputdata = file.read().strip("target area: x=").split(", y=")

xrange = (int(inputdata[0].split("..")[0]), int(inputdata[0].split("..")[1]))
yrange = (int(inputdata[1].split("..")[0]), int(inputdata[1].split("..")[1]))

targetarea = (xrange, yrange)


def cycle(p, v):
    newp = [0, 0]
    newv = [0, 0]

    newp[0] = p[0] + v[0]
    newp[1] = p[1] + v[1]

    newv[1] = v[1] - 1
    if v[0] > 0:
        newv[0] = v[0] - 1
    if v[0] < 0:
        newv[0] = v[0] + 1

    return newp, newv


def intarget(p, target):
    return (target[0][0] <= p[0] <= target[0][1]) and (target[1][0] <= p[1] <= target[1][1])


def passed(p, v, target):
    if v[0] > 0 and p[0] > target[0][1]:
        return True
    if v[0] < 0 and p[0] < target[0][0]:
        return True
    if v[1] < 0 and p[1] < target[1][0]:
        return True
    return False


def hits(v, target):
    p = (0, 0)
    max_y = 0
    while not passed(p, v, target):
        max_y = max(max_y, p[1])
        if intarget(p, target):
            return True, max_y
        p, v = cycle(p, v)

    return False


max_yv = abs(targetarea[1][0])

final = 0

yv = max_yv
while yv >= targetarea[1][0]:
    for xv in range(-1000, 1010):
        works = hits((xv, yv), targetarea)
        if works:
            final += 1

    yv -= 1

print(final)