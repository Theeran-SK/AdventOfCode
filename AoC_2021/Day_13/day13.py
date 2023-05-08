with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_13/input13.txt") as file:
    inputdata = file.read().strip().split("\n")

points = inputdata[:835]
folds = inputdata[836:]


def firstfold(fold):
    fold = fold.split(" ")[2].split("=")
    fold[1] = int(fold[1])
    return fold


for fold in folds:

    finallist = []
    f = firstfold(fold)

    if f[0] == 'y':
        for point in points:
            p = str(point)
            y = f[1]
            py = int(p.split(",")[1].strip(")"))
            px = int(p.split(",")[0].strip("("))
            if y > py:
                finallist.append((px, py))
            if y < py:
                diff = py - y
                newy = y - diff
                finallist.append((px, newy))

    if f[0] == 'x':
        for point in points:
            p = str(point)
            x = f[1]
            py = int(p.split(",")[1].strip(")"))
            px = int(p.split(",")[0].strip("("))
            if x > px:
                finallist.append((px, py))
            if x < px:
                diff = px - x
                newx = x - diff
                finallist.append((newx, py))

    finallist = set(finallist)
    points = finallist

for y in range(6):
    for x in range(40):
        if (x, y) in finallist:
            print("#", end="")
        else:
            print(".", end="")
    print()
