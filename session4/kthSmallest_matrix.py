import heapq

def ksmallest(mat, k):
    if len(mat) == 1:
        return mat[0][0]

    n = len(mat)    
    minheap = []

    #loop and all elements of 1st column into minheap
    for i in range(0, min(k, n) ):
        heapq.heappush(minheap, ( mat[i][0], i, 0 ) )
    
    #now pop n add new elemnts
    i = 0
    while i < k:
        ele, row, col = heapq.heappop(minheap)

        if col < (n-1):
            heapq.heappush(minheap, ( mat[row][col+1], row, col+1 ) )

        i += 1

    #return last popped ele
    return ele

matrix = [  [ 1,  5,  9],
            [10, 11, 13],
            [12, 13, 15]  ]
k = 8

print(k, "th smallest num=", ksmallest(matrix,k) )
