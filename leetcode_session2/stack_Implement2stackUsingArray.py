class twoStack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        #range of arr is [0,size-1]
        self.top1 = -1
        self.top2 = size
    
    def push1(self,ele):
        if self.top1 < self.top2 - 1:
            self.top1 +=1
            self.arr[self.top1] = ele
        else:
            print("Overflow")
            return
    def push2(self, ele):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = ele
    