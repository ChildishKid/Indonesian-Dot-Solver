class Agent:

    def run(self, **kwargs) -> (list, list):
        raise NotImplementedError

    def f(self, n) -> float:
        raise NotImplementedError

    def g(self, n) -> float:
        raise NotImplementedError

    def h(self, n) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    @classmethod
    def make(cls, k):
        v = None

        if k == 'dfs':
            from .dfs_agent import DFSAgent
            v = DFSAgent()

        return v
