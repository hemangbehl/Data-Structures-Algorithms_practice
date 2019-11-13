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


    def reverse(self, head, tailNext):
        curr = head
        newHead = curr
        newTail = head
        prev= None
        
        while curr != tailNext: #until we reach the tailNext node
            next = curr.next #stores next pointer
            curr.next = prev #curr points to previous node or None
            prev = curr #prev node is now the current node
            newHead = curr #newHead is now current node
            curr = next #current advances to the next node which was stored

        return newHead, newTail
    
    def k_reverse(self, curr, k):
        
        if curr == None:
            return None

        if curr == self.head: #change global head
            print (" head found ")

        temp = curr 
        i = 0
        while i < k and temp.next != None: #iterate k times to reach the next k group
            i += 1
            temp = temp.next
        
        if i==0:
            return

        newHead, newTail = self.reverse(curr, temp)
        print ("k-head", newHead.data)
        print ("k-tail", newTail.data)
        
        if curr == self.head: #change global head
            print ("changing head to ", newHead.data)
            self.head = newHead
        
        newTail.next = self.k_reverse(temp, k)
        
        # if newTail.next == None:
        #     print("stopping criteria")
        #     return

        ###debugging
        # head = curr
        # while curr != None:
        #     curr = curr.next
        
        # newHead, newTail = self.reverse(head, curr)
        # if head == self.head: #change global head
        #     self.head = newHead
        #     print(newHead.data, newTail.data)

        return newHead
        

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
ll.insertEnd(8)
ll.insertEnd(9)
ll.printList()
newHead = ll.k_reverse(ll.head, 3)
ll.printList()
