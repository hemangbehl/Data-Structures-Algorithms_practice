class Queue():
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.queue == []
        #returns true when empty
    
    def enqueue(self, ele):
        self.queue.append(ele)
    
    def dequeue(self):
        if self.isEmpty == True:
            return None
        #else
        return self.queue.pop(0) #pop starting element
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)

##driver code
q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.display()
q1.dequeue()
q1.display()