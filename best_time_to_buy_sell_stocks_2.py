class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = {}
        dp[0] = 0
        max_trade = max(prices)
        for sd in range(1, len(prices)):
            this_dp = 0
            for bd in range(max(0, sd-1), sd):
                curr_trade = prices[sd] - prices[bd]
                if curr_trade > 0:
                    this_dp = max(this_dp, dp[bd] + curr_trade)
                else:
                    this_dp = max(this_dp, dp[bd])
            dp[sd] = this_dp
        return dp[len(prices) - 1]
