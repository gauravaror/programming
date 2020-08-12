class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nrows = len(matrix)
        if nrows == 0:
            return []
        ncols = len(matrix[0])
        if nrows == 1:
            return matrix[0]
        if ncols == 1:
            return [i[0] for i in matrix]
        print(matrix, nrows, ncols)
        if len(matrix) == 1 and len(matrix[0])==1:
            return [matrix[0][0]]
        firstrow = matrix[0][:]
        lastrow = matrix[nrows-1][:][::-1]
        lastcol = []
        firstcol = []
        for i in range(1, nrows-1):
            lastcol.append(matrix[i][ncols-1])
            firstcol.append(matrix[i][0])
        firstcol = firstcol[::-1]
        remaining_matrix = []
        if 1 != ncols-1:
            for i in  matrix[1:nrows-1]:
                remaining_matrix.append(i[1:ncols-1])
        print(remaining_matrix, matrix[1:nrows-1])
        others = self.spiralOrder(remaining_matrix)
        return firstrow + lastcol + lastrow +  firstcol + others
