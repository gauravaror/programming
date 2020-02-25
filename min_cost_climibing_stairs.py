class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ar_len = len(cost)
        dp = [0]*(ar_len + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, ar_len+1):
            now_cost = 0 if i == ar_len else cost[i]
            dp[i] = min(dp[i-1], dp[i-2]) + now_cost
        return dp[ar_len]
