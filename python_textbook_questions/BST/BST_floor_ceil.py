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

def floor(curr, ele):
    if not curr:
        return None
    
    if ele< curr.data:
        #go left
        return floor(curr.left, ele)
    
    elif ele == curr.data:
        return curr.data
    
    elif ele > curr.data:
        #check right tree otherwise curr.data is the answer
        ans = floor(curr.right, ele)
        if ans == None:
            return curr.data
        else: #ans is not null
            return ans

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

ele = 0
print("floor(lowest nearest) of {} is {}".format(ele, floor(bt.root, ele) ) )
ele = 33
print("floor(lowest nearest) of {} is {}".format(ele, floor(bt.root, ele) ) )
ele = 43
print("floor(lowest nearest) of {} is {}".format(ele, floor(bt.root, ele) ) )