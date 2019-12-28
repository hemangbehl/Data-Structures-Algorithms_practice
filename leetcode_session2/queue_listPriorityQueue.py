#array list implementation of a Priority Queue in Python3

'''
#ref: https://www.geeksforgeeks.org/priority-queue-set-1-introduction/
A typical priority queue supports the following operations:
- insert(item, priority)    : Inserts an item with given priority.
- getHighestPriority()      : Returns the highest priority item.
- deleteHighestPriority()   : Removes the highest priority item.
'''

class PriorityQueue():
    def __init__(self):
        self.queue = []
        self.priority = []
    def enqueue(self, ele, prio):
        self.queue.append(ele)
        self.priority.append(prio)

    def isEmpty(self):
        #returns True when queue is empty
        return self.queue.append == []
    def dequeue(self):
        #remove the element with highest priority
        #linear search to find element with highest priority
        if self.isEmpty == True:
            return None
        #else
        max_prio = 0

        #get max from priority list
        for i in range(0, len(self.priority)):
            if max_prio < self.priority[i]:
                max_prio = self.priority[i]
                break
        self.priority.pop(i)
        return self.queue.pop(i) #return the dequeued item
    
    def display(self):
        print(self.queue)

##driver code
pq = PriorityQueue()
pq.enqueue("a",1)
pq.enqueue("b",5)
pq.enqueue("c",7)
pq.enqueue("d",3)
pq.display()

pq.dequeue()
pq.display()

pq.dequeue()
pq.display()