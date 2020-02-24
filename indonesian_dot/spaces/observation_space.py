from collections import OrderedDict


def node_builder():
    return OrderedDict({
        ('depth', 0)
    })


def edge_builder():
    return OrderedDict({
        ('action', None),
        ('cost', 0),
    })


class ObservationSpace:

    def __init__(self):
        self.nodes = OrderedDict()
        self.predecessors = OrderedDict()
        self.successors = OrderedDict()
        self.node_builder = node_builder
        self.edge_builder = edge_builder

    def add_node(self, node, **attributes):
        if node not in self.nodes:
            self.nodes[node] = self.node_builder()
            self.predecessors[node] = OrderedDict()
            self.successors[node] = OrderedDict()

        self.nodes[node].update(attributes)

    def add_edge(self, first_node, second_node, **attributes):
        if first_node not in self.nodes:
            self.add_node(first_node)
        if second_node not in self.nodes:
            self.add_node(second_node)

        edge_attributes = self.edge_builder()
        edge_attributes.update(attributes)

        self.predecessors[second_node][first_node] = self.successors[first_node][second_node] = edge_attributes

    def contains_node(self, node):
        return self.nodes.get(node, False) and True

    def contains_edge(self, first_node, second_node):
        return self.successors.get(first_node, False) \
               and self.successors[first_node].get(second_node, False) \
               and True

    def get_node(self, node):
        if node not in self.nodes[node]:
            return None

        return self.nodes[node], self.predecessors[node], self.successors[node]

    def node_view(self, node):
        if node not in self.nodes[node]:
            return None

        class NodeView:
            def __init__(self):
                pass

            def


    def reset(self):
        self.nodes.clear()
        self.predecessors.clear()
        self.successors.clear()
