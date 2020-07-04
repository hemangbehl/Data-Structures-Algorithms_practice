def runlen(s1):
    if len(s1) == 0: return ""
    cnt = 0
    list1 = []
    prev = None

    for ch in s1:
        if prev == None:
            cnt += 1
            list1.append(ch)
            prev = ch
        elif prev == ch:
            cnt += 1
        else: #ch changed
            list1.append( str(cnt) )
            cnt = 1
            list1.append(ch)
            prev = ch
    if cnt != 0:
        list1.append( str(cnt) )
    return "".join(list1)

s1 = "wwwwaaadexxxxxx"
s2 = "wwwwaaadexxxxxxywww"
print ( runlen(s1), runlen(s2) )
