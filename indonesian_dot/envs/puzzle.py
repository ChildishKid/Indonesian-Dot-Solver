from numpy import sqrt

from spaces.node import Node


class Puzzle:
    def __init__(self, root_state):
        self._size = len(root_state)
        self._length = int(sqrt(self._size))
        self._root_state = Node(root_state)

    @property
    def goal_state(self):
        return '0' * self._size

    @property
    def root_state(self):
        return self._root_state

    def step(self, node: Node, action):
        new_state = node.state_list(data_type=int)

        action_row, action_column = divmod(action, self._length)

        if action_column - 1 >= 0:
            new_state[action - 1] = (new_state[action - 1] + 1) % 2

        if action_column + 1 < self._length:
            new_state[action + 1] = (new_state[action + 1] + 1) % 2

        if action_row - 1 >= 0:
            new_state[action - self._length] = (new_state[action - self._length] + 1) % 2

        if action_row + 1 < self._length:
            new_state[action + self._length] = (new_state[action + self._length] + 1) % 2

        new_state[action] = (new_state[action] + 1) % 2
        new_state = [str(x) for x in new_state]
        new_state = ''.join(new_state)

        return Node(new_state, node, action)

    def reset(self):
        self._root_state = Node(self._root_state.state)
