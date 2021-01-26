class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrows = len(heights)
        ncols = len(heights[0])
        def neig(row, col):
            for r,c in list(itertools.permutations([-1, 0,1], 2)):
                if r == 0 and c == 0 :
                    continue
                if (row + r < nrows) and (row + r >= 0) and (col +  c < ncols) and (col + c >= 0):
                        yield (row + r, col + c)

        seen = set()
        dp = [[float('inf')]*ncols for i in range(nrows)]
        dp[0][0] = 0
        def dfs(row, col):
            #print("##", row, col, list(neig(row, col)))
            for r,c in neig(row, col):
                if (r,c) not in seen:
                    seen.add((r,c))
                    heigdiff = abs(heights[r][c] - heights[row][col])
                    heigdiff = max(heigdiff, dp[row][col])
                    if heigdiff < dp[r][c] or dp[r][c] == float('inf'):
                        dp[r][c] = heigdiff
                        dfs(r,c)
                    seen.remove((r,c))
                #print("!",row, col, r, c, seen)
                    
        dfs(0,0)
        print(dp)
        return dp[nrows-1][ncols-1]
        
