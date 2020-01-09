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
def leaf(curr, queue): 
    if curr == None:
        return
    #print("queue:", queue[-1].data)
    if curr.left == None and curr.right == None:
        #leaf node
        while queue != []:
            print ( "-->", queue.pop(0).data, end="" )
        print("")
        
    else: #not a leaf node
        #call recurssive funtion for both children whether empty or not

        queue.append( curr.left )
        leaf( curr.left, queue.copy()) #send a copy of queue not reference
        queue.pop() #remove left child as we do not need it for right

        queue.append( curr.right )
        leaf( curr.right, queue.copy() )
        queue.pop() #remove right child as we do not need it

def rootLeafPath(root): 
    
    if root == None:
        print("Empty tree")
    
    print("Root to leaf paths:")
    queue = [root]
    leaf(root, queue)

##driver code
bt = BinaryTree()
bt.root = Node('1')
bt.root.left = Node('2')
bt.root.left.left = Node('6')
bt.root.right = Node('3')
bt.root.right.left = Node('4')
bt.root.right.right = Node('5')
#bt.print()
rootLeafPath(bt.root)

#bt.print()
