class Node:
  def __init__(self, val):
    self.value = val
    self.neighbors = set()

  def addNeighbor(self, node):
    self.neighbors.add(node)

  def removeNeighbor(self, node):
    self.neighbors.pop(node, None)

  def __repr__(self):
    return str(self.value)

  def __lt__(self, other):
    return self.value < other.value