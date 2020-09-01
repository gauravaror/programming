def solution(A):
    nrows = len(A)
    ncols = len(A[0])
    seen = {}

    def neigh(row,col):
        if row < nrows-1:
            yield row + 1,col
        if row > 0:
            yield row - 1,col
        if col < ncols-1:
            yield row,col + 1
        if col > 0:
            yield row,col -1

    def dfs(r, c, color):
        for nr,nc in neigh(r,c):
            if A[nr][nc] == color:
                if (nr,nc) not in seen:
                    seen[nr,nc] = True
                    dfs(nr,nc, color)
    countries = 0
    for i in range(nrows):
        for j in range(ncols):
            if (i,j) not in seen:
                countries += 1
                dfs(i,j, A[i][j])
    return countries

print(solution([[5,4,4], [4,3,4], [3,2,4], [2,2,2], [3,3,4],[1,4,4],[4,1,1]]))
