class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = [] #to store answer
        n = len(nums)
        total = 0
        left, right = 0, n-1
        
        #sort the array
        nums.sort()
        
        for i in range(0, n-2): #loop from i to n-3
            
            if nums[i] > 0:
                #no need to check further as array is sorted
                break
            if i >= 1 and nums[i] == nums[i-1]:
                #skip current iteration as same no.
                continue
            
            left = i + 1 #left will be after current no. nums[i]
            right = n - 1 #right will be the last index
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    #decrement right index
                    right -= 1
                
                elif total < 0:
                    #increment left index
                    left += 1
                    
                else: #total == 0
                    ans.append( [ nums[i], nums[left], nums[right] ] )
                    
                    #check for same repeating nos.
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1 
                    right -= 1
        #end of for loop
        
        return ans