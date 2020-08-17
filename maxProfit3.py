class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy = -prices[0]
        sell = 0
        sell2 = -float('inf')
        buy2 = -float('inf')
        for i in prices[1:]:
            sell = max(sell, buy+i)
            buy = max(buy, -i)
            buy2 = max(buy2, sell - i)
            sell2 = max(sell2, buy2+i)
            #print(i, sell, buy, buy2, sell2)
        return max(0, sell2)
