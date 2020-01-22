import numpy

from .space import Space

"""
Creates a list of actions that the IndonesianEnv supports. The elements found within the list are the shapes that are
supported for each element of the board
"""


class ActionSpace(Space):

    def __init__(self, **kwargs):
        self.__action_matrix = []

        if not kwargs or 'dimension' in kwargs:
            dimension = 3 if not kwargs else kwargs.get('dimension')
            assert 3 <= dimension <= 10

            self.reset(dimension)

        elif 'space' in kwargs:
            self.__action_matrix = numpy.copy.deepcopy(kwargs.get('space'))

    def sample(self):
        return numpy.copy.deepcopy(self.__action_matrix)

    def contains(self, item):
        size = len(self.__action_matrix)
        for i in range(size):
            if numpy.equal(self.__action_matrix[i], item).all():
                return i
        return None

    def __len__(self):
        return len(self.__action_matrix)

    def step(self, action):
        index = self.contains(action)
        if 0 <= index < self.__len__():
            return self.__action_matrix.pop(index)
        return None

    def revert(self, action):
        self.__action_matrix.append(action)

    def reset(self, dimension):
        size = dimension ** 2
        for i in range(size):
            temp = numpy.zeros(size, int)
            temp[i] = 1

            if i - dimension >= 0:
                temp[i - dimension] = 1
            if i + dimension < size:
                temp[i + dimension] = 1
            if i % dimension != 0:
                temp[i - 1] = 1
            if i % dimension != dimension - 1:
                temp[i + 1] = 1

            temp = temp.reshape((dimension, dimension))
            self.__action_matrix.append(temp)