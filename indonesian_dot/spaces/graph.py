from . import graph_metadata


class Graph(object):
    def __init__(self, **args):
        self._metadata = graph_metadata()
        self._metadata.update(args)

        self._node = self._metadata['node_struct']()
        self._edge = self._metadata['edge_struct']()
        self._node_attr_builder = self._metadata['node_attr']
        self._edge_attr_builder = self._metadata['edge_attr']

    def add_node(self, n, **attributes):
        if n not in self._node:
            self._node[n] = self._node_attr_builder()
            self._metadata['node_count'] += 1

        self._node[n].update(attributes)

    def add_nodes(self, n):
        for node in n:
            self.add_node(node)

    def remove_node(self, n):

        for i, j in self._edge.keys():
            if i == n or j == n:
                del self._edge[(i, j)]

        del self._node[n]

    def contains_node(self, n):
        return n in self._node

    def node_at(self, n):
        return self._node[n]

    def add_edge(self, e, **attributes):
        i, j = e
        if i not in self._node:
            self.add_node(i)
        if j not in self._node:
            self.add_node(j)

        if e not in self._edge:
            self._edge[e] = self._edge_attr_builder()
            self._metadata['edge_count'] += 1

        self._edge[e].update(attributes)

    def add_edges(self, e):
        for edge in e:
            self.add_edge(edge)

    def remove_edge(self, e):
        i, j = e

        del self._edge[(i, j)]
        del self._edge[(j, i)]

    def contains_edge(self, e):
        return e in self._edge

    def edge_at(self, e):
        return self._edge[e]

    def reset(self):
        self._node.clear()
        self._edge.clear()

    def copy(self):
        from copy import deepcopy
        new_copy = self.__class__()
        new_copy.add_nodes((n, deepcopy(attr)) for n, attr in self._node)
        new_copy.add_edges((e, deepcopy(attr)) for e, attr in self._edge)

    def __getattr__(self, item):
        try:
            return self._metadata[item]
        except KeyError:
            return None

    @staticmethod
    def plot(obj):
        import matplotlib.pyplot as plt
        from numpy.random import rand

        n_size = obj.__getattr__('node_count')
        nodes = list(obj.__getattr__('node_struct'))
        edges = list(obj.__getattr__('edge_struct'))
        vertices = rand(n_size, 2) * n_size ** 2
        buf_dict = {}
        ii = 0

        _, area = plt.subplots(figsize=(n_size, n_size))
        area.plot(vertices[:, 0], vertices[:, 1], 'o', color='red', markersize='12.0', alpha=0.5)

        for n in nodes:
            plt.text(vertices[ii][0], vertices[ii][1], n)
            buf_dict[n] = vertices[ii]
            ii += 1

        for (i, j) in edges:
            x = buf_dict[i]
            y = buf_dict[j]
            area.plot([x[0], y[0]], [x[1], y[1]], '--.', color='grey', lw=1, alpha=0.5)

        area.set_axis_off()
        plt.show()
