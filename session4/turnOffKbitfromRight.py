def turnoffk(a, k):
    if a == 0 or k == 0:
        return a
    b = bin(a)[2:]
    n = len(b)

    if k > n:
        return a
    c = []

    for i in range(n):
        if i == n-k:
            c.append( "0" )
        else:
            c.append(b[i])
    ans = "".join(c)
    return int( ans, 2) #base 2

a = 15
k = 4
print ( turnoffk(a, k) )
