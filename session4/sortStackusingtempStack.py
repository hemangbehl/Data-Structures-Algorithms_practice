def sortstack(s1):
    s2 = []
    if s1 == []: return s1

    while s1 != []:
        x = s1.pop()
        while s2 != [] and x > s2[-1]:
            s1.append( s2.pop() )
        s2.append(x)
    
    while s2 != []:
        s1.append( s2.pop() )
    

s1 = [3, 5, 1, 4, 2, 8]
sortstack(s1)
print (s1 )