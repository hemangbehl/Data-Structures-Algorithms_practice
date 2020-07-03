import heapq
def k_largest(arr, k):
    if len(arr) == 0:
        return
    if len(arr) == 1:
        return arr[0]
    
    minheap = []

    for ele in arr:
        heapq.heappush(minheap, ele)

        #maintain heap size
        if len(minheap) > k:
            heapq.heappop(minheap) #remove top most (smallest) element
    
    #top most ele in minheap is kth largest
    return minheap[0]

arr = [12, 14, 9, 50, 61, 41]
print(arr)
k=2
print( "kth largest ", k, "=", k_largest(arr,k ) )