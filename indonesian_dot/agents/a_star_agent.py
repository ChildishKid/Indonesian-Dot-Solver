from . import Agent


class AStarAgent(Agent):

    def g(self, n) -> int:
        return n.count('1')

    def h(self, n) -> int:
        return n.count('1')

    def __str__(self) -> str:
        return 'a*'
