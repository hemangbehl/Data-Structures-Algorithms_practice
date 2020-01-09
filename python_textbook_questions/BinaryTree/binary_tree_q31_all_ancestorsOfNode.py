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

# Function
def all(curr, ele, stack):
    if curr == None:
        return (False, stack)
    if curr.data == ele:
        return (True, stack)
    found = False

    if curr.left:
        stack.append(curr.left.data)
        found= all(curr.left, ele, stack)
        if found:
            return True
        else: 
            stack.pop()
            #check right sub tree
    if curr.right:
        stack.append(curr.right.data)
        found = all(curr.right, ele, stack)
        if found == False:
            stack.pop()
    
    return found
    


#driver code
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right = Node(3)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

stack = [bt.root.data]
all(bt.root, 7, stack)
bt.print()
print("")
print("all ancestors:", stack)

