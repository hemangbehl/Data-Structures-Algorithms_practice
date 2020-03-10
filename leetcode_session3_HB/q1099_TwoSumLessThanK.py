class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
        left = 0
        right = len(A) - 1
        
        if right <= 1:
            return -1
        
        A.sort() #in-place sort        
        ans = -1
        
        while left < right:
            if A[left] >= K:
                #no need to check further as left pointer is higher than K
                break
                
            if A[left] + A[right] < K:
                
                if A[left] + A[right] > ans:
                    ans = A[left] + A[right]
                left += 1
                
            else: # A[left] + A[right] > K:
                right -= 1
        
        return ans
            