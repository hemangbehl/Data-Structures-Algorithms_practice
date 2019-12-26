'''
https://www.geeksforgeeks.org/expression-evaluation/
we need to convert infix to postfix and solve the postfix
expression inbetween. We use two stacks:
stack and var to store operators and variables respectively.

TC: O(n), 
SC: O(n)

'''
def operate(b, a, op):
    b = int(b)
    a = int(a)
    if op=='+':
        return b + a
    elif op=='-':
        return b - a
    elif op=='*':
        return b * a
    elif op=='/':
        return b // a
    elif op=='^':
        return b ^ a


def evaluateInfix( expr ):
    priority = {'+':1, '-':1, '*':2, '/':2,'^':3,'(':10,')':10}
    stack = [] #stores operators and brackets
    var = [] #stores variables

    expr2 = expr.split(" ")

    print("Input:", expr)
    print("after splitting:", expr2)

    for ele in expr2:
        if ele not in priority:
            #operand
            var.append(ele)
        elif ele=='(':
            stack.append('(')
        elif ele == ')':
            #pop until '(' is met
            while stack[-1] != '(':
                op = stack.pop()
                a= var.pop()
                b= var.pop()
                #print(b,a,op,operate(b, a, op) )
                var.append( operate(b, a, op) )
            #pop remaining '('
            stack.pop()
        else:
            #print("ele", ele)
            #operator
            #if intial operator or after opening bracket
            if stack==[] or stack[-1] == '(':
                #print("stack append", ele)
                stack.append( ele )
            #push if higher priority of new operator
            elif priority[ele] > priority[stack[-1]]:
                stack.append( ele )
            else: #new operator has less or equal priority
                while stack!=[] and \
                priority[ele] <= priority[stack[-1]]:
                    op= stack.pop()
                    a = var.pop()
                    b = var.pop()
                    #print(b,a,op,operate(b, a, op) )
                    var.append ( operate(b, a, op) )
                #push to stack after lower priority operators were popped
                stack.append(ele)
    #end of for loop
    #empty stack and use all operators if any were left
    #print("stack", stack)
    while stack != []:
        op= stack.pop()
        a = var.pop()
        b = var.pop()
        #print(b,a,op,operate(b, a, op) )
        var.append ( operate(b, a, op) )
    #var should have only one element in var
    return var.pop()

##driver code
expr = "100 * ( 2 + 12 ) / 14"
print ("evaluated answer of infix: ", evaluateInfix(expr))