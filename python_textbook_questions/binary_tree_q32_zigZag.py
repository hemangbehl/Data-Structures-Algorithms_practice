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
                               
                if currlvl != lvl:
                    lvl += 1
                    print("")
                    print("lvl",lvl, end="::  ")
                
                print(curr.data, end=" || ")

                currlvl = currlvl + 1
                if curr.left == None and curr.right == None:
                    continue
                queue.append([curr.left, currlvl])
                # if curr.right != None:
                queue.append([curr.right, currlvl])
                #lvl += 1
                
            else:
                print("--x--", lvl)
        print("")

# Function
def zigZag(root):
    if not root: return None
    lr = [root]
    rl = []
    way = "f"
    while lr or rl:
        if way == "f":
            curr = lr.pop()
            print(curr.data)
            if curr.left:
                rl.append(curr.left)
            if curr.right:
                rl.append(curr.right)
        else: #way == 'b'
            curr = rl.pop()
            print(curr.data)
            if curr.right:
                lr.append(curr.right)
            if curr.right:
                lr.append(curr.left)
        #check at end
        if lr == []:
            way = 'b'
        if rl == []:
            way = 'f'
    #end of while


#driver code
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right = Node(3)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)
bt.print()

zigZag(bt.root)