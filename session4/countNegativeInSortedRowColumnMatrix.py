def countNegative(mat):
    if len(mat) == 0: return 0
    m = len(mat)
    n = len(mat[0])
    cnt = 0
    i = 0
    j = n-1
    while i < m and j >= 0:
        ele = mat[i][j]
        if ele < 0:
            i += 1
            cnt = cnt + (j+1)
        else:
            j -= 1
    
    return cnt

M = [  
      [-3, -2, -1,  1], 
      [-2,  2,  3,  4], 
      [ 4,  5,  7,  8] 
    ] 
print(countNegative(M) ) 