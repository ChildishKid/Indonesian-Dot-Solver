import unittest

import agents
from envs.puzzle import Puzzle


class MyTestCase(unittest.TestCase):

    def test_bfs(self):
        bfs = agents.make('bfs')
        p = Puzzle('1010101110000000000000000')
        p.max_depth = 7
        p.max_length = 5
        sol, search = p.traverse(bfs)
        print(sol)
        print()
        print(search)

    def test_dfs(self):
        dfs = agents.make('dfs')
        p = Puzzle('0000000000000000000000000000000000000000000100000000111000000001000000000000000000000000000000000000')
        p.max_depth = 2
        p.max_length = 2
        sol, search = p.traverse(dfs)
        print(sol)
        print()
        print(search)

    def test_dfs2(self):
        dfs = agents.make('dfs')
        p = Puzzle('1010101110000000000000000')
        p.max_depth = 7
        p.max_length = 2
        sol, search = p.traverse(dfs)
        print(sol)
        print()
        print(search)

    def test_a_star(self):
        a_star = agents.make('a*')
        p = Puzzle('111111111')
        p.max_depth = 7
        p.max_length = 2
        sol, search = p.traverse(a_star)
        print(sol)
        print()
        print(search)

if __name__ == '__main__':
    unittest.main()
