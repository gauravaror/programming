class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        an = True
        nrow = len(matrix)
        ncol = len(matrix[0])
        def neig(r, c):
            if r < nrow-1 and c < ncol-1:
                yield (r,c)
                yield (r+1,c)
                yield (r, c+1)
                yield (r+1, c+1)
        while an:
            an = False
            #print(matrix)
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    this_makes = -1
                    for nr,nc in neig(i, j):
                        if this_makes == -1:
                            this_makes = matrix[nr][nc]
                        elif not this_makes == matrix[nr][nc]:
                            this_makes = -2
                    if this_makes != -2 and this_makes != -1 and this_makes != 0:
                        #print(i, j, this_makes)
                        an = True
                        matrix[i][j] += 1
        ans = sum([ sum(i) for i in matrix])
        #print(matrix, ans)
        return ans
