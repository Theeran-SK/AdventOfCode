from copy import deepcopy
import heapq
from collections import defaultdict

with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_15/input15.txt") as file:
    risks = [[int(i) for i in line] for line in file.read().strip().split("\n")]
risk = deepcopy(risks)
# -------------------- Part 1 -------------------- #

# N = len(risks)
# M = len(risks[0])

# cost = defaultdict(int)

# pq = [(0, 0, 0)]
# heapq.heapify(pq)
# visited = set()

# while len(pq) > 0:
#     c, row, col = heapq.heappop(pq)

#     if (row, col) in visited:
#         continue
#     visited.add((row, col))

#     cost[(row, col)] = c

#     if row == N - 1 and col == M - 1:
#         break

#     for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         rr = row + dr
#         cc = col + dc
#         if not (0 <= rr < N and 0 <= cc < M):
#             continue

#         heapq.heappush(pq, (c + risks[rr][cc], rr, cc))


# print(cost[(N - 1, M - 1)])

# -------------------- Part 2 -------------------- #

def step(map):
    newmap = deepcopy(map)
    for x, r in enumerate(newmap):
        for y, c in enumerate(r):
            if c == 9:
                c = 1
            else:
                c += 1
            newmap[x][y] = c
    
    return newmap

r = []

for x in range(5):
    r.extend(risks)
    risks = step(risks)

for x in range(4):
    c = []
    t = risk
    for y in range(x+1):
        t = step(t)
    for z in range(5):
        c.extend(t)
        t = step(t)
    for w in range(500):
        r[w].extend(c[w])

risks = r

N = len(risks)
M = len(risks[0])

cost = defaultdict(int)

pq = [(0, 0, 0)]
heapq.heapify(pq)
visited = set()

while len(pq) > 0:
    c, row, col = heapq.heappop(pq)

    if (row, col) in visited:
        continue
    visited.add((row, col))

    cost[(row, col)] = c

    if row == N - 1 and col == M - 1:
        break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        rr = row + dr
        cc = col + dc
        if not (0 <= rr < N and 0 <= cc < M):
            continue

        heapq.heappush(pq, (c + risks[rr][cc], rr, cc))


print(cost[(N - 1, M - 1)])

# for x in range(50):
#     for y in range(50):
#         print(r[x][y], end="")
#     print()