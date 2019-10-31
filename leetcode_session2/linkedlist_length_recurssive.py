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

    def deleteKey(self, key):
        curr = self.head

        #check of head conatins the key and delete
        if curr!=None and curr.data==key:
            self.head = curr.next
            print("Deleted key at head")
            return

        while curr!=None and curr.data!=key:
            #loop will break at end of list or if key is found
            prev = curr
            curr = curr.next #advance the list

        if curr == None:
            print ("No key found")    
            return
        if curr.data == key:
            prev.next = curr.next #prev cannot be empty as head case was handled earlier
            print ("Deleted key")

#outside function
def length(curr):
    #for the first iteration curr should be the head
    if curr==None:
        return 0
    return 1 + length(curr.next)


    
#code
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

#linking lists
ll.head.next = second
second.next = third

#print
#ll.printList()
ll.insertHead(11)
#ll.printList()
ll.insertEnd(100)
ll.printList()
print ( length(ll.head) )
# ll.deleteKey(11)
# ll.printList()
# ll.deleteKey(11)
# ll.printList()
# ll.deleteKey(2)
# ll.printList()

