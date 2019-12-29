class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
'''
The list is so created so that the highest priority element is always at the head of the list.
As such, Enqueue() will push the node in dedscending order. A priority of 10 is higher than 2.

Enqueue(ele, prio)  : O(n), node added according to its priority
Dequeue()           : O(1), node taken out from head

'last' pointer is not required as we do not add to the end.
'''
class PriorityQueue_ll:
    def __init__(self):
        self.head = None
        
    def enqueue(self, data, prio):
        '''
        Priority DOES affect enqueue operation.
        '''
        new = Node(data, prio)

        if self.head == None: #empty linked list
            self.head = new
            return
        #else
        #check if new node should be inserted at the head of the list
        if new.priority > self.head.priority:
            new.next = self.head
            self.head = new
        else: #check for rest
            curr = self.head
            
            #loop until we reach last node or the node before 'new' node should be inserted
            while curr.next != None and curr.next.priority > new.priority:
                curr = curr.next
            
            new.next = curr.next #new points to the next of curr node
            curr.next = new #curr points to the

        
    def isEmpty(self):
        #return True if empty
        return self.last == None
    
    def dequeue(self):
        ''' 
        We remove the head as it has the highest priority
        TC: O(1) '''
        #remove front element being head
        if self.head == None: #empty list
            return None
        #else
        del_data = self.head.data
        self.head = self.head.next
        #noting points to original head node so it is removed automatically
        return del_data

    def top(self):
        #returns data of the 'head' node of the linked list
        return self.head.data
    
    def printList(self):
        curr = self.head
        while curr!= None:
            print("->", curr.data, curr.priority, end="")
            curr = curr.next
        print("")

##driver code
q1 = PriorityQueue_ll()
q1.enqueue("A",4)
q1.enqueue("B",2)
q1.enqueue("C",7)
q1.enqueue("D",1)
q1.printList()
q1.dequeue()
q1.dequeue()
q1.printList()
