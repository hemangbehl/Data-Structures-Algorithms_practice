def flatten_helper(l1):
    flat = []
    return flatten(l1, flat) 
    

    # for sublist in l1:
    #     for ele in sublist:
    #         flat.append(ele)
    
    # return flat
    


def flatten(l1, flat):
    if len(l1) == 0:
        return None

    for ele in l1:
        #if ( type(ele) != type([]) ):
        if type(ele) == int:
            #digit
            # print("appending ", ele)
            flat.append(ele)
        else:
            #nested list encountered
            flatten(ele, flat) #call function to flat current nested list
    
    return flat

# l1 = [[1,1],2,[1,1]]
l1 = [1,[4,[6]], [[[]]], []]

print(l1)
print("List after flattening", flatten_helper(l1) )
# print("List after flattening", flatten(l1) )