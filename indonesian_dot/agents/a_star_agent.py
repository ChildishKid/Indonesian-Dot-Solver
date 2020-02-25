from . import Agent


class AStarAgent(Agent):

    def g(self, n) -> int:
        return n.depth

    def h(self, n) -> int:
        return n.state.count('1')

    def __str__(self) -> str:
        return 'a*'
