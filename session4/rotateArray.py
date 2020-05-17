arr = [1,2,3,4,5,6,7]

def rotateArr(arr, d, n = len(arr) ):
    curr = 0
    #arr2 = arr.copy() #duplicate array is created
    
    if d == 0: #no rotation
        return arr
    else:
        arr2 = [None] * n

    for i in range(d, n):
        arr2[curr] = arr[i]
        curr += 1 #increment arr
    
    #copy remaining elements
    for i in range(0, d):
        arr2[curr] = arr[i]
        curr += 1
    
    return arr2

print(arr)
d= 2
print("Rotated array by ",d ,"= ", rotateArr(arr,d) )