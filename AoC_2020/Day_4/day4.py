with open('Advent_Of_Code/AoC_2020/Day_4/input4.txt') as file:
    inputdata = file.read().strip().split("\n\n")

fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

valid = 0

# -------------------- Part 1 -------------------- #

# for passport in inputdata:
#     ok = False
#     for field in fields:
#         if field in passport:
#             continue
#         else:
#             ok = True
#     if ok == True:
#         continue
#     else:
#         valid += 1

# print(valid)

# -------------------- Part 2 -------------------- #

valids = []
valid = 0
eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
hexl = ['a', 'b', 'c', 'd', 'e', 'f']
hexnum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for passport in inputdata:
    ok = False
    for field in fields:
        if field in passport:
            continue
        else:
            ok = True
    if ok == True:
        continue
    else:
        valids.append(passport)

for passport in valids:
    passport = passport.replace('\n', ' ').split(' ')
    passport.sort()
    if len(passport) == 8:
        passport.remove(passport[1])

    if (int(passport[0][4:]) < 1920) or (int(passport[0][4:]) > 2002):
        continue
    if passport[1][4:] not in eyecolors:
        continue
    if (int(passport[2][4:]) < 2020) or (int(passport[0][4:]) > 2030):
        continue
    if (passport[3][4] != '#'):
        continue
    for each in passport[3][5:]:
        ok = False
        if (each not in hexl) and (int(each) not in hexnum):
            ok = True
    if ok == True:
        continue
    if ('cm' not in passport[4]) and ('in' not in passport[4]):
        continue
    ok = False
    if passport[4][-2] == 'cm':
        if (int(passport[4][4:-2]) < 150) or (int(passport[4][4:-2]) > 193):
            ok = True
    if passport[4][-2] == 'in':
        if (int(passport[4][4:-2]) < 59) or (int(passport[4][4:-2]) > 76):
            ok = True
    if ok == True:
        continue
    if (int(passport[5][4:]) < 2010) or (int(passport[5][4:]) > 2020):
        continue
    if (len(passport[6][4:]) != 9):
        continue
    valid += 1

print(valid)

