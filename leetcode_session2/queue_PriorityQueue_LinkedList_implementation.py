class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue_ll:
    def __init__(self):
        self.head = None
        self.last = None
    
    def enqueue(self, ele, prio):
        '''
        Priority doesn't affect enqueue operation.
        Without using 'last' pointer we can enqueue elements by reaching the last node pointing to null
        and then adding the node after it. As such TC: O(n)
        When we use 'last' pointer, TC: O(1)
        '''
        new = Node(ele, prio) #new points to None
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
        ''' 
        Priority affects dequeue operation. We need to search for the highest
        priority and then delete that node.
        TC: O(n) '''
        #remove front element being head
        if self.head == None: #empty list
            return None
        #else
        if self.head == self.last: #one node in list
            to_del_data = self.head.data
            self.head = None
            self.last = None
            return to_del_data
        #if nodes are greater than 1, we need to find the node with max priority
        to_del_data = 0
        prev = 0
        curr = self.head
        max_prio = curr.priority
        max_prio_prev_node = None

        while curr != None:
            if max_prio < curr.priority:
                max_prio_prev_node = prev
            prev = curr
            curr = curr.next    
        
        #to delete node after prev
        if max_prio_prev_node == None: #need to delete head
            to_del_data = self.head.data
            self.head = self.head.next
        else:
            #delete node after prev
            to_del_data = max_prio_prev_node.next.data
            max_prio_prev_node.next = max_prio_prev_node.next.next
            if max_prio_prev_node.next == None: #in case node removed was last
                self.last = max_prio_prev_node 
                        
        return to_del_data #return data of deleted node
    
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
