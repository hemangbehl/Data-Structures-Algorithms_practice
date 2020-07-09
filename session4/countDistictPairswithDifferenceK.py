def count(arr, k):
    if len(arr) == 0: return 0
    set1 = set()
    cnt = 0

    for ele in arr:
        if (ele + k) in set1:
            cnt += 1
        if (ele - k) in set1:
            cnt += 1
        set1.add(ele)

    return cnt

arr = [8, 12, 16, 4, 0, 20]
k = 4
print( count(arr, k))