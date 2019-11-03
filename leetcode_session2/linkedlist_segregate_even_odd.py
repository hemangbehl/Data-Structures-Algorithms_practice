class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        curr = self.head
        print("#start#")
        while curr:
            print(curr.data)
            curr = curr.next

    def segregate_even_odd(self):
        curr = self.head
        if not curr:
            return
        odd = 0
        even = 0
        if curr.data%2 == 0: #even
            even = curr
        else: #odd
            odd = curr
        
        while curr.next != None:
            if curr.next.data %2 ==0: #next is even
                if odd==0: #no odd before, curr is even and next is also even
                    even = curr.next #set even to new even
                    curr = curr.next #go next
                else: #current node is an odd no. and next is even
                    #need to swap
                    temp = curr.next.next
                    curr.next.next = odd #next even will point to odd
                    if even == 0: #no even before, then next node will be set as head
                        self.head = curr.next
                    else: #even existed before
                        #even will point to new even
                        even.next = curr.next
                    
                    even = curr.next #set new even
                    curr.next = temp
                    #we do not advance curr
            else: #next node is an odd no.
                #advance forward
                curr = curr.next
        
        return 


# Driver program
llist1 = LinkedList()
llist1.push(6)
llist1.push(5)
llist1.push(4)
llist1.push(3)
llist1.push(2)
llist1.push(1)


llist1.printList()      
llist1.segregate_even_odd()
llist1.printList()