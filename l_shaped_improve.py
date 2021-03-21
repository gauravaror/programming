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
    for di in ['r', 'l', 't','b']:
        col[di] = [[0]*ncol for _ in range(nrow)]
    for r in range(nrow):
        for c in range(ncol):
            if grid[r][c] == 1:
                col['t'][r][c] = 1
                col['r'][r][c] = 1
                col['b'][r][c] = 1
                col['l'][r][c] = 1
    #print(col)
    for r in range(0, nrow):
        for c in range(0, ncol):
            if grid[r][c] == 0:
                continue
            if r-1 >= 0:
                col['t'][r][c] = col['t'][r-1][c] + 1
            if c-1 >= 0:
                col['l'][r][c] = col['l'][r][c-1] + 1
    for r in range(nrow-1, -1, -1):
        for c in range(ncol-1, -1, -1):
            if grid[r][c] == 0:
                continue
            if r+1 < nrow:
                col['b'][r][c] = col['b'][r+1][c] + 1
            if c+1 < ncol:
                col['r'][r][c] = col['r'][r][c+1] + 1
                    
    #print(col) 
    ans = 0
    for r in range(nrow):
        for c in range(ncol):
            for d1, d2 in [('r', 't'), ('r', 'b'), ('l', 't'), ('l', 'b')]:
                if col[d1][r][c] >= 2 and col[d2][r][c] >= 2:
                    a = col[d1][r][c]
                    b = col[d2][r][c]
                    ans  += min(a//2, b) + min(b//2, a) -2
    return ans
#main code
T = inp()
for t in range(T):
    R, C = mul()
    grid = []
    for i in range(R):
        grid.append(list(mul()))
    print(f"Case #{t+1}: {solve(grid)}")
