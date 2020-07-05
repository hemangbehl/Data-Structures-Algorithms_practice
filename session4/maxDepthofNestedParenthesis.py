def maxdepth(s1):
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