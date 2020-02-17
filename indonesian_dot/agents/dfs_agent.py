from logging import info

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

        def dfs(e, depth=1):
            s, act = e.sample()
            search.append(f'{self.f(s)} {self.g(s)} {self.h(s)} {s}')
            visited.append(s)
            for k in act:

                n_e, sol = e.step(k)
                n_st = n_e.state
                if not sol and depth >= max_d or n_st in visited:
                    continue

                if sol or dfs(n_e, depth=depth + 1):
                    solution.append(f'{k} {n_st}')
                    return True

        new_environment = environment.copy()
        copy_depth = max_d

        for i in range(2, copy_depth + 1, 1):
            info(f"Agent dfs is running {new_environment.state} at max_depth of {i}")
            max_d = i
            dfs(new_environment)

            if not solution:
                new_environment = environment.copy()
                visited = []
                continue
            else:
                break

        st = ''.join(['0'] * len(new_environment.state))
        search.append(f"{self.f(st)} {self.g(st)} {self.h(st)} {st}")

        if solution:
            solution.append(f'0 {new_environment.state}')
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
