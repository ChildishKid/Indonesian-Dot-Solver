import math

from agents import Agent


class BFSAgent(Agent):
    def run(self, **kwargs) -> (list, list):
        # max_l = kwargs['max_l']
        max_l = 1000
        environment = kwargs['environment']

        solution = None
        root = environment.root_state
        root.g = root.state.count('1')

        visited = [root]
        search = [root]

        while search:
            current_node = search.pop(0)

            if environment.goal_state == current_node:
                solution = current_node
                break

            for i in range(current_node.previous_action + 1, len(current_node), 1):
                child = environment.step(current_node, i)
                if child not in visited:
                    child.g = child.state.count('1')
                    search.append(child)
                    visited.append(child)
                    if environment.goal_state == child:
                        break

            search.sort()

        if not solution:
            solution = 'no solution'
        else:
            buffer = []
            current_node = solution
            while current_node:
                buffer.append(current_node.solution_artifact())
                current_node = current_node.predecessor

            buffer.reverse()
            solution = '\n'.join(buffer)

        visited = [x.search_artifact() for x in visited]

        return solution, visited

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
