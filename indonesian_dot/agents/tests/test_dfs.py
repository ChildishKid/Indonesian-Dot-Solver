from agents.dfs import dfs

start = "1010010111001010"
search, sol = dfs(start=start, max_depth=10, size=4)
print(search)
print(sol)
