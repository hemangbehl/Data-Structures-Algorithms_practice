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


    def rotateRight(self, k):
        curr  =self.head
        if not curr:
            return
        #assuming k < len always
        l = 1
        prev = 0
        while curr.next!=None:
            curr = curr.next
            l+=1
        #curr is at last node
        #l is the length of list
        if k == 0:
            return
        #else:
        #point the end of list to the head
        curr.next = self.head
        #last node is now the head
        split = l - k #split contains the node which should be split and be the tail
        curr = self.head

        for i in range(0, split-1):
            curr= curr.next
        #curr reaches the split node

        self.head = curr.next #node after splitting node is Head
        curr.next = None #make the splitting node tail

        
#code
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)
#linking lists
ll.head.next = second
second.next = third
#print
ll.insertEnd(4)
ll.insertEnd(5)
ll.insertEnd(6)
ll.insertEnd(7)
ll.printList()
ll.rotateRight(5)
ll.printList()
