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
def height(root, ans): 
    if (root == None): 
        return 0
  
    left_height = height(root.left, ans)  
  
    right_height = height(root.right, ans)  
  
    # update the answer, because diameter  
    # of a tree is nothing but maximum  
    # value of (left_height + right_height + 1) 
    # for each node  
    ans[0] = max(ans[0], 1 + left_height + 
                             right_height)  
    #print("ans=", ans)
  
    return 1 + max(left_height, 
                   right_height) 
  
# Computes the diameter of binary  
# tree with given root.  
def diameter(root): 
    if (root == None):  
        return 0
    ans = [0] # This will store 
            # the final answer 
            # variable is kept as list so that it becomes global
            # while keeping it as an int makes its value remain as zero
    height_of_tree = height(root, ans)  
    return ( ans[0] - 1 )

##driver code
bt = BinaryTree()
bt.root = Node('1')
bt.root.left = Node('2')
bt.root.right = Node('3')
bt.print()
print("diameter= ", diameter(bt.root) )
#bt.print()
