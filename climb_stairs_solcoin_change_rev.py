class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n + 1)
        dp[0] = 1
        for j in range(1,n+1):
            for i in [1,2]:
                print(i, j, dp, j-i, dp[j-i])
                if j-i >= 0:
                    dp[j] += dp[j-i]
        print(dp)
        return dp[-1]
