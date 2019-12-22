def calc_span( price ):
    #price is a list containing daily prices of the stock
    span = [None] * len(price)
    stack = [] #stack to hold indexes

    #intially first element has a span of 1
    span[0] = 1 #intialize starting index to have span of 1
    stack.append (0) #index 0 is added as default

    #loops starts from index 1
    for i in range(1, len(price) ):
        #loop if stack is not empty and price of stack.top() is less
        # than price of current index
        while stack != [] and ( price[ stack[-1] ] <= price[i] ):
            stack.pop() #pop index from stack as it is lesser
        
        if stack == []:
            span[i] = i + 1 #inrement span for current index
            #               as it is larger than all previous prices
        else:
            # subtract index from the top most value of stack
            # as that price is higher
            span[i] = i - stack[-1]
        
        stack.append(i) #push current index to stack
    #end of for loop
    return span
        



print ( calc_span( [10, 4, 5, 90, 120, 80] ) )