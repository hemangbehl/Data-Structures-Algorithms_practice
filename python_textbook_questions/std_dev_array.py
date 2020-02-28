#1 pass solution
def std_dev(nos):
    #solving equation we get
    # std_dev = [ 1/n * E( x^2) ] - ( mean^2 )
    std_dev = 0
    n = 0
    mean = 0
    square = 0
    sumn = 0

    for i in nos:
        n += 1
        sumn += i
        squared = squared + (i * i)
    
    mean = sumn/n
    std_dev = squared/n - mean*mean


# 2 pass solution
# #cal mean and std deviation
# def std_dev( nos):
#     count = 0
#     sum1 = 0
#     mean = 0
#     std_dev = 0

#     for i in nos:
#         cnt += 1
#         sum1 += i
    
#     mean = sum1 / cnt  #decimal

#     #std dev= summation of squared deviation of each no. from the mean
#     #   = 1/N * E( x - mean)^2
#     dev = 0
#     diff = 0
#     for i in nos:
#         diff = i - mean
#         diff = diff * diff
#         dev += diff
    
#     std_dev = dev / count
#     return std_dev
