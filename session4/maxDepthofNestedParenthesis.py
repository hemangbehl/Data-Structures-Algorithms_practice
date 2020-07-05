def maxdepth_stack(s1): #TC:O(n) SC:O(n)
    if len (s1) ==0 : return 0
    stack = []
    maxn = 0
    for ch in s1:
        if ch == "(":
            stack.append("(")
            maxn = max(maxn, len(stack))
        elif ch == ")":
            if len(stack) == 0:
                return -1
            else: stack.pop()
    if len(stack) == 0: return maxn
    else: return -1

def maxdepth(s1): #TC:O(n) SC:O(1)
    if len(s1) == 0: return 0
    cnt = 0
    maxn = 0
    for ch in s1:
        if ch == "(": 
            cnt += 1
            maxn = max(maxn, cnt)
        elif ch == ")":
            cnt -= 1
            if cnt < 0: return -1
    if cnt != 0: return -1
    return maxn

s1 = "( a(b) (c) (d(e(f)g)h) I (j(k)l)m)"
s2 = "( p((q)) ((s)t) )"
s3 = ""
s4 = "b) (c) ()"
s5 = "(b) ((c) ()"

print( maxdepth(s1) )
print( maxdepth(s2) )
print( maxdepth(s3) )
print( maxdepth(s4) )
print( maxdepth(s5) )