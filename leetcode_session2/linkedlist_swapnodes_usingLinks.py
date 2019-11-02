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

    def swapNodesUsingLinks(self, k1, k2):
        curr = self.head
        if curr == None: 
            return
        prev = c1 = c2 = p1 = p2 = 0

        while curr != None:
            if curr.data == k1:
                c1 = curr
                if curr==self.head:
                    p1 = 1 #signifies header
                else:
                    p1 = prev
            elif curr.data == k2:
                c2 = curr
                if curr==self.head:
                    p2 = 1
                else:
                    p2 = prev
            #if both found
            if c1 != 0 and c2 != 0:
                temp = c2.next

                #handle c1,c2 in sequence
                if c1.next == c2: #check whether c1 points to c2
                    c2.next = c1
                else:
                    c2.next = c1.next

                c1.next = temp #point to waht c2 used to point
                if p1==1:
                    #c1 was the head
                    self.head = c2
                else:
                    p1.next = c2
                if p2==1:
                    self.head = c1
                else:
                    if p2 == c1:
                        pass #avoid pointing to itself
                    else:
                        p2.next = c1
                #nodes swapped now exit
                return
            
            if curr==self.head:
                prev = self.head #as head node has no previous node
            else:
                prev= prev.next
            
            curr = curr.next #go forward


        
#code
ll = LinkedList()
ll.head = Node(10)
second = Node(15)
third = Node(12)

#linking lists
ll.head.next = second
second.next = third

#print
ll.insertEnd(13)
#ll.printList()
ll.insertEnd(20)

ll.insertEnd(14)
ll.printList()
ll.swapNodesUsingLinks(12,20)
ll.printList()
