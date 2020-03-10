class Solution:
    def closestValue(self, curr: TreeNode, target: float) -> int:
        if curr == None:
            return None
        
        closest = curr.val #initial
        
        while curr:
            #change closest only when it is closer than before
            if abs(target - curr.val) < abs(target - closest):
                closest = curr.val
            #else: closest
            
            if target < curr.val:
                curr = curr.left #check left
            else:
                curr = curr.right #check right
        #end of while loop
        
        return closest
