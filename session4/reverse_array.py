def reverse(arr):

    n = len(arr)

    if n ==0:
        return -1
    
    left, right =0, n-1

    while left < right:
        #swap values at both the indexes
        arr[left], arr[right] = arr[right], arr[left]

        #inc and dec indexes
        left += 1
        right -= 1
    
    return arr

def recursive_reverse(arr, left, right):
    #in-place operation

    if left >= right:
        return
    #else
    #swap values
    arr[left], arr[right] = arr[right], arr[left]
    arr = recursive_reverse(arr, left+1, right-1)
    #return arr

arr = [4, 5, 1, 2]
print(arr)
# print ( reverse(arr) )
recursive_reverse(arr, 0, len(arr)-1)

print(arr)