def rearrange(arr):
    n = len(arr)

    if n == 0:
        return
    if n == 1:
        return arr
    
    arr2 = arr.copy() #deep copy
    arr2.sort() #inplace sort asc

    left = 0 #to get smallest num
    right = n-1 #to get greatest num
    i = n-1 #travering arr in reverse order
    
    while left <= right and i>= 0:
        if n%2 == 0: #even 2 ele will always be present
            arr[i] = arr2[right]
            arr[i-1] = arr2[left]
        else: #odd, 1 will ele remain
            if i == 0: #remaining ele
                arr[0] = arr2[left]
            else:
                arr[i] = arr2[left]
                arr[i-1] = arr2[right]

        left += 1
        right -=1
        i -= 2 #decrement index for populating arr by 2

    return arr

# arr = [ 1, 2, 3, 4, 5, 6, 7 ]
arr = [1, 2, 1, 4, 5, 6, 8, 8]

print(arr)
print( rearrange(arr) )
