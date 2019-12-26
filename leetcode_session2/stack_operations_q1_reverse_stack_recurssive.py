''' TC: O(n^2) as we call O(n) to insertatbottom for each 'n' element
'''
def insertBottom(stack, old):
    if stack != []:
        new = stack.pop()
        insertBottom(stack,old)
        stack.append(new)
    else:
        stack.append(old) #add the old element
                        #to the bottom of the empty 
                        #stack

def revStack(stack):
    if stack != []:
        a = stack.pop()
        revStack(stack)
        insertBottom(stack, a) #move 'a' to the bottom
    else:
        return

##driver code
stack = [1,2,3,4,5]
print (stack)
revStack(stack)
print(stack)