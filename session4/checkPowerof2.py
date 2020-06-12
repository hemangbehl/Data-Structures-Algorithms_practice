x = 3
n = 4

if n < 0:
    x = 1 / x
    n = -n

pow = 1

while n > 0:
    if n % 2 == 1: #if odd
        pow = pow * x

    x = x * x
    print("X=", x)
    n = n // 2 #remove last digit
    print("N=", n)

print ( pow )