class Stack:
    def __init__(self):
        self.stack = []
    def push(self, ele):
        self.stack.append(ele)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
    def isEmpty(self):
        return self.stack == []
    def printStack(self):
        for i in range (0, len (self.stack) ):
            print (self.stack[i])

#alone function
def postToPre(expr, stack):
    operators = set ( [ '+', '-', '/', '*', '^' ] )
    a = ''
    b = ''
    for ele in expr:
        if ele not in operators:
            stack.push(ele)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.push(ele + b + a)
    
    return stack.pop()

#driver code
#expr = "AB+CD-*"
expr = "ABC/-AK/L-*"
stack = Stack()
# stack.printStack() #doesn't print anything as it is empty
print ( "Prefix of postfix expr is: ", postToPre(expr, stack) )