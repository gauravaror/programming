class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = {}
        rows = {}
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(n_rows):
            for j in range(n_cols):
                if i in rows or j in cols:
                    matrix[i][j] = 0
