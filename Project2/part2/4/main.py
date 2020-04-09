from directedgraph import DirectedGraph
from topsort import TopSort
import random

def createRandomDAGIter(n: int):
  g = DirectedGraph()

  #Create nodes
  for i in range(n):
    g.addNode(i)

  #shuffle nodes
  all_nodes = list(g.getAllNodes())
  random.shuffle(all_nodes)

  #Iterate through nodes and assign directed edges from only random previous nodes to ensure it is acyclic
  for i in range(1, len(all_nodes)):
    for j in range(random.randint(1, 2)):
      prev = all_nodes[random.randint(0, i-1)]
      g.addDirectedEdge(prev, all_nodes[i])

  return g

#test methods
ts = TopSort()
ran_graph = createRandomDAGIter(10)
ran_graph.printAdjacencyList()
print("Kahns:")
print(ts.Kahns(ran_graph))
print("mDFS:")
print(ts.mDFS(ran_graph))