with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_10/input10.txt") as file:
    inputdata = file.read().strip().split("\n")

symbols = ["()", "[]", "{}", "<>"]

# -------------------- Part 1 -------------------- #

scoring1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


# score = 0

# for line in inputdata:
#     lst = []
#     for symbol in line:
#         ok = False
#         for pair in symbols:
#             if symbol == pair[0]:
#                 lst.append(symbol)
#                 ok = True
#             if symbol == pair[1]:
#                 if lst[-1] == pair[0]:
#                     lst.pop()
#                     ok = True

#         if ok == False:
#             score += scoring[symbol]
#             break

# print(score)

# -------------------- Part 2 -------------------- #

final = []

scoring = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


# Remove corrupted lines
def removeline(line):
    lst = []
    for symbol in line:
        ok = False
        for pair in symbols:
            if symbol == pair[0]:
                lst.append(symbol)
                ok = True
            if symbol == pair[1]:
                if lst[-1] == pair[0]:
                    lst.pop()
                    ok = True

        if ok == False:
            return "bad line!"

    return "goodline"

data = []

for line in inputdata:
    if removeline(line) == "goodline":
        data.append(line)

for line in data:
    lst = []
    score = 0
    for symbol in line:
        for pair in symbols:
            if symbol == pair[0]:
                lst.append(symbol)
            if symbol == pair[1]:
                if lst[-1] == pair[0]:
                    lst.pop()

    for start in lst[::-1]:
        score *= 5
        score += scoring[start]

    final.append(score)

final.sort()
score = final[len(final)//2]

print(score)