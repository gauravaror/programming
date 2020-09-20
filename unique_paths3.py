class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        starting = None
        ending = None
        free_nodes = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 0:
                    free_nodes += 1
                elif grid[i][j] == 1:
                    starting = (i,j)
                elif grid[i][j] == 2:
                    ending = (i,j)
        seen = set()
        self.output = 0
        dire = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(r, c, visited, path):
            
            if (r,c) == ending and (visited) == free_nodes:
                print(r,c, visited, free_nodes, ending)
                print(path)
                self.output += 1
                return
            for dr,dc in dire:
                if r+dr >= 0 and r + dr < nrows and c +dc >=0 and c+dc < ncols:
                    if (grid[r+dr][c+dc] == 0 or grid[r+dr][c+dc] == 2) and (r+dr, c + dc) not in seen:
                        seen.add((r+dr, c+dc))
                        vis = visited + 1 if grid[r+dr][c+dc] == 0 else visited
                        dfs(r+dr, c+dc, vis, path + [(r+dr,c+dc)])
                        seen.remove((r+dr, c+dc))
        dfs(starting[0], starting[1], 0, [(0,0)])
        return self.output
