class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy  = float('inf')
        profit = 0
        for i in prices:
            profit = max(profit, i-buy)
            buy = min(buy, i)
        return profit 
