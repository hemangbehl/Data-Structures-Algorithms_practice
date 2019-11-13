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

def preToInfix(expr):
    stack = Stack()
    expr = expr[::-1]

    operator = set( [ '+','-','/','*','^' ] )

    for new in expr:
        if new not in operator: #is an operand
            stack.push(new)
        else: #operator
            stack.push( stack.pop() + new + stack.pop() )

    return stack.pop()


### driver code

expr = "*+AB-CD"
# expr = "+1/*++3*46*6123"
infix = preToInfix(expr)

print ("Prefix: ", infix)
