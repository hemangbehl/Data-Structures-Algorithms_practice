def checkQueue( q1 ):
    q2 = []
    stack = []
    if len(q1) <=1:
        return False #yes it can be sorted
    while q1 != []:
        temp = q1.pop(0) #dequeue q1

        if q1 != [] and temp <= q1[0]: #as q1 was popped above
            q2.append(temp)
        elif stack == []:
            stack.append(temp)
        elif stack[-1] < temp:
            return False #cannot sort
        else:
            stack.append(temp)
    #end of while
    return True #since we reach the end, it can be sorted
    #to return back the sorted queue we can pop out the elements from stack
    #into q2
    while stack != []:
        q2.append(stack.pop())
    
##driver code
print ( checkQueue( [5, 1, 2, 6, 3, 4 ] ) )