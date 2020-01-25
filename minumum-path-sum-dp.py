class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        for i in range(1, nrows):
            grid[i][0] += grid[i-1][0]
        for j in range(1, ncols):
            grid[0][j] += grid[0][j-1]
        for i in range(1, nrows):
            for j in range(1, ncols):
                grid[i][j] = min( grid[i-1][j] + grid[i][j] , grid[i][j-1] + grid[i][j])
        print(grid)
        return grid[nrows-1][ncols-1]
