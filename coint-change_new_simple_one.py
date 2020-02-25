class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        neg_inf = float('inf')
        dp = [neg_inf]*(amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(0, len(coins)):
                val = (i - coins[j]) 
                if  val >= 0 and dp[val] != neg_inf:
                    dp[i] = min(dp[i], dp[val] + 1)
        print(dp)
        return dp[amount] if not dp[amount] == neg_inf else -1
