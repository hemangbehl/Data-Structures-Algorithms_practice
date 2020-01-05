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
        lvl = 0
        queue = [[self.root, lvl]]
        print("root-->", end='')
        while queue != []:
            curr, currlvl = queue.pop(0)

            #print curr element
            if curr != None:
                print(curr.data, currlvl)
                if curr.left == None and curr.right == None:
                    continue
                # if currlvl != lvl:
                #     #lvl += 1
                currlvl = currlvl + 1
                queue.append([curr.left, currlvl])
                # if curr.right != None:
                queue.append([curr.right, currlvl])
                #lvl += 1
                
            else:
                print("--x--", lvl)

# Function to construct BT

def constructBT( ele, preorder, inorder, inorder_index):
    if ele == None or inorder == []:
        return None
    
    left = []
    right = []

    #splitting inorder list into left and right is now in constant time O(1)
    midIndex = inorder_index[ele]
    print("inorder ={} ele={} indexofELE={}".format(inorder, ele, inorder_index) )
    left = inorder[:midIndex-1]
    right = inorder[midIndex+1:]
    print("left={} right={}".format(left,right) )

    mid = Node(ele)
    if preorder != [] and left != []:
        #not empty
        leftroot = preorder.pop(0) #get first element

        mid.left = constructBT(leftroot, preorder, left, inorder_index)
    
    print("after left, left={} right={}".format(left,right) )
    print("preorder len", len(preorder))
    if preorder != [] and right != []:
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
    i += 1

bt.root = constructBT(root, preorder, inorder, inorder_index)
# bt.root = Node(1)
# bt.root.left = Node(2)
# bt.root.left.left = Node(4)
# bt.root.left.right = Node(5)
# bt.root.right = Node(3)
# bt.root.right.left = Node(6)
# bt.root.right.right = Node(7)
bt.print()