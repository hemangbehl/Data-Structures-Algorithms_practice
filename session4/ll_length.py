class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #point to null
    
class LinkedList:
    def __init__(self):
        self.head = None #by default head is none

    
    def printList(self):
        curr = self.head
        print ("#start#")
        while curr!=None: #while loop until it reaches the end 
            print (curr.data)
            curr = curr.next #go to next node

    def insertHead(self, ele):
        new = Node(ele)
        new.next = self.head
        self.head = new
    
    def insertEnd(self, ele):
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

    def getLen(self):
        curr = self.head

        if curr == None:
            return 0

        cnt = 0

        while curr:
            cnt += 1
            curr = curr.next
        
        return cnt
    
    def getLen_recurssive(self, curr):
        if curr == None:
            return 0
        
        return 1 + self.getLen_recurssive(curr.next)
    



#code
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

#linking lists
ll.head.next = second
second.next = third

ll.insertHead(11)
# ll.printList()
ll.insertEnd(100)
ll.printList()
print ( ll.getLen() )
print( ll.getLen_recurssive(ll.head))

# ll.printList()
