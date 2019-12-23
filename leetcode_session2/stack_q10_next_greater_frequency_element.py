def next_greatest_freq_element( arr ):
    stack = []
    ans = [None] * len ( arr)
    freq = {} #dict to store the counts

    for ele in arr:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1
    #start from end to start of list
    for i in range( len(arr)-1, -1, -1):
        ele = arr[i]
        while stack != [] and freq[ele] >= freq[ stack[-1] ]:
            stack.pop() #remove element of lower freq
        if stack == []:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        stack.append(ele)
    
    return ans

#driver code
print ( next_greatest_freq_element( [1, 1, 2, 2, 2, 3] ) )
