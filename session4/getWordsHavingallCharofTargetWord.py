def getCommon(target, words):
    #TC: O(n) , n= total no. of char in list of items
    #SC: O(1) , assuming only 256 unique char can be input
    ## O(256) = O(1) as worst case has only a max of 256 char in set
    if len(target) == 0: return words
    if len(words) == 0 : return None

    set1 = set()
    for w in target:
        set1.add(w)
    temp = set()

    for word in words:
        temp = set()
        for w in word:
            if w in set1 and w not in temp:
                temp.add(w)
        if len(temp) == len(set1):
            print(word)

words = ["geeksforgeeks", "unsorted", "sunday", "just", "sss"] 
target = "sun"
getCommon(target, words)
