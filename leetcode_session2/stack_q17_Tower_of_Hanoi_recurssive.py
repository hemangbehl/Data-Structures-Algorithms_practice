'''
to move all disks from A to C with B as aux

1. move n-1 disks from A to B using C
2. move remaining 1 disk from A to C
3. move n-1 disks from B to C using A

TC: O(2^n - 1)

'''
def TOH ( n, A, C, B):
    #takes no. of disks, src, dest, using aux
    if n>0: 
        TOH(n-1, A, B, C) #A to B using C
        print("Move disk#",n," from",A," to", C)
        TOH(n-1, B, C, A) #B to C using A

#driver code
TOH(3, 'A', 'C', 'B')
