from math import sqrt

from agents.functions import dfs
from spaces import DiGraph

start = "1010010111001010"
goal = "0000000000000000"
size = len(start)
dim = int(sqrt(size))
actions = {}

for i in range(size):
    val = sum([2 ** (size - 1 - x) for x in
               [i - dim,
                i - 1 if i % dim > 0 else -1,
                i,
                i + 1 if i % dim < dim - 1 else -1,
                i + dim]
               if 0 <= x < size])
    key = chr(int(i / dim) + 65) + str((i % dim) + 1)
    actions[key] = val

graph = DiGraph()
ans = dfs(graph, actions, int(start, 2), int(goal, 2), '0' + str(size) + 'b', depth=(0, 4))
print(ans)
print(len(ans))
