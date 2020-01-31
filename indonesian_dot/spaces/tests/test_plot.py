from spaces import DiGraph, Graph

graph = DiGraph()
graph.add_edge((1, 2))
graph.add_edge((1, 3))
graph.add_edge((3, 5))
graph.add_edge((2, 3))
graph.add_edge((2, 7))
graph.add_edge((2, 8))
graph.add_edge((2, 9))
Graph.plot(graph)
