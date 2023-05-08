with open("Advent_Of_Code/AoC_2022/Day_2/input2.txt") as file:
    inputdata = file.read().strip().split("\n")

# score = 0

# for each in inputdata:
#     if each[0] == "A":
#         if each[2] == "X":
#             score += 4
#         if each[2] == "Y":
#             score += 8
#         if each[2] == "Z":
#             score += 3
#     if each[0] == "B":
#         if each[2] == "X":
#             score += 1
#         if each[2] == "Y":
#             score += 5
#         if each[2] == "Z":
#             score += 9
#     if each[0] == "C":
#         if each[2] == "X":
#             score += 7
#         if each[2] == "Y":
#             score += 2
#         if each[2] == "Z":
#             score += 6

# # print(score)

newscore = 0

for each in inputdata:
    if each[0] == "A":
        if each[2] == "X":
            newscore += 3
        if each[2] == "Y":
            newscore += 4
        if each[2] == "Z":
            newscore += 8
    if each[0] == "B":
        if each[2] == "X":
            newscore += 1
        if each[2] == "Y":
            newscore += 5
        if each[2] == "Z":
            newscore += 9
    if each[0] == "C":
        if each[2] == "X":
            newscore += 2
        if each[2] == "Y":
            newscore += 6
        if each[2] == "Z":
            newscore += 7

print(newscore)