def checkSubsequence(s1, s2):
    if len(s1) > len(s2): return False
    if len(s1) == 0: return True
    if len(s1) != 0 and len(s2) == 0: return False
    cnt = 0
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            cnt += 1
            i += 1
            j += 1
        else: j += 1
    if cnt == len(s1): return True
    else: return False

s1 = "AXY"
s2 = "ADXCPY"
s3 = "YADXCP"

print ( checkSubsequence(s1, s2) )
print ( checkSubsequence(s1, s3) )
print ( checkSubsequence("gksrek", "geeksforgeeks") )