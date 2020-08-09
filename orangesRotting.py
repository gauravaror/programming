class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        def neigh(r, c):
            if r < nrow-1:
                yield (r+1,c)
            if r >=1:
                yield (r-1,c)
            if c < ncol-1:
                yield (r, c+1)
            if c >=1:
                yield (r, c-1)
        seen = {}
        maxmin = 0
        def dfs(r,c):
            global maxmin
            for nr, nc in neigh(r, c):
                if grid[nr][nc] == 1:
                    if nr + 36*nc in seen:
                        old = seen[nr + 36*nc]
                        if old > seen[r + 36*c] + 1:
                            seen[nr + 36*nc] = seen[r + 36*c] + 1
                            dfs(nr, nc)
                    else:
                        seen[nr + 36*nc] = seen[r + 36*c] + 1
                        dfs(nr, nc)
                    #maxmin = max(maxmin, seen[nr + 36*nc])               
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 2:
                    seen[r + c*36] = 0
                    dfs(r, c)
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1 and r + 36*c not in seen:
                    return -1
                elif not grid[r][c] == 0:
                    maxmin = max(maxmin, seen[r+36*c])
        return maxmin
