def vaidateIP(ip):
    if len(ip) < 7 or len(ip) > 15:
        return False
    dots, cnt, num = 0, 0, 0
    next_digit = 1

    for ch in ip:
        # print(ch, type(ch))
        if ch != "." and not ch.isdigit(): 
            return False
        if next_digit == 1 and ch == ".": return False
        if next_digit == 0 and ch != ".": return False
        if ch.isdigit():
            cnt += 1
            next_digit = -1
            num = num*10 + int(ch)
            if num > 255: 
                return False
            if cnt == 3: 
                next_digit = 0
            if cnt > 3:
                return False
        if ch == ".":
            next_digit = 1
            dots += 1
            if dots > 3:
                return False
            num, cnt = 0, 0
    
    if next_digit == 1 or dots != 3:
        return False
    
    return True

ip = "172.16.254.1"
ip2= "128.0.0.1"
ip3= "125.16.100.1" 
ip4= "125.512.100.1"
ip5= "125.512.100.abc"
print(ip, vaidateIP(ip) )
print(ip, vaidateIP(ip2) )
print(ip, vaidateIP(ip3) )
print(ip, vaidateIP(ip4) )
print(ip, vaidateIP(ip5) )