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
    
def height(curr, dictdiam):
    if curr == None:
        return (0, dictdiam)
    left = right = 0
    if curr.left:
        left, dictdiam = height(curr.left, dictdiam)
        left += 1
    if curr.right:
        right, dictdiam = height(curr.right, dictdiam)
        right += 1
    dictdiam[curr] = left + right
    h = max(left, right)
    return (h, dictdiam)

def diameter(root):
    if root == None:
        return 0
    
    h, dictdiam = height( root, dict() )

    max_d = 0
    for node in dictdiam:
        if dictdiam[node] > max_d:
            max_d = dictdiam[node]
    
    return max_d
    #end of function()

##driver code
bt = BinaryTree()
bt.root = Node('1')
bt.root.left = Node('2')
bt.root.right = Node('3')
bt.print()
print("diameter= ", diameter(bt.root) )
bt.print()
