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
    # print("ele", ele)
    if ele == None or ele == "" or ele == " ":
        return None
    
    mid = Node(ele)
    if inorder == []:
        return mid
    left = right = ""
    split = inorder.split(ele)
    if len(split) < 2:
        return mid
    left = split[0]
    right = split[1]
    
    # print("left = {} and right={}".format(left,right) )
    # print("len pre = {} and in={}".format(len(preorder),len(inorder)) )


    if left != "":
        #not empty
        # leftroot = preorder.pop(0) #get first element
        # leftroot = preorder[0] #get first element
        leftroot = None
        for i in preorder:
            if i in left:
                leftroot = i
                break
        preorder = preorder[1:] #discard first element
        mid.left = constructBT(leftroot, preorder, left)
        
    if right != "":
        # rightroot = preorder.pop(0)
        rightroot = None
        for i in preorder:
            if i in right:
                rightroot = i
                break
        #print("preorder list", preorder)        
        preorder = preorder[1:] #discard first element
        mid.right = constructBT(rightroot, preorder, right)
    
    return mid

#driver code
bt = BinaryTree()
# inorder = "DBEAFC"
# preorder = "ABDECF"
inorder = "HDBIEAFJCKG"
preorder = "ABDHEICFJGK"
root = preorder[0]
preorder = preorder[1:]
bt.root = constructBT(root, preorder, inorder)
bt.print()