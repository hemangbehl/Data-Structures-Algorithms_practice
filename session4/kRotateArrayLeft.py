def rev(arr, i, j):
    #in place reverse array
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def krotateleft(arr, k):
    if len(arr) <= 1: return arr
    k = k % len(arr)
    if k <= 0: return arr
    n = len(arr)
    rev(arr, 0, n-1)
    rev(arr, 0, n-k-1)
    rev(arr, n-k, n-1)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
print( krotateleft( arr, 2) )