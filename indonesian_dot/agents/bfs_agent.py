from . import Agent


class BFSAgent(Agent):

    def g(self, n) -> int:
        return n.count('1')

    def h(self, n) -> int:
        return 0

    def __str__(self) -> str:
        return 'bfs'
