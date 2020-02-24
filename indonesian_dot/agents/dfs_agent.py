from agents import Agent


class DFSAgent(Agent):
    def run(self, **kwargs) -> (str, str):
        max_d = kwargs['max_d']
        environment = kwargs['environment']

        root = environment.root_state

        search = [root]

        visited = []
        found = environment.goal_state in root
        solution = None

        while search and not found:

            current_node = search.pop(0)
            visited.append(current_node)
            previous_action = current_node.previous_action + 1

            if previous_action < len(current_node):

                for i in range(previous_action, len(current_node), 1):
                    next_node = environment.step(current_node, i)
                    found = environment.goal_state in next_node

                    if not found and next_node not in visited:
                        search.insert(0, next_node)
                    elif found:
                        visited.append(next_node)
                        solution = next_node
                        break

        if solution:
            current_node = solution
            buffer = []
            while current_node:
                buffer.append(current_node.solution_artifact())
                current_node = current_node.predecessor
            buffer.reverse()
            solution = '\n'.join(buffer)
        else:
            solution = 'no solution'

        visited = [x.search_artifact() for x in visited]
        visited = '\n'.join(visited)
        return visited, solution

    def f(self, n) -> float:
        return 0

    def g(self, n) -> float:
        return 0

    def h(self, n) -> float:
        return 0

    def __str__(self) -> str:
        return 'DFS'
