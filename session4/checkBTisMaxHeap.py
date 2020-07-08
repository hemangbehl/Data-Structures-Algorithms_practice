from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def checkMaxHeap(head):
    if not head: return False
    last_level = 0
    queue = deque()
    queue.append( head )
    curr = head
    i = 0
    while queue:
        if last_level == 1: return False
        if ( 2**i) != len(queue):
            last_level = 1
        for j in range( len(queue) ):
            curr = queue.popleft()
            if curr.left:
                if curr.val < curr.left.val: return False
                queue.append( curr.left )
            if curr.right:
                if curr.val < curr.right.val: return False
                queue.append( curr.right )
        i += 1
    
    return True

root = Node(10)
root.left, root.right = Node(8), Node(9)
root.left.left, root.left.right = Node(5), Node(5)
# root.left.left.left = Node(1)

print( checkMaxHeap(root) )