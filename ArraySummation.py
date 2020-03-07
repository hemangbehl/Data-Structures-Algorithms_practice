# inputs = [-1, 8, 3]
# tests = [3, 7, 2]

def arraySum(inputs, tests):

    test_set = set( tests )

    for i in range( 0, len(inputs) - 1):
        for j in range( i + 1, len(inputs) ):
            if ( inputs[i] + inputs[j] ) in test_set:
                return True

    return False

inputs = [9,6,12]
tests = [1,2,3]

print( arraySum(inputs, tests) )