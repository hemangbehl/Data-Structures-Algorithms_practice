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
        while curr:
            print(curr.data)
            curr = curr.next

    def sorted_intersect(self, a, b):
        head = None
        
        while a and b:
            if a.data == b.data:
                if head is None:
                    head = Node(a.data)
                    #tail is like curr pointer, points to last
                    tail = head
                    a = a.next
                    b = b.next
                else:
                    tail.next = Node(a.data)
                    tail = tail.next
                    a = a.next
                    b = b.next

            elif a.data < b.data:
                a = a.next

            else: #a.data < b.data
                b = b.next
        #end of while
        return head


# Driver program
llist1 = LinkedList()
llist1.push(6)
llist1.push(5)
llist1.push(4)
llist1.push(3)
llist1.push(2)
llist1.push(1)

llist2 = LinkedList()
llist2.push(8)
llist2.push(6)
llist2.push(4)
llist2.push(2)

llist3 = LinkedList()
llist3.head = llist3.sorted_intersect(llist1.head, llist2.head)
llist3.printList()      


