from agents import Agent


class DFSAgent(Agent):
    def run(self, **kwargs) -> (list, list):
        max_d = kwargs['max_d']
        environment = kwargs['environment']

        if environment.solved():
            return [f'0 {environment.state}'], [f'0 0 0 {environment.state}']

        solution = []
        search = []
        visited = []

        def dfs(e, depth=0):
            s, act = e.sample()
            search.append(f'{self.f(s)} {self.g(s)} {self.h(s)} {s}')
            visited.append(s)
            for k in act:

                n_e, sol = e.step(k)
                n_st = n_e.state
                if not sol and depth > max_d - 1 or n_st in visited:
                    continue

                if sol or dfs(n_e, depth=depth + 1):
                    solution.append(f'{k} {n_st}')
                    return True

        dfs(environment)

        st = ''.join(['0'] * len(environment.state))
        search.append(f"{self.f(st)} {self.g(st)} {self.h(st)} {st}")

        if solution:
            solution.append(f'0 {environment.state}')
            solution.reverse()
        else:
            solution = ['no solution']
        return solution, search

    def f(self, n) -> float:
        return 0

    def g(self, n) -> float:
        return 0

    def h(self, n) -> float:
        return 0

    def __str__(self) -> str:
        return 'DFS'
