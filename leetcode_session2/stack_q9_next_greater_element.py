def get_NGE( arr ):
    #NGE = next greater element in an array

    if len(arr) == 0:
        return -1

    stack = []
    ans = [None] * len(arr)

    #iterate list in reverse order
    for i in range( len(arr)-1, -1, -1 ):
        ele = arr[i]
        
        while stack != [] and ele > stack[-1]:
            stack.pop() #remove lesser element from stack
        
        if stack == []: #ele is the greatest element and ans is -1
            ans[i] = -1
        else:   #ele is less than the top of stack which is the ans
            ans[i] = stack[-1]
        
        stack.append(ele)
    #end of for loop
    print ("input: ", arr)
    return ans
    
""" Time Complexity = O(n)
as each element is atmost pushed and popped from the stack once. This is a 
constant and as such while loop is O(c) being a constant.
Space Complexity: O(n) as stack is required
"""

print (get_NGE( [ 13, 21, -1, 11, -1 ] ))