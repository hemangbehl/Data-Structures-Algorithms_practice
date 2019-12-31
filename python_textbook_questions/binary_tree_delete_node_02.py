class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Inorder traversal of a binary tree
def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    dict={}
    while (len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
            dict[temp.left.data]=temp
        if temp.right:
            dict[temp.right.data] = temp
            q.append(temp.right)
        if len(q)==0:
            for x, y in dict.items():
                if(x==temp.data):
                    if(not y.left==None and not y.right==None):
                        dict[x].right=None
                    else:
                        dict[x].left = None
                if key_node:
                    key_node.data = temp.data
    return root

# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inorder(root)
    key = 10
    root = deletion(root, key)
    print()
    print("The tree after the deletion;")
    inorder(root)