class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        self.seen = {}
        self.maximum = 0
        def neigh(r,c):
            if r > 0:
                yield (r-1, c)
            if c > 0:
                yield (r,c-1)
            if r < nrows-1:
                yield (r+1,c)
            if c < ncols-1:
                yield (r, c+1)
        def dfs(r, c):
            maxa = 0
            for nr,nc in neigh(r,c):
                if (nr,nc) not in self.seen:
                    if matrix[nr][nc] > matrix[r][c]:
                        self.seen[(nr,nc)] = True
                        lis = dfs(nr, nc)
                    else:
                        lis = 0
                else:
                    if matrix[nr][nc] > matrix[r][c]:
                        lis = self.seen[nr, nc]
                    else:
                        lis = 0
                maxa = max(maxa, lis)
            self.seen[(r,c)] = maxa + 1
            self.maximum = max(self.maximum, maxa + 1)
            return maxa + 1
        for i in range(nrows):
            for j in range(ncols):
                if (i,j) not in self.seen:
                    self.seen[(i, j)] = True
                    dfs(i,j)
        print(self.seen)
        return self.maximum
