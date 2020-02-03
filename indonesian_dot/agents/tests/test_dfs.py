from math import sqrt

from agents.dfs import dfs

from spaces import action_space

start = "1010010111001010"
goal = "0000000000000000"
size = len(start)
actions = action_space(size)

search, sol = dfs(start, goal)
print(search)
print(sol)
