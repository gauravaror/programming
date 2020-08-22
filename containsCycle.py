class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        nrow = len(grid)
        ncol = len(grid[0])
        def neigh(r,c):
            if r > 0:
                yield r-1,c
            if c > 0:
                yield r,c-1
            if r < nrow-1:
                yield r+1,c
            if c < ncol-1:
                yield r, c+1
        self.seen = {}
        def dfs(r,c,le):
            for nr,nc in neigh(r,c):
                if (nr,nc) in self.seen and abs(self.seen[(nr,nc)] - le) >= 3 and grid[nr][nc] == grid[r][c]:
                    return True
                elif (nr,nc) not in self.seen and grid[nr][nc] == grid[r][c]:
                    self.seen[(nr,nc)] = le
                    if dfs(nr,nc, le+1):
                        return True
                    #del self.seen[(nr,nc)]
        for i in range(nrow):
            for j in range(ncol):
                if (i,j) not in self.seen:
                    self.seen[(i,j)] = True
                    if dfs(i,j, 1):
                        print(i, j)
                        return True
                #del self.seen[(i,j)]
        return False
