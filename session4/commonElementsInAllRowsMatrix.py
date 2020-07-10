def getCommon(amt):
    if len(mat) == 0: return None
    m = len(mat)
    n = len(mat[0])
    common = set(mat[0])
    temp = set()

    for i in range(m):
        temp = set()
        for j in range(n):
            if mat[i][j] in common:
                temp.add( mat[i][j] )
        if len(temp) == 0: return None
        common = temp
    
    return common

mat = [[1, 2, 1, 4, 8], 
       [3, 7, 8, 5, 1], 
       [8, 7, 7, 3, 1], 
       [8, 1, 2, 7, 9]] 

print( getCommon(mat) )