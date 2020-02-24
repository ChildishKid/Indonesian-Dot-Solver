from numpy import array, sqrt

from spaces.action_space import ActionSpace
from spaces.observation_space import ObservationSpace


class Puzzle:

    def __init__(self, root_state):
        self._size = len(root_state)
        self._length = int(sqrt(self._size))
        self._goal_state = '0' * self._size
        self._root_state = root_state

        self._observation_space = ObservationSpace()
        self._action_space = ActionSpace()

        self._solved = self._root_state == self._goal_state

    def step(self, state, action):
        if self._solved:
            return self._goal_state, True

        transposed_state = list(state)
        row, column = divmod(action, self._length)

        transposed_state = array(transposed_state, dtype=int)
        transposed_state = transposed_state.reshape((self._length, self._length))

        if row - 1 >= 0:
            transposed_state[row - 1, column] = (transposed_state[row - 1, column] + 1) % 2
        if row + 1 < self._size:
            transposed_state[row + 1, column] = (transposed_state[row + 1, column] + 1) % 2
        if column - 1 >= 0:
            transposed_state[row, column - 1] = (transposed_state[row, column - 1] + 1) % 2
        if column + 1 < self._size:
            transposed_state[row, column + 1] = (transposed_state[row, column + 1] + 1) % 2
        transposed_state[row, column] = (transposed_state[row, column] + 1) % 2

        transposed_state = transposed_state.reshape(self._size)
        transposed_state = transposed_state.astype(dtype=str)
        transposed_state = ''.join(transposed_state)

        self._observation_space.add_edge(state, transposed_state, action=action, cost=1)
        self._solved = transposed_state == self._goal_state

        return self._observation_space, transposed_state, self._solved

    def update(self, state, depth, predicted_rem_depth):
        if self._observation_space.contains_node(state):
            self._observation_space.add_node(state,
                                             f_value=predicted_rem_depth + depth,
                                             depth=depth,
                                             h_value=predicted_rem_depth)

    def __contains__(self, item):
        return self._observation_space.contains_node(item)

    def run(self, agent):
        actions = tuple(self._action_space.actions)
        start = self._root_state
        puzzle = self
        observation = self._observation_space
        agent.run(puzzle, observation, start, actions)

    def reset(self):
        self._observation_space.reset()
        self._solved = self._root_state == self._goal_state
        self._observation_space.add_node(self._root_state)
