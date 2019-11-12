#ref: https://www.includehelp.com/c/infix-to-postfix-conversion-using-stack-with-c-program.aspx

def infixToPostfix( expr):
    #takes expr a a string or list

    stack = [] #empty stack
    operator = {'(':10,
                ')':10,
                '^':7, #added 
                '/':5,
                '*':5,
                '+':3,
                '-':3,
                }

    for new in expr:
        if new not in operator.keys(): #an operand and not an operator
            print(new)
        elif new == '(': #special case
            stack.append('(')
        elif new ==')':
            #pop all until '('
            while len(stack) != 0 and stack[-1] != '(':
                print(stack.pop())
            
            #top of stack is now '('
            stack.pop()
            #( and ) discarded
        elif len(stack) == 0 or stack[-1] == '(':
            #push new initial operator if stack is empty or top is (
            stack.append(new)
        elif operator[new] > operator[stack[-1]]: #high precendence
            #push
            stack.append(new)
        else: #last case, equal or low priority of new operator
            #pop first operator
            print(stack.pop())
            #pop all in stack with higher or equal priority than new operator
            while len(stack) != 0 \
                and operator[stack[-1]] >= operator[new] \
                and stack[-1] != '(':
                print ( stack.pop() )
            #now push new
            stack.append(new)
            
    #end of for loop
    #we reach the end of expr
    #pop remaining operators if any
    while len(stack) != 0: #not empty
        print ( stack.pop() )
        

### driver code

# expr = 'a+b*(c-d)/e-f*g'

expr = "a+b*(c^d-e)^(f+g*h)-i"

infixToPostfix(expr)
