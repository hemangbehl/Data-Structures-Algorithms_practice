class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_ll:
    def __init__(self):
        self.head = None
        self.last = None
    
    def enqueue(self, ele):
        new = Node(ele) #new points to None
        if self.last == None:
            self.last = new
            self.head = new
        else: #not empty
            self.last.next = new
            self.last = new
    def isEmpty(self):
        #return True if empty
        return self.last == None
    
    def dequeue(self):
        #remove front element being head
        if self.head == None: #empty
            return None
        #else
        to_del_data = self.head.data

        if self.head == self.last: #one node list
            self.head = None
            self.last = None
        else: #more than 1 nodes in list
            self.head = self.head.next
            #as nothing points to old head it is deleted automatically
        return to_del_data #return data of deleted node
    
    def printList(self):
        curr = self.head
        while curr!= None:
            print("->", curr.data, end="")
            curr = curr.next
        print("")

##driver code
q1 = Queue_ll()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.printList()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.printList()
