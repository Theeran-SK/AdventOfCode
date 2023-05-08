with open('Advent_Of_Code/AoC_2020/Day_9/input9.txt') as file:
    inputdata = file.read().strip().split('\n')

i = 0
l = len(inputdata) - 26
invalid = None

while (i != l) and (invalid == None):
    pre = inputdata[i:i+25]
    nth = inputdata[i+25]
    ok = False
    for term in pre:
        for t in pre:
            if term != t:
                if int(term) + int(t) == int(nth):
                    ok = True
    
    if ok == False:
        invalid = int(nth)

    i += 1

# -------------------- Part 1 -------------------- #

# print(nth)

# -------------------- Part 2 -------------------- #

for i, term in enumerate(inputdata):
    ok, lst, ind, sum = False, [], inputdata.index(term), 0

    while sum < invalid:
        sum += int(inputdata[i])
        lst.append(int(inputdata[i]))
        if sum == invalid:
            print(int(max(lst)) + int(min(lst)))
            ok = True
    
        i += 1

    if ok == True:
        break

