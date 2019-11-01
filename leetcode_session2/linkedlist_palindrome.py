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

    def palindrome(self):
        curr = self.head
        if curr==None:
            return -1 #error empty list
        
        i = 1
        n = 0
        rev = 0
        while curr!=None:
            n = n * 10 + curr.data #stores current no.
            rev = curr.data * i + rev #reverses and stores current no.
            curr = curr.next #advance to next in list
            i*=10 #multiply by 10

        if n == rev:
            return 1 #palindrome
        else:
            print(n, rev)
            return 0 #not palindrome

#code
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

#linking lists
ll.head.next = second
second.next = third

#print
ll.insertEnd(3)
#ll.printList()
ll.insertEnd(2)

ll.insertEnd(1)
ll.printList()
print ("Palindrome or not:", ll.palindrome())
