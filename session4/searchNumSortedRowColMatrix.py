def checknum(mat, target):
    if len(mat) == 0: return False
    row = 0
    col = len(mat[0]) - 1
    while row < len(mat) and col >= 0:
        print(mat[row][col])
        if mat[row][col] == target:
            return row, col
        elif mat[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

mat =   [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
print(mat)
print( checknum(mat, 6))