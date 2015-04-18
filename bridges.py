# FINDING ALL BRIDGES IN GRAPH 

graph = {
    1: [2,3],
    2: [1,3,4],
    3: [1,2],
    4: [5,2],
    5: [4],
}

FORBIDEN_EDGE = (0,0)


class Stack:
    
    def __init__(self):
      self.elements = []
        
    def pop(self):
      if len(self.elements) > 0: 
        return self.elements.pop(-1)
      else:
        return "ERROR"
           
    def push(self, a):
      self.elements.append(a)

    def empty(self):
      if len(self.elements) == 0:
        return True
      else:
        return False


def edges():
  set_of_edges = set()
  for v in graph:
    for u in graph[v]:
      set_of_edges.add((v,u))
  return set_of_edges

# DFS

def dfs(v):
  s = Stack()
  visited = set()
  s.push(v)
  while not s.empty():
    v = s.pop()
    if v not in visited:
      neighbors = graph[v]
      visited.add(v)
      for element in neighbors:
        if v == FORBIDEN_EDGE[0] and element == FORBIDEN_EDGE[1]:   
          continue
        elif v == FORBIDEN_EDGE[1] and element == FORBIDEN_EDGE[0]:   
          continue
        else:
          s.push(element)
          
  return visited

  
def components():
  c = 0
  visited = set()
  for v in graph:
    if v in visited:
      continue 
    elements = dfs(v)
    c += 1
    for element in elements:
      visited.add(element)
    
  return c


def main():
    
    c = components()
    set_of_edges = edges()
    global FORBIDEN_EDGE
    for (v, u) in set_of_edges:
      FORBIDEN_EDGE = (v, u)
      c2 = components() 
      if c2 > c:
          print FORBIDEN_EDGE, "bridge"
      else:
          pass
        
if __name__ == "__main__":
    main()






  
  

    
    
      
      
     
     






    
    





