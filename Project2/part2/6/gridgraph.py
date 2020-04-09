from gridnode import GridNode

class GridGraph:
  def __init__(self):
    self.graph = set()
    self.first = None
    self.last = None

  def addGridNode(self, x, y, nodeVal):
    node = GridNode(x, y, nodeVal)
    self.graph.add(node)

    if self.first is None:
      self.first = node
    self.last = node

    return node

  def addUndirectedEdge(self, first, second):
    if first.x == second.x or first.y == second.y: #check if neighbor
      first.addNeighbor(second)
      second.addNeighbor(first)

  def removeUndirectedEdge(self, first, second):
    first.removeNeighbor(second)
    second.removeNeighbor(first)

  def getAllNodes(self):
    return self.graph

  def printAdjacencyList(self):
    sorted_set = sorted(self.graph)
    for i in sorted_set:
      print(i, i.neighbors)