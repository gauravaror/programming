class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = dungeon.copy()
        dp[m-1][n-1] = max(1, -dp[m-1][n-1] + 1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if i < m-1 and j < n-1:
                    dp[i][j] = max(1, min(-dp[i][j] + dp[i+1][j], -dp[i][j] + dp[i][j+1]))
                elif i < m-1:
                    dp[i][j] = max(1, -dp[i][j] + dp[i+1][j])
                else:
                    dp[i][j] = max(1, -dp[i][j] + dp[i][j+1])
        return dp[0][0]
