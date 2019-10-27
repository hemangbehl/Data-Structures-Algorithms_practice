def binarysearch(list1, left, right, x):
    while (left <= right):

        mid = (left + right) // 2 #remove floating point by rounding
        #print ("mid: ",mid)
        #check if mid is x
        if (list1[mid] == x):
            return mid #return index of 'x'

        elif list1[mid] < x:
            #x is greater, so ignore left half
            left = mid + 1
        else:
            #x is less and ignore right half
            right = mid -1
        #print(left, right)
    return -1



list1 = [1,4,235,545,781]
x = 781
print(binarysearch(list1,0, len(list1)-1 , x))
#print(list1[4])