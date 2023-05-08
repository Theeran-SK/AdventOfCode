from collections import defaultdict, deque
from pprint import pprint


def s(c):
    return c.islower()

adj = defaultdict(list)

with open("/Users/theeran-new/VSCode/Advent_Of_Code/Day_12/input12.txt") as file:
    inputdata = file.read().strip().split("\n")

# -------------------- Part 1 -------------------- #

# for i, each in enumerate(inputdata):
#     each = each.split("-")
#     inputdata[i] = each

# for a, b in inputdata:
#     adj[a].append(b)
#     adj[b].append(a)


# global final
# final = 0

# vis = set()


# def dfs(c):
#     global final

#     if c == "end":
#         final += 1
#         return

#     if s(c) and c in vis:
#         return

#     if s(c):
#         vis.add(c)

#     for nbr in adj[c]:
#         if nbr == "start":
#             continue
#         dfs(nbr)

#     if s(c):
#         vis.remove(c)


# dfs("start")


# print(final)

# -------------------- Part 2 -------------------- #

for a, b in inputdata:
    adj[a].append(b)
    adj[b].append(a)


global final
final = 0

vis = defaultdict(int)


def dfs(c):
    global final

    if c == "end":
        final += 1
        return

    if s(c):
        vis[c] += 1

        more_than_once = 0
        for small in vis:
            more_than_once += vis[small] > 1

            if vis[small] > 2:
                vis[c] -= 1
                return

        if more_than_once > 1:
            vis[c] -= 1
            return

    for nbr in adj[c]:
        if nbr == "start":
            continue
        dfs(nbr)

    if s(c):
        vis[c] -= 1


dfs("start")

print(final)