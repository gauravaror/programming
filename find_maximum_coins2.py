from sys import stdin

def neig(row, col, grid):
    if row + 1 < len(grid):
        yield (row+1, col)
        if col + 1 < len(grid[0]):
           yield (row+1, col+1)
        if col-1 >= 0:
            yield (row + 1, col-1)

def get_hash(ag, ag2):
    return str(ag[0]) + '_'  + str(ag[1]) + '_' + str(ag2[0]) + '_' + str(ag2[1])

def max_coins(ag1, ag2, grid, dp):
    if ag1 == (len(grid)-1,0) and ag2 == (len(grid)-1,len(grid[0])-1):
        return 0
    cmax = -float('inf')
    for an1 in neig(ag1[0],ag1[1],grid):
        for an2 in neig(ag2[0], ag2[1], grid):
            if get_hash(an1, an2) in dp:
                currn = dp[get_hash(an1, an2)]
            else:
                currn = max_coins(an1, an2, grid, dp)
            if an1 == an2:
                if currn + grid[an1[0]][an1[1]] > cmax:
                    cmax = currn + grid[an1[0]][an1[1]]
            elif currn +  grid[an1[0]][an1[1]] +  grid[an2[0]][an2[1]] > cmax:
                cmax = currn +  grid[an1[0]][an1[1]] +  grid[an2[0]][an2[1]]
    dp[get_hash(ag1, ag2)] = cmax
    return cmax

def solve(grid):
    if len(grid) == 0:
        return -1
    if len(grid[0]) < 2:
        return -1
    dp = {}
    output = max_coins((0,0), (0, len(grid[0])-1), grid, dp)
    return output + grid[0][0] + grid[0][len(grid[0])-1]

def read_test_cases():
    nr,nc = stdin.readline().split()
    all_elems = stdin.readline().split()
    curr_elem = 0
    grid = []
    for r in range(int(nr)):
        this_col = []
        for c in range(int(nc)):
            this_col.append(int(all_elems[curr_elem]))
            curr_elem += 1
        grid.append(this_col)
    print(solve(grid))

read_test_cases()    
