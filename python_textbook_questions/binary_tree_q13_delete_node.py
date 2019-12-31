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
    
    def delete_node(self, del_data):
        if self.root == None:
            return
        del_node = 0
        prev = 0
        curr = 0
        dir_prev = 0
        queue = [self.root]
        while queue != []:
            curr = queue.pop(0)
            if curr.data == del_data:
                del_node = curr
            if curr.left!= None:
                prev = curr
                dir_prev = 'l'
                queue.append(curr.left)
            if curr.right!= None:
                prev = curr
                dir_prev = 'r'
                queue.append(curr.right)
        #end of while
        if del_node == 0:
            #node to delete not found in tree
            return
        #else del node exists
        #curr is the last deepest node with no children --> a leaf node
        if del_node == curr == self.root:
            #single node tree. root is the del_node and last node
            self.root = None
            del del_node
            del curr
            return
        else:
            #del_node can be last node or in middle of tree
            del_node.data = curr.data #copy curr data into del_node
            
            #destroy links to del_node using prev node and its direction
            if dir_prev == 'l':
                prev.left = None
                del curr
            else: #right direction of prev node
                prev.right = None
                del curr
        #end of def delete_node()

##driver code
bt = BinaryTree()
bt.root = Node('1')
# bt.root.left = Node('2')
# bt.root.right = Node('3')
bt.print()
bt.delete_node('1')
bt.print()
