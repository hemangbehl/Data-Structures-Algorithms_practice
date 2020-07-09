def group(arr):
    if len(arr) <= 2: return arr
    dict1 = {}
    for ele in arr:
        dict1[ele] = dict1.get(ele, 0) + 1
    
    ans = []
    for key in dict1.keys():
        for i in range(0, dict1[key] ):
            ans.append(key)
    
    return ans

arr = [4, 6, 9, 2, 3, 4, 9, 6, 10, 4] 
print(arr)
print(group([arr]) )
