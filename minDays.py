class Solution:
    def num_islands(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        seen = {}

        def neigh(row,col):
            if row < nrows-1:
                yield row + 1,col
            if row > 0:
                yield row - 1,col
            if col < ncols-1:
                yield row,col + 1
            if col > 0:
                yield row,col -1

        def dfs(r, c):
            num_connection = 0
            for nr,nc in neigh(r,c):
                if grid[nr][nc] == 1:
                    num_connection += 1
                    if (nr,nc) not in seen:
                        seen[nr,nc] = True
                        dfs(nr,nc)
            return num_connection
        islands = 0
        for i in range(nrows):
            for j in range(ncols):
                if (i,j) not in seen and grid[i][j] == 1:
                    islands += 1
                    dfs(i,j)
        return islands
        
    def minDays(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        copy_g = copy.deepcopy(grid)
        ans =  self.num_islands(copy_g) 
        if ans != 1:
            return 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    copy_g = copy.deepcopy(grid)
                    copy_g[i][j] = 0
                    ans = self.num_islands(copy_g)
                    if ans != 1:
                        return 1
        return 2
