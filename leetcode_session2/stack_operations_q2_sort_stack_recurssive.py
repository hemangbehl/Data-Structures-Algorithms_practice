def sortedInsert(st, old):
    if st!=[] and old < st[-1]:
        #old ele is less than top of stack
        #so we check again with n-1 element of stack
        temp = st.pop()
        sortedInsert(st, old) #check with below element
        st.append(temp) #now add temp to top of stack
    else:
        st.append(old) #no match or stack is empty
                    # so we add old ele back

def sortStack(st):
    #call sortStack 'n-1' times
    #each call of sortStack then calls sortedInsert O(n) times
    if st != []:
        a = st.pop()
        sortStack(st) #call for rest of n-1 elements
        sortedInsert(st, a) #check and insert
    else:
        return

##driver code
stack = [-3, 14, 18, -5, 30]
print(stack)
print("top of stack", stack[-1])
sortStack(stack)
print(stack)
