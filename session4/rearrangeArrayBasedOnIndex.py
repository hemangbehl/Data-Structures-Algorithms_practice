def rearrange(arr):
    #need to rearrange array according to its index value

    n = len(arr)

    if n == 0:
        return -1
    
    # i = 0
    # while i < n:
    #     print("# ", end = " ")
    #     if arr[i] == -1 or arr[i] == i:
    #         #skip value as -1
    #         i += 1
    #     else:
    #         #swap values with the index contained within the ele
    #         arr[ arr[i] ], arr[i] = arr[i], arr[ arr[i] ]
    #         #index is not inceremented
    
    #optimzed TC: O(n) and SC: O(n) , using set

    set1 = set()

    for ele in arr:
        #adding to set
        set1.add(ele)
    
    #now loop and set avlue for each index present in set
    for i in range(0, n):
        if i in set1:
            arr[i] = i
        else:
            #not present
            arr[i] = -1
    
    return arr

arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4]

# arr = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
print(arr)
print ( rearrange(arr) )
