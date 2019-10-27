l1 = [10,20,30,40,100]
#l1 = [1,2,3,4,5,7]

sum = 70

def findsumnos(l1):

    if len(l1) < 2:
        #print ("Insufficient Length")
        return -2,-2
    else:
        left = 0
        right = len(l1)-1
        while left < right:
            if (l1[left] + l1[right]) > sum:
                right -= 1
            elif (l1[left] + l1[right]) < sum:
                left += 1
            else:
                return l1[left] ,l1[right]
        #nothing found
        return (-1,-1)

a,b = findsumnos(l1)
if a == -2:
    print ("Insufficient length")
elif a ==-1:
    print ("Not found")
else:
    print ("Two nums are:", a, b)

