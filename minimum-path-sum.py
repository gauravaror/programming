import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        
        def get_neigbours(row:int, col:int):
            for i,j in [(0,1), (1,0)]:
                if row + i >= 0 and col + j >= 0 and row + i < nrows  and  col + j < ncols:
                    yield (row + i, col + j)
        
        if nrows == 1  and ncols == 1:
            return grid[0][0]
            
        stack = []
        seen = {}
        heapq.heappush(stack, (grid[0][0], (0,0)))
        while True:
            if len(stack) == 0:
                break
            elem = heapq.heappop(stack)
            #print(elem)
            for i,j in get_neigbours(elem[1][0] , elem[1][1]):  
                if (i,j) in seen:
                    continue
                seen[(i,j)] = True
                cost = elem[0] + grid[i][j]
                #print(i,j, cost, grid[i][j])
                if i == nrows-1 and  j == ncols - 1:
                        return cost
                heapq.heappush(stack, (cost,(i, j)))
                #print(stack)
