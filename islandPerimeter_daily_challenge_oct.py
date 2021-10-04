class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        self.ans = 0
        def dfs(x, y):
            if (x,y) in seen:
                return
            seen.add((x,y))
            for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= x + dx  < rows and 0 <= y + dy < cols:
                    if grid[x+dx][y+dy] == 0:
                        self.ans += 1
                    else:
                        dfs(x+dx, y+dy)
                else:
                    self.ans  += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
        return self.ans
