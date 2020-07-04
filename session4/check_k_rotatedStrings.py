def checkrotate(s1, s2):
    if len(s1) != len(s2):
        return False
    
    for i in range( len(s1) ):
        if s2[i] == s1[0]:
            if checkstrings(s1, s2, i):
                return True
    
    return False

def checkstrings(s1, s2, i):
    n = len(s1)
    cnt = 0
    while cnt < n:
        i = i % n
        if s1[cnt] != s2[i]:
            return False
        cnt += 1
        i += 1
    
    return True

s1 = "ABACD"
s2 = "CDABA"

print ( checkrotate(s1, s2) )
