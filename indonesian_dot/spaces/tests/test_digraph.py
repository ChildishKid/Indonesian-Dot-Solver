from spaces import DiGraph

graph = DiGraph()


def create_node_with_no_attributes():
    graph.add_node(1)
    n_s = graph.__getattr__(1)
    assert all(y is None for y in n_s.values())


def create_node_with_some_attributes():
    graph.add_node(2, degree=3, depth=2)
    n_s = graph.__getattr__(2)
    assert n_s['degree'] == 3 and n_s['depth'] == 2


def create_nodes():
    nodes = [(3, {'depth': 2}), (4, {'degree': 4}), (5, {})]

    graph.add_nodes(nodes)

    n_s = graph.__getattr__(3)
    nn_s = graph.__getattr__(4)
    nnn_s = graph.__getattr__(5)

    assert n_s['depth'] == 2 and n_s['degree'] is None \
           and nn_s['degree'] == 4 and nn_s['depth'] is None \
           and all(y is None for y in nnn_s.values())


def remove_node():
    n_s = list(graph.__getattr__('node_struct'))
    assert len(n_s) > 0
    n_s = n_s[0]
    graph.remove_node(n_s)
    assert not graph.contains_node(n_s)


def add_edge_with_no_attributes():
    graph.add_edge((1, 2))
    assert graph.contains_edge((1, 2))


def add_edge_with_attributes():
    graph.add_edges([((1, 2), {'weight': 1}), ((2, 3), {'action': 'B1'})])
    assert graph.contains_edge((1, 2)) and graph.contains_edge((2, 3))
    n_s = graph.__getattr__((1, 2))
    nn_s = graph.__getattr__((2, 3))
    assert n_s['action'] is None and n_s['weight'] == 1 \
           and nn_s['action'] == 'B1' and nn_s['weight'] is None


def remove_edge():
    graph.add_edge((3, 4))
    graph.remove_edge((3, 4))
    assert not graph.contains_edge((3, 4))


def node_count():
    count = graph.__getattr__('node_count')
    assert count == len(graph.__getattr__('node_struct'))


def edge_count():
    count = graph.__getattr__('edge_count')
    assert count == len(graph.__getattr__('edge_struct'))


def contains_node():
    graph.add_node(100)
    assert graph.contains_node(100)


def contains_edge():
    graph.add_edge((5, 8))
    assert graph.contains_edge((5, 8))


def predecessors_of():
    graph.add_edge((203, 202))
    graph.add_edge((204, 202))
    graph.add_edge((205, 202))
    # for sanity checking
    graph.remove_edge((205, 202))
    assert graph.predecessors_of(202) == [203, 204]


def sucessors_of():
    graph.add_edge((102, 103))
    graph.add_edge((102, 105))
    graph.add_edge((102, 106))
    # for sanity checking
    graph.remove_edge((102, 106))
    assert graph.successors_of(102) == [103, 105]


def print_metadata_of(query):
    assert type(query) is str
    print(graph.__getattr__(query))


create_node_with_no_attributes()
create_node_with_some_attributes()
create_nodes()
remove_node()
add_edge_with_no_attributes()
add_edge_with_attributes()
remove_edge()
node_count()
edge_count()
contains_node()
contains_edge()
predecessors_of()
sucessors_of()

"""
# Misc calls
print_metadata_of('node_struct')
print_metadata_of('edge_struct')
print_metadata_of('node_pred')
print_metadata_of('node_suc')
"""
