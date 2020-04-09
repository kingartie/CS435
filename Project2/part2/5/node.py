class Node:
  def __init__(self, val):
    self.value = val
    self.neighbors = {}

  def addNeighbor(self, node, edgeWeight=1):
    self.neighbors[node] = edgeWeight

  def removeNeighbor(self, node):
    self.neighbors.pop(node, None)

  def getWeight(self, node):
    return self.neighbors[node]
    
  def __repr__(self):
    return str(self.value)

  def __lt__(self, other):
    return self.value < other.value