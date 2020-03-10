class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                #reset candidate, disregard equal no. of candidate and non-candidate pairs
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

#         n = len(nums)
        
#         if n <= 2: 
#             return nums[0]
        
#         maxnum = nums[0]
#         dictnum = { nums[0]:1 }
#         key = 0 
        
#         for i in range(1, n):
#             #add or inc to dict
#             key = nums[i]
#             dictnum[key] = dictnum.get(key, 0) + 1
            
#             if dictnum[key] > dictnum[maxnum]:
#                 maxnum = key
#             if dictnum[maxnum] > (n//2):
#                 return maxnum
            
#         return maxnum