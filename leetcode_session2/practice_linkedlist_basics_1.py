class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #initialize linkedlist as empty at the start
    
    def printList(self):
        #prints linked list from start to end
        curr = self.head
        while (curr != None):
            print (curr.data)
            curr = curr.next
    
    def addNodeAtStart(self, ele):
        curr = self.head
        new_node = Node(ele) #create a new node for ele
        
        if curr == None:
            self.head = new_node
        elif curr.next == None:
            curr.next = new_node
        else: #go to next in list
            curr = curr.next

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.printList()
