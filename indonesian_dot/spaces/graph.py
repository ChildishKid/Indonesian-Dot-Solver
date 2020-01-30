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

    def add_edge(self, e, **attributes):
        raise NotImplementedError

    def add_edges(self, edges_and_attributes):
        raise NotImplementedError

    def remove_edge(self, e):
        raise NotImplementedError

    def contains_node(self, n):
        raise NotImplementedError

    def contains_edge(self, e):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError
