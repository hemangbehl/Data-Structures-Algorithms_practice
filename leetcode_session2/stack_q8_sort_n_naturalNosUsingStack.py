def checkQueue( q1):
    stack = []
    ele = 0
    expected = 1 #as we expect natural nos

    if q1 == []:
        return False

    while q1 != []:
        ele = q1[0] #get front element
        #print(ele, expected)
        
        if ele == expected:
            #print("expected found in q1",ele, expected)
            expected += 1
            q1.pop(0)
        elif stack == []:
            stack.append( ele )
            q1.pop(0)
        elif stack[-1] < ele:
            #invalid, cannot sort
            return False
        else: #top of stack is greater than
            stack.append(ele)
            q1.pop(0)
        
        while stack != [] and stack[-1] == expected:
            stack.pop()
            expected += 1
            
    if stack == []:
        return True
    else:
        #print("stack is not empty")
        return False

##driver code
q1 = [7,6,5,4,3,2,1]
print ( checkQueue( [5, 1, 2, 6, 3, 4 ] ) )