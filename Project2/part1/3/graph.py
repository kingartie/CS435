from node import Node

class Graph:
  def __init__(self):
    self.graph = set()
    self.first = None
    self.last = None

  def addNode(self, nodeVal):
    node = Node(nodeVal)
    self.graph.add(node)

    if self.first is None:
      self.first = node
    self.last = node

    return node

  def addUndirectedEdge(self, first, second):
    first.addNeighbor(second)
    second.addNeighbor(first)

  def removeUndirectedEdge(self, first, second):
    first.removeNeighbor(second)
    second.removeNeighbor(first)

  def getAllNodes(self):
    return self.graph

  def printAdjacencyList(self):
    for i in self.graph:
      print(i, i.neighbors)