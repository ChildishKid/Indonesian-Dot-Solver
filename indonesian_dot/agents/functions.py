"""
actions:
    A dict containing the string identifier of an action as a key followed by its equivalent list of indices represented actions.

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
graph:
    A graph object to use for the search. The graph does not need to contain existing nodes/edges


start:
    The starting string value of a node

    Example:
        186 = int('010111010', 2)
goal:
    The ending string value of a node

    Example:
        0 = int('000000000', 2)
"""
import math

from numpy.ma import array

from spaces import DiGraph, Graph

def dfs(graph, actions, start, goal, opt, depth=0):

    if start == goal:
        return 0
    elif depth > 1000 or not actions:
        return None

    graph.add_node(f'{start:{opt}}', depth=depth)
    new_depth = depth + 1

    int_result = [(k, v ^ start) for k, v in actions.items()]
    int_result = dict(int_result)
    copy_d = {}
    copy_d.update(actions)

    for k, v in int_result.items():
        graph.add_edge((f'{start:{opt}}', f'{v:{opt}}'), id=k)
        del copy_d[k]
        ans = dfs(graph, copy_d, v, goal, opt, depth=new_depth)
        # copy_d[k] = v
        if ans is not None:
            print(k, f'{v:{opt}}')
            return 0





_start =    "000110010"
_start = "111001011"
_start =    "1010000111111111"
_goal =     "0000000000000000"
size = len(_start)
dim = int(math.sqrt(size))
_actions = {}

for i in range(size):
    val = sum([2 ** (size-1-x) for x in [i - dim, i - 1 if i % dim > 0 else -1, i, i + 1 if i % dim < dim-1 else -1, i + dim] if 0 <= x < size])
    key = chr(int(i / dim) + 65) + str((i % dim) + 1)
    _actions[key] = val

_graph = DiGraph()
dfs(_graph, _actions, int(_start, 2), int(_goal, 2), '0' + str(size) + 'b')
# Graph.plot(_graph)


