from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def neig(r, c):
            if r < len(grid)-1:
                yield (r+1, c)
            if c < len(grid[0])-1:
                yield (r, c+1)
            if r>0:
                yield (r-1,c)
            if c> 0:
                yield (r,c-1)
                
        seen = {}
        last_grid = -1
        components = []
        largest_island = 0
        empty = defaultdict(list)
        def hash(nr, nc):
            return nr + (37**2)*nc
            
        def dfs(r,c):
            for (nr, nc) in neig(r,c):
                if hash(nr,nc) not in seen and grid[nr][nc] == 1:
                    seen[hash(nr,nc)] = True
                    components[-1] += 1
                    dfs(nr, nc)
                elif grid[nr][nc] == 0:
                    has = hash(nr, nc)
                    empty[hash(nr, nc)].append(last_grid)
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if hash(a,b) not in seen and grid[a][b] == 1:
                    seen[hash(a,b)] =  True
                    last_grid += 1
                    components.append(1)
                    dfs(a,b)
        if last_grid == -1:
            return 1
        largest_island = max(components)
        for k in empty.keys():
            this_node = 0
            for ss in set(empty[k]):
                this_node += components[ss]
            this_node += 1
            if largest_island < this_node:
                largest_island = this_node
        return largest_island
