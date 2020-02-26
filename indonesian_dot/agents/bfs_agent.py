from math import floor

from . import Agent


class BFSAgent(Agent):

    def g(self, n) -> int:
        return 0

    def h(self, n) -> int:
        x = n.state.count('1')
        # https://www.wolframalpha.com/input/?i=exponential+fit+%7B%7B0%2C+0%7D%2C+%7B9%2C+5%7D%2C+%7B16%2C+4%7D%2C+%7B25%2C+15%7D%2C+%7B36%2C+28%7D%7D
        return floor(0.22835 + 0.0993001 * x + 0.0161855 * x ** 2)

    def __str__(self) -> str:
        return 'bfs'
