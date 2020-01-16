class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
          if self.heapList[i] > self.heapList[i // 2]:
             #if child is greater than parent, swap them
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self, ele):
      self.heapList.append(ele)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self, i):
      while (i * 2) <= self.currentSize:
          mc = self.maxChild(i)
          if self.heapList[i] < self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self, i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1
        
    def maxChild(self, i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] > self.heapList[i*2+1]:
              #left child is greater than rt child
              return i * 2
          else:
              return i * 2 + 1

    def delTopOfHeap(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self, arr):
      i = len(arr) // 2
      self.currentSize = len(arr)
      self.heapList = [0] + arr[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])
print( "HeapList is: ", bh.heapList[1:] )
print(bh.delTopOfHeap())
print(bh.delTopOfHeap())
print(bh.delTopOfHeap())
print(bh.delTopOfHeap())
print(bh.delTopOfHeap())
