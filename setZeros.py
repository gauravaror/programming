class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        zrow = False
        zcol = False
        for i in range(nrows):
            if matrix[i][0] == 0:
                zrow = True
                break
        for j in range(ncols):
            if matrix[0][j] == 0:
                zcol = True
                break
        for i in range(1, nrows):
            for j in range(1, ncols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0   
        for i in range(1, nrows):
            if matrix[i][0] == 0:
                for j in range(ncols):
                    matrix[i][j] = 0
        for i in range(1, ncols):
            if matrix[0][i] == 0:
                for j in range(nrows):
                    matrix[j][i] = 0
        if zrow:
            for i in range(nrows):
                matrix[i][0] = 0
        if zcol:
            for j in range(ncols):
                matrix[0][j] = 0
