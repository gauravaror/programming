class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neigh(row, col):
            if row <= len(grid)-2:
                yield (row + 1, col)
            if row >= 1:
                yield (row - 1, col)
            if col <= len(grid[0]) -2:
                yield (row, col+1)
            if col >= 1:
                yield (row, col-1)
                

        seen = {}
        regions = []
        def dfs(row, col):
            #print(row, col, seen)
            for i,j in neigh(row, col):
                if grid[i][j] == "1":
                    has = str(i)+"_" +str(j)
                    if (has) not in seen:
                        regions[-1].append((i,j))
                        seen[has] = 1
                        dfs(i, j)

                  
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                has = str(r)+"_" +str(c)
                #print(grid[r][c], grid[r][c] == "1",has, r,c , has not in seen, regions)
                if  grid[r][c] == "1" and has not in seen:
                    #print(r,c)
                    seen[has] = 1
                    regions.append([(r,c)])
                    dfs(r,c)
        #print("Final", regions)
        return len(regions)
