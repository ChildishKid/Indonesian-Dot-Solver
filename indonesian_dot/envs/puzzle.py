from heapq import heappush, heappop

from spaces import Node

"""
Creates an environment for agents to play the game of Indonesian Dot.

----------
Parameters
----------

puzzle_id : int
    The puzzle id of this puzzle.
    
root_state : Node
    The starting node of this puzzle, with the current state.

max_length : int
    The maximum length that each node can support (number of children per predecessor).

max_depth : int
    The maximum depth that each node is allowed (number of children from the first predecessor).
    
goal_state : str
    The goal to achieve for this puzzle to be complete.

-------
Methods
-------

step(node : Node, action: int) -> Node
    returns a new node after performing an action on a current node and acquiring a new state.
    Each node represents a state of the puzzle.
    Action must be in range of [0, puzzle_size - 1 ].
    Node must exist.
    
traverse(agent : str) -> solution : str, search : str
    returns the solution and search paths of an agent after completing it's traversal.
    Node creation is performed dynamically; New nodes are added as the agent discovers new states. 

reset() -> None
    resets the puzzle.
"""


class Puzzle:
    __puzzle_id = 0

    def __init__(self, root_state, max_depth=0, max_length=0):
        self._puzzle_id = Puzzle.__puzzle_id
        Puzzle.__puzzle_id += 1

        self.root_state = root_state
        self.max_length = max_length
        self.max_depth = max_depth
        
    @property
    def id(self):
        return self._puzzle_id

    @property
    def root_state(self):
        return self._root_state

    @root_state.setter
    def root_state(self, new_root_state):
        self._root_state = Node(new_root_state)

    @property
    def goal_state(self):
        return '0' * self._root_state.size

    def traverse(self, agent):
        root = self._root_state
        size = self._root_state.size

        if str(agent) == 'dfs':
            max_depth = self.max_depth
            max_length = 2 ** 100

            def lt(orig, other):
                return orig.depth > other.depth or (orig.depth == other.depth and orig.state < other.state)

            Node.__lt__ = lt
        else:
            max_depth = 2 ** 100
            max_length = self.max_length

        goal = self.goal_state
        root.g = agent.g(root)
        root.h = agent.h(root)

        visited = []
        unvisited = []

        solution = None

        if goal in root:
            solution = root
        else:
            unvisited.append(root)

        while unvisited and max_length > 0:
            max_length -= 1
            current_node = heappop(unvisited)
            visited.append(current_node)

            if current_node.depth + 1 < max_depth:
                start = current_node.previous_action + 1

                for i in range(start, size, 1):
                    child = current_node.touch(i)
                    child.g = agent.g(child)
                    child.h = agent.h(child)

                    heappush(unvisited, child)

                    if goal in child:
                        visited.append(child)
                        solution = child
                        unvisited.clear()
                        break

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
        visited = '\n'.join(visited)

        return solution, visited

    def reset(self):
        self._root_state = Node(self._root_state.state)
