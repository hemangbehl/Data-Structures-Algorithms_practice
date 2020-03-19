class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or not beginWord or not endWord:
            return 0
        if endWord not in wordList:
            return 0
        
        level = 0
        queue = [beginWord, 1]
        
        #assuming length is same for all the words
        length = len(beginWord)
        
        dict_word = {}
        
        #add all possible transformations as keys and the words associated to it as values as a list
        for word in wordList:
            for i in range(0, length):
                transf = word[0:i] + "*" + word[i+1:length]
                                
                if transf not in dict_word: #add to dict
                    dict_word[transf] = [word]
                    
                else: #append to list
                    dict_word[transf].append(word)

        queue = [ (beginWord, 1) ]
        visited = set()
        
        while queue:
            word, level = queue.pop(0)
            
            if word in visited:
                continue #skip current iteration
            
            if word == endWord:
                #found
                return level
            
            visited.add( word ) #add current word to visited
            
            #loop through all transformations of that word
            for i in range(0, length):
                transf = word[0:i] + "*" + word[i+1:length]
                
                if transf in dict_word:
                    #enqueue next words check
                    for val in dict_word[transf]:
                        if val not in visited:
                            queue.append( (val, level + 1) )
        
        #end of while, endWord not found
        return 0