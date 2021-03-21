import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007

def solve(grid):
    nrow = len(grid)
    ncol = len(grid[0])
    col = {}
    for i in ['r', 'l', 'u', 'd']:        
        col[i] = [[0]*ncol for _ in range(nrow)]
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    col[i][r][c] = 1
    seen = set()
    def neigh(r, c):
        if r < nrow-1:
            yield ((r+1, c, 'd'))
        if r > 0:
            yield ((r-1, c, 'u'))
        if c > 0:
            yield ((r, c-1, 'l'))
        if c < ncol-1:
            yield ((r, c+1, 'r'))

    def dfs(r, c):
        seen.add((r,c))
        for nr, nc, di in neigh(r, c):
            if grid[nr][nc] == 1:
                if (nr, nc) not in seen:
                    dfs(nr, nc)
                    col[di][r][c] = col[di][nr][nc] + 1
        seen.remove((r,c))
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] == 1:
                dfs(i,j)
    # print(col)
    ans = 0
    for r in range(nrow):
        for c in range(ncol):
            for d1, d2 in [('r', 'u'), ('r', 'd'), ('l', 'u'), ('l', 'd')]:
                if col[d1][r][c] >= 2 and col[d2][r][c] >= 2:
                    a = col[d1][r][c]
                    b = col[d2][r][c]
                    mina = min(a, b)
                    for n in range(2, mina+2):
                        if n <= a and 2*n <= b:
                            ans += 1
                        if n <= b and 2*n <= a:
                            ans += 1
    return ans
#main code
T = inp()
for t in range(T):
    R, C = mul()
    grid = []
    for i in range(R):
        grid.append(list(mul()))
    print(f"Case #{t+1}: {solve(grid)}")

