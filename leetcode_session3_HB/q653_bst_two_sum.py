class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        #inorder traversal dfs
        
        ans = self.traversal(root, set(), k)
        return ans
    
    def traversal(self, curr, num_set, target):
        if not curr:
            return None
        
        if (target - curr.val) in num_set:
            return True
        
        num_set.add( curr.val )
        
        if curr.left:
            #check left sub tree
            if self.traversal(curr.left, num_set, target):
                return True
        
        if curr.right:
            #check right sub tree
            if self.traversal(curr.right, num_set, target):
                return True
        
        return False
        