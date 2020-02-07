from agents.bfs import bfs

start = "1010010111001010"
search, sol = bfs(start=start, max_length=7, size=4)
print(search)
print(sol)
