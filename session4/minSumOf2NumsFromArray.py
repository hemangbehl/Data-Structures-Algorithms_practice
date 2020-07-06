def minsum(digits):
    if len(digits) == 0 : return None
    if len(digits) == 1 : return digits[0]
    a, b = 0, 0
    digits.sort()
    i = 0
    n = len(digits)
    
    while i < n:
        a = a * 10 + digits[i]
        i += 1
        if i < n:
            b = b * 10 + digits[i]
            i += 1
    
    return (a + b)

print( minsum([6, 8, 4, 5, 2, 3]))
print( minsum([5, 3, 0, 7, 4]))
