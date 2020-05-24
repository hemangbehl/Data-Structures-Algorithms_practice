# Complete the 'closestStraightCity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY c
#  2. INTEGER_ARRAY x
#  3. INTEGER_ARRAY y
#  4. STRING_ARRAY q
#

def closestStraightCity(c, x, y, q):
    # Write your code here
    n = len(c) #get no. of cities

    sameCityDictX = {}
    sameCityDictY = {}
    closestCityX = [None] * n 
    closestCityY = [None] * n
    closestCityAns = [None] * n

    dist = 0
    sameX = []
    sameY= []

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue #skip same city
            
                #X coordinate
            if x[i] == x[j]: #same x coord
                #cal dist
                dist = abs( x[i] - x[j] )
                sameX = [j, dist]
                #print(sameX)
                if i not in sameCityDictX:
                    sameCityDictX[i] = [sameX]
                    closestCityX[i] = sameX #initial values is set
                else:
                    #sameCityDictX[i] = sameCityDictX[i].append(sameX)
                    
                    #print("inside else", sameX, closestCityX[i] )
                    if sameX[1] < closestCityX[i][1]:
                        #replace closest city as less distance found
                        closestCityX[i] = sameX
                    elif sameX[1] == closestCityX[i][1]: #if same dist
                        if c[ sameX[0] ] < c[ closestCityX[i][0] ]: #comapre city name
                            closestCityX[i] = sameX #replace

            
            #Y coordinate
            if y[i] == y[j]: #same x coord
                #cal dist
                dist = abs( y[i] - y[j] )
                sameY = [j, dist]

                if i not in sameCityDictX:
                    sameCityDictY[i] = [sameY]
                    closestCityY[i] = sameY #initial values is set
                else:
                    #sameCityDictY[i] = sameCityDictY[i].append(sameX)
                    
                    if sameY[1] < closestCityX[i][1]:
                        #replace closest city as less distance found
                        closestCityY[i] = sameY
                    elif sameY[1] == closestCityY[i][1]: #if same dist
                        if c[ sameX[0] ] < c[ closestCityX[i][0] ]: #check city name
                            closestCityY[i] = sameY #replace
    #end of outer loop

    print ("X", closestCityX)
    print ("Y", closestCityY )
    for i in range(0, n):
        if closestCityX[i] == None and closestCityY[i] == None:
            closestCityAns[i] = "NONE"
        elif closestCityX[i] == None and closestCityY[i] != None:
            closestCityAns[i] = c[ closestCityY[i][0] ]
        elif closestCityX[i] != None and closestCityY[i] == None :
            closestCityAns[i] = c[ closestCityX[i][0] ]
        else:
            #compare city names
            #print( "error", closestCityX)
            if c[ closestCityX[i][0] ] < c[ closestCityY[i][0] ]:
                closestCityAns[i] = c[ closestCityX[i][0] ]
            else:
                closestCityAns[i] = c[ closestCityY[i][0] ]
    
        
    print(closestCityAns )

    return closestCityAns

c = [ "city1", "city2", "city3" ]
x = [ 0, 0, 0 ]
y = [ 1, 5, 6 ]
q = [0, 1, 2]

print("closest city", closestStraightCity(c, x, y, q) )
