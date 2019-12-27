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
    
    def reversestack(self, prev, curr):
        if curr == None:
            #empty list
            return
        if curr.next == None:
            #end node
            self.head = curr
            curr.next = prev
            return
        else:
            self.reversestack(curr, curr.next)
            curr.next = prev
            return


#code
stack = LinkedList()
stack.head = Node(1)
second = Node(2)
third = Node(3)

#linking lists
stack.head.next = second
second.next = third

#print
stack.insertEnd(4)
#stack.printList()
stack.insertEnd(5)
stack.insertEnd(6)
stack.printList()
stack.reversestack( None, stack.head)
stack.printList()