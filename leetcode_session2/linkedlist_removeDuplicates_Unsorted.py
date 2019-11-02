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

    def removeDuplicates_unsorted(self):
        curr = self.head
        if curr == None:
            return
        prev = 0
        ele = dict()
        temp = 0

        while curr!=None:
            if curr == self.head:
                prev = curr
                ele[curr.data]=1 #add to dict
                curr = curr.next
            else: #not head
                if curr.data in ele.keys():
                    #remove duplicate
                    temp = curr.next
                    prev.next = curr.next #previous node points from current node to the next
                    prev = prev.next #advance prev
                    curr.data = None
                    curr.next = None #point the duplicate node to None
                    curr = temp
                    #print("removing")
                    
                else:
                    #add to dict 
                    print(ele)
                    ele[curr.data] = 1
                    curr= curr.next
                    prev = prev.next #advance prev
        
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
#ll.printList()
ll.insertEnd(5)

ll.insertEnd(5)
ll.printList()
ll.removeDuplicates_unsorted()
ll.printList()
