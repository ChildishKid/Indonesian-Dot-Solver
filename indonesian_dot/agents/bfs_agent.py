from agents import Agent
from agents import PriorityQueue
from envs import Env

class BFSAgent(Agent):
    def run(self, **kwargs) -> (list, list):
        max_l = kwargs['max_l']
        environment = kwargs['environment']

        if environment.solved():
            return [f'0 {environment.state}'], [f'0 0 0 {environment.state}']

        solution = []
        search = []
        visited = []
        queue = PriorityQueue()


        def bfs(e):
            # queue.insert (self.h(s), s)
            while True:
                s, act = e.sample()
                search.append(f'{self.f(s)} {self.g(s)} {self.h(s)} {s}')
                visited.append(s)

                for k in act:
                    n_e, sol = e.step(k)
                    n_st = n_e.state
                    if n_st in visited:
                        continue

                    if sol:
                        print('It got solved!')
                        search.append(f'{self.f(s)} {self.g(s)} {self.h(s)} {s}')
                        return

                    queue.insert(self.h(n_st), (k, n_st))

                if len(queue) == 0:
                    break

                if len(search) == max_l:
                    return False

                #action = queue.delete()[1][0]
                #e, sol = e.step(action)

                next_state = queue.delete()[1][1]
                kwargs['state'] = next_state
                e = Env.make('puzzle', **kwargs)


        bfs(environment)

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
        return n.count("1")

    def __str__(self) -> str:
        return 'BFS'
