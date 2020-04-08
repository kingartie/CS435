class Node:
  def __init__(self, val):
    self.value = val
    self.neighbors = set()

  def addNeighbor(self, node):
    self.neighbors.add(node)

  def removeNeighbor(self, node):
    self.neighbors.remove(node)

  def __repr__(self):
    return str(self.value)