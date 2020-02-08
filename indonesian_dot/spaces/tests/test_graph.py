import unittest

from spaces import Graph, graph_metadata

graph = Graph(**graph_metadata())

class MyTestCase(unittest.TestCase):

    def test_create_node(self):
        graph.put_node(2)
        assert graph.exists_node(2)

    def test_create_edge(self):
        graph.put_edge(1, 2, action='A1')
        assert graph.exists_edge(1, 2) and graph.exists_edge(2, 1)

    def test_delete_edge(self):
        self.test_create_edge()
        graph.del_edge(1, 2)
        assert not graph.exists_edge(1, 2)


if __name__ == '__main__':
    unittest.main()
