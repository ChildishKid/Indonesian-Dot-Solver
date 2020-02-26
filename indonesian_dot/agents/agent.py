class Agent:
    def g(self, n) -> int:
        raise NotImplementedError

    def h(self, n) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        return 'agent'
