class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_buy = 0
        index = 0
        probables = []
        output = 0
        while index < len(prices) - 1:
            start = index
            change = 0
            so = 0
            eo = 0
            while index <= len(prices) - 2 and prices[index+1] > prices[index]:
                oo = prices[index+1] - prices[index]
                if change == 0:
                    so = oo
                change = oo
                output += oo
                index += 1
            eo = change
            end = index
            if end > start:
                probables.append((start, end, so, eo))
            while index <= len(prices) - 2 and prices[index+1] <= prices[index]:
                index += 1
        print(probables)
        dp = [[0]*3 for _ in range(len(probables))]
        for i in range(0, len(probables)-1):
            for j in [0,1,2]:
                prev = probables[i]
                ne = probables[i+1]
            if prev[1] + 1 == ne[0]:
                output -= min(prev[3], ne[2], prices[prev[1]] - prices[ne[0]])
        return output
