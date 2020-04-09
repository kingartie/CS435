class TopSort:

  def Kahns(self, graph):
    all_nodes = graph.getAllNodes()
    topSort = []
    zeroDegreeQueue = []
    inDegree = { n : 0 for n in all_nodes } #initialize hashmap with all 0s

    #populate hashmap with the current numbers of incoming edges
    for node in all_nodes:
      for neighbor in node.neighbors:
        inDegree[neighbor] += 1

    #find nodes with 0 degree
    self.addNodesWithZeroDegree(inDegree, zeroDegreeQueue)

    #process nodes with 0 degree
    while zeroDegreeQueue:
      s = zeroDegreeQueue.pop(0)
      topSort.append(s)

      for neighbor in s.neighbors:
        inDegree[neighbor] -= 1
      
      self.addNodesWithZeroDegree(inDegree,zeroDegreeQueue)

    return topSort

  def addNodesWithZeroDegree(self, inDegree, queue):
    for current in inDegree:
      if inDegree[current] == 0:
        queue.append(current)
        inDegree[current] -= 1 

  def mDFS(self, graph):
    visited = []
    stack = []

    for node in graph.getAllNodes():
      if node not in visited:
        self.mDFSHelper(node, stack, visited)

    return stack[::-1] #reverse of stack list

  def mDFSHelper(self, node, stack, visited):
    visited.append(node)

    for neighbor in node.neighbors:
      if neighbor not in visited:
        self.mDFSHelper(neighbor, stack, visited)

    stack.append(node)