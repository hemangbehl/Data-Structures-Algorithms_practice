class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if head == None:
            return True
        
        if head.next == None:
            #len of list is 1, is a palindrome
            return True 
        
        curr = head
        slow = curr
        fast = curr
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow points to end of first half
        #second half
        second = slow.next
        #we reverse second half
        second = self.reverse(second)
        
        curr_second = second
        ans = True
        
        while curr and second:
            if curr.val != second.val:
                ans = False
                break #end loop
            curr = curr.next
            second = second.next
        
        #end of loop
        #put second half back
        curr_second = self.reverse(curr_second)
        
        #re-attach second half to first half
        slow.next = curr_second
        
        return ans

    def reverse(self, head):
        if head == None:
            return curr
        curr = head
        prev = None
        temp = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    