def rotate90_ant(mat):
    m = len(mat)
    n = len(mat[0])
    i, j = 0, m-1

    while i < j:
        for col in range(0, n):
            mat[i][col], mat[j][col] = mat[j][col], mat[i][col]
        i += 1
        j -= 1
    
    row = m-1
    col = 0
    
    while row >= 0 and col < n:
        for i in range(1, m - col):
            mat[row-i][col], mat[row][col+i] = mat[row][col+i], mat[row-i][col]
        row -= 1
        col += 1
    
    return mat




mat =   [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
print(mat)
print( rotate90_ant(mat))
print("2nd example")
mat =   [[1,2,3],
        [4,5,6],
        [7,8,9] ]
print(mat)
print( rotate90_ant(mat))