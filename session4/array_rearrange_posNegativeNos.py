def rearrange(arr):
    n = len(arr)

    if n == 0:
        return
    if n == 1:
        return arr
    
    i = -1 #initially set as -1 to count negative nos

    #place all negative nums at the beginning
    for j in range(0, n):
        if arr[j] < 0:
            #negative num
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    pos = i + 1
    neg = 0 #set as starting ele

    while pos < n and neg < pos and arr[neg] < 0:
        #swap pos and neg
        arr[neg], arr[pos] = arr[pos], arr[neg]

        pos += 1
        neg += 2 #inc by 2 as we keepp swapping alt locations of the negative nums
    
    return arr

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
print(arr)
print ( rearrange(arr) )
