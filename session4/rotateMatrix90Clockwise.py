def rotate(mat):
    rotated = []
    row = len(mat)
    col = len( mat[0] )

    for i in range(col):
        new_row = []
        for j in range(row -1, -1, -1):
            new_row.append( mat[j][i] ) #
        rotated.append( new_row )
    
    return rotated

mat =   [[1,2,3,4,5],
        [6,7,8,9,1],
        [1,2,3,3,2]]
print(mat)
print( rotate(mat))