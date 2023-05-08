with open('Advent_Of_Code/AoC_2020/Day_6/input6.txt') as file:
    inputdata = file.read().strip().split("\n\n")

final = 0

# -------------------- Part 1 -------------------- #

# for question in inputdata:
#     final += len("".join(set(question.replace('\n', ''))))

# print(final)

# -------------------- Part 2 -------------------- #

for question in inputdata:
    question = question.split('\n')
    for answer in question[0]:
        ok = False
        for person in question:
            if answer in person:
                continue
            else:
                ok = True
        if ok == False:
            final += 1

print(final)
            
            