from spaces import graph_metadata


class Graph(object):
    def __init__(self, **args):
        metadata = graph_metadata()
        metadata.update(args)
        self._metadata = metadata

        self._node = metadata.get('node_struct')
        self._node_attr_builder = metadata.get('node_attr')

        self._edge = metadata.get('edge_struct')
        self._edge_attr_builder = metadata.get('edge_attr')

    def add_node(self, n):
        raise NotImplementedError

    def add_nodes(self, nodes_and_attributes):
        raise NotImplementedError

    def remove_node(self, n):
        raise NotImplementedError

    def contains_node(self, n):
        raise NotImplementedError

    def node_at(self, n):
        raise NotImplementedError

    def add_edge(self, e, **attributes):
        raise NotImplementedError

    def add_edges(self, edges_and_attributes):
        raise NotImplementedError

    def remove_edge(self, e):
        raise NotImplementedError

    def contains_edge(self, e):
        raise NotImplementedError

    def edge_at(self, e):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError

    def __getattr__(self, item):
        try:
<<<<<<< HEAD
            if type(item) is int:
                return self._node[item]
            elif type(item) is tuple:
                return self._edge[item]
            elif item in self._metadata:
                return self._metadata[item]
        except KeyError:
            pass

        return None
=======
            return self._metadata[item]
        except KeyError:
            return None
>>>>>>> origin

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
<<<<<<< HEAD
        area.plot(vertices[:, 0], vertices[:, 1], 'o', color='red', markersize='10.0', alpha=0.5)
=======
        area.plot(vertices[:, 0], vertices[:, 1], 'o', color='red', markersize='12.0', alpha=0.5)
>>>>>>> origin

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
