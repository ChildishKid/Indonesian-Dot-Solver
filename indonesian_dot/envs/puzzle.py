from math import sqrt

from spaces import DiGraph


class Puzzle(object):

    def __init__(self, init_state=None, final_state=None, **args):
        encoded = int(init_state, 2)
        self._init_state = encoded
        self._current_state = encoded
        self._final_state = int(final_state, 2)
        self._size = len(init_state)
        self._act_space = self.__act_space()

        self._obs_space = DiGraph(**args)
        self._obs_space.add_node(self._current_state, depth=0, value=init_state)
        self._obs_space.add_node(self._final_state, depth=float('inf'), value=final_state)

    def step(self, action=None):
        v = None if not action else self._act_space[action]
        new_depth = self._obs_space.node_at(self._current_state)['depth'] + 1
        a = [(k, self._current_state ^ o) for k, o in self._act_space.items()]
        a = dict(sorted(a, key=lambda x: x[1]))

        if v is not None:
            for k, o in a.items():
                opt = '0' + str(self._size) + 'b'
                self._obs_space.add_node(o, depth=new_depth, value=f'{o:{opt}}')
                self._obs_space.add_edge((self._current_state, o))

            self._current_state = a[action]
            del self._act_space[action]
            del a[action]

        return list(a.keys()), self._current_state == self._final_state

    def actions(self):
        return list(self._act_space.values())

    def reset(self):
        self._current_state = self._init_state
        self._obs_space.reset()

    def __act_space(self):
        dim = int(sqrt(self._size))
        actions = {}
        for i in range(self._size):
            val = sum([2 ** (self._size - 1 - x) for x in
                       [i - dim,
                        i - 1 if i % dim > 0 else -1,
                        i,
                        i + 1 if i % dim < dim - 1 else -1,
                        i + dim]
                       if 0 <= x < self._size])
            key = chr(int(i / dim) + 65) + str((i % dim) + 1)
            actions[key] = val
        return actions
