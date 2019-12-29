#import package to use deque
import collections

de = collections.deque( [1,2,3] )
print("initial state of deque", de)
de.append(5) #appends to the end of the list
print ("after appending to right:", de)

de.appendleft(6)
print("after appending to the left", de)

print("Popped element from left using .pop():", de.pop() )
print (de)

print("peek first element", de[0])
print("peek last element", de[-1])
