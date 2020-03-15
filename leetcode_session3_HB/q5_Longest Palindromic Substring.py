class Solution:
    def longestPalindrome(self, s: str) -> str:
        #loop and set middle from start 0 to last index of len(s)-1 and check for palindrome
        
        if len(s) == 0:
            return ""
        
        ans = ""
        temp = ""
        
        for i in range(0, len(s)):
            #check for odd case, center index is the same
            temp = self.checkPalindrome(s, i, i)
            if len(temp) > len(ans):
                ans = temp
            
            #even case, middle indices are i and i+1
            temp = self.checkPalindrome(s, i, i+1)
            if len(temp) > len(ans):
                ans = temp
        
        #end of loop
        
        return ans
        
    def checkPalindrome(self, s, left, right):
        #expand from middle indices left and right
        
        #check if indices are out of bounds and the char at each index is the same to be a palindrome
        while (left >= 0 and right < len(s) and s[left] == s[right] ):
            
            left -= 1 #expand left
            right += 1 #expand right
        
        return s[left + 1 : right] # left+1 to right-1
        
        