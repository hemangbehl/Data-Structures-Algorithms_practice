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

    
#code
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

#linking lists
ll.head.next = second
second.next = third

#print
ll.printList()
ll.insertHead(11)
# ll.printList()
# ll.deleteKey(11)
# ll.printList()
# ll.deleteKey(11)
# ll.printList()
# ll.deleteKey(2)
# ll.printList()

