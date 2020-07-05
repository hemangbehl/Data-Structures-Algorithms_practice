a = 705
b = 26
n = a
keys = [ i for i in range(0, 26) ]
values = [ ( chr(ord("A") + i) ) for i in range(0, 26)]
dict1 = dict( zip (keys, values))
# print( dict1 )
ans = []
while n != 0:
    n = n -1
    rem = n % b
    n = n // 26 #quotient
    # print( "mod of",n ,"%",b,"=", rem)
    # print( n,"/", b, " =", n)
    ans.append( dict1[rem] )
print("ans", ans[::-1])