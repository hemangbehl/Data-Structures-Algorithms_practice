def printrev( s ):
    stack = []
    for ele in s:
        if ele != " ":
            stack.append(ele)
        else:
            while stack != []:
                print( stack.pop() , end ="")
            print( end=" " ) #as ele is " "
    #end of for loop

    #handling the contents of the last word in stack
    while stack != []:
        print( stack.pop() , end ="" )

##driver code
s = "Geeks for Geeks"
print ("reverse of string:", s, " is:")
printrev( s )
