class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            this_amount = float('inf')
            for c in coins:
                if i - c >= 0:
                    this_amount = min(this_amount, 1  + dp[i-c])
            dp[i] = this_amount
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
