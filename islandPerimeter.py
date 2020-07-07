class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        seen = {}
        pm = []
        
        def neig(row, col):
            if row < nrows-1:
                yield row + 1,col
            else:
                yield -1,-1
            if row > 0:
                yield row - 1,col
            else:
                yield -1,-1
            if col < ncols-1:
                yield row,col + 1
            else:
                yield -1,-1
            if col > 0:
                yield row,col -1
            else:
                yield -1,-1

        def hash(r, c):
            return r + (37**2)*c
        
        def dfs(row, col):
            for r,c in neig(row, col):
                if r==-1 and c==-1:
                    pm.append((r,c))
                elif hash(r,c) in seen:
                    continue
                elif grid[r][c] == 1:
                    seen[hash(r,c)] = True    
                    dfs(r, c)
                else:
                    pm.append((r,c))

        for ro in range(nrows):
            for co in range(ncols):
                if grid[ro][co] == 1 and (hash(ro,co) not in seen):
                    seen[hash(ro,co)] = True
                    dfs(ro,co)
        #print(pm)
        return len(pm)
