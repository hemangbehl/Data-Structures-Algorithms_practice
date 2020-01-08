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

def ele(curr, k1, k2, ans = []):
    if not curr:
        return ans
    if k2 < curr.data:
        #check left tree
        ele(curr.left, k1, k2 ,ans)
    elif k1<= curr.data <= k2:
        ele(curr.left, k1, k2, ans)
        ans.append(curr.data)
        ele(curr.right,k1 ,k2, ans)
    elif curr.data < k1:
        #check right tree
        ele(curr.right, k1, k2, ans)
    
    return ans #return ans list

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
print(ele(bt.root, 31,35, []))