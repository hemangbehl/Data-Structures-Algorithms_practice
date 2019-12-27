def delsmallertonext(arr, k):
    stack = []
    if len(arr) < 2:
        return arr
    stack.append(arr[0])
    cnt = 0
    for i in range(1, len(arr)):
        while stack!=[] and cnt<k:
            if stack[-1]<arr[i]:
                stack.pop()
                cnt +=1
            else:
                break
        #end of while loop
        stack.append(arr[i])
    #end of for loop

    #empty the contents of stack into an array
    arr2 = []
    if cnt ==0:
        return [None]
    else:
        while stack != []:
            arr2.append( stack.pop() )
        arr2 = arr2[::-1] #reverse the array
        return arr2

## driver code
arr = [23, 45, 11, 77, 18]
print(arr)
print ( delsmallertonext(arr, 3) )