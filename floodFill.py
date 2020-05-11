class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        nrow = len(image)
        ncol = len(image[0])
        def neig(r,c):
            if r < nrow-1:
                yield (r + 1,c)
            if r > 0:
                yield (r - 1, c)
            if c < ncol-1:
                yield (r, c + 1)
            if c > 0:
                yield (r, c -1)
        seen = {}
        def hash(nr, nc):
            return nr + 1 + 37*(nc+1)
        def dfs(r, c, pc, nc):
            for rr,cc in neig(r,c):
                hh = hash(rr, cc)
                if not hh in seen:
                    if image[rr][cc] == pc:
                        image[rr][cc] = nc
                        #print(rr, cc, image[rr][cc], pc, nc)
                        seen[hh] = True
                        dfs(rr, cc, pc, nc)
                seen[hh] = True
        seen[hash(sr, sc)] = True
        dfs(sr,sc,image[sr][sc], newColor)
        image[sr][sc] = newColor
        #print(seen)
        return image
