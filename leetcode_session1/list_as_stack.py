# -*- coding: utf-8 -*-


stack = ['a','b','c','d','e','f']
print(stack)
stack.pop()
print(stack)

stack.append('f')
print(stack)


print("pop 1st element in list")
stack.pop(0)
print(stack)

stack_2 = stack.copy()
print (stack_2)

stack.pop()
print (stack)
print (stack_2)
stack[1]='ae'
print (stack[1])

print(stack)
print (stack_2)

print("checking shallow copy")
stack_2[1]='shallow'

print(stack)
print (stack_2)