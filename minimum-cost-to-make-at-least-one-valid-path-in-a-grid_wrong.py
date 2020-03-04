class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        inf = float('inf')
        dp = [[inf]*cols for _ in range(rows) ]
        dp[0][0] = 0
        
        def possible_paths(r, c):
            if r > 0:
                yield r-1,c,3
            if c > 0:
                yield r, c-1,1
            if r <rows-2:
                yield r+1,c,4
            if c <cols-1:
                yield r,c+1,2

        max_rep = rows*cols
        for _ in range(max_rep):
            for r in range(0, rows):
                for c in range(0, cols):
                    for r1,c1,dire in possible_paths(r,c):
                        ccost = dp[r1][c1]
                        if not grid[r1][c1] == dire:
                            ccost += 1
                        dp[r][c] = min(dp[r][c], ccost)
        print(dp[-5:][-5:])
        return dp[rows-1][cols-1]
