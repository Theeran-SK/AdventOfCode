file = open("Advent_Of_Code/AoC_2021/Day_21/input21.txt", "r")
inputdata = file.readlines()

p1 = int(inputdata[0].split(":")[1].strip())
p2 = int(inputdata[1].split(":")[1].strip())

# -------------------- Part 1 -------------------- #

# dice = 1

# score1 = 0
# score2 = 0

# counter = 0

# while score1 < 1000 and score2 < 1000:
#     for x in range(3):
#         if dice == 101:
#             dice = 1
#         p1 += dice
#         dice +=1
#         counter+=1
#     if p1 > 10:
#         p1 = p1 % 10
#         if p1 == 0:
#             p1 = 10
#     score1 += p1

#     if score1 >= 1000:
#         print(score2 * counter)


#     for x in range(3):
#         if dice == 101:
#             dice = 1
#         p2 += dice
#         dice +=1
#         counter +=1
#     if p2 > 10:
#         p2 = p2 % 10
#         if p2 == 0:
#             p2 = 10
#     score2 += p2

#     if score2 >= 1000:
#         print(score1 * counter)

# -------------------- Part 2 -------------------- #





