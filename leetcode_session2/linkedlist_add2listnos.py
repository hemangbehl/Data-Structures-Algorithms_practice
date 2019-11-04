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


    def add2listnos(self, a, b):
        a = a.head
        b= b.head
        if not a and not b:
            return -1 #both empty
        sum = 0
        c = 0 #carry
        ans = Node(0) #dummy node
        ans_head = ans #dummy pointer to dummy node
        while a or b: #atleast one list has value
            if a and b: #case 1 a + b
                sum = a.data + b.data + c
                a=a.next
                b=b.next
            elif a and b==None: #case 2: a + 0
                sum = a.data + c
                a = a.next
            else: #case 3: 0 + b
                sum = b.data + c
                b = b.next
            
            #common to all 3 cases
            if sum>9:
                c = 1
                ans.next = Node(sum - 10) #create next node for ans
                ans = ans.next
            else: #sum<=9 single digit
                c = 0 #no carry
                ans.next = Node(sum)
                ans = ans.next
        
        #end of while
        if ans_head.next == None:
            # no and , error
            return -1
        else: #return head node
            return ans_head.next #points to first ANS node
        


        
#code
ll = LinkedList()
ll.head = Node(7)
ll.insertEnd(5)
ll.insertEnd(9)
ll.insertEnd(4)
ll.insertEnd(6)
ll.printList()

ll2 = LinkedList()
ll2.head = Node(8)
ll2.insertEnd(4)
ll2.printList()

ll3 = LinkedList()
ll3.head = ll3.add2listnos(ll, ll2)
ll3.printList()
