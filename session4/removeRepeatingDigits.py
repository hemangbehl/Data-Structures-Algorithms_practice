def removeRepeatingDigits(n):
    old = None
    n1 = n
    new = 0
    a = 0
    i = 0
    while n1 > 0:
        a = n1 % 10
        if a != old:
            old = a
            new = a * (10 ** i) + new
            i += 1
        n1 = n1 // 10
    
    return new

n = 12224
print(n, removeRepeatingDigits(n) )
