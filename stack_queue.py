# Stack, Queue, StackWithLimit, PriorityQueue

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

    

def test_stack():
    
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')
    print s.pop() # -> zwraca 'c'
    print s.pop() # -> zwraca 'b'
    print s.pop() # -> zwraca 'a'
    print s.pop() # -> zwraca 'ERROR'

test_stack()  


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
        
    

def test_queue():
    
    s = Queue()
    s.push('a')
    s.push('b')
    s.push('c')
    print s.pop() # -> zwraca 'a'
    print s.pop() # -> zwraca 'b'
    print s.pop() # -> zwraca 'c'
    print s.pop() # -> zwraca 'ERROR'

test_queue()



class StackWithLimit:
    
    def __init__(self,limit):
      self.elements = []
      self.limit = limit 
    
    def push(self, x):
      if len(self.elements) < self.limit:
        self.elements.append(x)
        return "OK"
      else:
        return "PUSH ERROR"
    
    def pop(self):
      if len(self.elements) > 0:
        return self.elements.pop(-1)
      else:
        return "POP ERROR"


def test_stack_with_limit():
    print '--- TEST test_stos_with_limit ---'
    s = StackWithLimit(2)
    print s.push('a')  # -> "OK"
    print s.push('b')  # -> "OK"
    print s.push('c')  # -> "PUSH_ERROR"
    print s.pop()      # -> "b"
    print s.pop()      # -> "a"
    print s.pop()      # -> "POP_ERROR"
    
test_stack_with_limit()

class PriorityQueue:
    
    def __init__(self):
      self.elements = []
        
        
    def push(self, weight, x):
      self.elements.append((weight, x))
        
                                   
    def pop(self):
      pass
            
       
        
            
            
def test_priority_queue():
    pq = PriorityQueue()
    pq.push(1, "kota")
    pq.push(3, "ala")
    print pq.pop()  # -> "ala"
    pq.push(2, "ma")
    print pq.pop() # -> "ma"
    print pq.pop() # -> "kota"
   

test_priority_queue()





    





