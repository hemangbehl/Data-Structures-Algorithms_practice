def getpair(arr):
    if len(arr) <= 1: return -1
    if len(arr) == 2: return arr[0], arr[1]

    arr.sort()
    n = len(arr)
    left = 0
    right = n-1
    a, b = arr[left], arr[right]
    minsum = c = abs ( a + b )
    while left < right:
        c = abs ( arr[left] + arr[right] )
        if c < minsum:
            minsum = c
            a, b = arr[left], arr[right]
        
        if c == 0: return a,b
        if c < 0:
            left += 1
        elif c > 0:
            right -= 1
    
    return a,b

arr = [1, 60, -10, 70, -80, 85]
print (arr)
print( getpair(arr) )