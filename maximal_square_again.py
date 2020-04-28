from copy import deepcopy
class Solution:
    def find_maximal(self, matrix: List[List[str]], level) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        if min(rows, cols) <= level:
            return level
        found_blocks = 0
        nmatrix = [['0']*cols for _ in range(rows)]
        for i  in range(rows-1):
            for j in range(cols-1):
                if matrix[i][j]  == '1' and matrix[i+1][j] == '1' and matrix[i][j+1] == '1' and matrix[i+1][j+1] == '1':
                    found_blocks +=1
                    nmatrix[i][j] = '1'
                else:
                    nmatrix[i][j] = '0'
        print(level, nmatrix, found_blocks)
        if found_blocks > 0:
            return self.find_maximal(nmatrix, level + 1)
        else:
            return level
                    
        
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        print(matrix)
        print(len(matrix))
        if len(matrix) == 0:
            return 0
        
        sa = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    sa += 1
        if len(matrix) == 1 or sa == 0:
            if sa != 0:
                return 1
            return 0
        level = self.find_maximal(matrix, 1)
        return level**2
