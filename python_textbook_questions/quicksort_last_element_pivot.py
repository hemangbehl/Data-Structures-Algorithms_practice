def quicksort(arr, low, high):
    #does inplace sort
    if low < high: #atleast 2 elements
        #get partition index
        pi = partition(arr, low, high)

        #call quicksort again for left and right parts
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

def partition(arr, low, high):
    #set pivot as last ele, high
    pivot = arr[high]
    #set index i for smaller element as low-1
    i = low - 1
    print("partition", )
    for j in range(low, high): # j = low, j < high
        #check if curr ele 'j' is < pivot
        print("curr:{}, pivot:{}".format(arr[j], pivot ) )
        if arr[j] < pivot:
            #inc 'i' and swap i and j elements
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            print("swapped", arr)
    #end of for

    #inc 'i' and swap pivot
    i = i + 1
    arr[i], arr[high] = arr[high], arr[i]

    return i #this is the partition index

#driver code
if __name__ == "__main__":
    arr = [1,8,2,4]
    print(arr)
    quicksort(arr, 0, len(arr)-1 )
    print("after sorting", arr)