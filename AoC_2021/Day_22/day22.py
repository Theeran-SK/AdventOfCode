import numpy
from collections import defaultdict

with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_22/input22.txt") as file:
    inputdata = file.read().strip().split("\n")

# -------------------- Part 1 -------------------- #

# inputdata = inputdata[:20]
# steps = []

# for each in inputdata:
#     each = each.split(" ")
#     switch = each[0] == "on"
#     bounds = []
#     for c in each[1].split(","):
#         c = c.split("..")
#         bounds.append((int(c[0][2:]) + 50, int(c[1]) + 50))

#     steps.append((switch, bounds))

# grid = numpy.zeros((101, 101, 101), dtype=bool)

# for switch, bounds in steps:
#     xr, yr, zr = bounds

#     for x in range(xr[0], xr[1] + 1):
#         for y in range(yr[0], yr[1] + 1):
#             for z in range(zr[0], zr[1] + 1):
#                 grid[x, y, z] = switch


# final = 0
# for x in grid.flatten():
#     final += x
# print(final)

# -------------------- Part 2 -------------------- #

steps = []


def volume(c):
    x = 1
    for b in c:
        x *= abs(b[1] - b[0]) + 1
    return x


def overlap(bounds1, bounds2):
    ans = []
    for b1, b2 in zip(bounds1, bounds2):
        if b1[1] < b2[0] or b2[1] < b1[0]:
            return None

        bounds = (max(b1[0], b2[0]), min(b1[1], b2[1]))
        ans.append(bounds)

    return tuple(ans)


for each in inputdata:
    each = each.split(" ")
    switch = each[0] == "on"
    bounds = []
    for c in each[1].split(","):
        c = c.split("..")
        bounds.append((int(c[0][2:]), int(c[1])))

    steps.append((switch, tuple(bounds)))


counts = defaultdict(int)

for i in range(len(steps)):
    switch, bounds = steps[i]

    new_counts = defaultdict(int)
    keys = set(counts.keys())

    for cube in keys:
        o = overlap(bounds, cube)
        if o == None:
            continue

        new_counts[o] -= counts[cube]

    if switch:
        new_counts[bounds] += 1

    for c in new_counts:
        counts[c] += new_counts[c]


final = 0

for cube in counts:
    final += volume(cube) * counts[cube]

print(final)