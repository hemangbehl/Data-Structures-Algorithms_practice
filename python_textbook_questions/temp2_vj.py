def x(y, z):
    res = z

    i = 0

    while i < len(z):
        z_value = z[i]
        res[i] = y(z_value )
        i += 1
    
    return res

def addition(n): 
    return n + n 

y = [0,1]
z = [0,1]
## map function
print( x(addition, z) )