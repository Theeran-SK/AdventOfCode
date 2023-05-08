with open('Advent_Of_Code/AoC_2020/Day_8/input8.txt') as file:
    inputdata = file.read().strip().split('\n')

acc = 0
v = []
ok = False
i = 0

while ok == False:
    if i in v:
        print(acc)
        break
    else:
        v.append(i)

    instruction = inputdata[i]
    operation = instruction[:3]
    argument = instruction[4:]

    if operation == 'nop':
        i += 1
        continue
    elif operation == 'acc':
        acc += int(argument)
        i += 1
    elif operation == 'jmp':
        i += int(argument)

