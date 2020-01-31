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
    A graph object to use for the search.
    The graph does not need to contain existing nodes/edges.

start:
    The starting string value of a node

    Example:
        186 (= int('010111010', 2))
goal:
    The ending string value of a node

    Example:
        0 (= int('000000000', 2))

form:
    Used to recreate the string representation of a board state. Initially it is in int form

depth:
    The initial depth of the function represented as a tuple with minimum (inclusive) and a maximum (exclusive)
"""
from math import sqrt
from spaces import DiGraph, Graph


def dfs(graph, actions, start, goal, form, depth=(0, 10)):
    if start == goal:
        return []
    elif depth[0] > depth[1] or not actions:
        return None

    graph.add_node(f'{start:{form}}', depth=depth)
    new_depth = (depth[0] + 1, depth[1])
    int_result = dict([(k, v ^ start) for k, v in actions.items()])
    copy_d = {}
    copy_d.update(actions)

    for k, v in int_result.items():
        graph.add_edge((f'{start:{form}}', f'{v:{form}}'), id=k)
        del copy_d[k]
        ans = dfs(graph, copy_d, v, goal, form, depth=new_depth)

        if ans is not None:
            return [(k, f'{v:{form}}')] + ans


_start = "000110010"
_start = "111001011"
_start = "1010010111001010"
_goal = "0000000000000000"
size = len(_start)
dim = int(sqrt(size))
_actions = {}

for i in range(size):
    val = sum([2 ** (size - 1 - x) for x in
               [i - dim,
                i - 1 if i % dim > 0 else -1,
                i,
                i + 1 if i % dim < dim - 1 else -1,
                i + dim]
               if 0 <= x < size])
    key = chr(int(i / dim) + 65) + str((i % dim) + 1)
    _actions[key] = val

_graph = DiGraph()
_ans = dfs(_graph, _actions, int(_start, 2), int(_goal, 2), '0' + str(size) + 'b', depth=(0, 4))
print(_ans)
print(len(_ans))
Graph.plot(_graph)
