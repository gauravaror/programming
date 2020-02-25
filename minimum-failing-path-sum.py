class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])
        dp = [[float('inf')]*cols for i in range(rows)]
        for i in range(cols):
            dp[0][i] = A[0][i]
            
        def gen_possible(c):
            if not (c == 0):
                yield c-1
            yield c
            if c<cols-1:
                yield c+1
        for i in range(1, rows):
            for j in range(cols):
                m = float('inf')
                for l in gen_possible(j):
                    m = min(m, dp[i-1][l])
                dp[i][j] = min(dp[i][j], m + A[i][j])
        #print(dp)
        return min(dp[rows-1])
