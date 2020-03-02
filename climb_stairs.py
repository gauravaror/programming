class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        def climb_stairs(item):
            if item < 0:
                return 0
            if dp[item] != 0:
                return dp[item]
            dp[item] = climb_stairs(item-1) + climb_stairs(item-2)
            return dp[item]
        return climb_stairs(n)
