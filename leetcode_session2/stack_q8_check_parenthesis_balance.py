def check_brackets_balance(expr):
    stack = []
    opening = set([ '(', '[', '{' ])
    brackets = { ')':'(', '}':'{', ']':'[' }

    for ele in expr:
        if ele in opening:
            stack.append(ele)
        elif stack == []: #empty stack
            return 0 #closing bracket without opening
        elif stack.pop() != brackets[ele]:
            return 0 #imbalanced brackets
        else: #matching brackets
            continue
    #end of for loop

    if stack == []:
        return 1
    else:
        return 0

#driver code
print ( check_brackets_balance( '{()}[]' ) )