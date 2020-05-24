def binarySearch(arr, x):
    n = len(arr)

    left, right = 0, n-1


    while left <= right:
        mid = ( left + right) // 2
        
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        else: #arr[mid] < x
            left = mid + 1
    
    return -1 #not found

arr = [1, 2, 3, 4, 5, 6, 10, 20]
print ( binarySearch(arr, 6) )
