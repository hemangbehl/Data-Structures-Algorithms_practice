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


#new function

def detectLoop(head):
    if not head or not head.next: return False
    slow = head.next
    fast = head.next.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False


#code
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

#linking lists
ll.head.next = second
second.next = second

# ll.insertHead(11)
# ll.printList()
# ll.insertEnd(100)
# ll.printList()

print( detectLoop(ll.head))
