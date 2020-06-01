class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #point to null
    
class LinkedList:
    def __init__(self):
        self.head = None #by default head is none

    def delKey(self, delkey):
        #to del del node at delkey index
        if self.head == None:
            return
        
        curr = self.head
        prev = -1
        cnt = 0
        while curr:
            if cnt == delkey:
                if curr == self.head:
                    #to del start node
                    self.head = curr.next
                    break
                else: #not the start node
                    prev.next = curr.next #skip curr node
                    break
            
            cnt += 1
            prev = curr #store curr node in prev
            curr = curr.next #go to next
    
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
print("Deleting")
ll.delKey(4)

ll.printList()
