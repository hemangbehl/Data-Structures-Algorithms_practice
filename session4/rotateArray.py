arr = [1,2,3,4,5,6,7]

def rotateArr(arr, d, n = len(arr) ):
    curr = 0
    #arr2 = arr.copy() #duplicate array is created
    
    if d == 0: #no rotation
        return arr
    elif d > n: #handle overflow of rotation size
        d = d - n
    #else:
    temparr = []

    #store first d elements in temp array
    for i in range(0, d):
        temparr.append( arr[i] )
    
    #copy remaining elements d to n inplace in array
    for i in range(d, n):
        arr[curr] = arr[i]
        curr += 1
    
    #copy remaining elements from temp array to original array
    for ele in temparr:
        arr[curr] = ele
        curr += 1
    
    return arr

print(arr)

d = 9
print("Rotated array by ",d ,"= ", rotateArr(arr, d) )