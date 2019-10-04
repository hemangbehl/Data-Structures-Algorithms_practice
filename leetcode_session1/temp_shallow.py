li1 = [1, 2, [3,5], 4] 
  
# using copy to shallow copy  
li2 = li1.copy()

# original elements of list 
print ("The original elements before shallow copying") 
#for i in range(0,len(li1)): 
 #   print (li1[i],end=" ") 
print(li1)
  
print("\r") 
  
# adding and element to new list 
li2[2][0] = 7
  
# checking if change is reflected 
print ("The original elements after shallow copying") 
#for i in range(0,len( li1)): 
#    print (li1[i],end=" ") 
print( li2)