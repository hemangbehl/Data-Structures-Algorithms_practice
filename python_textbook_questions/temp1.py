def mostFrequentDigits(arr):
    freq = {0:0,
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0}
    
    for ele in arr:
        for digit in [int(d) for d in str(ele)]:
            #print(digit)
            freq[digit] += 1 #increment 1
    #O(n * k)     #k= size of each num in arr

    freq_digits = []
    max_freq = freq[0]

    for i in range(0, 10): #0 to 9
        if max_freq == freq[i]:
            #add to list
            freq_digits.append(i) # we iterated in asc order
        elif freq[i] > max_freq:
            #new list
            max_freq = freq[i]
            freq_digits = [i]
    
    return freq_digits

arr = [25, 2, 3, 57, 38, 41]
# arr = [1]
print( mostFrequentDigits(arr) )
