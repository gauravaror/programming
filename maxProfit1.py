class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        buy = -float('inf')
        sell = -float('inf')
        for i in range(len(prices)):
            buy = max(buy, -prices[i])
            sell = max(sell, buy+prices[i])
            maxprof = max(maxprof, sell)
        return maxprof
