import re

file = open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_2/input2.txt", "r")
inputdata = file.readlines()

# -------------------- Part 1 -------------------- #

# forward = 0
# up = 0
# down = 0

# for line in inputdata:
#     if "forward" in line:
#         value = int(re.sub("[^0-9]", "", line))
#         forward = forward + value

#     if "up" in line:
#         value = int(re.sub("[^0-9]", "", line))
#         up = up - value

#     if "down" in line:
#         value = int(re.sub("[^0-9]", "", line))
#         down = down + value
    
#     value = 0

# vertical = up + down
# final = vertical * forward

# print(final)

# -------------------- Part 2 -------------------- #

forward = 0
aim = 0
vertical = 0

for line in inputdata:
    if "forward" in line:
        value = int(re.sub("[^0-9]", "", line))
        forward = forward + value
        vertical = vertical + (aim * value)

    if "up" in line:
        value = int(re.sub("[^0-9]", "", line))
        aim = aim - value

    if "down" in line:
        value = int(re.sub("[^0-9]", "", line))
        aim = aim + value

final = vertical * forward
print(final)







    