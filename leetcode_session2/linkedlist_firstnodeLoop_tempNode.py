class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        curr = self.head
        print ("#start#")
        while curr!=None: #while loop until it reaches the end 
            print (curr.data)
            curr = curr.next #go to next node

    def insertHead(self,ele):
        new = Node(ele)
        new.next = self.head
        self.head = new
    
    def insertEnd(self,ele):
        new = Node(ele)
        new.next = None
        curr = self.head
        #check id list is empty
        if self.head == None:
            self.head = new
            print("Inserted at head as list was empty")
            return
        else:
            while (curr!=None):
                prev = curr
                curr = curr.next
            
            #at end of loop, curr is none and prev has some value
            prev.next = new
            new.next = curr
            print ("Inserted at the end")
            return


    def firstNodeLoop_tempNode(self):
        if self.head == None:
            return -1
        temp = Node(0)
        curr = self.head
        store = 0 #
        while curr!=None:
            if curr.next == temp:
                return curr
            #else
            store = curr.next
            curr.next = temp
            curr = store
        #end of while loop, no loop
        return 0        
        
#code
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
#linking lists
ll.head.next = second
second.next = third
#print
# ll.insertEnd(4)
# ll.insertEnd(5)
# ll.insertEnd(6)
#ll.printList()
print( ll.firstNodeLoop_tempNode() )
#ll.printList()
