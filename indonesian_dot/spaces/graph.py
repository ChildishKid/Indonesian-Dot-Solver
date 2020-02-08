"""
Configuration of vanilla data structure provision through builder functions.

These functions may be implemented outside of the Graph class, and the Graph classes will manipulate or react to
the data within them
"""


def graph_metadata():
    return {
        'max_depth': None,
        'max_length': None,
    }


def node_attr():
    return {
        'depth': float('inf')
    }


def edge_attr():
    return {
        'label': None,
        'cost': None
    }


class Graph(object):
    def __init__(self, **args):
        self.metadata = args
        self._node = {}
        self._edge = {}

    def put_node(self, n, **attributes):
        if n not in self._node:
            self._node[n] = node_attr()
            self._edge[n] = {}

        self._node[n].update(attributes)

    def node(self, n):
        return self._node.get(n, None)

    def exists_node(self, n):
        return n in self._node

    def put_edge(self, n, nn, **attributes):
        if n not in self._node:
            self.put_node(n)
        if nn not in self._node:
            self.put_node(nn)

        data = self._edge[n].get(nn, edge_attr())
        self._edge[nn][n] = self._edge[n][nn] = data
        data.update(**attributes)

    def edge(self, n):
        return self._edge.get(n, None)

    def exists_edge(self, n, nn):
        return self._edge.get(n, None) is not None and self._edge[n].get(nn, None) is not None

    def reset(self):
        self._node.clear()
        self._edge.clear()
