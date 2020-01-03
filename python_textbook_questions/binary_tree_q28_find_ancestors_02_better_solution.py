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
def ancestor(curr, a, b, ans = None):
    #takes current node, number a, number b, ans as default None
    if curr == None or ans != None:
        return False, False, ans
    
    midA = (curr.data == a)
    midB = (curr.data == b)

    #left sub tree
    a1, b1, ans = ancestor(curr.left, a, b, ans)
    if ans != None: #both a and b were found with 'ans' as ancestor
        return True, True, ans
    
    #right sub tree
    a2, b2, ans = ancestor(curr.right, a, b, ans)
    if ans != None: #both a and b were found with 'ans' as ancestor
        return True, True, ans
    
    found_A = (a1 or a2 or midA)
    found_B = (b1 or b2 or midB)

    if found_A and found_B:
        #found both numbers with current node as ancestor
        return True, True, curr.data
    else: #not found
        return found_A, found_B, ans


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

#ancestors
a, b = 6, 5
foundA, foundB, answer = ancestor(bt.root, a, b, None)
print("Ancestor of {} and {} = {}".format(a, b, answer) )
