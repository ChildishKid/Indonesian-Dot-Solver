import unittest
from spaces import DiGraph, Graph, graph_metadata

g = graph_metadata()
graph = DiGraph(**g)


class MyTestCase(unittest.TestCase):

    def test_put_node(self):
        graph.put_node(1)
        graph.put_node(2, depth=1)
        assert graph.exists_node(1) and graph.exists_node(2) and graph.node(2)['depth'] == 1

    def test_del_node(self):
        graph.put_node(1)
        graph.del_node(1)
        assert not graph.exists_node(1)

    def test_put_edge(self):
        graph.put_edge(1, 2)
        assert graph.exists_edge(1, 2) and not graph.exists_edge(2, 1)

    def test_edge(self):
        graph.put_edge(1, 2)
        p, s = graph.edge(1)
        assert len(p) == 0 and s[2]

    def test_del_edge(self):
        graph.put_edge(1, 2)
        graph.del_edge(1, 2)
        assert not graph.exists_edge(1, 2)

    def test_reset(self):
        graph.put_node(1)
        graph.put_node(2, depth=1)
        graph.put_edge(1, 2)
        graph.reset()
        assert not graph.exists_node(1) and not graph.exists_edge(1, 2) and not graph.exists_node(2)


if __name__ == '__main__':
    unittest.main()
