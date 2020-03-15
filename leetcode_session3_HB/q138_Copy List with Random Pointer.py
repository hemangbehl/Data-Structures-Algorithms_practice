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
        
        curr_old = head
        head_new = Node(curr_old.val, curr_old.next, None)
        curr_old.next= head_new
        curr_new = head_new.next
        
        
        
        #interweave/interlink orig and new lists
        while curr_new:
            next = curr_new.next
            new = Node(curr_new.val, None, None) #create a copy
                        
            curr_new.next = new
            new.next = next
            
            curr_new = curr_new.next.next
        
        #now set random pointers for each copy
        curr_old = head
        curr_new = head_new
        
        while curr_old:
            if curr_old.random: #if not None
                curr_new.random = curr_old.random.next
            
            curr_old = curr_new.next
            if curr_new.next:
                curr_new = curr_new.next.next
        
        #split the lists back to original and new copy
        curr_old = head
        curr_new = head_new
        
        while curr_old:
            curr_old.next = curr_new.next
            if curr_new.next: #if not None
                curr_new.next = curr_new.next.next

            curr_old = curr_old.next
            curr_new = curr_new.next
        
        return head_new
        # if not head:
        #     return None
        
        # curr = head
        # prev = None
        # new = None
        # new_head = None
        # dict_new = {} #stores index of pointers
        
        # while curr:
        #     #check for current pointer
        #     if curr not in dict_new:
        #         #create new node
        #         new = Node(curr.val, None, None) #next None, random None
        #         #add to dict
        #         dict_new[curr] = new
        #         if new_head == None: #no new head is set
        #             new_head = new
        #     else:
        #         new = dict_new[curr]
            
        #     #check for new pointer
        #     if curr.next and curr.next not in dict_new:
        #         new_next = Node(curr.next.val, None, None )
        #         new.next = new_next
        #         #add to dict
        #         dict_new[curr.next] = new_next
        #     else:
        #         new.next = dict_new.get(curr.next, None)
            
        #     #check for random pointer
        #     if curr.random and curr.random not in dict_new:
        #         new_random = Node(curr.random.val, None, None )
        #         new.random = new_random
        #         #add to dict
        #         dict_new[curr.random] = new_random
        #     else:
        #         new.random = dict_new.get(curr.random, None)
            
        #     curr = curr.next #advance pointer in original list
        # #end of loop
        
        # return new_head
