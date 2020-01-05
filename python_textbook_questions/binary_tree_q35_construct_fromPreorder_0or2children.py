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
def con(ele, preorder):
    #ele -->element, preorder--> list
    if ele == None or preorder == []:
        return None
    if ele == "L":
        #leaf node
        return Node("L")
    if ele == "I":
        #internal node, 2 children
        mid = Node("I")
        mid.left = con(preorder.pop(0), preorder)
        mid.right = con(preorder.pop(0), preorder)
        return mid

#driver code
bt = BinaryTree()
# bt.root = Node(1)
# bt.root.left = Node(2)
# bt.root.left.left = Node(4)
# bt.root.left.right = Node(5)
# bt.root.right = Node(3)
# bt.root.right.left = Node(6)
# bt.root.right.right = Node(7)
preorder = "I,L,I,L,L" #TEST #1
preorder = "I,I,L,I,L,L,I,L,L" #TEST #2
preorder = preorder.split(",")
# preorder = []
# print(preorder)
if preorder != []:
    bt.root = con(preorder.pop(0), preorder)
    bt.print()
else:
    print("empty list")