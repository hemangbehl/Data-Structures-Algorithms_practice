class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prisdces)
        
        if n <= 1:
            return 0
        
        prev = prices[0]
        profit = 0
        
        for i in range(1, n):
            if prev < prices[i]:
                profit += ( prices[i] - prev )
                prev = prices[i]
            else:
                prev = prices[i]
        
        return profit