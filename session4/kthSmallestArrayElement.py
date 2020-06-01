import heapq

arr = 7, 10, 4, 3, 20, 15
k = 4

maxheap = []

for ele in arr:
    heapq.heappush(maxheap, -ele)

    if len(maxheap) > k:
        heapq.heappop(maxheap)
    
print(k, "th smallest element=", -maxheap[0] )
