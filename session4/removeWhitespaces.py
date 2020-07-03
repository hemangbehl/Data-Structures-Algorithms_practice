def removespace(arr):
    if len(arr) == 0: return ""
    w = -1
    
    for c in range( len(arr) ):
        if arr[c] == " " and w == -1:
            w = c
        elif arr[c] != " " and w != -1:
            arr[c], arr[w] = arr[w], arr[c]
            w += 1
    
    if w == -1: return arr
    else: return arr[:w]

print( removespace( ["a"," ", " ", "", "d", "  "] ) )
