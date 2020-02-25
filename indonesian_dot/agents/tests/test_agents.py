import unittest

import agents


class MyTestCase(unittest.TestCase):
    def test_dfs(self):
        dfs = agents.make('dfs')
        assert str(dfs) == 'dfs'

    def test_bfs(self):
        bfs = agents.make('bfs')
        assert str(bfs) == 'bfs'

    def test_a_star(self):
        a_star = agents.make('a*')
        assert str(a_star) == 'a*'

if __name__ == '__main__':
    unittest.main()
