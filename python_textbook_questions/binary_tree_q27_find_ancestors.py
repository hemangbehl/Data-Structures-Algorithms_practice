''' works only when no duplicate nodes exist.
Assumes unique nodes. Returns false if not found.
'''
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
    
# Function 
def findAncestors( root, n1, n2):
    if root == None:
        return None
    ans = [None] #mutable list stores ancestor

    #call recursive func to set ans[0]
    ancestor(root, n1, n2, ans)

    return ans[0]

def ancestor(curr, n1, n2, ans):
    if curr == None or ans[0] != None:
        return False
    
    mid = False #default
    if curr.data == n1 or curr.data == n2:
        mid = True
    left = ancestor(curr.left, n1, n2, ans)

    if (mid + left) == 2:
        #found ancestor as mid and left are true
        ans[0] = curr.data
        return False
    
    right = ancestor(curr.right, n1, n2, ans)

    if (mid + left + right) >= 2:
        #found twice
        ans[0] = curr.data
        return False
    
    return (mid or left or right) #returns True if present, False if absent



##driver code
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right = Node(3)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)
bt.print()
print("Ancestor= {}".format(findAncestors(bt.root, 5, 6)) )
print("Ancestor= {}".format(findAncestors(bt.root, 4,5)) )
print("Ancestor= {}".format(findAncestors(bt.root, 3,3)) )
print("Ancestor= {}".format(findAncestors(bt.root, 5, 10)) )