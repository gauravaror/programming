class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0]*(len(prices)+1)
        sell = [0]*(len(prices)+1)
        rest = [0]*(len(prices)+1)
        buy[0] = -float('inf')
        for i in range(1, len(prices)+1):
            index = i-1
            sell[i] = max(sell[index], buy[index] + prices[index])
            buy[i] = max(buy[index], rest[index] -prices[index])
            rest[i] = max(rest[index], sell[index])
        return max(sell[-1], buy[-1], rest[-1])
