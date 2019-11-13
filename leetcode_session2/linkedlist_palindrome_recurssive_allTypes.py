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

    def palindrome(self, curr, right, head):
        if curr.next != right:
            flag , compare_head = self.palindrome(curr.next, right, head)
            if flag == False:
                #print("flag was false",compare_head.data)
                return False, compare_head.next
            else: #previous comparision was True
                if curr.data == compare_head.data :
                    #print("true==>", curr.data, compare_head.data)
                    return (True, compare_head.next)
                else:
                    #print("false==>", curr.data, compare_head.data)
                    return False, compare_head.next
        
        else: #last node before None
            if curr.data == head.data:
                #print("last node, same",curr.data, head.data)
                return True, head.next
            else:
                #print("last node, NOT same")
                return False, head.next
       

#code
ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

#linking lists
ll.head.next = second
second.next = third

#print
#ll.insertEnd(111)
ll.insertEnd(3)
#ll.printList()
ll.insertEnd(2)

ll.insertEnd(1)
ll.printList()
flag, curr = ll.palindrome(ll.head, None, ll.head)
print ("Palindrome or not:", flag)
