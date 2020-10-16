class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        if nrows == 0:
            return False
        ncols = len(matrix[0])
        if ncols == 0:
            return False
        start = 0
        end = nrows
        while start < end:
            mid = start + (end-start)//2
            if matrix[mid][0] >= target:
                end = mid
            else:
                start = mid + 1
        if start >= nrows:
            start -= 1
        if start > 0 and matrix[start][0] > target:
            start = start-1
        pos = start
        start = 0
        end = ncols
        while start < end:
            mid = start + (end-start)//2
            if matrix[pos][mid] >= target:
                end = mid
            else:
                start = mid + 1
        if start >= ncols:
            return False
        print(pos, start)
        if matrix[pos][start] == target:
            return True
        else:
            return False
