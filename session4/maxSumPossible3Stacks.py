def maxSum3Stacks(s1, s2, s3):
    a ,b , c = sum(s1), sum(s2), sum(s3)
    maxsum = 0
    while s1 and s2 and s3:
        # print("sums", a,b,c ,"top", s1[-1] , s2[-1] , s3[-1])
        if a == b == c:
            maxsum = max(maxsum, a )
            a -= s1.pop()
            b -= s2.pop()
            c -= s3.pop()
        else:
            if a >= b and a >= c:
                a -= s1.pop()
            elif b >= a and b >= c:
                b -= s2.pop()
            elif c >= a and c >= b:
                c -= s3.pop()
        
        
    return maxsum

s1 = [ 1,1,1,2,3 ] 
s2 = [ 2,3,4 ] 
s3 = [ 1,4,5,2 ] 
print( maxSum3Stacks(s1, s2, s3) )