from copy import deepcopy

with open('Advent_Of_Code/AoC_2020/Day_10/input10.txt') as file:
    inputdata = sorted([int(char) for char in file.read().strip().split()])

inputdata.insert(0, 0)
inputdata.append(inputdata[-1] + 3)

# -------------------- Part 1 -------------------- #

# one = 0
# three = 0

# for i, e in enumerate(inputdata):
#     if e == inputdata[-1]:
#         print(one * three)
#         break

#     n = inputdata[i+1]

#     if n - e == 1:
#         one += 1
#     if n - e == 3:
#         three += 1

# -------------------- Part 2 -------------------- #

l = [inputdata]
possible = 0

iter = 0

def find(l):
    n = []
    for e in l:
        for t in e:
            if (t != e[-1]) and (t != e[-2]):
                if e[e.index(t)+2] - t <= 3:
                    a = deepcopy(e)
                    a.pop(e.index(t)+1)
                    n.append(a)
    
    return n

while l != []:
    possible += len(l)
    l = find(l)
    res = []

    for i in l:
        if i not in res:
            res.append(i)
    l = res

    iter += 1
    print(iter)
    

print(possible)
    
