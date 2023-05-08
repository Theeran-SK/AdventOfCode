from math import floor, ceil
from copy import deepcopy

sfn1 = "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]"
sfn2 = "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"

with open('/Users/theeran-new/VSCode/Advent_Of_Code/Day_18/input18.txt') as file:
    inputdata = file.read().strip().split("\n")


def explode(sfn, i):

    a, b = sfn[i], sfn[i+2]

    i += 1
    i1 = i + 2

    sfn.insert(0, ' ')
    sfn.extend(' ')


    ok = False
    index = 3

    while ok == False:
        isnum = sfn[i - index]

        if isnum.isnumeric():
            num1 = int(isnum) + int(a)
            sfn[i - index] = str(num1)
            ok = True

        elif isnum == " ":
            num1 = 0
            ok = True

        index += 1

    ok = False
    index = 2

    while ok == False:
        isnum = sfn[i1 + index]

        if isnum.isnumeric():
            num2 = int(isnum) + int(b)
            sfn[i1 + index] = str(num2)
            ok = True

        elif isnum == " ":
            num2 = 0
            ok = True

        index += 1

    sfn[i-1:i1+2] = "0"
    sfn.pop(0)
    sfn.pop(-1)

    return sfn


def split(sfn, i):
    sfn[i:i+1] = list("[{},{}]".format(floor(int(sfn[i])/2), ceil(int(sfn[i])/2)))
    return sfn


def add(sfn1, sfn2):
    sfn1 = list(sfn1)
    sfn2 = list(sfn2)

    sfn = ["["]
    sfn.extend(sfn1)
    sfn.append(",")
    sfn.extend(sfn2)
    sfn.append("]")

    bracklst = []

    ok = False
    while ok == False:
        i = 0

        oldsfn = deepcopy(sfn)

        while i < len(sfn) - 1:
            char = sfn[i]
            if len(bracklst) == 5:
                sfn = explode(sfn, i)
                i = 0
                bracklst = []
                continue
            else:
                if char == "[":
                    bracklst.append("[")
                if char == "]":
                    bracklst.pop()
                i += 1
        
        i = 0

        while i < len(sfn) - 1:
            if sfn[i].isnumeric():
                if int(sfn[i]) >= 10:
                    sfn = split(sfn, i)
            
            i += 1
        
        if sfn == oldsfn:
            ok = True


    return sfn

print(add(sfn1, sfn2))
final = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"


