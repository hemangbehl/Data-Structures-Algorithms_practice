def local(a):
    count = [a]

    def sublocal(b):
        #b = count + 1

        if b[0] > 5:
            # return sublocal(b)
            #count = 5
            return count[0] + 1 + count[0]
        else:
            count[0] = count[0] * 10
            return 0
    print("outside count = {}".format(count))
    a = sublocal(count)
    print("inside count = {}".format(a))
    print("outside count = {}".format(count[0]))


print( local(1) )
#print ( True + True + False + True )