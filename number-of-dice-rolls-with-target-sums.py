class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0]*(target+1) for _ in range(d)]
        for i in range(1, f+1):
            if i < target+1:
                dp[0][i] = 1
        for i in range(1,d):
            for j in range(1, target+1):
                num_ways = 0
                for face in range(1, f+1):
                    if j-face > 0:
                        num_ways += dp[i-1][j-face]
                dp[i][j] = num_ways
        print(dp)
        return int(dp[d-1][target] % (10**9 + 7))
