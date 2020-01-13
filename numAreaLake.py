from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = {}
        elements = []            
        num_rows = len(grid)
        num_cols = len(grid[0])
        def neighbours(i,j):
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dire in directions:
                print(dire)
                if (i + dire[0] < num_rows) and (i + dire[0] >= 0) and (j + dire[1] < num_cols) and (j + dire[1] >= 0):
                    print("Sending ", dire)
                    yield (i + dire[0] , j + dire[1])
        
        def dfs(i, j):
            print("DFS", i, j)
            seen[(i,j)] = True
            for n in neighbours(i,j):
                print("Accessing neigbours", n)
                if grid[n[0]][n[1]] == 1 and (not (n[0],n[1]) in seen):
                    elements[-1] += 1
                    dfs(n[0], n[1])
                    
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                if (not (i,j) in seen) and grid[i][j] == 1:
                    print(elements)
                    elements.append(0)
                    elements[-1] += 1
                    dfs(i,j)
        if len(elements) == 0:
            return 0
        return max(elements)

sol =  Solution()
print(sol.maxAreaOfIsland([[1,1],[1,0]]))
