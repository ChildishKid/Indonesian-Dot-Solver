import numpy

import spaces
from indonesian_dot import Env

"""
An environment for simulating the Indonesian Puzzle using matrix manipulations
"""


class IndonesianEnv(Env):

    def __init__(self, init_state, action_space=None):
        self.dimension = init_state.shape[0]
        self.size = self.dimension ** 2
        self.observation_space = init_state

        self.action_space = action_space if action_space \
            else spaces.make(self.dimension)

        self.history_space = []
        self.max_depth = self.size

    """
    The environment will only accept new actions if these actions do not exceed the maximum depth value set
    when either the environment has been first solved. The maximum depth value decreases as new solutions are found
    and are better than the previous solutions.
    """

    def step(self, action):
        stop_flag = len(self.history_space) >= self.max_depth
        if stop_flag:
            return self.observation_space, self.history_space, [False, stop_flag]

        for i in range(len(self.action_space)):
            if numpy.equal(self.action_space[i], action).all():
                self.action_space.pop(i)
                break

        self.history_space.append(action)
        action = action.reshape((self.dimension, self.dimension))
        self.observation_space = numpy.add(self.observation_space, action) % 2
        solved = numpy.count_nonzero(self.observation_space) == self.size

        if solved:
            self.max_depth = len(self.history_space)

        return self.observation_space, self.history_space, [solved, not stop_flag]

    def revert(self):
        if self.history_space:
            action = self.history_space.pop()
            self.observation_space = numpy.add(self.observation_space, action) % 2
            self.action_space.append(action)

    def reset(self):
        while self.history_space:
            self.revert()

