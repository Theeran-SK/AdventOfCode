file = open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_14/input14.txt", "r")
# inputdata = file.readlines()


# def stringtolist(string):
#     list1 = []
#     list1[:0] = string.strip()
#     return list1


# polymertemplate = stringtolist(inputdata[0])
# polymertemp = stringtolist(inputdata[0])

# for i in range(10):

#     polymerindex = 0

#     for n in range(len(polymertemplate) - 1):

#         polymerlist = []

#         polymerlist.append(polymertemplate[polymerindex])
#         polymerlist.append(polymertemplate[polymerindex + 1])

#         for index, item in enumerate(inputdata):
#             if index < 2:
#                 continue
#             else:
#                 data = list(item.split("->")[0].strip())
#                 output = item.split("->")[1].strip()

#                 y = n + 1

#                 if polymerlist == data:
#                     polymertemp.insert(2*y-1, output)
                    


#         polymerindex += 1
#     polymertemplate = polymertemp.copy()
#     print(i, len(polymertemplate))
  




# def most_frequent(List):
#     counter = 0
#     num = List[0]
     
#     for i in List:
#         curr_frequency = List.count(i)
#         if(curr_frequency > counter):
#             counter = curr_frequency
#             num = i
 
#     return num

# def least_frequent(arr):
#     temp_arr, leastCtr, leastElement, currentCtr = arr.copy(), len(arr), -99, 1
#     temp_arr.sort()
#     for i in range(len(temp_arr) - 1):
#         if (temp_arr[i] == temp_arr[i + 1]):
#             currentCtr += 1
#         else:
#             if (currentCtr < leastCtr):
#                 leastCtr, leastElement = currentCtr, temp_arr[i]
#             currentCtr = 1
#     if (currentCtr < leastCtr):
#         leastCtr, leastElement = currentCtr, temp_arr[len(temp_arr) - 1]
#     return leastElement


import string
from collections import defaultdict
import copy


inputdata = file.read().strip().split("\n")

template = inputdata[0]
rules = [line.split(" -> ") for line in inputdata[2:]]

freqs = defaultdict(int)
for i in range(len(template) - 1):
    freqs[template[i:i + 2]] += 1

elements = string.ascii_uppercase


def replace(freqs):
    new_freqs = copy.copy(freqs)
    for pair in freqs:
        for start, end in rules:
            if pair == start:
                occs = freqs[pair]
                new_freqs[pair] -= occs
                new_freqs[pair[0] + end] += occs
                new_freqs[end + pair[1]] += occs
                break

    return new_freqs


for i in range(40):
    freqs = replace(freqs)

count = defaultdict(int)
for pair in freqs:
    count[pair[0]] += freqs[pair]
    count[pair[1]] += freqs[pair]

count[template[0]] += 1
count[template[-1]] += 1

count_vals = [c[1] // 2 for c in count.items()]

ans = max(count_vals) - min(count_vals)
print(ans)