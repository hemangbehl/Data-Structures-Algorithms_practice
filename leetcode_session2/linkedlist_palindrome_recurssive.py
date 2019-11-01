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
    
    def pailndrome_wrap(self):
        if self.head == None:
            return False #empty list
        else:
            return self.palindrome(self.head, 0, 0, 1)

    def palindrome(self, curr, n, rev, i):
        if curr == None:
            if n == rev:
                return True #palindrome
            else:
                return False #not a palindrome
        else: #call recurssively
            print (n,rev)        
            return True and self.palindrome(curr.next, n*10 + curr.data, rev + curr.data*i, i*10)
        

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
print ("Palindrome or not:", ll.pailndrome_wrap())
