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

def constructBT( ele, preorder, inorder):
    if ele == None:
        return None
    
    mid = Node(ele)

    left = []
    right = []
    found = 0
    for i in inorder: #split INORDER list into left and right by mid(root)
                        #this loop is O(n) so total recursive function has O(n^2)
        if i == ele:
            found = 1
        elif found == 0:
            left.append(i)
        else:
            right.append(i)
    
    # print("left = {} and right={}".format(left,right) )
    # print("len pre = {} and in={}".format(len(preorder),len(inorder)) )


    if left != []:
        #not empty
        leftroot = preorder.pop(0) #get first element

        mid.left = constructBT(leftroot, preorder, left)
        
    if right != []:
        rightroot = preorder.pop(0)

        mid.right = constructBT(rightroot, preorder, right)
    
    return mid

#driver code
bt = BinaryTree()
# inorder = "DBEAFC"
# preorder = "ABDECF"
inorder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preorder = ['A', 'B', 'D', 'E', 'C', 'F'] 
root = preorder[0]
preorder = preorder[1:]
bt.root = constructBT(root, preorder, inorder)
bt.print()