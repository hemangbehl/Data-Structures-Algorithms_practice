class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []
        
        for ss in s:
            if ss.isdigit():
                num = 10 * num + int(ss) #make a no. out of digits
            
            elif ss in ["-", "+"]: #sing encountered
                num = sign * num
                res = res + num
                num = 0
                
                if ss == "+":
                    sign = 1
                else:
                    sign = -1
            
            elif ss == "(": #bracket opens, save res and sign to stack
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
                num = 0
            
            elif ss == ")": #pop previous sign and apply to result
                num = sign * num
                res = res + num   
                res = res * stack.pop()
                res = res + stack.pop()
                num = 0
                sign = 1
        #end of for loop
        
        return res + num*sign