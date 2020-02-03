from envs.puzzle import Puzzle

puzzle = Puzzle(init_state='010111010', final_state='000000000')
s, m = puzzle.step('A1')

print(s)
