'''
TC: O(n^2) , n squared coz in the worst case, we will push all the 
elements to the temp stack.
SC: O(n), as we have a temp stack, s2
'''
def sortStackUsingTempStack(s1):
    s2 = [] #empty
    if s1 == []:
        return s1
    temp = 0
    s2.append( s1.pop() ) #move s1 top to s2

    while s1!=[]: #s1 is not empty
        if s1[-1] >= s2[-1]: #s1 is greater or equal
            #move top s1 to s2
            s2.append(s1.pop())
        else: #s1 top is lesser
            temp = s1.pop()
            while s2 != [] and temp < s2[-1]:
                #keep shifting top s2 to s1 if less than temp
                s1.append( s2.pop() )
            #end of inner loop
            s2.append(temp) #add the lesser element
    #end of outer while
    return s2 #in ascending order

##driver code
stack = [34, 3, 31, 98, 92, 23]
print (stack)
print ( sortStackUsingTempStack(stack) )