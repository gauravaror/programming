class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows = len(matrix)
        start = 0
        end = nrows-1
        while start<end:
            matrix[start], matrix[end] = matrix[end],matrix[start]
            start += 1
            end -= 1
        for r in range(nrows):
            for i in range(r, nrows):
                matrix[r][i], matrix[i][r] = matrix[i][r], matrix[r][i]
