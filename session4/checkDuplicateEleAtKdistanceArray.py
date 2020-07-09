def isduplicate(arr , k):
    if k == 0: return False
    if len(arr) <= 1: return False
    n = len(arr)
    window = set()
    l, r = 0, 0
    while l < (n-k) and r < n:
        if arr[r] in window: 
            return True
        else:
            window.add( arr[r] )
            r += 1
            if (r-l) > k:
                window.remove(arr[l])
                l += 1
    
    return False

arr = [1, 2, 3, 4, 1, 2, 3, 4] 
k = 4
print(isduplicate(arr, k))
