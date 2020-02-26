from . import Agent


class AStarAgent(Agent):
    def g(self, n) -> int:
        return 1

    def h(self, n) -> int:
        x = n.state.count('1')
        count = 0

        if not (0 < x % 5 < 3):
            count += x // 5
            x = x % 5

        if not (0 < x % 4 < 3):
            count += x // 4
            x = x % 4

        count += x // 3
        x = x % 3
        count += x
        return count

    def __str__(self) -> str:
        return 'astar'
