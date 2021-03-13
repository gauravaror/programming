class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for a in range(amount+1):
            for c in coins:
                if a+c <= amount:
                    dp[a+c] = min(dp[a+c], dp[a] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]
