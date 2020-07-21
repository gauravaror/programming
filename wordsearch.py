class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])
        def neigh(r, c):
            if r > 0:
                yield (r-1,c)
            if r < nrows-1:
                yield (r+1,c)
            if c >0:
                yield (r, c-1)
            if c < ncols-1:
                yield (r, c+1)
        seen = {}
        def hash(r,c):
            return str(r) + "_" + str(c)
        def dfs(r, c, ward):
            if len(ward) == 0:
                return True
            #print(r,c,ward)
            if hash(r,c) not in seen:
                seen[hash(r, c)] = True
                for nr,nc in neigh(r,c):
                    #print("checking neigh", nr, nc, ward[0] , board[nr][nc], hash(nr, nc) not in seen)
                    if ward[0] == board[nr][nc] and hash(nr, nc) not in seen:
                        if dfs(nr, nc, ward[1:]):
                            return True
                del seen[hash(r, c)]
                
            return False
        for cr in range(nrows):
            for cc in range(ncols):
                seen = {}
                if word[0] == board[cr][cc]:
                    if dfs(cr,cc, word[1:]):
                        return True
