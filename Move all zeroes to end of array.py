def move_zeroes(arr):
    n = len(arr)
    
    count = 0

    for i in range(0, n):
        if arr[i] != 0:
            arr[count] = arr[i]

            if i != count:
                arr[i] = 0

            count += 1

    return arr

arr = arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
print(arr)
print( move_zeroes( arr ) )