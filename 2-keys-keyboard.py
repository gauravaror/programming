class Solution:
    def minSteps(self, n: int) -> int:
        inf = float('inf')
        dp = [[inf]*(n+1) for _ in range(n+1)]
        dp[0][1] = 0
        dp[1] = list(range(0,n+1))
        for i in range(2, n+1):
            for j in range(1, i):
                dp[j][i] = min(dp[j][i-j] + 1, dp[j][i])
                dp[i][i] = min(dp[i][i], dp[j][i] + 1)
        #print(dp[:])
        newdp = [dp[i][n] for i in range(n+1)]
        return min(newdp)
