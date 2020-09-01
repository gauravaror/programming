import copy
def solution(A):
    nrows = len(A)
    ncols = len(A[0])
    seen = {}
    maxzeros = 0

    def neigh(row,col):
        if row < nrows-1:
            yield row + 1,col
        if row > 0:
            yield row - 1,col
        if col < ncols-1:
            yield row,col + 1
        if col > 0:
            yield row,col -1

    def dfs(r, c):
        print(r,c)
        nonlocal maxzeros
        maxprod = 1
        mzeros = 0
        for nr,nc in neigh(r,c):
            if (nr,nc) not in seen:
                seen[nr,nc] = True
                prod,zeros = dfs(nr,nc)
                if zeros > mzeros:
                    maxprod = prod
                    mzeros = zeros
                #del seen[nr,nc]
            elif seen[nr,nc] != True:
                prod,zeros = seen[nr,nc]
                if zeros > mzeros:
                    maxprod = prod
                    mzeros = zeros
        print(r,c, maxprod)
        maxprod = maxprod*A[r][c]
        thione = 0
        maxprod1 = copy.copy(maxprod)
        while maxprod % 10 == 0 and maxprod > 0:
            thione += 1
            maxprod /= 10
        seen[r,c] = (maxprod1, thione)
        if thione > maxzeros:
            maxzeros = thione
        return (maxprod1, thione)


    for i in range(nrows):
        for j in range(ncols):
            if (i,j) not in seen:
                seen[i,j] = True
                dfs(i,j)
    print(seen)
    return maxzeros

def solution1(A):
    nrows = len(A)
    ncols = len(A[0])
    def prod(li):
        cum = 1
        for i in li:
            cum *= i
        return cum
    max([prod(A[i]) for i in range(nrows)])

print(solution([[10,100,10],[1,10,1],[1,10,1]]))
#print(solution([[6,25,4,10],[12,25,1,15],[7,15,15,5]]))
#print(solution([[5,8,3,1],[4,15,12,1],[6,7,10,1],[9,1,2,1]]))
