from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        dp = [0]*n
        if dp[n-1] != 0:
            return dp[n-1]
        i = 0
        for j in range(n):
            sum_j = 0
            for k in range(0, j+1):
                left =  self.numTrees(k-0)
                right = self.numTrees(j- k)
                sum_j += (left*right)
            dp[j] = sum_j
        return dp[n-1]
