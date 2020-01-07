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
def delete(curr, ele):
    #current node, element to delete
    if not curr or not ele:
        return None
    if curr.data == ele:
        #found
        print("FOUND", ele)
        if not curr.left and not curr.right:
            #leaf node, case 1
            return None
        elif curr.left and curr.right:
            #parent node, case 2
            parent = curr
            suc = curr.right
            while suc.left:
                parent = suc
                suc = suc.left
            #swap data
            curr.data = suc.data
            if curr == parent: #same
                curr.right = None
            else: #not same, left child is suc
                parent.left = None
        #case 3
        elif curr.left: #only left exists
            curr.data = curr.left.data
            curr.left = None #point to NULL
        else: #only right exists
            curr.data = curr.right.data
            curr.right = None
    elif ele < curr.data:
        curr.left = delete(curr.left, ele)
    elif ele > curr.data:
        curr.right = delete(curr.right, ele)
    
    return curr


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
bt.root = delete(bt.root, 80)
bt.print()
