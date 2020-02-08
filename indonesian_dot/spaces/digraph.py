from . import Graph, edge_attr


class DiGraph(Graph):

    def __init__(self, **args):
        super().__init__(**args)
        self.metadata['is_directed'] = True

        self._node_pred = {}
        self._node_suc = {}

    def put_node(self, n, **attributes):
        if n not in self._node:
            self._node[n] = {}
            self._node_suc[n] = {}
            self._node_pred[n] = {}

        self._node[n].update(attributes)

    def put_edge(self, n, nn, **attributes):
        if n not in self._node:
            self.put_node(n)
        if nn not in self._node:
            self.put_node(nn)

        if len(self._node_pred[nn]) == 1:
            raise AttributeError(f'Adding {n}-{nn} may cause a cycle')

        self._node[nn]['depth'] = self._node[n]['depth'] + 1

        data = self._node_suc[n].get(nn, edge_attr())
        self._node_suc[n][nn] = self._node_pred[nn][n] = data
        data.update(**attributes)

    def edge(self, n):
        try:
            return self._node_pred[n], self._node_suc[n]
        except KeyError:
            return None

    def exists_edge(self, n, nn):
        try:
            return self._node_pred[nn][n] is not None and self._node_suc[n][nn] is not None
        except KeyError:
            return False

    def reset(self):
        super().reset()
        self._node_pred.clear()
        self._node_suc.clear()
