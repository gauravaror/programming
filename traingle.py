class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def get_previous(i, leng):
            if i == 0:
                yield 0
            elif i == (leng-1):
                yield i-1
            else:
                yield i-1
                yield i
        rows = len(triangle)
        dp = []
        dp.append(triangle[0])
        for i in range(1, rows):
            col_len = len(triangle[i])
            this_row = []
            for j in range(col_len):
                min_this = float('inf')
                for k in get_previous(j, col_len):
                    #print(col_len, k, i, j)
                    min_this = min(min_this, dp[i-1][k] + triangle[i][j])
                this_row.append(min_this)
            dp.append(this_row)
        return min(dp[-1])
