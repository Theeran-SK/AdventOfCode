file = open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_8/input8.txt", "r")
inputdata = file.readlines()

# -------------------- Part 1 -------------------- #

# counter = 0

# for line in inputdata:
#     line = str(line).lstrip("abcdefg ").split(" ")
#     line.remove("|")
#     for element in line:
#         if len(element.strip()) == 2:
#             counter +=1
#         elif len(element.strip()) == 3:
#             counter +=1
#         elif len(element.strip()) == 4:
#             counter +=1
#         elif len(element.strip()) == 7:
#             counter +=1
#         else:
#             continue

# print(counter)

# -------------------- Part 2 -------------------- #

totalsum = 0

segments = "abcdefg"

A = ""
B = ""
C = ""
D = ""
E = ""
F = ""
G = ""


def listtostring(list):
    new = ""
    for x in list:
        new += str(x)
    return new


def diffchar(word1, word2):
    lst = []
    for char in word1:
        if char not in word2:
            lst.append(char)

    return listtostring(lst)


def split(word):
    return [char for char in word]


def diffcharbothways(word1, word2):
    x = len(diffchar(word1, word2))
    y = len(diffchar(word2, word1))

    return x + y

for line in inputdata:

    rightline = str(line).lstrip("abcdefg ").split(" ")
    leftline = line.split(" ")

    for element in rightline:
        if element in leftline:
            leftline.remove(element)

    rightline.remove("|")

    count = 0
    tempone = ""
    tempseven = ""
    tempfour = ""
    tempeight = ""

    while count < 4:
        for element in leftline:
            if len(element) == 2:
                tempone = element
                count += 1
            if len(element) == 3:
                tempseven = element
                count += 1
            if len(element) == 4:
                tempfour = element
                count += 1
            if len(element) == 7:
                tempeight = element
                count += 1

    for element in leftline:
        if len(element) == 5:
            if len(''.join(set(element).intersection(tempfour))) == 2:
                C = ''.join(set(element).intersection(tempone))
                F = tempone.replace(C, "")
            if len(''.join(set(element).intersection(tempseven))) == 3:
                A = tempseven
                for character in tempone:
                    A = A.replace(character, "")

    for element in leftline:
        if len(element) == 6:
            missingsegment = diffchar(segments, element)
            comparetofour = diffchar(tempfour, element)

            if len(comparetofour) == 0:
                G = diffchar(element, tempfour).replace(A, "")

    for element in leftline:
        if len(element) == 5:
            knownelements = listtostring([A, C, F, G])
            if len(diffchar(element, knownelements)) == 1:
                D = diffchar(element, knownelements)

    for element in leftline:
        if len(element) == 6:
            knownelements = listtostring([A, C, D, F, G])
            if len(diffchar(element, knownelements)) == 1:
                B = diffchar(element, knownelements)

    knownelements = listtostring([A, B, C, D, F, G])
    E = diffchar(tempeight, knownelements)

    zero = {"segment": listtostring([A, B, C, E, F, G]), "value": 0}
    one = {"segment": tempone, "value": 1}
    two = {"segment": listtostring([A, C, D, E, G]), "value": 2}
    three = {"segment": listtostring([A, C, D, F, G]), "value": 3}
    four = {"segment": tempfour, "value": 4}
    five = {"segment": listtostring([A, B, D, F, G]), "value": 5}
    six = {"segment": listtostring([A, B, D, E, F, G]), "value": 6}
    seven = {"segment": tempseven, "value": 7}
    eight = {"segment": tempeight, "value": 8}
    nine = {"segment": listtostring([A, B, C, D, F, G]), "value": 9}

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]

    number = []

    for element in rightline:
        for digit in digits:
            if diffcharbothways(element.strip(), digit["segment"]) == 0:
                number.append(digit["value"])
    
    numberval = int(listtostring(number))

    totalsum += numberval

print(totalsum)           

