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
def diameter(curr, diam): 
    if curr == None:
        return 0, diam
    
    l, diam = diameter(curr.left, diam)
    r, diam = diameter(curr.right, diam)
    
    if curr.left: #if left child exists
        l += 1
    if curr.right: #if right child exists
        r += 1
    diam = max(diam, l+r)

    max_h = max(l, r)

    return max_h, diam


def diam_helper(root): 
    
    if root == None:
        return 0
    h, diam = diameter( root, 0 )
    return diam

##driver code
bt = BinaryTree()
bt.root = Node('1')
bt.root.left = Node('2')
bt.root.right = Node('3')
bt.print()
print("diameter= ", diam_helper(bt.root) )
#bt.print()
