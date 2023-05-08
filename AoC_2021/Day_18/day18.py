import re
from math import floor, ceil
from copy import deepcopy

with open('/Users/theeran-new/VSCode/Advent_Of_Code/Day_18/input18.txt') as file:
    inputdata = file.read().strip().split("\n")


def split(num):
    num1, num2 = str(floor(int(num)/2)), str(ceil(int(num)/2))
    return ['[', num1, ',', num2, ']']


def explode(sfn, i):
    a, b = sfn[i], sfn[i+2]
    i1 = i + 2
    sfn.extend(' ')

    index = 1
    while i - index > 0:
        if sfn[i - index].isnumeric():
            sfn[i - index] = str(int(sfn[i - index]) + int(a))
            break
        index += 1

    index = 1
    while sfn[i1 + index] != ' ':
        if sfn[i1 + index].isnumeric():
            sfn[i1 + index] = str(int(sfn[i1 + index]) + int(b))
            break
        index += 1

    sfn[i-1:i1+2] = "0"
    sfn.pop()

    return sfn


def combine(sfn1, sfn2):
    sfn1 = list(sfn1)
    sfn2 = list(sfn2)
    sfn = ["["]
    sfn.extend(sfn1)
    sfn.extend([","])
    sfn.extend(sfn2)
    sfn.extend(["]"])
    return sfn


def s(sfn):
    for i, element in enumerate(sfn):
        if element.isnumeric():
            if int(element) > 9:
                return i

    return None


def e(sfn):
    brack = 0
    for i, element in enumerate(sfn):
        if brack == 5:
            return i
        else:
            if element == '[':
                brack += 1
            if element == ']':
                brack -= 1

    return None


def reduce(sfn):
    ok = False
    while ok == False:
        old = deepcopy(sfn)
        if e(sfn) != None:
            sfn = explode(sfn, e(sfn))
        else:
            if s(sfn) != None:
                sfn[s(sfn):s(sfn)+1] = split(sfn[s(sfn)])

        if old == sfn:
            ok = True

    return sfn


def add(a, b):
    return ''.join(reduce(combine(a, b)))


for i, line in enumerate(inputdata):
    if line == inputdata[-1]:
        break
    elif line == inputdata[0]:
        sfn = line

    sfn = add(sfn, inputdata[i+1])


def magnitude(data):
    while data.count(",") > 1:
        for p in re.findall("\[\d+,\d+\]", data):
            pair = re.search(re.escape(p), data)
            left_digit, right_digit = p[1:-1].split(",")
            data = f"{data[: pair.start()]}{int(left_digit) * 3 + int(right_digit) * 2}{data[pair.end() :]}"
    left_digit, right_digit = data[1:-1].split(",")
    return int(left_digit) * 3 + int(right_digit) * 2


def mag(a, b):
    return magnitude(add(a, b))


part1 = magnitude(sfn)
part2 = 0

for x in inputdata:
    for y in inputdata:
        if x == y:
            continue
        else:
            if mag(x, y) > part2:
                part2 = mag(x, y)

print(part2)
