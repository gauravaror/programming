class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        nrows = len(matrix)
        if nrows == 0:
            return []
        ncols = len(matrix[0])
        def neigh(r, c):
            if r > 0:
                yield (r-1,c)
            if r <= nrows-2:
                yield (r+1,c)
            if c > 0:
                yield (r, c-1)
            if c <= ncols-2:
                yield (r, c+1)
                
        def pacificAtlantic(r, c):
            out = []
            if r == nrows-1 or c == ncols-1:
                out.append('A')
            if r == 0 or c == 0:
                out.append('P')
            return out
        
        def hash(r, c):
            return str(r) + "_" + str(c)
        
        seen = {}
        output = []
                    
        def dfs(r, c):
            pa = pacificAtlantic(r, c)
            mp = set(pa)
            for nr, nc in neigh(r, c):
                if len(mp) == 2:
                    break
                if matrix[nr][nc] <= matrix[r][c]:
                    if not hash(nr, nc) in seen:
                        seen[hash(nr, nc)] = True
                        out = dfs(nr, nc)
                        del seen[hash(nr, nc)]
                        mp.update(out)
                    else:
                        out = seen[hash(nr,nc)]
                        if type(out) != bool:
                            mp.update(out)
            #print(r, c, mp, seen)
            if len(mp) == 2 and [r,c] not in output:
                output.append([r,c])
            return mp
        for i in range(nrows):
            for j in range(ncols):
                if hash(i, j) not in seen:
                    seen[hash(i,j)] = True
                    out = dfs(i, j)
                    seen[hash(i,j)] = out
        return output
