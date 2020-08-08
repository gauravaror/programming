class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        ps = []
        for i in range(n):
            sq = i**2
            if sq <= n:
                ps.append(sq)
        dp = [float('inf')]*(n + 1)
        dp[0] = 0
        for s in ps:
            for i in range(n+1):
                if i-s >= 0:
                    dp[i] = min(dp[i], dp[i-s] + 1)
        return dp[-1]
