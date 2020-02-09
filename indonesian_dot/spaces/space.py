"""
The function returns a dictionary containing the key of the action and it's corresponding integer value.

Example:
    {'A1': 832, (where 832 is 110100000 in binary)
    'A2': 928,
    'A3': 464,
    'B1': 744,
    'B2': 372,
    'B3': 186,
    'C1': 92,
    'C2': 46,
    'C3': 22}
"""


def sample(dim: int):
    size = dim ** 2
    actions = {}

    for i in range(size):
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


"""
step function takes a state, and a sample dictionary of actions with their associated numerical values.
 
It outputs the result of applying xor on the state with every action

"""


def step(state: str, samples: dict):
    # the form defines the presentation of the string when converted from int to str
    form = '0' + str(len(state)) + 'b'

    # the state is converted to an int var
    i = int(state, 2)

    # the state var is xored with every value of the actions and stored as a list
    results = [(k, f'{v ^ i:{form}}') for k, v in samples.items()]

    # the list is converted back into a dictionary containing the action applied to state and the value result
    results = dict(sorted(results, key=lambda x: x[1]))
    return results
