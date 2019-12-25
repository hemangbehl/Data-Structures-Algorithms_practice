def find_celeb(arr):
    max_n = len(arr)-1
    cnt = 0

    for i in range (0, len(arr) ):
        cnt = 0 #set as 0 for each i
        for j in range (0, len(arr) ):
            if i == j:
                continue #skip for same index
            if HaveAcq(i, j) == False:
                cnt += 1
            else:
                break #leave 2nd loop
        
        if cnt < max_n: #not a celeb as it known someone
            #print ("cnt < max_n, cnt and max_n are", cnt, max_n)
            continue
        else: #could be a celeb as it doesn't know anyone
            #print ("else entered by", i)
            for j in range(0, len(arr) ):
                if i == j: #same index, skip
                    continue
                if HaveAcq(j, i) == False: #j doensn't know i, not a celeb
                    #print ("1st return -1")
                    return -1
                else:
                    continue
            #rest of all the people know 'i'
            # 'i' is a celeb
            #print (i)
            return i
    #print ("2nd return -1, end of outer for loop") 
    return -1

#dummy
def HaveAcq(i, j):
    return False

#driver code
print ( find_celeb ( [1, 1] ))