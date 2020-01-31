import numpy

from spaces import DiGraph, Graph

graph = DiGraph()
for i in range(50):
    x = int(numpy.random.rand() * 50)
    y = int(numpy.random.rand() * 50)
    graph.add_edge((x, y))
Graph.plot(graph)
