def searchRotatedArray(arr, target):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if target == arr[0] else -1
    
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = ( left + right ) // 2 #get mid point by ceiling decimal

        #check for target
        if arr[mid] == target:
            return mid
        
        #check if left partition is conesecutively in asc order
        elif arr[left] <= arr[mid]:
            
            #now check if target exists within this unbroken asc partition
            if arr[left] <= target < arr[mid]:
                #check within the left part
                right = mid - 1 #reduce right boundary to mid-1
            else: #target is in the right part
                left = mid + 1 #reduce left boundary to mid+1
        
        else: #right part is unbroken and in asc order
            
            #check if target exists within right part
            if arr[mid] < target <= arr[right]:
                #check within right itself
                left = mid + 1
            else: #target is in the left partition
                right = mid - 1
        
    #if while loop ends without returning, taget does not exist
    return -1
    
    



arr = [4,5,6,7,0,1,2]

print (arr)
target = 0
print("target exists at", searchRotatedArray(arr, target) )
