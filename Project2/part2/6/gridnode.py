class GridNode:
  def __init__(self, x, y, val):
    self.value = val
    self.x = x
    self.y = y
    self.neighbors = set()

  def addNeighbor(self, node):
    if len(self.neighbors) < 4:
        self.neighbors.add(node)

  def removeNeighbor(self, node):
    self.neighbors.pop(node, None)

  def __repr__(self):
    return str((self.x, self.y))

  def __lt__(self, other):
    return self.value < other.value