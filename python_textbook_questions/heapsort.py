def percolateUp(arr, i):
    while ( (i-1)//2 ) >= 0:
        if arr[i] > arr[ (i-1)//2 ]:
            #child is greater than parent
            #swap them
            arr[i], arr[ (i-1)//2 ] = arr[ (i-1)//2 ], arr[i]
        
        i = (i-1)//2
    #end of while
    

def getMax(arr, i, n):
    #'n' is last index
    left = (i*2) +1
    right = (i*2) + 2

    if right > n:
        return left
    else:
        if arr[left] > arr[right]:
            #left child is greater than rt child
            return left
        else:
            return right
    
def percolateDown(arr, n):
    #'n' is last index of heap
    i = 0 #start from index 0 

    while (i*2 +1) <= n: #till left child exists
        mc = getMax(arr, i, n)

        if arr[i] < arr[mc]:
            #swap child and parent as child is greater
            arr[mc], arr[i] = arr[i], arr[mc] 
        # else:
        #     #rest of the heap is MaxHeap
        #     #so parent cannot be less
        #     break
        
        i = mc
    #end of while


def buildMaxHeap(arr):
    
    for i in range(0, len(arr) ):
        # print(" percUp {} index:{}".format(arr, i) )
        percolateUp( arr, i )


def heapSort(arr):
    #inplace heapsort
    last_index = len(arr) - 1

    buildMaxHeap(arr) #converts array into MaxHeap

    #reverse iterate and swap top of heap 
    # with last ele
    for j in range(last_index, -1, -1): #step -1
        arr[0], arr[j] = arr[j], arr[0]
        #go top-down and swap untill MaxHeap compliant
        percolateDown(arr, j-1) #do not include index of deleted element


#driver code
if __name__ == "__main__":
    arr = [1,8,2,4,3,565,87,12]
    print(arr)
    heapSort(arr)
    print("after sorting", arr)
