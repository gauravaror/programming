from sys import stdin
from functools import lru_cache
def solve(grid):
    print(grid)
    def neig(row, col):
        if row + 1 < len(grid):
            yield (row+1, col)
            if col + 1 < len(grid[1]):
               yield (row+1, col+1)
            if col-1 >=0:
                yield (row + 1, col-1)

    @lru_cache(None)
    def max_coins(agent1_loc, agent2_loc):
        #print(agent1_loc, agent2_loc)
        if agent1_loc == (len(grid)-1,0) and agent2_loc == (len(grid)-1,len(grid[0])-1):
            return 0
        cmax = -float('inf')
        for agen1_neig in neig(*agent1_loc):
            for agen2_neig in neig(*agent2_loc):
                currn = max_coins(agen1_neig, agen2_neig)
                #print(agen1_neig, agen2_neig, currn)
                if agen1_neig == agen2_neig:
                    if currn + grid[agen1_neig[0]][agen1_neig[1]] > cmax:
                        cmax = currn + grid[agen1_neig[0]][agen1_neig[1]]
                elif currn +  grid[agen1_neig[0]][agen1_neig[1]] +  grid[agen2_neig[0]][agen2_neig[1]] > cmax:
                    cmax = currn +  grid[agen1_neig[0]][agen1_neig[1]] +  grid[agen2_neig[0]][agen2_neig[1]]
        #print("Return ", cmax)
        return cmax
    output = max_coins((0,0), (0, len(grid[0])-1))
    #print("Output ", grid, output + grid[0][0] + grid[0][len(grid[0])-1])
    return output + grid[0][0] + grid[0][len(grid[0])-1]

def read_grid(num):
    grid = []
    for row in range(num):
        line = stdin.readline()
        grid.append([int(val) for val in line.split()])
    return grid

def read_test_cases():
    test_cases = int(stdin.readline())
    stdin.readline()
    for tc in range(test_cases):
        grid_size = int(stdin.readline())
        grid = read_grid(grid_size)
        max_coins = solve(grid)
        print('Case #%d: %d'%(tc+1, max_coins))
        stdin.readline()


read_test_cases()    
