class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        total = 0
        n = 0
        stack = []
        
        for ch in ops:
            if ch == '+':
                if len(stack) >= 2:
                    #requires last 2 valid rounds
                    total += stack[-1] + stack[-2]
                    stack.append( stack[-1] + stack[-2] )

            elif ch == 'D':
                if len(stack) >= 1:
                    total += ( stack[-1] * 2 )
                    stack.append( stack[-1] * 2 )
                
            elif ch == 'C':
                #remove last valid score
                if len(stack) >= 1:
                    total -= stack[-1]
                    stack.pop()
            else:
                #has to be an integer
                n = int(ch)
                total += n
                stack.append(n)
        
        return total