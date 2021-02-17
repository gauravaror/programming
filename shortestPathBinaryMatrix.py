class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1:
            return -1

        def neig(r, c):
            for nr, nc in [(0,0),(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                cr = r + nr
                cc = c + nc
                if cr >= 0 and cc >=0 and cr < len(grid) and cc < len(grid[0]) and grid[cr][cc] == 0:
                    yield (cr, cc)
        stack = [(0,0,1)]
        seen = set()
        seen.add((0,0))
        while stack:
            elem = stack.pop(0)
            if elem[0] == len(grid)-1 and elem[1] == len(grid[0])-1:
                return elem[2]
            for nr, nc in neig(elem[0], elem[1]):
                if (nr, nc) not in seen:
                    seen.add((nr,nc))
                    stack.append([nr,nc,elem[2]+1])
        return -1
                
