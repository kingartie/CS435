from gridgraph import GridGraph
from priorityqueue import PriorityQueue
import random

def createRandomGridGraph(n: int):
  g = GridGraph()
  all_nodes = []
  for y in range(n):
    for x in range(n):
      node = g.addGridNode(x, y, len(all_nodes))
      all_nodes.append(node)
      #since we are generating a grid going right and down, we can add neighboring nodes left and up
      
      size = len(all_nodes)-1
      #connect top neighbor with 50% chance
      if size >= n and random.random() > 0.5:
        g.addUndirectedEdge(node, all_nodes[size-n])

      #connect left neighbor with 50% chance
      if size % n > 0 and random.random() > 0.5:
        g.addUndirectedEdge(node, all_nodes[size-1])

  return g

def heuristic(a, b):
  return abs(a.x - b.x) + abs(a.y - b.y)

def astar(sourceNode, destNode):
  queue = PriorityQueue()
  queue.put(sourceNode, 0)
  previous = {sourceNode: None}
  distance = {sourceNode: 0}
  
  while not queue.empty():
    current = queue.get()
    
    if current == destNode:
      #return path src -> dest
      path = []
      n = destNode
      while n:
        path.insert(0, n)
        n = previous[n]
      return path
    
    for next in current.neighbors:
      new_cost = distance[current] + 1
      if next not in distance or new_cost < distance[next]:
        distance[next] = new_cost
        priority = new_cost + heuristic(destNode, next)
        queue.put(next, priority)
        previous[next] = current

  return None


#test methods
#Gridsize 100 has an extremely low chance of finding a path and often returns None. To see actual results, try increasing the chances for connecting edges
ran_graph = createRandomGridGraph(3)
ran_graph.printAdjacencyList()
print("A* from", ran_graph.first, "->", ran_graph.last, ":")
print(astar(ran_graph.first, ran_graph.last))
