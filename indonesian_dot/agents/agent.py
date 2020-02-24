class Agent:

    def run(self, **kwargs) -> (str, str):
        raise NotImplementedError

    def f(self, n) -> int:
        raise NotImplementedError

    def g(self, n) -> int:
        raise NotImplementedError

    def h(self, n) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    @classmethod
    def make(cls, k):
        v = None

        if k == 'dfs':
            from .dfs_agent import DFSAgent
            v = DFSAgent()
        elif k == 'bfs':
            from .bfs_agent import BFSAgent
            v = BFSAgent()
        return v
