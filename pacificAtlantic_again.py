class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        nrow = len(matrix)
        if nrow == 0:
            return []
        ncol = len(matrix[0])
        
        stack = []
        for i in range(nrow):
            stack.append((i, 0, 'P'))
            stack.append((i, ncol-1, 'A'))
        for i in range(ncol):
            stack.append((0, i, 'P'))
            stack.append((nrow-1, i, 'A'))
            
    
        def neig(r, c):
            if r > 0:
                yield (r-1, c)
            if r < nrow-1:
                yield (r+1,c)
            if c > 0:
                yield (r, c-1)
            if c < ncol-1:
                yield (r, c+1)
        
        dp = {}
        dp['A'] = [[False]*ncol for _ in range(nrow)]
        dp['P'] = [[False]*ncol for _ in range(nrow)]
        seen = set()
        while stack:
            r, c, t = stack.pop()
            seen.add((r,c,t))
            dp[t][r][c] = True
            for nr, nc in neig(r,c):
                if matrix[nr][nc] >= matrix[r][c]:
                    if (nr, nc, t) not in seen:
                        stack.append((nr, nc, t))
        output = []
        for r in range(nrow):
            for c in range(ncol):
                if dp['A'][r][c] and dp['P'][r][c]:
                    output.append([r,c])
        return output
