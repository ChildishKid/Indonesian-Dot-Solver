import math

import numpy

from .space import Space


class ObservationSpace(Space):
    def __init__(self, **kwargs):
        if 'state' in kwargs:
            state = kwargs.get('state')
            dimension = int(math.sqrt(len(state)))
            assert state
            assert dimension ** 2 == len(state)

            lst = list(state)
            lst = numpy.array(lst, int)
            self.__state = lst.reshape((dimension, dimension))

        elif 'obj' in kwargs:
            obj = kwargs.get('obj')
            assert obj and isinstance(obj, ObservationSpace)

            self.__state = numpy.copy.deepcopy(obj.__state)

        else:
            lst = numpy.ones(9)
            self.__state = lst.reshape((3, 3))

    def sample(self):
        return self.__state

    def contains(self, item):
        if item == 0 or item == 1:
            temp = self.__state.flatten()
            return item in temp
        return None

    def __len__(self):
        return self.__state.shape[0]

    def step(self, action):
        self.__state = numpy.add(self.__state, action) % 2

    def revert(self, action):
        self.step(action)

    def reset(self):
        raise NotImplementedError
