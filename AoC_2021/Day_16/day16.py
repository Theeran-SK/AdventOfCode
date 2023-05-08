with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_16/input16.txt") as file:
    inputdata = file.readline()


def base10(binnum):
    return int(binnum, 2)


def checkforzero(lst):
    string = lst[0]
    ok = False
    if "1" in string:
        ok = True

    return ok


hex = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

data = ""

for chars in inputdata:
    for char in chars:
        data += hex[char]

# -------------------- Part 1 -------------------- #

# versionsum = 0

# lst = [data]

# while checkforzero(lst) == True:
#     data = lst[0]
#     version = data[:3]
#     versionsum += base10(version)
#     id = data[3:6]

#     if base10(id) == 4:
#         ind = 6
#         while data[ind] != "0":
#             ind += 5
#         ind += 5
#         d = data[ind:]
#         lst.append(d)

#     else:
#         if data[6] == "0":
#             l = data[7:22]
#             i = base10(l)
#             d = data[22:]
#             lst.append(d)

#         if data[6] == "1":
#             l = data[7:18]
#             i = base10(l)
#             d = data[18:]
#             lst.append(d)

#     lst.remove(data)


# print(versionsum)

# -------------------- Part 2 -------------------- #

lst = [data]
packets = []

while checkforzero(lst) == True:
    data = lst[0]
    id = data[3:6]

    if base10(id) == 4:
        ind = 6
        while data[ind] != "0":
            ind += 5
        ind += 5
        d = data[ind:]
        lst.append(d)

    else:
        if data[6] == "0":
            l = data[7:22]
            i = base10(l)
            d = data[22:]
            lst.append(d)

        if data[6] == "1":
            l = data[7:18]
            i = base10(l)
            d = data[18:]
            lst.append(d)

    lst.remove(data)
    packets.append(data)

for index, each in enumerate(packets):
    if each != packets[-1]:
        new = each.replace(packets[index+1], "")
        packets[index] = new
    else:
        each = each

print(packets)

for packet in packets:
    id = packet[3:6]
    l = packet[6]

    if base10(id) == 4:
        continue
    else:
        if l == "0":
            sub = base10(packet[7:22])
        if l == "1":
            sub = base10(packet[7:18])

        print(sub)



