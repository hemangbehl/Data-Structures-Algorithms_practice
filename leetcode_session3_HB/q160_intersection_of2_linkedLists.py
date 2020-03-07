class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        currA, currB = headA, headB
        changeA, changeB = 0, 0
        
        while currA != currB:
            if currA == None and changeA == 0:
                currA = headB
                changeA = 1
            else:
                currA = currA.next
            if currB == None and changeB == 0:
                currB = headA
                changeB = 1
            else:
                currB = currB.next            
            
        return currA   