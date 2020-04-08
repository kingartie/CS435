
from graph import Graph
from graphsearch import GraphSearch
import random

gs = GraphSearch()

def createRandomUnweightedGraphIter(n: int):
  g = Graph()
  #Create nodes
  for i in range(n):
    g.addNode(i)
  
  #shuffle nodes
  list_nodes = list(g.getAllNodes())
  random.shuffle(list_nodes)

  #connect edges in order, like a double-linked list
  prev = None
  for i in list_nodes:
    if prev:
      g.addUndirectedEdge(i, prev)
    prev = i
  return g

def createLinkedList(n: int):
  g = Graph()
  prev = None
  for i in range(n):
    n = g.addNode(i)
    if prev:
      prev.addNeighbor(n)
    prev = n
  return g

def BFTRecLinkedList(graph):
  return gs.BFTRec(graph)

def BFTIterLinkedList(graph):
  return gs.BFTIter(graph)


#test methods
ran_graph = createRandomUnweightedGraphIter(10)
ran_graph.printAdjacencyList()
#Note: DFSIter and DFSRec search in different order. DFSIter starts with the last neighbor, and DFSRec starts with the first
print("DFSIter:", gs.DFSIter(ran_graph.first, ran_graph.last))
print("DFSRec:", gs.DFSRec(ran_graph.first, ran_graph.last))
print("BFTIter:", gs.BFTIter(ran_graph))
print("BFTRec:", gs.BFTRec(ran_graph))
print("BFTIterLink:", BFTIterLinkedList(createLinkedList(10)))
print("BFTIterLink:", BFTIterLinkedList(createLinkedList(10)))
print("BFTRecLink:", BFTRecLinkedList(createLinkedList(10)))