#ref: https://www.includehelp.com/c/infix-to-postfix-conversion-using-stack-with-c-program.aspx
#ref: https://github.com/souvikhaldar/DSA-in-python-and-go/blob/master/stacks/infix_to_postfix_prefix.py

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1] #return last element
    
    def isEmpty(self):
        return self.stack == [] #empty list is []
    
    def printStack(self):
        return self.stack

def infixToPostfix(expr, stack):
    #takes expr a a string or list
    #stack is the list object
    operator = {'(':10,
                ')':10,
                '^':7, #added 
                '/':5,
                '*':5,
                '+':3,
                '-':3,
                }

    postfix = [] #empty list to store postfix expr

    for new in expr:
        if new not in operator.keys(): #an operand and not an operator
            postfix.append(new)
        elif new == '(': #special case
            stack.push('(')
        elif new ==')':
            #pop all until '('
            while stack.isEmpty() == False and stack.top() != '(':
                postfix.append(stack.pop())
            
            #top of stack is now '('
            stack.pop()
            #( and ) discarded
        elif stack.isEmpty() == True or stack.top() == '(':
            #push new initial operator if stack is empty or top is (
            stack.push(new)
        elif operator[new] > operator[stack.top()]: #high precendence
            #push
            stack.push(new)
        else: #last case, equal or low priority of new operator
            #pop first operator
            postfix.append(stack.pop())
            #pop all in stack with higher or equal priority than new operator
            while stack.isEmpty() == False \
                and operator[stack.top()] >= operator[new] \
                and stack.top() != '(':
                postfix.append ( stack.pop() )
            #now push new
            stack.push(new)
            
    #end of for loop
    #we reach the end of expr
    #pop remaining operators if any
    while stack.isEmpty() == False: #not empty
        postfix.append ( stack.pop() )
    
    return postfix

### driver code
# expr = 'a+b*(c-d)/e-f*g'
stack = Stack()
expr = "a+b*(c^d-e)^(f+g*h)-i"
postfix = infixToPostfix(expr, stack)
#convert list into string
postfix_str =  "" .join ( postfix )
print ("Postfix: ", postfix_str)
