def infixToPrefix(expr):
    #takes string as infix expr
    op_stack = []
    expr_stack = []
    priority = { '+':1, '-':1, '*':2, '/':2, '^':3 }
    brackets = set( ['(', ')'] )

    for ele in expr:
        if ele not in priority and ele not in brackets:
            #simple operand-alphabet
            #push in to expr stack
            expr_stack.append(ele)
        elif ele == '(':
            op_stack.append(ele)
        elif ele == ')':
            #loop until '('
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = expr_stack.pop()
                b = expr_stack.pop()
                expr_stack.append( op + b + a )
            op_stack.pop() #pop and ignore '('
        else:
            #only operators
            while op_stack != [] and op_stack[-1] != '(' \
            and priority[ele] <= priority[ op_stack[-1] ]:
                op = op_stack.pop()
                a = expr_stack.pop()
                b = expr_stack.pop()
                expr_stack.append( op + b + a )
            op_stack.append(ele) #push current operator into op_stack
    #end of for loop

    #handle remaining operators
    while op_stack != []:
        op = op_stack.pop()
        a = expr_stack.pop()
        b = expr_stack.pop()
        expr_stack.append( op + b + a )

    return expr_stack.pop()

#driver code
expr = "(A-B/C)*(A/K-L)"
#expr = "1+(3+4*6+6*1)*2/3"
print ("Prefix of infix expr is: ", infixToPrefix(expr))