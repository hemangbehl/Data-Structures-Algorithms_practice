s = "If you want to jumpstart the process of talking to us about this role, here’s a little challenge: write a program that outputs the largest unique set of characters that can be removed from this paragraph without letting its length drop below 50."

# For example: [‘H’, ‘i’, ‘!’, ‘ ’]

def get_unique_char(s):
    total_len = len(s)
    max_len = 50
    dict1 = {}
    ans = []
    dictlist = []
    
    #loop and add to dict
    for ch in s: #O(n)
        dict1[ch] = dict1.get(ch, 0) + 1
    
    if len(s) <= max_len:
        return [None]
    #else

    #convert dict to list
    for key, val in dict1.items():
        dictlist.append( [key, val] )
    
    #sort dictlist according to count in asc order
    dictlist.sort(key= lambda x: x[1]) # O(nlogn)

    #loop through and check what can be removed and add it to ans
    for i in dictlist: #O(n)
        if total_len <= 50:
            return ans
        #else
        # print("total_len", total_len, max_len)
        total_len = total_len - i[1] #subtract occurence
        ans.append(i[0])
    
    # return ans

print("list of unique char that can be removed", get_unique_char(s) )
