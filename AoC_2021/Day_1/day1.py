file = open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_1/input1.txt", "r")
inputdata = file.readlines()

# -------------------- Part 1 -------------------- #

intpreviousline = 0
inc_or_dec = ""
inc_counter = 0

for line in inputdata:

    intline = int(line)

    if (intline > intpreviousline):
        if intpreviousline == 0:
            break
        inc_counter += 1

    intpreviousline = intline

# print(inc_counter-1)

# -------------------- Part 2 -------------------- #
previousthree = 0
inc_counter = 0


for index, value in enumerate (inputdata):
    if int(index) == 1998:
        break

    sumofthree = int(inputdata[index]) + int(inputdata[index+1]) + int(inputdata[index+2])

    if (sumofthree > previousthree):
        inc_counter = inc_counter + 1

    previousthree = sumofthree

print(inc_counter-1)





    













