def find_celeb(arr):

    ## Time Complexity = O(3n) = O(n)
    ## SC = O(n)

    '''for lintcode
    arr = []
    for i in range (0, n):
        arr.append (i)
    '''
    # HaveAxq(a, b) becomes Celebrity.knows(a, b)

    if len(arr) < 1:
        return -1
    #create a stack
    stack = []
    for ele in arr:
        stack.append(ele)
    
    #check 2 elements in stack till 1 remains
    while len(stack) != 1:
        a = stack.pop()
        b = stack.pop()
        if HaveAcq(a, b) == True:
            #'a' cannot be a celeb, but 'b' can
            stack.append(b)
        else:
            #'b' cannot be a celeb but 'a' can
            stack.append(a)
    #end of while loop
    rem = stack.pop()

    #check the rest against rem
    for ele in arr:
        # if ele == rem:
        #     #skip if same element
        #     continue
        #else
        if HaveAcq(ele, rem) == False: #rem is not a celeb as ele doesn't know rem
            return -1
    #end of for loop
    #'rem' is a celeb as everyone else know 'rem'
    return rem

#dummy
def HaveAcq(i, j):
    return False

#driver code
print ( find_celeb ( [0, 1] ))