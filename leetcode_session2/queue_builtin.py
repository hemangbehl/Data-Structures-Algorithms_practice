from queue import Queue

a = Queue()

print (a)
print("size", a.qsize())
a.put(1)
a.put(2)
a.put(3)
print(a)
a.get() #removes and returns an item
print ("size", a.qsize())
 
#print queue
for i in range(a.qsize()):
    print (a.get())
