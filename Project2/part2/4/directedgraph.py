from node import Node

class DirectedGraph:
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

	def addDirectedEdge(self, first, second):
		first.addNeighbor(second)

	def removeDirectedEdge(self, first, second):
		first.removeNeighbor(second)

	def getAllNodes(self):
		return self.graph

	def printAdjacencyList(self):
		sorted_set = sorted(self.graph)
		for i in sorted_set:
			print(i, i.neighbors)