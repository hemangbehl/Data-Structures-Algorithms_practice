def reverse(arr, i, j):
    #in place reverse array
    while i < j:
        arr[i], arr[j] = arr[j], arr[i] #swap both elements
        i += 1 #inc
        j -= 1 #dec
    

def rotate_array_right(arr, k):
    
    n = len(arr)
    if k > n:
        k = k % n
    
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)

    return arr

arr = [1,2,3,4,5,6,7]

print(arr)
k = 9
print("Rotated array by ", k, "= ", rotate_array_right(arr, k) )