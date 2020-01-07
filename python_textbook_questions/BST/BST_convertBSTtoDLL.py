class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
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
            if currlvl != lvl:
                lvl += 1
                print("")
                print("lvl",lvl, end="::  ")
            if curr != None:
                print(curr.data, end=" || ")
                currlvl = currlvl + 1
                queue.append([curr.left, currlvl])
                queue.append([curr.right, currlvl])   
            else:
                print("--x--", end=" || ")
        print("")

# Function
def dll(curr): #convert BST into DLL
    if curr == None:
        return (None, None)
    if not curr.left and not curr.right:
        #leaf node, no children
        return (curr, curr)
    elif curr.left and curr.right:
        #both exist, parent node
        lstart, lend = dll(curr.left)
        rstart, rend = dll(curr.right)
        #now double link the inorder lists
        lend.right = curr
        curr.left = lend
        curr.right = rstart
        rstart.left = curr
        return (lstart, rend)
    #onlt one child cna exist now
    elif curr.left: #only left child exists
        lstart, lend= dll(curr.left)
        lend.right = curr
        curr.left = lend
        return (lstart, curr)
    elif curr.right: #only right child exists
        rstart, rend = dll(curr.right)
        curr.right = rstart
        rstart.left = curr
        return (curr, rend)

def converttoDLL(root):
    if not root:
        print("empty tree")
        return
    start, end = dll(root)
    start.left = end
    end.right = start
    print("root-->",start.data, end="")
    #start is now the root
    curr = start.right
    while curr != start: #stop when looped back to itself
        print("-->",curr.data, end="")
        curr = curr.right
    return start

#driver code
bt = BinarySearchTree()
bt.root = Node(50)
bt.root.left = Node(40)
bt.root.left.left = Node(30)
bt.root.left.right = Node(45)
bt.root.right = Node(80)
bt.root.right.left = Node(60)
bt.root.right.right = Node(90)
bt.print()
bt.root = converttoDLL(bt.root)
# bt.print()
