from weightedgraph import WeightedGraph
from priorityqueue import PriorityQueue
import random


def createRandomCompleteWeightedGraph(n: int):
  g = WeightedGraph()
  all_nodes = []
  
  #Create nodes
  for i in range(n):
    node = g.addNode(i)
    all_nodes.append(node)
  
  #Connect all nodes to each other
  for n1 in all_nodes:
    for n2 in all_nodes:
      if n1 is not n2:
        g.addWeightedEdge(n1, n2, random.randint(1, 100))
  
  return g

def createLinkedList(n: int):
  g = WeightedGraph()
  prev = None
  for i in range(n):
    n = g.addNode(i)
    if prev:
      prev.addNeighbor(n)
    prev = n
  return g
  
def dijkstras(start):
  queue = PriorityQueue()
  queue.put(start, 0)
  visited = []
  distance = {start: 0}
  previous = {start: None}
  inf = float('inf')
  
  while not queue.empty():
    u = queue.get()
    visited.append(u)

    for v in u.neighbors:
      if v not in visited:
        tempDistance = distance.get(u, inf) + u.getWeight(v)
        if tempDistance < distance.get(v, inf):
          distance[v] = tempDistance
          queue.put(v, tempDistance)
          previous[v] = u

  return distance


#test methods
ran_graph = createRandomCompleteWeightedGraph(5)
ran_graph.printAdjacencyList()
print("dijkstras from node ", ran_graph.first, ":")
print(dijkstras(ran_graph.first))

print()
link_list = createLinkedList(5)
link_list.printAdjacencyList()
print("dijkstras from node ", link_list.first, ":")
print(dijkstras(link_list.first))