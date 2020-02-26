from heapq import heappush, heappop
from logging import info
from threading import Lock

from spaces import Node

"""
Creates an environment for agents to play the game of Indonesian Dot.

----------
Parameters
----------

lock : threading.Lock
    A lock used for acquiring exclusive access to the static puzzle id variable.

puzzle_id : int
    The puzzle id of this puzzle.
    
root_state : Node
    The starting node of this puzzle, with the current state.

max_length : int
    The maximum length that each node can support (number of children per predecessor).

max_depth : int
    The maximum depth that each node is allowed (number of children from the first predecessor).
    
puzzle_size : int
    The size of this puzzle.
    Equivalent to the length of the root's state.

puzzle_length : int
    The dimension of this puzzle.
    Equivalent to length and width of a n x n square.

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
    __lock = Lock()
    __puzzle_id = 1

    def __init__(self, root_state):
        self._puzzle_id = Puzzle.__puzzle_id
        Puzzle.__puzzle_id += 1

        self._root_state = Node(root_state)
        self._max_length = self._root_state.size
        self._max_depth = self._root_state.size

    @property
    def id(self):
        return self._puzzle_id

    @property
    def root_state(self):
        return self._root_state

    @root_state.setter
    def root_state(self, new_root_state):
        info(f'Root state for puzzle #{self._puzzle_id} has been set to {new_root_state}')
        self._root_state = Node(new_root_state)

    @property
    def max_depth(self):
        return self._max_depth

    @max_depth.setter
    def max_depth(self, new_max_depth):
        info(f'Maximum depth for puzzle #{self._puzzle_id} has been set to {new_max_depth}')
        self._max_depth = new_max_depth

    @property
    def max_length(self):
        return self._max_length

    @max_length.setter
    def max_length(self, new_max_length):
        info(f'Maximum length for puzzle #{self._puzzle_id} has been set to appropriate length of {new_max_length}')
        self._max_length = new_max_length

    @property
    def goal_state(self):
        return '0' * self._root_state.size

    def traverse(self, agent):
        root = self._root_state
        size = self._root_state.size
        max_depth = self._max_depth if str(agent) == 'dfs' else 2 ** self._root_state.size
        max_length = self._max_length if not str(agent) == 'dfs' else 2 ** self._root_state.size
        goal = self.goal_state

        root.g = agent.g(root)
        root.h = agent.h(root)

        visited = []
        unvisited = []
        seen = set()

        solution = None

        if goal in root:
            solution = root
        else:
            unvisited.append(root)

        while unvisited and max_length > 0:
            max_length -= 1
            current_node = heappop(unvisited)
            seen.add(current_node)
            visited.append(current_node)

            if current_node.depth + 1 < max_depth:
                start = current_node.previous_action + 1

                for i in range(start, current_node.size, 1):
                    child = current_node.touch(i)

                    if child not in seen:
                        info(f'puzzle #{self._puzzle_id} discovered new node {str(child)} from {str(current_node)}')
                        child.g = agent.g(child)
                        child.h = agent.h(child)
                        heappush(unvisited, child)
                        seen.add(child)

                        if goal in child:
                            info(f'puzzle #{self._puzzle_id} found the goal state')
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
