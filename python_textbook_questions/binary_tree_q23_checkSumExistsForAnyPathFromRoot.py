class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def print(self):
        curr = self.root
        if curr == None:
            print("Empty tree")
            return
        queue = [self.root]
        print("root-->", end='')
        while queue != []:
            curr = queue.pop(0)

            #print curr element
            print(curr.data)

            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)
    
# Function to find height of a tree  
def checkSum(curr, n):
    if curr == None:
        return False
    rem = n - curr.data
    if rem == 0: #found sum
        return True
    elif rem < 0: #sum of path is too large
        return False
    
    #else: #keep checking
    left = checkSum(curr.left, rem)
    right = checkSum(curr.right, rem)
    return (left or right) #return OR of left, right
    
##driver code
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.left.left = Node(6)
bt.root.right = Node(3)
bt.root.right.left = Node(4)
bt.root.right.right = Node(5)
bt.print()
print("sum of exists:", checkSum(bt.root, 5) )
