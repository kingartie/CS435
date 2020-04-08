class GraphSearch:
  def DFSRec(self, start, end, visited=None):
    if visited is None:
      visited = []

    visited.append(start)

    if start is end:
      return visited

    for neighbor in start.neighbors:
      if neighbor not in visited:
        if self.DFSRec(neighbor, end, visited):
          return visited
    return None

  def DFSIter(self, start, end):
    visited = []
    stack = [start]

    while stack:
      s = stack.pop()
      
      visited.append(s)

      if s is end:
        return visited

      for neighbor in s.neighbors:
        if neighbor not in visited:
          stack.append(neighbor)

  def BFTRec(self, graph, queue=None, visited=None):
    if queue is None:
      queue = [graph.first]
      visited = [graph.first]

    if len(queue) == 0:
      return visited

    s = queue.pop(0)

    if s not in visited:
        visited.append(s)
    
    for neighbor in s.neighbors:
      if neighbor not in visited:
        queue.append(neighbor)
    return self.BFTRec(graph, queue, visited)
  
  def BFTIter(self, graph):
    visited = [graph.first]
    queue = [graph.first]

    while queue:
      s = queue.pop(0)

      if s not in visited:
        visited.append(s)

      for neighbor in s.neighbors:
        if neighbor not in visited:
          queue.append(neighbor)

    return visited