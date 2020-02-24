import unittest

from agents import Agent
from envs.puzzle import Puzzle


class MyTestCase(unittest.TestCase):
    def test_something(self):
        e = Puzzle("010111010")
        a = Agent.make('bfs')
        sea, sol = a.run(max_l=100, environment=e)
        print(sea)
        print()
        print(sol)


if __name__ == '__main__':
    unittest.main()
