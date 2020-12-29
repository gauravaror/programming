class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        nrow = len(grid)
        ncol = len(grid[0])
        def get_out_col(col):
            row = 0
            while row < nrow:
                if grid[row][col] == 1:
                    if col < ncol-1 and grid[row][col+1] == 1:
                        col += 1
                        row += 1
                    else:
                        return -1
                else:
                    if col > 0 and grid[row][col-1] == -1:
                        col -= 1
                        row += 1
                    else:
                        return -1
            return col
        output = []
        for i in range(ncol):
            output.append(get_out_col(i))
        return output
                    
            
            
        
