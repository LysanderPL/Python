# Breadth-first search

class Queue:

  def __init__(self):
    self.elements = []
    
  def pop(self):
    if len(self.elements) > 0:
      return self.elements.pop(0)
    else:
      return "ERROR"
    
  def push(self, a):
    self.elements.append(a)

  def empty(self):
    if len(self.elements) == 0:
      return True
    else:
      return False 
        


graph = {
    1: [2,3],
    2: [1,3,4],
    3: [1,2],
    4: [2,5],
    5: [4],
}




def bfs(v):
  q = Queue()
  visited = set()
  q.push(v)
  while not q.empty():
    v = q.pop()
    if v not in visited:
      neighbors = graph[v]
      visited.add(v)
      for element in neighbors:
        q.push(element)



  return visited
    


print bfs(1)

    
   





    
    





