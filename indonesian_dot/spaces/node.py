from math import sqrt


class Node:
    def __init__(self, state, predecessor=None, action=None):
        self._predecessor = predecessor
        self._previous_action = action
        self._state = state
        self.g = 0
        self.h = 0

    @property
    def f(self):
        return self._g + self._h

    @property
    def g(self):
        return self._g

    @property
    def h(self):
        return self._h

    @g.setter
    def g(self, new_g):
        self._g = new_g

    @h.setter
    def h(self, new_h):
        self._h = new_h

    @property
    def predecessor(self):
        return self._predecessor

    @property
    def previous_action(self):
        if self._previous_action is None:
            return -1
        else:
            return self._previous_action

    @property
    def state(self):
        return self._state

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.f == other.f and self.g == other.g and self.h == other.h and self._state == other._state
        elif isinstance(other, str):
            return self.state == other

    def __str__(self):
        return self._state

    def __le__(self, other):
        if isinstance(other, Node):
            return self.f <= other.f and self._state <= other._state

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.f < other.f and self._state < other._state

    def __ge__(self, other):
        if isinstance(other, Node):
            return self.f >= other.f and self._state >= other._state

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.f > other.f and self._state > other._state

    def __cmp__(self, other):
        if isinstance(other, Node):
            if self.f == other.f:
                if self._state == other._state:
                    return 0
                elif self._state > other._state:
                    return 1
                else:
                    return -1
            elif self.f > other.f:
                return 1
            else:
                return -1

    def __contains__(self, item):
        if isinstance(item, str):
            return self._state == item

    def __len__(self):
        return len(self._state)

    def state_list(self, data_type=int):
        return [data_type(x) for x in self._state]

    def search_artifact(self):
        return f'{self.f} {self._g} {self._h} {self._state}'

    def solution_artifact(self):
        if self._previous_action is None:
            return f'0 {self._state}'
        else:
            length = int(sqrt(len(self._state)))
            row, column = divmod(self._previous_action, length)
            row = chr(row + ord('A'))
            column += 1
            return f'{row}{column} {self._state}'
