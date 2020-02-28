class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = [None] * 2029    #list * prime no. 2029
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % 2029
        
        if self.hashmap[index] == None:
            self.hashmap[index] = [ [key, value] ]
        else:
            for pair in self.hashmap[index]:
                if pair[0] == key:
                    pair[1] = value #update val
                    return
            
            #append key val
            self.hashmap[index].append( [key, value] )
            return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % 2029
        
        if self.hashmap[index] != None:
            for pair in self.hashmap[index]:
                if pair[0] == key:
                    return pair[1] #return value
            #not found
            return -1
            
        else:
            #not found
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % 2029
        
        if self.hashmap[index] != None:
            for i, pair in enumerate( self.hashmap[index] ):
                #i is iterator from 0 to n
                if pair[0] == key:
                    self.hashmap[index].pop(i)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)