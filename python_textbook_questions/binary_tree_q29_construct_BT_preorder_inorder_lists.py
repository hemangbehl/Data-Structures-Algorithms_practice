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
    
# Function to construct BT

def constructBT( ele, preorder, inorder, inorder_index):
    if ele == None:
        return None
    left = []
    right = []

    #splitting inorder list into left and right is now in constant time O(1)
    midIndex = inorder_index[ele]
    left = inorder[:midIndex]
    right = inorder[midIndex:]

    mid = Node(ele)
    if preorder != []:
        #not empty
        leftroot = preorder.pop(0) #get first element

        mid.left = constructBT(leftroot, preorder, left, inorder_index)

    if preorder != []:
        rightroot = preorder.pop(0)

        mid.right = constructBT(rightroot, preorder, right, inorder_index)
    
    return mid

#driver code
bt = BinaryTree()
inorder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preorder = ['A', 'B', 'D', 'E', 'C', 'F'] 

root = preorder[0]
preorder = preorder[1:]
inorder_index = {} #dict

#add indexes of elements in INORDER to a dict
i = 0
for ele in inorder:
    inorder_index[ele] = i

bt.root = constructBT(root, preorder, inorder, inorder_index)
bt.print()