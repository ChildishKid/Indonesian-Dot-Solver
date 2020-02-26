from . import Agent


class DFSAgent(Agent):

    def g(self, n) -> int:
        return 0

    def h(self, n) -> int:
        return 0

    def __str__(self) -> str:
        return 'dfs'
