# inorder = 'ABCDEF'

# left, right = inorder.split("A")
# print("left", left, left == "")
# print (left,"-", right)

inorder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preorder = ['A', 'B', 'D', 'E', 'C', 'F'] 

ele = "A"
left = []
right = []
found = 0
for i in inorder:
    if i == ele:
        found = 1
    elif found == 0:
        left.append(i)
    else:
        right.append(i)

# print("left ={} ,right={}".format(left, right))
print  ( inorder[100:] )