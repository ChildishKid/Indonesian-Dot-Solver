from agents import Agent
from agents import PriorityQueue
import math
from envs import Env


class BFSAgent(Agent):
    def run(self, **kwargs) -> (list, list):
        # max_l = kwargs['max_l']
        max_l = 1000
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

                # action = queue.delete()[1][0]
                # e, sol = e.step(action)

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

    def count_overlap(self, n, substring) -> float:
        count = 0
        start = 0
        while start < len(n):
            index = n.find(substring, start)

            if index != -1:
                start = index + 1
                count += 1
            else:
                return count

    def h1(self, n) -> float:
        # Count numbers of 1
        return n.count("1")

    def h2(self, n) -> float:
        # Count numbers of pair of 1
        return n.count("11")

    def h2overlap(self, n) -> float:
        # Count numbers of pair of 1
        return self.count_overlap(n, "11")

    def h3(self, n) -> float:
        # Count numbers of three consecutive 1
        return n.count("111")

    def h3overlap(self, n) -> float:
        # Count numbers of three consecutive 1
        return self.count_overlap(n, "111")

    def haround(self, n) -> float:
        # Set reverse to False in sort (PriorityQueue)
        count = 0
        size = int(math.sqrt(len(n)))

        for i in range(len(n)):
            new_count = 0
            if n[i] == '1':
                new_count += 1
            if ((i % size) - 1) >= 0:
                if n[i - 1] == '1':
                    new_count += 1
            if ((i % size) + 1) < size:
                if n[i + 1] == '1':
                    new_count += 1
            if i - size > 0:
                if n[i - size] == '1':
                    new_count += 1
            if i + size < len(n):
                if n[i + size] == '1':
                    new_count += 1
            if new_count > count:
                count = new_count
        return count

    def hrows(self, n) -> float:
        # Set reverse to False in sort (PriorityQueue)
        count = 0
        size = math.sqrt(len(n))
        for i in range(len(n)):
            if n[i] == '1':
                return count
            elif ((i + 1) % size) == 0:
                count += 1
        return count

    def f(self, n) -> float:
        return 0

    def g(self, n) -> float:
        return 0

    def h(self, n) -> float:
        return self.haround(n)

    def __str__(self) -> str:
        return 'BFS'

