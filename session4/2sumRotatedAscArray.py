def getPivotLargest(arr):
    left = 0
    right = len(arr) - 1 #last index

    while left <= right:
        mid = (left + right) // 2
        
        if arr[left] < arr[right]:
            return 0 #no rotation
        if arr[mid] > arr[mid+1]:
            return mid #mid has the largest num
        elif arr[left] < arr[mid]:
            #left part is unbroken
            left = mid + 1
        else:
            #right part is unbroken
            right = mid - 1

def search2sum(arr, target):

    if len(arr) == 0 or len(arr) == 1:
        return False
    if len(arr) == 2:
        if ( arr[0] + arr[1] ) != target:
            return False
        else:
            return True
    n = len(arr)


    pivot = getPivotLargest(arr)

    if pivot == n-1:
        #no break in array
        left = 0
        right = n - 1 #last index
    else: #array has rotation
        left = pivot + 1
        right = pivot
    
    #now search for pair
    while left != right:

        mid = (left + right) // 2

        if ( arr[left] + arr[right] ) == target:
            return True
        
        elif ( arr[left] + arr[right] ) < target:
            left = (left + 1) % n
        else:
            right = (right - 1) % n
    
    return False

arr = [11, 15, 26, 38, 9, 10] 
sum = 26
  
if ( search2sum(arr, sum) ): 
    print ("Array has two elements with sum", sum) 
else: 
    print ("Array doesn't have two elements with sum", sum) 
      