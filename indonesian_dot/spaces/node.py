from math import sqrt

"""
Creates a node, forming the basis of a graph or tree.

----------
Parameters
----------

state : str
    The state of this node as a string. 

predecessor : Node
    A predecessor of this node.

previous_action : int
    An action that resulted from the creation of this node from the predecessor node. 
    The range is [0, len(state) - 1].

g : int
    The cost from the predecessor node to this node.

h : int
    The estimated cost from this node to the goal node.

f : int
    The estimated cost from the predecessor node to the goal node.

depth : int
    The depth of this node. 
    This parameter is not enforced.
    Note: predecessor's depth + 1 = this node's depth
    
-------
Methods
-------

__eq__(other) -> {None, True, False}
    returns True iff the other object is an instance of a Node, and they have the same f, g, h and state parameters 

__str__() -> str
    return the state of the node.
    
__le__(other) -> {None, True, False}
    return True iff the function and the state of this object are less than or equal to the other object's.
    
__lt__(other) -> {None, True, False}
    return True iff the function and the state of this object are less than the other object's.

__ge__(other) -> {None, True, False}
     return True iff the function and the state of this object are greater than or equal to the other object's.
     
__gt__(other) -> {None, True, False}
    return True iff the function and the state of this object are greater than the other object's.
    
__cmp__(other) -> {None, -1, 0, 1}
    returns -1 if the function and the state of this object is less than the other.
    0 if it's equal to the other object's.
    1 if it's greater than the other object's.
    None if that object is not of type Node.
    
__contains__(item) -> {None, True, False}
    return True if the item state is contained in this object.

__len__() -> int
    return the length of the state this node is wrapped around.
    
search_artifact() -> str
    return the string representation of a search artifact.
    Example: 0 0 0 010111010

solution_artifact() -> str
    return the string representation of a solution artifact.
    Example: B2 000000000
    
"""


class Node:
    def __init__(self, state, predecessor=None, action=None):
        self._predecessor = predecessor
        self._previous_action = action
        self._state = state
        self.g = 0
        self.h = 0
        self._depth = 0 if not predecessor else predecessor.depth + 1

    @property
    def length(self):
        return int(sqrt(len(self._state)))

    @property
    def width(self):
        return self.length

    @property
    def size(self):
        return len(self._state)

    @property
    def depth(self):
        return self._depth

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
            return self.f == other.f and self._state == other._state

    def __str__(self):
        return self._state

    def __le__(self, other):
        if isinstance(other, Node):
            return self.f <= other.f and self._state <= other._state

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.f < other.f or (self.f == self.f and self._state < other._state)

    def __ge__(self, other):
        if isinstance(other, Node):
            return self.f >= other.f and self._state >= other._state

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.f > other.f or (self.f == self.f and self._state > other._state)

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
        return self.length

    def __iter__(self):
        for x in self._state:
            yield int(x)

    def __hash__(self):
        return hash(self._state)

    def touch(self, action):
        if not (0 <= action < self.size):
            raise ValueError
        new_state = list(self)
        length = self.length

        action_row, action_column = divmod(action, length)

        if action_column - 1 >= 0:
            new_state[action - 1] = (new_state[action - 1] + 1) % 2

        if action_column + 1 < length:
            new_state[action + 1] = (new_state[action + 1] + 1) % 2

        if action_row - 1 >= 0:
            new_state[action - length] = (new_state[action - length] + 1) % 2

        if action_row + 1 < length:
            new_state[action + length] = (new_state[action + length] + 1) % 2

        new_state[action] = (new_state[action] + 1) % 2
        new_state = [str(x) for x in new_state]
        new_state = ''.join(new_state)

        return Node(new_state, self, action)

    def search_artifact(self):
        return f'{self.f} {self._g} {self._h} {self._state}'

    def solution_artifact(self):
        if self._previous_action is None:
            return f'0 {self._state}'
        else:
            length = self.length
            row, column = divmod(self._previous_action, length)
            row = chr(row + ord('A'))
            column += 1
            return f'{row}{column} {self._state}'
