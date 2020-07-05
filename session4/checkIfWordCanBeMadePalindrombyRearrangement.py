def checkPalin(s1):
    if len(s1) <= 1: return True
    dict1 = {}
    odd = 0
    for ch in s1:
        if ch in dict1:
            dict1[ch] += 1
            if dict1[ch] % 2 == 0:
                odd -= 1
            else: #odd freq
                odd += 1
        else: #not in dict
            dict1[ch] = 1
            odd += 1
    
    if len(s1) % 2 == 0 and odd != 0:
        return False
    if len(s1) % 2 == 1 and odd > 1:
        return False
    
    return True

s1 = "geeksogeeks"
s2 = "geeksforgeeks"
print ( checkPalin(s1) )
print ( checkPalin(s2) )