import unittest

from agents.agent import Agent
from envs.env import Env


class MyTestCase(unittest.TestCase):
    def test_something(self):
        e = Env.make('puzzle', state="1010010111001010", size=4)
        a = Agent.make('dfs')
        sea, sol = a.run(max_d=10, environment=e)
        print(sea)
        print()
        print(sol)


if __name__ == '__main__':
    unittest.main()
