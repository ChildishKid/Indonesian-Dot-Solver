import numpy

from indonesian_dot import Env


class IndonesianEnv(Env):

    def __init__(self, init_state):
        self.dimension = init_state.shape[0]
        self.size = self.dimension ** 2
        self.observation_space = init_state
        self.action_space = self.__make_action_space()
        self.history_space = []
        self.max_depth = self.size

    def step(self, action):
        assert action in self.action_space

        stop_flag = len(self.history_space) >= self.max_depth
        if stop_flag:
            return self.observation_space, self.history_space, False, stop_flag

        self.action_space.remove(action)
        self.history_space.append(action)
        self.observation_space = numpy.add(self.observation_space, action) % 2
        solved = numpy.count_nonzero(self.observation_space) == self.size
        if solved:
            self.max_depth = len(self.history_space)

        return self.observation_space, self.history_space, solved, True

    def revert(self):
        if self.history_space:
            action = self.history_space.pop()
            self.observation_space = numpy.add(self.observation_space, action) % 2
            self.action_space.append(action)

    def reset(self):
        while self.history_space:
            self.revert()

    def __make_action_space(self):
        buffer = []

        for i in range(self.size):
            temp = numpy.zeros(self.size, int)
            temp[i] = 1

            if i - self.dimension >= 0:
                temp[i - self.dimension] = 1
            if i + self.dimension < self.dimension:
                temp[i + self.dimension] = 1
            if i % self.dimension != 0:
                temp[i - 1] = 1
            if i % self.dimension != self.dimension - 1:
                temp[i + 1] = 1

            buffer.append(temp.reshape(self.dimension, self.dimension))

        return buffer
