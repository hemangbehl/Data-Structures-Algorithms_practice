"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        curr = head
        prev = None
        new = None
        new_head = None
        dict_new = {} #stores index of pointers
        
        while curr:
            #check for current pointer
            if curr not in dict_new:
                #create new node
                new = Node(curr.val, None, None) #next None, random None
                #add to dict
                dict_new[curr] = new
                if new_head == None: #no new head is set
                    new_head = new
            else:
                new = dict_new[curr]
            
            #check for new pointer
            if curr.next and curr.next not in dict_new:
                new_next = Node(curr.next.val, None, None )
                new.next = new_next
                #add to dict
                dict_new[curr.next] = new_next
            else:
                new.next = dict_new.get(curr.next, None)
            
            #check for random pointer
            if curr.random and curr.random not in dict_new:
                new_random = Node(curr.random.val, None, None )
                new.random = new_random
                #add to dict
                dict_new[curr.random] = new_random
            else:
                new.random = dict_new.get(curr.random, None)
            
            curr = curr.next #advance pointer in original list
        #end of loop
        
        return new_head
