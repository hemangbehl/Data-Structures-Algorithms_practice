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
def sum_path(curr, num): 
    if curr == None:
        return 0
    
    #form the number using digits
    num = num * 10 + curr.data

    if curr.left == None and curr.right == None:
        #leaf node
        return num #return the num    
    
    #else:
    left = sum_path(curr.left, num)
    right = sum_path(curr.right, num)
    
    return (left + right)

    
##driver code
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.left.left = Node(6)
bt.root.right = Node(3)
bt.root.right.left = Node(4)
bt.root.right.right = Node(5)
bt.print()
print("sum pf all paths:", sum_path(bt.root, 0) )
