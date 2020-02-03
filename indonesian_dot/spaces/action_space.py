from math import sqrt

"""
The function returns a dictionary containing the key of the action and it's corresponding integer value.

Example:
    {'A1': 832,
    'A2': 928,
    'A3': 464,
    'B1': 744,
    'B2': 372,
    'B3': 186,
    'C1': 92,
    'C2': 46,
    'C3': 22}
"""


def action_space(size: int, start: int = 0):
    dim = int(sqrt(size))
    actions = {}

    for i in range(start, size):
        val = sum([2 ** (size - 1 - x) for x in
                   [i - dim,
                    i - 1 if i % dim > 0 else -1,
                    i,
                    i + 1 if i % dim < dim - 1 else -1,
                    i + dim]
                   if 0 <= x < size])
        key = chr(int(i / dim) + 65) + str((i % dim) + 1)
        actions[key] = val

    return actions
