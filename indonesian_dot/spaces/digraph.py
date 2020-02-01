from . import node_pred, node_suc, node_pred_builder, node_suc_builder, Graph


class DiGraph(Graph):

    def __init__(self, **args):
        buf = {'node_pred_builder': node_pred_builder,
               'node_suc_builder': node_suc_builder,
               'node_pred': node_pred,
               'node_suc': node_suc
               }
        buf.update(args)
        super().__init__(**buf)

        self._node_pred_builder = self._metadata['node_pred_builder']
        self._node_suc_builder = self._metadata['node_suc_builder']
        self._node_pred = self._metadata['node_pred']()
        self._node_suc = self._metadata['node_suc']()

        self._metadata['node_pred'] = self._node_pred
        self._metadata['node_suc'] = self._node_suc

        self._metadata['is_directed'] = True

    def add_node(self, n, **attributes):
        if n not in self._node:
            self._node[n] = self._node_attr_builder()
            self._node_suc[n] = self._node_suc_builder()
            self._node_pred[n] = self._node_pred_builder()
            self._metadata['node_count'] += 1

        self._node[n].update(attributes)

    def add_nodes(self, n):
        for node in n:
            self.add_node(node)

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

    def add_edges(self, e):
        for edge in e:
            self.add_edge(edge)

    def remove_edge(self, e):
        i, j = e

        del self._node_suc[i][j]
        del self._node_pred[j][i]
        del self._edge[(i, j)]
        self._metadata['edge_count'] -= 1

    def predecessors_of(self, n):

        buf = self._node_pred[n]
        buf = list(buf.keys())
        return buf

    def successors_of(self, n):

        buf = self._node_suc[n]
        buf = list(buf.keys())
        return buf

    def reset(self):
        super().reset()
        self._node_pred.clear()
        self._node_suc.clear()
