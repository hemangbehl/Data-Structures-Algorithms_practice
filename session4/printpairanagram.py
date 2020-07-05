def printanagram(arr):

    dict1 = {}
    for i in range( len(arr) ):
        w =  sorted(arr[i])
        w = "".join(w)

        if w in dict1:
            dict1[w].append(i)
        else:
            dict1[w] = [i]
    
    for key, val in dict1.items():
        if len(val) > 1:
            for i in val:
                print( arr[i], end=" = " )
            print()

arr = ["geeksquiz", "geeksforgeeks", "abcd",
        "forgeeksgeeks", "zuiqkeegs"]
print ( printanagram(arr) )
        