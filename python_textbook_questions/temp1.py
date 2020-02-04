rotset = set()
i = 0
j = 0
rotset.add( (i, j) )
rotset.add( (i, j) )
rotset.add( (i+1, j) )
rotset.add( (i, j+1) )

set2 =  (i,j+2)
rotset.add(set2)

print( rotset )

for ele in rotset:
    a = ele[0]
    b = ele[1]
    print(a, b)

# def countWays( arr,  n):
#     prevOneIdx = -1
#     numWays = 0
#     #for ( i = 0; i < n; ++i)
#     for i in range(0, n):
#         if arr[i] == '1':
#             if prevOneIdx != -1:
#                 numOnes = i - prevOneIdx
#                 numWays *= numOnes
#             else:
#                 # there is at least one in the input
#                 numWays = 1
#             prevOneIdx = i
#     return numWays

# #driver code

# arr = '10101'
# print ("num ways:", countWays(arr, len(arr) ) )
