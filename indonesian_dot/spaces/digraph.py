from . import node_pred, node_suc, node_pred_builder, node_suc_builder
from .graph import Graph


class DiGraph(Graph):

    def __init__(self, **args):
        buf = {'node_pred_builder': node_pred_builder,
               'node_suc_builder': node_suc_builder,
               'node_pred': node_pred(),
               'node_suc': node_suc()
               }
        buf.update(args)
        super().__init__(**buf)

        self._node_pred_builder = self._metadata.get('node_pred_builder')
        self._node_suc_builder = self._metadata.get('node_suc_builder')

        self._node_pred = self._metadata.get('node_pred')
        self._node_suc = self._metadata.get('node_suc')

        self._metadata['is_directed'] = True

    def add_node(self, n, **attributes):
        if n not in self._node:
            self._node[n] = self._node_attr_builder()
            self._node_suc[n] = self._node_suc_builder()
            self._node_pred[n] = self._node_pred_builder()
            self._metadata['node_count'] += 1

        self._node[n].update(attributes)

    def add_nodes(self, nodes_and_attributes):
        try:
            for n, attr in nodes_and_attributes:
                self.add_node(n, **attr)

        except TypeError:
            raise Warning(f"DiGraph::add_nodes(self, nodes_and_attributes)::"
                          "Type must be tuple, containing node information and attributes.")

    def remove_node(self, n):
        try:
            del self._node[n]
        except KeyError:
            raise Warning(f"DiGraph::remove_node(self, n)::Node {n} does not exist.")

        suc = self._node_suc[n]
        pred = self._node_pred[n]

        for x in suc:
            del self._node_pred[x][n]

        for x in pred:
            del self._node_pred[x][n]

        del self._node_suc[n]
        del self._node_pred[n]
        self._metadata['node_count'] -= 1

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
        self._node_suc[i][j] = self._edge[e]
        self._node_pred[j][i] = self._edge[e]

    def add_edges(self, edges_and_attributes):
        try:
            for e, attr in edges_and_attributes:
                self.add_edge(e, **attr)

        except TypeError:
            raise Warning(f"DiGraph::add_edges(self, edges_and_attributes)::"
                          "Type must be tuple, containing node information and attributes.")

    def remove_edge(self, e):
        i, j = e

        try:
            del self._node_suc[i][j]
            del self._node_pred[j][i]
            del self._edge[(i, j)]
            self._metadata['edge_count'] -= 1
        except KeyError:
            raise Warning(f"DiGraph::remove_edge(self, e)::Edge {i}-{j} does not exist.")

    def contains_edge(self, e):
        return e in self._edge

    def edge_at(self, e):
        return self._edge[e]

    def predecessors_of(self, n):
        try:
            buf = self._node_pred[n]
            buf = list(buf.keys())
            return buf
        except KeyError:
            raise Warning(f"DiGraph::predecessors_of(self, n)::Node {n} does not exist.")

    def successors_of(self, n):
        try:
            buf = self._node_suc[n]
            buf = list(buf.keys())
            return buf
        except KeyError:
            raise Warning(f"DiGraph::successors_of(self, n)::Node {n} does not exist.")

    def reset(self):
        self._node_pred.clear()
        self._node_suc.clear()
        self._node.clear()

    def copy(self):
        from copy import deepcopy
        new_copy = self.__class__()
        new_copy.add_nodes((n, deepcopy(attr)) for n, attr in self._node)
        new_copy.add_edges((e, deepcopy(attr)) for e, attr in self._edge)
<<<<<<< HEAD

=======
>>>>>>> origin
