def getStackLen(stack, cnt = 0):
    #takes stack and current cnt of stack
    if stack != []:
        print ( " inc cnt",cnt+1)
        cnt += 1
        temp = stack.pop()
        cnt = getStackLen(stack, cnt)
        stack.append(temp)
        return cnt
    else:
        return cnt

def delMiddle(stack, del_i, cnt):
    #takes stack, index to delete, and len of stack
    if stack == []:
        return
    elif del_i == cnt:
        stack.pop()
        return
    else: #pop to reach del_i and 
        #then push elements back into the stack
        temp = stack.pop()
        cnt += 1
        delMiddle(stack, del_i, cnt)
        stack.append(temp)

##driver code
# stack = [1, 2, 3, 4, 5]
stack = [1, 2, 3, 4, 5, 6, 7]
print (stack)
cnt = getStackLen( stack )
i = (cnt//2)
print(i, cnt)
delMiddle(stack, i, 0)
print(stack)
